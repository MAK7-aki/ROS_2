from setuptools import setup

package_name = 'pkg_name'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tunga',
    maintainer_email='tunga@gmail.com',
    description='A minimal publisher/subscriber using ROS',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'my_publisher = pkg_name.my_publisher_node:main',
        	'my_subscriber = pkg_name.my_subscriber_node:main',
        ],
    },
)
