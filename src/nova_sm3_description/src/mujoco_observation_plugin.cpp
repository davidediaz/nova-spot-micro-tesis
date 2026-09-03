#include "nova_sm3_description/mujoco_observation_plugin.hpp"

#include <iomanip>
#include <cmath>
#include <sstream>
#include <utility>

#include <geometry_msgs/msg/transform_stamped.hpp>
#include <pluginlib/class_list_macros.hpp>

namespace nova_sm3_description
{

namespace
{
constexpr std::array<const char *, 4> kLegs{{"fl", "fr", "rl", "rr"}};
constexpr std::array<const char *, 4> kContactSensors{{
  "front_left_contact", "front_right_contact", "rear_left_contact", "rear_right_contact"}};
}

int MujocoObservationPlugin::sensor_address(
  const mjModel * model, const std::string & name) const
{
  const int id = mj_name2id(model, mjOBJ_SENSOR, name.c_str());
  return id < 0 ? -1 : model->sensor_adr[id];
}

bool MujocoObservationPlugin::init(
  rclcpp::Node::SharedPtr node, const mjModel * model, mjData *)
{
  node_ = std::move(node);
  const auto declare_if_missing = [this](const std::string & name, double value) {
      if (!node_->has_parameter(name)) {
        node_->declare_parameter(name, value);
      }
    };
  declare_if_missing("mujoco_plugins.nova_observations.publish_rate", 100.0);
  declare_if_missing("mujoco_plugins.nova_observations.contact_threshold", 1.0e-6);
  declare_if_missing("mujoco_plugins.nova_observations.contact_off_debounce", 0.12);
  declare_if_missing("mujoco_plugins.nova_observations.contact_on_debounce", 0.03);
  declare_if_missing("mujoco_plugins.nova_observations.wrench_duration", 0.25);
  const double rate = node_->get_parameter(
    "mujoco_plugins.nova_observations.publish_rate").as_double();
  publish_period_ = 1.0 / rate;
  contact_threshold_ = node_->get_parameter(
    "mujoco_plugins.nova_observations.contact_threshold").as_double();
  contact_off_debounce_ = node_->get_parameter(
    "mujoco_plugins.nova_observations.contact_off_debounce").as_double();
  contact_on_debounce_ = node_->get_parameter(
    "mujoco_plugins.nova_observations.contact_on_debounce").as_double();
  wrench_duration_ = node_->get_parameter(
    "mujoco_plugins.nova_observations.wrench_duration").as_double();

  base_body_id_ = mj_name2id(model, mjOBJ_BODY, "base_link");
  orientation_address_ = sensor_address(model, "imu_orientation");
  gyro_address_ = sensor_address(model, "imu_gyro");
  acceleration_address_ = sensor_address(model, "imu_accel");
  for (std::size_t i = 0; i < kContactSensors.size(); ++i) {
    contact_addresses_[i] = sensor_address(model, kContactSensors[i]);
  }
  if (base_body_id_ < 0 || orientation_address_ < 0 || gyro_address_ < 0 ||
    acceleration_address_ < 0)
  {
    RCLCPP_ERROR(node_->get_logger(), "Faltan cuerpo base o sensores IMU en el MJCF");
    return false;
  }
  for (const int address : contact_addresses_) {
    if (address < 0) {
      RCLCPP_ERROR(node_->get_logger(), "Falta un sensor táctil en el MJCF");
      return false;
    }
  }

  pose_publisher_ = node_->create_publisher<tf2_msgs::msg::TFMessage>(
    "/world/empty/dynamic_pose/info", 10);
  imu_publisher_ = node_->create_publisher<sensor_msgs::msg::Imu>("/nova/imu", 10);
  contacts_publisher_ = node_->create_publisher<std_msgs::msg::String>(
    "/nova/foot_contacts", 10);
  wrench_subscription_ = node_->create_subscription<geometry_msgs::msg::WrenchStamped>(
    "/nova/mujoco/external_wrench", 10,
    [this](const geometry_msgs::msg::WrenchStamped & message) {wrench_callback(message);});
  friction_subscription_ = node_->create_subscription<std_msgs::msg::Float64>(
    "/nova/mujoco/ground_friction", 10,
    [this](const std_msgs::msg::Float64 & message) {friction_callback(message);});
  RCLCPP_INFO(node_->get_logger(), "Observaciones Nova MuJoCo listas a %.1f Hz", rate);
  return true;
}

void MujocoObservationPlugin::wrench_callback(
  const geometry_msgs::msg::WrenchStamped & message)
{
  std::lock_guard<std::mutex> lock(perturbation_mutex_);
  requested_wrench_ = {{message.wrench.force.x, message.wrench.force.y,
    message.wrench.force.z, message.wrench.torque.x, message.wrench.torque.y,
    message.wrench.torque.z}};
  new_wrench_.store(true);
}

void MujocoObservationPlugin::friction_callback(const std_msgs::msg::Float64 & message)
{
  if (std::isfinite(message.data) && message.data >= 0.05 && message.data <= 2.0) {
    requested_friction_.store(message.data);
  } else {
    RCLCPP_WARN(node_->get_logger(), "Fricción rechazada: debe estar entre 0.05 y 2.0");
  }
}

void MujocoObservationPlugin::update_contact_filter(
  ContactFilter & filter, bool raw, double now)
{
  if (!filter.initialized) {
    filter.initialized = true;
    filter.stable = raw;
    return;
  }
  if (raw == filter.stable) {
    filter.pending = false;
    return;
  }
  if (!filter.pending || filter.candidate != raw) {
    filter.pending = true;
    filter.candidate = raw;
    filter.candidate_since = now;
    return;
  }
  const double required = raw ? contact_on_debounce_ : contact_off_debounce_;
  if (now - filter.candidate_since >= required) {
    filter.stable = raw;
    filter.pending = false;
  }
}

void MujocoObservationPlugin::update(const mjModel * model, mjData * data)
{
  if (new_wrench_.exchange(false)) {
    wrench_until_ = data->time + wrench_duration_;
  }
  {
    std::lock_guard<std::mutex> lock(perturbation_mutex_);
    mjtNum * applied = data->xfrc_applied + 6 * base_body_id_;
    for (std::size_t i = 0; i < requested_wrench_.size(); ++i) {
      applied[i] = data->time <= wrench_until_ ? requested_wrench_[i] : 0.0;
    }
  }
  const double friction = requested_friction_.exchange(-1.0);
  if (friction > 0.0) {
    mjModel * mutable_model = const_cast<mjModel *>(model);
    const int floor_id = mj_name2id(model, mjOBJ_GEOM, "floor");
    if (floor_id >= 0) {
      mutable_model->geom_friction[3 * floor_id] = friction;
    }
  }
  if (last_publish_time_ >= 0.0 && data->time - last_publish_time_ < publish_period_) {
    return;
  }
  last_publish_time_ = data->time;
  const auto stamp = rclcpp::Time(static_cast<int64_t>(data->time * 1.0e9));

  geometry_msgs::msg::TransformStamped transform;
  transform.header.stamp = stamp;
  transform.header.frame_id = "world";
  transform.child_frame_id = "nova_sm3";
  const mjtNum * position = data->xpos + 3 * base_body_id_;
  const mjtNum * quaternion = data->xquat + 4 * base_body_id_;
  transform.transform.translation.x = position[0];
  transform.transform.translation.y = position[1];
  transform.transform.translation.z = position[2];
  transform.transform.rotation.w = quaternion[0];
  transform.transform.rotation.x = quaternion[1];
  transform.transform.rotation.y = quaternion[2];
  transform.transform.rotation.z = quaternion[3];
  tf2_msgs::msg::TFMessage pose_message;
  pose_message.transforms.push_back(transform);
  pose_publisher_->publish(pose_message);

  sensor_msgs::msg::Imu imu;
  imu.header.stamp = stamp;
  imu.header.frame_id = "imu_link";
  const mjtNum * orientation = data->sensordata + orientation_address_;
  imu.orientation.w = orientation[0];
  imu.orientation.x = orientation[1];
  imu.orientation.y = orientation[2];
  imu.orientation.z = orientation[3];
  const mjtNum * gyro = data->sensordata + gyro_address_;
  imu.angular_velocity.x = gyro[0];
  imu.angular_velocity.y = gyro[1];
  imu.angular_velocity.z = gyro[2];
  const mjtNum * acceleration = data->sensordata + acceleration_address_;
  imu.linear_acceleration.x = acceleration[0];
  imu.linear_acceleration.y = acceleration[1];
  imu.linear_acceleration.z = acceleration[2];
  imu_publisher_->publish(imu);

  std::array<bool, 4> raw{};
  std::array<double, 4> force{};
  for (std::size_t i = 0; i < raw.size(); ++i) {
    force[i] = data->sensordata[contact_addresses_[i]];
    raw[i] = force[i] > contact_threshold_;
    update_contact_filter(contact_filters_[i], raw[i], data->time);
  }
  std::ostringstream json;
  json << std::setprecision(10) << "{\"stamp_sec\":" << data->time
       << ",\"all_sensors_valid\":true,\"observed_contacts\":[";
  bool first = true;
  for (std::size_t i = 0; i < raw.size(); ++i) {
    if (contact_filters_[i].stable) {
      if (!first) {json << ',';}
      json << '\"' << kLegs[i] << '\"';
      first = false;
    }
  }
  json << "],\"feet\":{";
  for (std::size_t i = 0; i < raw.size(); ++i) {
    if (i > 0) {json << ',';}
    json << '\"' << kLegs[i] << "\":{\"contact\":"
         << (contact_filters_[i].stable ? "true" : "false")
         << ",\"raw_contact\":" << (raw[i] ? "true" : "false")
         << ",\"transition_pending\":" << (contact_filters_[i].pending ? "true" : "false")
         << ",\"valid\":true,\"age_s\":0.0,\"approximate_force_n\":"
         << (contact_filters_[i].stable ? force[i] : 0.0) << '}';
  }
  json << "}}";
  std_msgs::msg::String contacts;
  contacts.data = json.str();
  contacts_publisher_->publish(contacts);
}

void MujocoObservationPlugin::cleanup()
{
  friction_subscription_.reset();
  wrench_subscription_.reset();
  contacts_publisher_.reset();
  imu_publisher_.reset();
  pose_publisher_.reset();
  node_.reset();
}

}  // namespace nova_sm3_description

PLUGINLIB_EXPORT_CLASS(
  nova_sm3_description::MujocoObservationPlugin,
  mujoco_ros2_control_plugins::MuJoCoROS2ControlPluginBase)
