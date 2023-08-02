# Create a Package

Navigate to the src directory of workspace:

```sh
cd ~/dev_ws/src
```
Create a Package named pkg_name:

```sh
ros2 pkg create --build-type ament_python pkg_name
```

# Write a Publisher Node
Move to the **/dev_ws/src/pkg_name/pkg_name** folder.This is where Python code will go for publisher and subscriber.
```sh
cd dev_ws/src/pkg_name/pkg_name
```
Create a blank Python file called **my_publisher_node.py**.
```sh
gedit my_publisher_node.py
```
Write the Publisher Node code in the python file

# Add Dependencies
To let the system know what libraries the node needs in order to execute properly.

To know the node's dependencies.Go to the **/dev_ws/src/pkg_name** folder:
```sh
cd dev_ws/src/pkg_name
```
```sh
dir
```
The package.xml file contains key information about the pkg_name package. 

Open the package.xml file.
```sh
gedit package.xml
```
Fill in the description,mail address and name on the maintainer line, and the license.

Now,after the **<build_type>ament_python</build_type>** line,add the two dependencies node needs in order to compile.
```xml
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```
Save and Close the file.
# Modify Setup.py
Open setup.py
```sh
gedit setup.py
```
Fill in the description ,maintainer name and email,and license.

Now, after that add the following line within the console_scripts brackets of the entry_points field:
```py
entry_points={
        'console_scripts': [
                'my_publisher = py_pubsub.my_publisher_node:main',
        ],
},
```
Save and close the file.

# Write a Subscriber Node
Navigate to the **/dev_ws/src/pkg_name/pkg_name** directory.
```sh
cd dev_ws/src/pkg_name/pkg_name
```
Create a blank Python file called **my_subscriber_node.py**.
```sh
gedit my_subscriber_node.py
```
Write the Subscriber Node code in the python file
# Modify Setup.py
Go to the dev_ws/src/py_pubsub folder.

```sh
cd dev_ws/src/pkg_name
```
Open setup.py
```sh
gedit setup.py
```
Add the following line within the console_scripts brackets of the entry_points field:
```py
entry_points={
        'console_scripts': [
                 'my_publisher = pkg_name.my_publisher_node:main',
                 'my_subscriber = pkg_name.my_subscriber_node:main',
        ],
},
```
Save and close the file.

# Build the Package 
Return to the root of the workspace:
```sh
cd dev_ws/
```
To double check that all the dependencies needed (rclpy and std_msgs) are already installed:
```sh
rosdep install -i --from-path src --rosdistro foxy -y
```
Build all packages in the workspace.
```sh
colcon build
```
# Create a Launch File
The launch file will enable to launch the publisher and subscriber nodes simultaneously with a single command.
Go to the following directory:
```sh
cd ~/dev_ws/src/pkg_name/
```
Type the following command to create a new folder:

```sh
mkdir launch
```
Move inside that folder.

```sh
cd launch
```
Open up a new launch file.

```sh
gedit pkg_name_launch.py
```
Write the code and save.


