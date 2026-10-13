# eProsima Fast DDS

eProsima Fast DDS
*****************

eProsima Fast DDS is a complete open-source DDS implementation for
real time embedded architectures and operating systems. See also:
https://www.eprosima.com/index.php/products-all/eprosima-fast-dds

Prerequisites
=============

Have rosdep installed.

Install packages
================

The easiest way is to install from ROS 2 apt repository.

   $ sudo apt install ros-rolling-rmw-fastrtps-cpp

Build from source code
======================

Building from source code is also another way to install.

First, clone Fast DDS and rmw_fastrtps in the ROS 2 workspace source
directory.

   $ cd ros2_ws/src
   $ git clone https://github.com/ros2/rmw_fastrtps ros2/rmw_fastrtps -b rolling
   $ git clone https://github.com/eProsima/Fast-DDS eProsima/fastrtps

Then, install necessary packages for Fast DDS.

   $ cd ..
   $ rosdep install --from src -i

Finally, run colcon build.

   $ colcon build --symlink-install

Switch to rmw_fastrtps
======================

The eProsima Fast DDS RMW can be selected by specifying the
environment variable:

   $ export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

See also: Working with multiple RMW implementations

Run the talker and listener
===========================

Now run "talker" and "listener" to test Fast DDS.

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp talker

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp listener
