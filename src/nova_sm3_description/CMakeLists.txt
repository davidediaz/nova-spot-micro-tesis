cmake_minimum_required(VERSION 3.8)
project(nova_sm3_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch mujoco rviz urdf worlds
  DESTINATION share/${PROJECT_NAME})

ament_package()
