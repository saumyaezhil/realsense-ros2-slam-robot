from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    realsense = Node(
        package='realsense2_camera',
        executable='realsense2_camera_node',
        output='screen'
    )

    depth_to_scan = Node(
        package='depthimage_to_laserscan',
        executable='depthimage_to_laserscan_node',
        parameters=[{
            'output_frame': 'camera_depth_frame'
        }],
        remappings=[
            ('depth', '/camera/depth/image_rect_raw'),
            ('depth_camera_info', '/camera/depth/camera_info'),
            ('scan', '/scan')
        ]
    )

    slam = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        output='screen',
        parameters=[{
            'use_sim_time': False
        }]
    )

    return LaunchDescription([
        realsense,
        depth_to_scan,
        slam
    ])
