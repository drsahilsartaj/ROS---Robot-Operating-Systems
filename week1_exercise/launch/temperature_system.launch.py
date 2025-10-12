from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='week1_exercise', executable='temperature_sensor', name='temperature_sensor'),
        Node(package='week1_exercise', executable='temperature_monitor', name='temperature_monitor'),
    ])
