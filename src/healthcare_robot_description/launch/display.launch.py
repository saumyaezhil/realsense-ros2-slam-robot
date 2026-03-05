from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro

def generate_launch_description():

	pkg_path = get_package_share_directory('healthcare_robot_description')
	xacro_file = os.path.join(pkg_path, 'urdf', 'healthcare_robot.xacro')

	doc = xacro.process_file(xacro_file)
	robot_description = {'robot_description': doc.toxml()}

	robot_state_publisher = Node(
    		package='robot_state_publisher',
    		executable='robot_state_publisher',
    		output='screen',
    		parameters=[robot_description]
	)	

	return LaunchDescription([
    		robot_state_publisher
	])
