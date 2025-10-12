from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node

def generate_launch_description():
    server = Node(
        package='week2_exercise',
        executable='book_server.py',
        name='book_server',
        output='screen'
    )
    client = Node(
        package='week2_exercise',
        executable='book_client.py',
        name='book_client',
        output='screen',
        parameters=[{'book_title': 'The Great Gatsby'}]
    )
    delayed_client = TimerAction(period=5.0, actions=[client])
    return LaunchDescription([server, delayed_client])
