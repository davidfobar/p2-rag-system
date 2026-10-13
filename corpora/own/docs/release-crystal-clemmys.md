# Crystal Clemmys ("crystal")

Crystal Clemmys ("crystal")
***************************

Table of Contents
^^^^^^^^^^^^^^^^^

* Supported Platforms

* New features in this ROS 2 release

* Changes since the Bouncy release

* Known Issues

*Crystal Clemmys* is the third release of ROS 2.

Supported Platforms
===================

Crystal Clemmys supports the following platforms according to the
platform support tiers:

Tier 1 platforms:

* Ubuntu 18.04 (Bionic)

* Mac macOS 10.12 (Sierra)

* Windows 10

Tier 2 platforms:

* Ubuntu 16.04 (Xenial)

Targeted platforms:

+----------------+-------------------------+------------------------+----------------------+-------------------------+---------------------+
| Architecture | Ubuntu Bionic (18.04) | MacOS Sierra (10.12) | Windows 10 (VS2017) | Ubuntu Xenial (16.04) | Debian Stretch (9) |
|================|=========================|========================|======================|=========================|=====================|
| amd64 | Tier 1 [d][a][s] | Tier 1 [a][s] | Tier 1 [a][s] | Tier 2 [s] | Tier 3 [s] |
+----------------+-------------------------+------------------------+----------------------+-------------------------+---------------------+
| arm64 | Tier 1 [d][a][s] | | | Tier 2 [s] | Tier 3 [s] |
+----------------+-------------------------+------------------------+----------------------+-------------------------+---------------------+

The following indicators show what delivery mechanisms are available
for each platform.

" [d] " Debian packages will be provided for this platform for
packages submitted to the rosdistro.

" [a] " Binary releases are provided as a single archive per platform
containing all packages in the Crystal ROS 2 repos file[^4].

" [s] " Compilation from source.

Middleware Implementation Support:

+----------------------------+-----------------------+-----------------+-------------------------------+----------------------------------+
| Middleware Library | Middleware Provider | Support Level | Platforms | Architectures |
|============================|=======================|=================|===============================|==================================|
| rmw_fastrtps_cpp* | eProsima Fast-RTPS | Tier 1 | All Platforms | All Architectures |
+----------------------------+-----------------------+-----------------+-------------------------------+----------------------------------+
| rmw_connext_cpp | RTI Connext | Tier 1 | All Platforms except Debian | All Architectures except arm64 |
+----------------------------+-----------------------+-----------------+-------------------------------+----------------------------------+
| rmw_opensplice_cpp | ADLINK OpenSplice | Tier 2 | All Platforms except Debian | All Architectures |
+----------------------------+-----------------------+-----------------+-------------------------------+----------------------------------+
| rmw_fastrtps_dynamic_cpp | eProsima Fast-RTPS | Tier 2 | All Platforms | All Architectures |
+----------------------------+-----------------------+-----------------+-------------------------------+----------------------------------+
| rmw_connext_dynamic_cpp | RTI Connext | Tier 2 | All platforms except Debian | All architectures except arm64 |
+----------------------------+-----------------------+-----------------+-------------------------------+----------------------------------+

" * " means default RMW implementation.

Middleware implementation support is dependent upon the platform
support tier. For example a Tier 1 middleware implementation on a Tier
2 platform can only receive Tier 2 support.

Minimum language requirements:

* C11[^5]

* C++14

* Python 3.5

Dependency Requirements:

+--------------+-----------------+------------+---------------+-------------------+----------------------+
| | Required Support | Recommended Support |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Package | Ubuntu Bionic | MacOS** | Windows 10* | Ubuntu Xenial[s] | Debian Stretch [s] |
|==============|=================|============|===============|===================|======================|
| CMake | 3.10.2 | 3.13.3 | 3.13.3 | 3.5.1 | 3.7.2 |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| EmPY | 3.3.2 | 3.3.2 | 3.3.2 | 3.3.2 | 3.3.2 |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Gazebo | 9.0.0 | 9.9.0 | N/A | 9.9.0* | 9.8.0* |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Ogre | 1.10* |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| OpenCV | 3.2.0 | 4.0.1 | 3.4.1* | 2.4.9 | 3.2* |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| OpenSSL | 1.1.0g | 1.0.2q | 1.0.2q | 1.0.2g | 1.1.0j |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Poco | 1.8.0 | 1.9.0 | 1.8.0* | 1.8.0* | 1.8.0* |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Python | 3.6.5 | 3.7.2 | 3.7.2 | 3.5.1 | 3.5.3 |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Qt | 5.9.5 | 5.12.0 | 5.10.0 | 5.5.1 | 5.7.1 |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| | **Linux only** | |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| PCL | 1.8.1 | N/A | N/A | 1.7.2 | 1.8.0 |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| **RMW DDS Middleware Providers** |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Connext DDS | 5.3.1 | N/A |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| Fast-RTPS | 1.7.0 |
+--------------+-----------------+------------+---------------+-------------------+----------------------+
| OpenSplice | 6.9.181127OSS |
+--------------+-----------------+------------+---------------+-------------------+----------------------+

" * " means that this is not the upstream version (available on the
official Operating System repositories) but a package distributed by
OSRF or the community (package built and distributed on custom
repositories).

" ** " Rolling distributions will see multiple version changes of
these dependencies during their lifetime.

" [s] " Compilation from source, the ROS buildfarm will not produce
any binary packages for these platforms.

This document only captures the version at the first release of a ROS
distribution and will not be updated as the dependencies move forward.
These versions are thus a low watermark.

Package manager use for dependencies:

* Ubuntu, Debian: apt

* MacOS: Homebrew, pip

* Windows: Chocolatey, pip

Build System Support:

* ament_cmake

* cmake

* setuptools

New features in this ROS 2 release
==================================

* Actions in C / C++ (server / client examples)

* gazebo_ros_pkgs

* image_transport

* navigation2

* rosbag2

* rqt

* Improvement in memory management

* Introspection information about nodes

* Launch system improvements

  * Arguments

  * Nested launch files

  * Conditions

  * Pass params to Nodes

* Laid the groundwork for file-based logging and /rosout publishing

* Time and Duration API in Python

* Parameters work with Python nodes

Changes since the Bouncy release
================================

Changes since the Bouncy Bolson release:

* geometry2 - "tf2_ros::Buffer" API Change

  "tf2_ros::Buffer" now uses "rclcpp::Time", with the constructor
  requiring a "shared_ptr" to a "rclcpp::Clock" instance. See
  https://github.com/ros2/geometry2/pull/67 for details, with example
  usage:

     #include <tf2_ros/transform_listener.h>
     #include <rclcpp/rclcpp.hpp>
     ...
     # Assuming you have a rclcpp::Node my_node
     tf2_ros::Buffer buffer(my_node.get_clock());
     tf2_ros::TransformListener tf_listener(buffer);

* All "rclcpp" and "rcutils" logging macros require semicolons.

  See https://github.com/ros2/rcutils/issues/113 for details.

* "rcutils_get_error_string_safe()" and "rcl_get_error_string_safe()"
  have been replaced with "rcutils_get_error_string().str" and
  "rcl_get_error_string().str".

  See https://github.com/ros2/rcutils/pull/121 for details.

* rmw - "rmw_init" API Change

  There are two new structs, the "rcl_context_t" and the
  "rcl_init_options_t", which are used with "rmw_init". The init
  options struct is used to pass options down to the middleware and is
  an input to "rmw_init". The context is a handle which is an output
  of "rmw_init" function is used to identify which init-shutdown cycle
  each entity is associated with, where an "entity" is anything
  created like a node, guard condition, etc.

  This is listed here because maintainers of alternative rmw
  implementations will need to implement these new functions to have
  their rmw implementation work in Crystal.

  This is the function that had a signature change:

  * rmw_init

  Additionally, there are these new functions which need to be
  implemented by each rmw implementation:

  * rmw_shutdown

  * rmw_init_options_init

  * rmw_init_options_copy

  * rmw_init_options_fini

  Here's an example of what minimally needs to be changed in an rmw
  implementation to adhere to this API change:

  * rmw_fastrtps pr

* rcl - "rcl_init" API Change

  Like the "rmw" change above, there's two new structs in "rcl" called
  "rcl_context_t" and "rcl_init_options_t". The init options are
  passed into "rcl_init" as an input and the context is passed in as
  an output. The context is used to associate all other rcl entities
  to a specific init-shutdown cycle, effectively making init and
  shutdown no longer global functions, or rather those functions no
  longer use an global state and instead encapsulate all state within
  the context type.

  Any maintainers of a client library implementation (that also uses
  "rcl" under the hood) will need to make changes to work with
  Crystal.

  These functions were removed:

  * "rcl_get_global_arguments"

  * "rcl_get_instance_id"

  * "rcl_ok"

  These functions had signature changes:

  * rcl_init

  * rcl_shutdown

  * rcl_guard_condition_init

  * rcl_guard_condition_init_from_rmw

  * rcl_node_init

  * rcl_timer_init

  These are the new functions and types:

  * rcl_context_t

  * rcl_get_zero_initialized_context

  * rcl_context_fini

  * rcl_context_get_init_options

  * rcl_context_get_instance_id

  * rcl_context_is_valid

  * rcl_init_options_t

  * rcl_get_zero_initialized_init_options

  * rcl_init_options_init

  * rcl_init_options_copy

  * rcl_init_options_fini

  * rcl_init_options_get_rmw_init_options

  * rcl_node_is_valid_except_context

  * rcl_publisher_get_context

  * rcl_publisher_is_valid_except_context

  These new and changed functions will impact how you handle init and
  shutdown in your client library. For examples, look at the following
  "rclcpp" and "rclpy" PR's:

  * rclcpp

  * rclpy

  However, you may just continue to offer a single, global init and
  shutdown in your client library, and just store a single global
  context object.

Known Issues
============

* A race condition in Fast-RTPS 1.7.0 may cause messages to drop under
  stress (Issue).

* Using the TRANSIENT_LOCAL QoS setting with rmw_fastrtps_cpp can
  crash applications with large messages (Issue).

* Cross-vendor communication between rmw_fastrtps_cpp and other
  implementations is not functioning on Windows (Issue).

* When using OpenSplice (version < 6.9.190227) on macOS and Windows
  you might experience naming conflicts when when referencing field
  types with names from other packages if the same name also exist in
  the current package (Issue). By updating to a newer OpenSplice
  version as well as at least the third patch release of Crystal the
  problem should be resolved. On Linux updating to the latest Debian
  packages will include the newest OpenSplice version.
