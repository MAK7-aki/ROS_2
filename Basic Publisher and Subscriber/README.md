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
cd pkg_name/pkg_name
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

