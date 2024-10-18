import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf_file_name= 'robot.urdf'
    urdf_file = os.path.join(get_package_share_directory('robot_description'), 'urdf', urdf_file_name)

    assert os.path.exists(urdf_file), "URDF file does not exist at: {}".format(urdf_file)


    return LaunchDescription([
        Node(
            package='robot_descriptio',
            executable='robot_state_publisher',
            output='screen',
            arguments=[urdf_file]
            ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_packages_share_directory('robot_description'), 'rviz2', 'config.rviz')]
                )
        ])
