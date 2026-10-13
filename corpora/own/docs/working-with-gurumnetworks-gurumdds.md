# GurumNetworks GurumDDS

GurumNetworks GurumDDS
**********************

"rmw_gurumdds" is an implementation of the ROS middleware interface
using GurumNetworks GurumDDS. For more information about GurumDDS,
visit the GurumNetworks website.

Prerequisites
=============

This guide assumes you have completed the ROS 2 environment setup
process, either by Installing ROS 2 via Deb Packages or Building ROS 2
from source on Ubuntu.

Version Requirements (see the README for details):

+------------------+------------------+
| ROS 2 Distro | GurumDDS Version |
|==================|==================|
| rolling | ">= 3.2.0" |
+------------------+------------------+
| lyrical | ">= 3.2.0" |
+------------------+------------------+
| kilted | ">= 3.2.0" |
+------------------+------------------+
| jazzy | ">= 3.2.0" |
+------------------+------------------+
| humble | "3.1.x" |
+------------------+------------------+

Deb packages of GurumDDS are provided in the ROS 2 apt repositories on
Ubuntu. Windows binary installer of GurumDDS will be available soon.

You can obtain a free trial license from the GurumDDS Free Trial page.

After acquiring a license, place it in the following location:
"/etc/gurumnet"

Installation
============

Option 1: Install from the ROS 2 apt repository (Recommended)
-------------------------------------------------------------

   $ sudo apt install ros-rolling-rmw-gurumdds-cpp

This installs both "rmw_gurumdds_cpp" and "gurumdds".

Option 2: Build from source code
--------------------------------

1. Clone the repository

   $ cd ros2_ws/src
   $ git clone https://github.com/ros2/rmw_gurumdds -b rolling ros2/rmw_gurumdds

2. Install dependencies:

   $ cd ..
   $ rosdep install --from src -i --rosdistro rolling

3. Build the workspace using Colcon:

   $ colcon build --symlink-install

Switch to rmw_gurumdds
======================

Switch from other RMW implementations to rmw_gurumdds by setting the
environment variable:

   $ export RMW_IMPLEMENTATION=rmw_gurumdds_cpp

For more information on working with multiple RMW implementations, see
Working with multiple RMW implementations.

Testing the installation
========================

Run the "talker" and "listener" nodes to verify your installation:

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp talker

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp listener

If the nodes communicate successfully, your installation is working
correctly.

Note:

  Remember to source your ROS 2 setup script before running these
  commands.
