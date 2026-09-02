#ifndef NOVA_SM3_DESCRIPTION__MUJOCO_OBSERVATION_PLUGIN_HPP_
#define NOVA_SM3_DESCRIPTION__MUJOCO_OBSERVATION_PLUGIN_HPP_

#include <array>
#include <memory>
#include <string>

#include <mujoco/mujoco.h>
#include <mujoco_ros2_control_plugins/mujoco_ros2_control_plugins_base.hpp>
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/imu.hpp>
#include <std_msgs/msg/string.hpp>
#include <tf2_msgs/msg/tf_message.hpp>

namespace nova_sm3_description
{

class MujocoObservationPlugin
  : public mujoco_ros2_control_plugins::MuJoCoROS2ControlPluginBase
{
public:
  bool init(rclcpp::Node::SharedPtr node, const mjModel * model, mjData * data) override;
  void update(const mjModel * model, mjData * data) override;
  void cleanup() override;

private:
  struct ContactFilter
  {
    bool initialized{false};
    bool stable{false};
    bool candidate{false};
    bool pending{false};
    double candidate_since{0.0};
  };

  int sensor_address(const mjModel * model, const std::string & name) const;
  void update_contact_filter(ContactFilter & filter, bool raw, double now);

  rclcpp::Node::SharedPtr node_;
  rclcpp::Publisher<tf2_msgs::msg::TFMessage>::SharedPtr pose_publisher_;
  rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr imu_publisher_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr contacts_publisher_;
  int base_body_id_{-1};
  int orientation_address_{-1};
  int gyro_address_{-1};
  int acceleration_address_{-1};
  std::array<int, 4> contact_addresses_{{-1, -1, -1, -1}};
  std::array<ContactFilter, 4> contact_filters_{};
  double last_publish_time_{-1.0};
  double publish_period_{0.01};
  double contact_threshold_{1.0e-6};
  double contact_off_debounce_{0.12};
  double contact_on_debounce_{0.03};
};

}  // namespace nova_sm3_description

#endif  // NOVA_SM3_DESCRIPTION__MUJOCO_OBSERVATION_PLUGIN_HPP_
