from setuptools import find_packages, setup

package_name = 'healthcare_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        ('share/' + package_name + '/launch',
            ['launch/nav2.launch.py',
             'launch/localization.launch.py']),
    ],
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saumya',
    maintainer_email='saumya.ezhil4@gmail.com',
    description='Healthcare robot navigation package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
