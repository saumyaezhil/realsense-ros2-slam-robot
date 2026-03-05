from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    world = os.path.join(
        get_package_share_directory('healthcare_robot_gazebo'),
        'worlds',
        'test_world.world'
    )

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            world,
            '--verbose',
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'healthcare_robot'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])
