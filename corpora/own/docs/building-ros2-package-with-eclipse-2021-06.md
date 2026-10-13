# Building a package with Eclipse 2021-06

Building a package with Eclipse 2021-06
***************************************

You cannot create a ROS 2 package with eclipse, you need to create it
with commandline tools. Follow the Create a package tutorial.

After you created your project, you can edit the source code and build
it with eclipse.

We start eclipse and select a eclipse-workspace.

[image: eclipse_work_dir][image]

We create a C++ project

[image: eclipse_create_c++_project][image][image:
eclipse_c++_project_select_type][image]

We see that we got C++ includes.

[image: eclipse_c++_project_includes][image]

We now import our ROS 2 project. The code is still in the old place.

[image: eclipse_import_project][image][image:
eclipse_import_filesystem][image]

Click the Advanced in the Options and check the **Create links in
worksapce**.

[image: eclipse_import_select_my_package][image]

We see in the source code that the C++ includes got resolved but not
the ROS 2 ones.

[image: eclipse_c++_wo_ros_includes][image][image:
eclipse_c++_path_and_symbols][image]

Add include paths of needed packages. (e.g.
**/opt/ros/lyrical/include/rclcpp**,
**/opt/ros/lyrical/include/std_msgs**, etc.)

[image: eclipse_c++_add_directory_path][image]

We now see that the ROS 2 includes got resolved too.

[image: eclipse_c++_indexer_ok][image]

Adding Builder colcon, so that we can build with right-click on
project and "Build project".

[image: eclipse_c++_properties_builders][image][image:
eclipse_c++_builder_main][image]

With PYTHONPATH you can also build python projects.

[image: eclipse_c++_builder_env][image][image:
eclipse_c++_properties_builders_with_colcon][image]

Right-click on the project and select "Build Project".

[image: eclipse_c++_build_project_with_colcon][image]
