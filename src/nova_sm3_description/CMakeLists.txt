cmake_minimum_required(VERSION 3.8)
project(nova_sm3_description)

find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(mujoco_ros2_control_plugins REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf2_msgs REQUIRED)

add_library(nova_mujoco_observation_plugin SHARED
  src/mujoco_observation_plugin.cpp)
target_include_directories(nova_mujoco_observation_plugin PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
ament_target_dependencies(nova_mujoco_observation_plugin
  geometry_msgs mujoco_ros2_control_plugins pluginlib rclcpp sensor_msgs
  std_msgs tf2_msgs)
pluginlib_export_plugin_description_file(
  mujoco_ros2_control_plugins nova_mujoco_plugins.xml)

install(TARGETS nova_mujoco_observation_plugin
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)
install(DIRECTORY include/ DESTINATION include)

install(DIRECTORY config launch mujoco rviz urdf worlds
  DESTINATION share/${PROJECT_NAME})

ament_package()
