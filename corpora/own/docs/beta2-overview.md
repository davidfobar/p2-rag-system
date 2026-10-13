# Beta 2 ("r2b2")

Beta 2 ("r2b2")
***************

Table of Contents
^^^^^^^^^^^^^^^^^

* Supported Platforms

* Features

  * Improvements since Beta 1 release

  * New demo application

  * Selected features from previous Alpha/Beta releases

  * Known issues

Supported Platforms
===================

We support ROS 2 Beta 2 on three platforms: Ubuntu 16.04 (Xenial),
macOS 10.12 (Sierra), and Windows 10. We provide both binary packages
and instructions for how to compile from source for all 3 platforms
(see install instructions as well as documentation).

Features
========

Improvements since Beta 1 release
---------------------------------

* DDS_Security support (aka SROS2, see sros2)

* Debian packages for Ubuntu Xenial

* Typesupport has been redesigned so that you only build a single
  executable and can choose one of the available RMW implementations
  by setting an environment variable (see documentation).

* Namespace support for nodes and topics (see design article, see
  known issues below).

* A set of command-line tools using the extensible "ros2" command (see
  conceptual article).

* A set of macros for logging messages in C / C++ (see API docs of
  rcutils).

New demo application
--------------------

* Turtlebot 2 demos using the following repositories that have been
  (partially) converted to ROS 2 (Linux only):

  * ros_astra_camera

  * depthimage_to_laserscan

  * pcl_conversions

  * cartographer

  * cartographer_ros

  * ceres-solver

  * navigation

  * teleop_twist_keyboard

  * joystick_drivers

  * teleop_twist_joy

* Dummy_robot demo:

  * robot_model

  * robot_state_publisher

Selected features from previous Alpha/Beta releases
---------------------------------------------------

For the complete list, see earlier release notes.

* C++ and Python implementations of ROS 2 client libraries including
  APIs for:

  * Publishing and subscribing to ROS topics

  * Requesting and replying ROS services (synchronous (C++ only) and
    asynchronous)

  * Getting and setting ROS parameters (C++ only, synchronous and
    asynchronous)

  * Timer callbacks

* Support for interoperability between multiple DDS/RTPS
  implementations

  * eProsima Fast RTPS is our default implementation, and is included
    in the binary packages

  * RTI Connext is supported: build from source to try it out

  * We initially supported PrismTech OpenSplice but support for it is
    currently on hold

* A graph API for network events

* Distributed discovery

* Realtime safe code paths for publish and subscribe with compatible
  DDS implementation (only Connext at the moment)

  * Support for custom allocators

* ROS 1 <-> ROS 2 dynamic bridge node

* Executor threading model (C++ only)

* Component model to compose nodes at compile / link / runtime

* Managed component using a standard lifecycle

* Extended ".msg" format with new features:

  * Bounded arrays

  * Default values

Known issues
------------

* We're tracking issues in various repositories, but the main entry
  point is the ros2/ros2 issue tracker

* We'd like to highlight a known issue that we are looking into which
  doesn't allow two topics with the same base name but different
  namespaces to have a different type when using "rmw_connext_cpp".

* Services with long responses are not working with Fast-RTPS. The
  fix, while not being part of beta2, is available upstream so you can
  work around this issue by building from source using Fast-RTPS
  master branch.
