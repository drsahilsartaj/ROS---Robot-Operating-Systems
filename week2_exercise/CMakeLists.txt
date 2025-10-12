cmake_minimum_required(VERSION 3.5)
project(week2_exercise)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/BookLookup.srv"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()

# Install python scripts (service server / client)
install(PROGRAMS
  scripts/book_server.py
  scripts/book_server_extended.py
  scripts/book_client.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
