from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    nav2_launch = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(

            os.path.join(

                get_package_share_directory('nav2_bringup'),

                'launch',

                'localization_launch.py'

            )

        ),

        launch_arguments={

            'use_sim_time': 'false',

            'map': '/home/saumya/healthcare_robot_ws/maps/hospital_map.yaml'

        }.items()

    )

    return LaunchDescription([

        nav2_launch

    ])
