# Zenoh

Zenoh
*****

Zenoh is an open source communication protocol and middleware designed
to facilitate efficient data distribution across heterogeneous
systems. It provides location-transparent abstractions for high
performance pub/sub and distributed queries. See also:
https://zenoh.io/docs/getting-started/first-app/

Prerequisites
=============

Have rosdep installed.

Installation packages
=====================

The rmw implementation Zenoh can be installed via binaries,
recommended for stable development.

Binary packages for supported ROS 2 distributions (see distro
branches) are available on respective Tier-1 platforms for the
distributions. First ensure that your system is set up to install ROS
2 binaries by following the instructions here.

Then install rmw_zenoh binaries using the command

   sudo apt install ros-rolling-rmw-zenoh-cpp

Build from source code
======================

Building from source is only recommended if latest features are
needed.

By default, we vendor and compile "zenoh-cpp" with a subset of zenoh
features. The "ZENOHC_CARGO_FLAGS" CMake argument may be overwritten
with other features included if required. See
zenoh_cpp_vendor/CMakeLists.txt for more details.

1. Clone the repository

   mkdir ~/ws_rmw_zenoh/src -p && cd ~/ws_rmw_zenoh/src
   git clone https://github.com/ros2/rmw_zenoh.git -b rolling

1. Install dependencies:

   cd ~/ws_rmw_zenoh
   rosdep install --from-paths src --ignore-src --rosdistro rolling -y

3. Build the workspace using Colcon:

   source /opt/ros/rolling/setup.bash
   colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

Switch to rmw_zenoh_cpp
=======================

Switch from other rmw to rmw_zenoh_cpp by specifying the environment
variable.

   export RMW_IMPLEMENTATION=rmw_zenoh_cpp

Run the talker and listener
===========================

Now run "talker" and "listener" to test Zenoh.

Start the Zenoh router

   # terminal 1
   source /opt/ros/rolling/setup.bash
   ros2 run rmw_zenoh_cpp rmw_zenohd

Note:

  Without the Zenoh router, nodes will not be able to discover each
  other since multicast discovery is disabled by default in the node's
  session config. Instead, nodes will receive discovery information
  about other peers via the Zenoh router's gossip functionality.

   # terminal 2
   export RMW_IMPLEMENTATION=rmw_zenoh_cpp
   source /opt/ros/rolling/setup.bash
   ros2 run demo_nodes_cpp talker

   # terminal 3
   export RMW_IMPLEMENTATION=rmw_zenoh_cpp
   source /opt/ros/rolling/setup.bash
   ros2 run demo_nodes_cpp listener

Note:

  Remember to source your ROS 2 setup script before running these
  commands.
