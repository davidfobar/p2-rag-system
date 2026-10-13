# Eclipse Cyclone DDS

Eclipse Cyclone DDS
*******************

Eclipse Cyclone DDS is a very performant and robust open-source DDS
implementation. Cyclone DDS is developed completely in the open as an
Eclipse IoT project. See also:
https://projects.eclipse.org/projects/iot.cyclonedds

Prerequisites
=============

Have rosdep installed.

Install packages
================

The easiest way is to install from ROS 2 apt repository.

   $ sudo apt install ros-rolling-rmw-cyclonedds-cpp

Build from source code
======================

Building from source code is also another way to install.

First, clone Cyclone DDS and rmw_cyclonedds in the ROS 2 workspace
source directory. To determine the correct branches to checkout, you
need to find what versions are specified in your ROS distribution's
ros2.repos file.

Alternatively, you can run the following code to fetch the correct
branch/tag needed for Cyclone DDS:

   $ CYCLONEDDS_BRANCH=$(curl -s https://raw.githubusercontent.com/ros2/ros2/refs/heads/rolling/ros2.repos | grep -A 3 "eclipse-cyclonedds/cyclonedds:" | grep "version:" | awk '{print $2}')

And now, clone and checkout the code:

   $ cd ros2_ws/src
   $ git clone https://github.com/ros2/rmw_cyclonedds ros2/rmw_cyclonedds -b rolling
   $ git clone https://github.com/eclipse-cyclonedds/cyclonedds eclipse-cyclonedds/cyclonedds -b ${CYCLONEDDS_BRANCH}

Then, install necessary packages for Cyclone DDS.

   $ cd ..
   $ rosdep install --from src -i

Finally, run colcon build.

   $ colcon build --symlink-install

Switch to rmw_cyclonedds
========================

Switch from other rmw to rmw_cyclonedds by specifying the environment
variable.

   $ export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

See also: Working with multiple RMW implementations

Run the talker and listener
===========================

Now run "talker" and "listener" to test Cyclone DDS.

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp talker

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp listener
