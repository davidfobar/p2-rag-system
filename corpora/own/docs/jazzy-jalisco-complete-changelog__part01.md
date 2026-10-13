# Jazzy Jalisco changelog (part 1 of 5)

Jazzy Jalisco changelog
***********************

This page is a list of the complete changes in all ROS 2 core packages
since the previous release.

Table of Contents
^^^^^^^^^^^^^^^^^

* action_tutorials_cpp

* action_tutorials_interfaces

* action_tutorials_py

* actionlib_msgs

* ament_clang_format

* ament_clang_tidy

* ament_cmake

* ament_cmake_auto

* ament_cmake_clang_format

* ament_cmake_clang_tidy

* ament_cmake_copyright

* ament_cmake_core

* ament_cmake_cppcheck

* ament_cmake_cpplint

* ament_cmake_export_definitions

* ament_cmake_export_dependencies

* ament_cmake_export_include_directories

* ament_cmake_export_interfaces

* ament_cmake_export_libraries

* ament_cmake_export_link_flags

* ament_cmake_export_targets

* ament_cmake_flake8

* ament_cmake_gen_version_h

* ament_cmake_gmock

* ament_cmake_google_benchmark

* ament_cmake_gtest

* ament_cmake_include_directories

* ament_cmake_libraries

* ament_cmake_lint_cmake

* ament_cmake_mypy

* ament_cmake_pclint

* ament_cmake_pep257

* ament_cmake_pycodestyle

* ament_cmake_pyflakes

* ament_cmake_pytest

* ament_cmake_python

* ament_cmake_target_dependencies

* ament_cmake_test

* ament_cmake_uncrustify

* ament_cmake_vendor_package

* ament_cmake_version

* ament_cmake_xmllint

* ament_copyright

* ament_cppcheck

* ament_cpplint

* ament_flake8

* ament_index_cpp

* ament_index_python

* ament_lint

* ament_lint_auto

* ament_lint_cmake

* ament_lint_common

* ament_mypy

* ament_package

* ament_pclint

* ament_pep257

* ament_pycodestyle

* ament_pyflakes

* ament_uncrustify

* ament_xmllint

* camera_calibration_parsers

* camera_info_manager

* class_loader

* common_interfaces

* composition

* demo_nodes_cpp

* demo_nodes_cpp_native

* demo_nodes_py

* diagnostic_msgs

* dummy_map_server

* dummy_robot_bringup

* dummy_sensors

* example_interfaces

* examples_rclcpp_minimal_subscriber

* examples_rclcpp_wait_set

* foonathan_memory_vendor

* geometry_msgs

* google_benchmark_vendor

* gz_cmake_vendor

* gz_math_vendor

* gz_utils_vendor

* image_tools

* image_transport

* interactive_markers

* intra_process_demo

* kdl_parser

* keyboard_handler

* laser_geometry

* launch

* launch_pytest

* launch_ros

* launch_testing

* launch_testing_examples

* launch_testing_ros

* launch_xml

* launch_yaml

* libcurl_vendor

* liblz4_vendor

* libstatistics_collector

* libyaml_vendor

* lifecycle

* lifecycle_py

* logging_demo

* lttngpy

* map_msgs

* mcap_vendor

* message_filters

* mimick_vendor

* nav_msgs

* orocos_kdl_vendor

* osrf_pycommon

* osrf_testing_tools_cpp

* pendulum_control

* pendulum_msgs

* pluginlib

* pybind11_vendor

* python_cmake_module

* python_orocos_kdl_vendor

* python_qt_binding

* qt_dotgraph

* qt_gui

* qt_gui_cpp

* quality_of_service_demo_cpp

* quality_of_service_demo_py

* rcl

* rcl_action

* rcl_interfaces

* rcl_lifecycle

* rcl_logging_interface

* rcl_logging_noop

* rcl_logging_spdlog

* rcl_yaml_param_parser

* rclcpp

* rclcpp_action

* rclcpp_components

* rclcpp_lifecycle

* rclpy

* rcpputils

* rcutils

* resource_retriever

* rmw

* rmw_connextdds

* rmw_connextdds_common

* rmw_connextddsmicro

* rmw_cyclonedds_cpp

* rmw_dds_common

* rmw_fastrtps_cpp

* rmw_fastrtps_dynamic_cpp

* rmw_fastrtps_shared_cpp

* rmw_implementation

* robot_state_publisher

* ros2action

* ros2bag

* ros2cli

* ros2cli_test_interfaces

* ros2component

* ros2doctor

* ros2interface

* ros2param

* ros2pkg

* ros2service

* ros2topic

* ros2trace

* rosbag2_compression

* rosbag2_compression_zstd

* rosbag2_cpp

* rosbag2_examples_cpp

* rosbag2_examples_py

* rosbag2_interfaces

* rosbag2_performance_benchmarking

* rosbag2_py

* rosbag2_storage

* rosbag2_storage_mcap

* rosbag2_storage_sqlite3

* rosbag2_test_common

* rosbag2_test_msgdefs

* rosbag2_tests

* rosbag2_transport

* rosidl_cmake

* rosidl_dynamic_typesupport

* rosidl_generator_c

* rosidl_generator_cpp

* rosidl_generator_dds_idl

* rosidl_generator_py

* rosidl_generator_tests

* rosidl_generator_type_description

* rosidl_parser

* rosidl_pycommon

* rosidl_runtime_c

* rosidl_runtime_cpp

* rosidl_runtime_py

* rosidl_typesupport_c

* rosidl_typesupport_cpp

* rosidl_typesupport_fastrtps_c

* rosidl_typesupport_fastrtps_cpp

* rosidl_typesupport_introspection_c

* rosidl_typesupport_introspection_cpp

* rosidl_typesupport_introspection_tests

* rosidl_typesupport_tests

* rpyutils

* rqt

* rqt_bag

* rqt_bag_plugins

* rqt_console

* rqt_graph

* rqt_gui_cpp

* rqt_gui_py

* rqt_msg

* rqt_plot

* rqt_publisher

* rqt_py_common

* rqt_py_console

* rqt_reconfigure

* rqt_service_caller

* rqt_shell

* rqt_srv

* rqt_topic

* rti_connext_dds_cmake_module

* rttest

* rviz2

* rviz_assimp_vendor

* rviz_common

* rviz_default_plugins

* rviz_ogre_vendor

* rviz_rendering

* rviz_rendering_tests

* rviz_visual_testing_framework

* sensor_msgs

* sensor_msgs_py

* shape_msgs

* shared_queues_vendor

* spdlog_vendor

* sqlite3_vendor

* sros2

* std_msgs

* std_srvs

* stereo_msgs

* test_cli

* test_cli_remapping

* test_communication

* test_launch_ros

* test_launch_testing

* test_msgs

* test_quality_of_service

* test_rclcpp

* test_rmw_implementation

* test_ros2trace

* test_security

* test_tf2

* test_tracetools

* test_tracetools_launch

* tf2

* tf2_bullet

* tf2_eigen

* tf2_eigen_kdl

* tf2_geometry_msgs

* tf2_kdl

* tf2_py

* tf2_ros

* tf2_ros_py

* tf2_sensor_msgs

* tf2_tools

* topic_monitor

* topic_statistics_demo

* tracetools

* tracetools_launch

* tracetools_read

* tracetools_test

* tracetools_trace

* trajectory_msgs

* turtlesim

* uncrustify_vendor

* unique_identifier_msgs

* urdf

* urdf_parser_plugin

* visualization_msgs

* yaml_cpp_vendor

* zstd_vendor

action_tutorials_cpp
====================

* Update maintainer list in package.xml files (#665)

* Fix format-security warning with clang. (#663)

* Migrate std::bind calls to lambda expressions (#659)

* Contributors: Chris Lalancette, Felipe Gomes de Melo, Michael
  Jeronimo

action_tutorials_interfaces
===========================

* Update maintainer list in package.xml files (#665)

* Contributors: Michael Jeronimo

action_tutorials_py
===================

* Update maintainer list in package.xml files (#665)

* Add tests to action_tutorials_py. (#664)

* Contributors: Chris Lalancette, Michael Jeronimo

actionlib_msgs
==============

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

ament_clang_format
==================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_clang_tidy
================

* Update maintainer list in package.xml files (#474)

* Fix a warning from newer versions of flake8. (#469)

* remove AMENT_IGNORE check in clang-tidy when looking for compilation
  db (#441)

* Contributors: Alberto Soragna, Chris Lalancette, Michael Jeronimo

ament_cmake
===========

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_auto
================

* Update maintainer list in package.xml files (#503)

* Add ament_auto_add_gmock to ament_cmake_auto (#482)

* Contributors: Jordan Palacios, Michael Jeronimo

ament_cmake_clang_format
========================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_clang_tidy
======================

* Update maintainer list in package.xml files (#474)

* Provide --header-filter and --jobs to CMake. (#450)

* Contributors: Michael Jeronimo, Roderick Taylor

ament_cmake_copyright
=====================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_core
================

* Set hints to find the python version we actually want. (#508)

* Update maintainer list in package.xml files (#503)

* Use CMAKE_CURRENT_BINARY_DIR instead of CMAKE_BINARY_DIR in
  ament_generate_environment (#485)

* Fix CMake error when entire ament projects are added via
  add_subdirectory (#484)

* Contributors: Chris Lalancette, Michael Jeronimo, Silvio Traversaro

ament_cmake_cppcheck
====================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_cpplint
===================

* Increased cpplint timeout by default on Windows (#486)

* Update maintainer list in package.xml files (#474)

* Contributors: Alejandro Hernández Cordero, Michael Jeronimo

ament_cmake_export_definitions
==============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_export_dependencies
===============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_export_include_directories
======================================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_export_interfaces
=============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_export_libraries
============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_export_link_flags
=============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_export_targets
==========================

* Update maintainer list in package.xml files (#503)

* Add NAMESPACE support to ament_export_targets (#498)

* Contributors: Michael Jeronimo, Ryan

ament_cmake_flake8
==================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_gen_version_h
=========================

* Update maintainer list in package.xml files (#503)

* Update to C++17 (#488)

* Contributors: Chris Lalancette, Michael Jeronimo

ament_cmake_gmock
=================

* Update maintainer list in package.xml files (#503)

* Split ament_add_gmock into _executable and _test. (#497)

* Contributors: Chris Lalancette, Michael Jeronimo

ament_cmake_google_benchmark
============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_gtest
=================

* Update maintainer list in package.xml files (#503)

* Split ament_add_gmock into _executable and _test. (#497)

* ament_add_gtest_test: add TEST_NAME parameter (#492)

* Contributors: Chris Lalancette, Christopher Wecht, Michael Jeronimo

ament_cmake_include_directories
===============================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_libraries
=====================

* perf: faster ament_libraries_deduplicate implementation (#448) Co-
  authored-by: Scott K Logan <logans@cottsay.net>

* Subtle fix for ament_libraries_deduplicate tests (#516)

* Add some basic tests to ament_cmake_libraries (#512)

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo, Scott K Logan, Vincent Richard

ament_cmake_lint_cmake
======================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_mypy
================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_pclint
==================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_pep257
==================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_pycodestyle
=======================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_pyflakes
====================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_cmake_pytest
==================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_python
==================

* Add in a comment explaining where Python3::Interpreter comes from.
  (#510)

* Update maintainer list in package.xml files (#503)

* Contributors: Chris Lalancette, Michael Jeronimo

ament_cmake_target_dependencies
===============================

* Update maintainer list in package.xml files (#503)

* Fix "ament_target_dependencies" (#452)

* Contributors: Michael Jeronimo, Vincent Richard

ament_cmake_test
================

* Update maintainer list in package.xml files (#503)

* Recursively check for errors/failures in produced JUnit result XMLs
  (#446)

* Contributors: Michael Jeronimo, Nick Morales

ament_cmake_uncrustify
======================

* Added Timeout to ament_uncrustify (#485)

* Update maintainer list in package.xml files (#474)

* Contributors: Alejandro Hernández Cordero, Michael Jeronimo

ament_cmake_vendor_package
==========================

* Add more CMake variables to pass to vendor projects (#519)

* Fix patch file dependencies in ament_cmake_vendor_package (#520)

* Update maintainer list in package.xml files (#503)

* Always set CMAKE_C[XX]_COMPILER for vendor packages if needed (#476)

* Switch to CMake 'braket arguments' (#461)

* Replace 'git' dep with 'vcstool' (#462)

* Add support for specifying a patch directory in ament_vendor (#449)

* Contributors: Christophe Bedard, Michael Jeronimo, Scott K Logan

ament_cmake_version
===================

* Update maintainer list in package.xml files (#503)

* Contributors: Michael Jeronimo

ament_cmake_xmllint
===================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_copyright
===============

* Small fixes for modern flake8. (#484)

* Fix add-copyright year function (#466)

* Update maintainer list in package.xml files (#474)

* Contributors: Chris Lalancette, Lloyd Pearson, Michael Jeronimo

ament_cppcheck
==============

* Update maintainer list in package.xml files (#474)

* Add in checks to ament_cppcheck code. (#472)

* Contributors: Chris Lalancette, Michael Jeronimo

ament_cpplint
=============

* Update maintainer list in package.xml files (#474)

* Pass --output argument to cpplint (#453)

* Contributors: Michael Jeronimo, Vladimir Ivan

ament_flake8
============

* Update maintainer list in package.xml files (#474)

* Changes to make ament_flake8 work with v6+ (#459)

* Add additional dependencies to ament_flake8. (#454)

* Fix compatibility with flake8 version 5 (#410)

* Contributors: Chris Lalancette, Michael Carroll, Michael Jeronimo,
  Timo Röhling

ament_index_cpp
===============

* Update quality declaration documents (#94)

* only append search paths on first PackageNotFound (#91)

* Update to C++17 (#90)

* Contributors: Chris Lalancette, Christophe Bedard, Lucas Walter

ament_index_python
==================

* Update quality declaration documents (#94)

* Add type annotations to python files. (#93)

* Contributors: Christophe Bedard, Michael Carlstrom

ament_lint
==========

* Update maintainer list in package.xml files (#474)

* Add an ament_lint test dependency on python3-pytest. (#473)

* Contributors: Chris Lalancette, Michael Jeronimo

ament_lint_auto
===============

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_lint_cmake
================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_lint_common
=================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_mypy
==========

* Update maintainer list in package.xml files (#474)

* Fix a flake8 warning in ament_mypy. (#470) No need for parentheses
  around an assert.

* Contributors: Chris Lalancette, Michael Jeronimo

ament_package
=============

* Migrate from legacy importlib-resources (#143)

* Add setuptools dependency back in. (#141)

* Make python dependencies exec_depend. (#140)

* Contributors: Chris Lalancette, Isabel Paredes

ament_pclint
============

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_pep257
============

* Update maintainer list in package.xml files (#474)

* Convert linenumber to string when printing errors (#443)

* Contributors: Michael Jeronimo, Robert Brothers

ament_pycodestyle
=================

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_pyflakes
==============

* Update maintainer list in package.xml files (#474)

* Contributors: Michael Jeronimo

ament_uncrustify
================

* Adds uncrustify 0.78.1 config (#475)

* Update maintainer list in package.xml files (#474)

* Fix a flake8 warning in ament_uncrustify. (#471)

* Contributors: Chris Lalancette, Marco A. Gutierrez, Michael Jeronimo

ament_xmllint
=============

* Update maintainer list in package.xml files (#474)

* (ament_xmllint) add extensions argument (#456)

* Contributors: Matthijs van der Burgh, Michael Jeronimo

camera_calibration_parsers
==========================

* Update to yaml-cpp 0.8.0. (#305)

* Switch from rcpputils::fs to std::filesystem (#300)

* Removed C headers: camera_info_manager camera_calibration_parsers
  (#290)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard

camera_info_manager
===================

* Switch from rcpputils::fs to std::filesystem (#300)

* Removed C headers: camera_info_manager camera_calibration_parsers
  (#290)

* Contributors: Alejandro Hernández Cordero, Christophe Bedard

class_loader
============

* Remove all uses of ament_target_dependencies. (#210)

* Update to C++17 (#209)

* Contributors: Chris Lalancette

common_interfaces
=================

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

composition
===========

* [composition] add launch action console output in the verify section
  (#677) (#681) (cherry picked from commit
  34d29db73e78a84a174ad8699a2d646b0eeb1cdf) Co-authored-by: Mikael
  Arguedas <mikael.arguedas@gmail.com>

* Update maintainer list in package.xml files (#665)

* Migrate std::bind calls to lambda expressions (#659)

* Contributors: Felipe Gomes de Melo, Michael Jeronimo, mergify[bot]

demo_nodes_cpp
==============

* [demo_nodes_cpp] some readme and executable name fixups (#678)
  (#688) (cherry picked from commit
  aa8df8904b864d063e31fd5b953ffe561c7a9fe0) Co-authored-by: Mikael
  Arguedas <mikael.arguedas@gmail.com>

* Fix gcc warnings when building with optimizations. (#672) (#673) *
  Fix gcc warnings when building with optimizations. When building the
  allocator_tutorial_pmr demo with -O2, gcc is throwing an error
  saying that new and delete are mismatched. This is something of a
  misnomer, however; the real problem is that the global new override
  we have in that demo is actually implemented incorrectly. In
  particular, the documentation at
  https://en.cppreference.com/w/cpp/memory/new/operator_new very
  clearly specifies that operator new either has to return a valid
  pointer, or throw an exception on error. Our version wasn't throwing
  the exception, so change it to throw std::bad_alloc if std::malloc
  fails. While we are in here, also fix another small possible is
  where std::malloc could return nullptr on a zero-sized object, thus
  throwing an exception it shouldn't. * Always inline the new and
  delete operators. That's because gcc 13 has a bug where it can
  sometimes inline one or the other, and then it detects that they
  mismatch. For gcc and clang, just force them to always be inline in
  this demo. * Switch to NOINLINE instead. Both clang and MSVC don't
  like inlining these, so instead ensure that they are *not* inlined.
  This also works because the problem is when new is inlined but not
  delete (or vice-versa). As long as they are both not inlined, this
  should fix the warning. (cherry picked from commit
  957ddbb9f04f55cabd8496e8d74eb35ee4d29105) Co-authored-by: Chris
  Lalancette <clalancette@gmail.com>

* A few uncrustify fixes for 0.78. (#667)

* Allow users to configure the executor for executables in
  "demo_nodes_cpp" (#666)

* Update maintainer list in package.xml files (#665)

* Added extra documentation and clarifications. (#651)

* Add in support for both the PMR and custom allocator tutorials.
  (#655)

* Replacing old-style C++ allocator with a polymorphic memory resource
  (PMR) (#653)

* Remove unnecessary captures in the various demos. (#647)

* Dramatically speed up the demo_nodes_cpp tests (#641)

* Switch to using RCLCPP logging macros in the lifecycle package.
  (#644)

* failed to call introspection_client (#643)

* Small cleanups to the demos when running through them. (#639)

* Cleanup demo_nodes_cpp CMake and dependencies (#638)

* Change the service introspection parameter off value to 'disabled'
  (#634)

* Add demos for using logger service (#611)

* Contributors: Ali Ashkani Nia, Barry Xu, Chen Lihui, Chris
  Lalancette, Michael Jeronimo, Yadu, jrutgeer, mergify[bot]

demo_nodes_cpp_native
=====================

* Update maintainer list in package.xml files (#665)

* Contributors: Michael Jeronimo

demo_nodes_py
=============

* Update maintainer list in package.xml files (#665)

* Change the service introspection parameter off value to 'disabled'
  (#634) With this we can avoid the tricky bits around YAML
  interpretation of 'off' as a boolean.

* Add demos for using logger service (#611)

* Contributors: Barry Xu, Chris Lalancette, Michael Jeronimo

diagnostic_msgs
===============

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

dummy_map_server
================

* Update maintainer list in package.xml files (#665)

* Contributors: Michael Jeronimo

dummy_robot_bringup
===================

* Update maintainer list in package.xml files (#665)

* Switch to file-content launch substitution (#627)

* Contributors: Michael Jeronimo, Scott K Logan

dummy_sensors
=============

* Update dummy_sensors readme to echo the correct topic (#675) (#684)
  (cherry picked from commit eec5c12ea95dfaaa230f9f1a8e9cff9b09dde5d5)
  Co-authored-by: jmackay2 <1.732mackay@gmail.com>

* Update maintainer list in package.xml files (#665)

* Fix unstable LaserScan status for rviz2 (#614)

* Contributors: Chen Lihui, Michael Jeronimo, mergify[bot]

example_interfaces
==================

* Update to C++17. (#18)

* Contributors: Chris Lalancette

examples_rclcpp_minimal_subscriber
==================================

* fix: Fixed compilation after API change of TimerBase::execute (#375)
  Co-authored-by: Janosch Machowinski <J.Machowinski@cellumation.com>

* Split lambda and subscriber def in minimal example (#363)

* Contributors: Felipe Gomes de Melo, jmachowinski

examples_rclcpp_wait_set
========================

* fix: Fixed compilation after API change of TimerBase::execute (#375)
  Co-authored-by: Janosch Machowinski <J.Machowinski@cellumation.com>

* Contributors: jmachowinski

foonathan_memory_vendor
=======================

* Improve mechanism to find an installation of foonathan_memory (#67)

* Added support for QNX 7.1 build (#65)

geometry_msgs
=============

* Remove references to index.ros.org. (#244)

* Create new messages with all fields needed to define a velocity and
  transform it (#240) Co-authored-by: Dr. Denis
  <denis@stoglrobotics.de> Co-authored-by: Addisu Z. Taddese
  <addisuzt@intrinsic.ai> Co-authored-by: Tully Foote
  <tullyfoote@intrinsic.ai>

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* adding IDs to geometry_msgs/Polygon, PolygonStamped (#232)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Steve
  Macenski

google_benchmark_vendor
=======================

* Update to 1.8.3. (#29)

* Contributors: Marco A. Gutierrez

gz_cmake_vendor
===============

* Update vendored version to 3.5.3

* Use an alias target for root library

* Add support for the "<pkg>::<pkg>" and "<pkg>::all" targets, fix
  sourcing of dsv files

* Update vendored version to 3.5.2

* Update vendored package version

* Patch the pkg-config directory in the gz-cmake code. (#4) * Patch
  the pkg-config directory in the gz-cmake code. When building on the
  ROS 2 buildfarm, we aren't setting some of the CMAKE_PREFIX
  variables. This means that using CMAKE_INSTALL_FULL_LIBDIR actually
  creates a path like /opt/ros/rolling/... , which makes debuild
  upset. However, we actually need the FULL_LIBDIR in order to
  calculate the relative path between it and the INSTALL_PREFIX. Work
  around this by having two variables; the pkgconfig_install_dir
  (relative), used to install the files, and pkgconfig_abs_install_dir
  (absolute), used to calculate the relative path between them. This
  should fix the build on the buildfarm. I'll note that we are doing
  it here and not in gz-cmake proper because of knock-on effects to
  downstream gazebo. If this is successful we may end up merging it
  there, at which point we can drop this patch. * Update GzPackage as
  well. ---------

* Require calling find_package on the underlying package (#3) This
  also changes the version of the vendor package to 0.0.1 and adds the
  version of the vendored package in the description

* Fix linter (#2)

* Use "<depend>" on upstream package so that dependency is exported

* Update maintainer

* Add package.xml and CMakeLists (#1)

* Initial import

* Contributors: Addisu Z. Taddese, Chris Lalancette

gz_math_vendor
==============

* Use an alias target for root library

* Add support for the "<pkg>::<pkg>" and "<pkg>::all" targets, fix
  sourcing of dsv files

* Disable SWIG to fix CMake warning

* Disable pybind11 for now

* Require calling find_package on the underlying package (#2)

* Fix linter (#1)

* Remove Nate

* Update maintainers

* Initial import

* Contributors: Addisu Z. Taddese

gz_utils_vendor
===============

* Use an alias target for root library

* Add support for the "<pkg>::<pkg>" and "<pkg>::all" targets, fix
  sourcing of dsv files

* Require calling find_package on the underlying package (#2)

* Fix linter (#1)

* Initial import

* Contributors: Addisu Z. Taddese

image_tools
===========

* A few uncrustify fixes for 0.78. (#667)

* Update maintainer list in package.xml files (#665)

* Migrate std::bind calls to lambda expressions (#659)

* Contributors: Chris Lalancette, Felipe Gomes de Melo, Michael
  Jeronimo

image_transport
===============

* Added rclcpp component to Republish (#275)

* Add QoS option reliability to republisher qos params (#296)

* implement CameraSubscriber::getNumPublishers (#297)

* Add missing definition for CameraPublisher::publish overload (#278)

* Advertize and subscribe with custom qos (#288)

* Removed C headers (#289)

* Switch to using the override keyword for simple_publisher_plugin.
  (#285)

* feat: enable plugin allowlist (#264)

* Expose option to set callback groups (#274)

* add support for lazy subscribers (#272)

* Contributors: Aditya Pande, Alejandro Hernández Cordero, Carlos
  Andrés Álvarez Restrepo, Chris Lalancette, Daisuke Nishimatsu,
  Michael Ferguson, s-hall

interactive_markers
===================

* Shorten the length of a lambda. (#106)

* Fixed C++20 warning that ‘++’ expression of ‘volatile’-qualified
  type is deprecated (#102)

* Cleanup of interactive markers (#101)

* Contributors: AiVerisimilitude, Chris Lalancette

intra_process_demo
==================

* Update maintainer list in package.xml files (#665)

* Migrate std::bind calls to lambda expressions (#659)

* Fix executable name in README (#618)

* Contributors: Felipe Gomes de Melo, Michael Jeronimo, Yadunund

kdl_parser
==========

* Update to C++17. (#82)

* Contributors: Chris Lalancette

keyboard_handler
================

* Shorten lambdas so newer uncrustify is happier. (#42)

* Fixed C++20 warning implicit capture of this in lambda (#41)

* Update to C++17. (#37)

* Contributors: AiVerisimilitude, Chris Lalancette

laser_geometry
==============

* Switch to target_link_libraries. (#92)

* Contributors: Chris Lalancette

launch
======

* (launch) fix describe of PathJoinSubstitution (#771)

* Small fixes for modern flake8. (#772)

* Cleanup some type annotations.

* Rework task exceptions loop. (#755)

* add format overriding by environment variables (#722)

* Add exception type to error output (#753)

* Let XML executables/nodes be "required" (like in ROS 1) (#751)

* Add conditional substitution (#734)

* Add maximum times for a process to respawn (#696)

* Add in a timeout for launch pytests. (#725)

* Fix remaining occurrences of "There is no current event loop" (#723)

* Update the launch code for newer flake8 and mypy. (#719)

* Remove the deprecated some_actions_type.py (#718)

* Improve launch file parsing error messages (#626)

* Add file-content launch substitution (#708)

* Contributors: Chris Lalancette, David Yackzan, Marc Bestmann,
  Matthew Elwin, Matthijs van der Burgh, Nick Lamprianidis, Santti4go,
  Scott K Logan, Timon Engelke

launch_pytest
=============

* Switch tryfirst/trylast to hookimpl.

* Contributors: Chris Lalancette

launch_ros
==========

* Fix: typing. Iterable doesn't have __getitem__ (#393)

* Cleanup some type annotations. (#392)

* Create py.typed to mark this library as typed (#379)

* Remove create_future implementation. (#372)

* cache lookup of importlib metadata in Node action (#365)

* Get rid of unnecessary checks in composable_node_container. (#364)

* Contributors: Chris Lalancette, Jonas Otto, Matthijs van der Burgh,
  William Woodall

launch_testing
==============

* Fix a warning in modern unittest. (#773) Newer versions of unittest
  no longer store an errors list; instead, they store a result, which
  then stores an error list. Update the code here to be able to deal
  with either version.

* Add consider_namespace_packages=False (#766)

* to open expected outpout file with an encoding parameter (#717)

* Contributors: Chen Lihui, Chris Lalancette, Tony Najjar

launch_testing_examples
=======================

* Cleanup the launch_testing_examples. (#374)

* Refactor WaitForNodes class. (#373)

* Contributors: Chris Lalancette

launch_testing_ros
==================

* Make launch_testing_ros examples more robust. (#394)

* added type hinting to launch_testing_ros/test/examples (#386)

* Handle spin() ExternalShutdownException. (#378)

* Increase the timeout in wait_for_topic_launch_test. (#377)

* "WaitForTopics": get content of messages for each topic (#353)

* Contributors: Chris Lalancette, Giorgio Pintaudi, Yaswanth

launch_xml
==========

* launch_xml: fix xml syntax in README (#770)

* Let XML executables/nodes be "required" (like in ROS 1) (#751) * Let
  XML nodes be "required" Essentially on_exit="shutdown" is equivalent
  to ROS 1 required="true". This feature is implemented using the
  python launchfile on_exit mechanism. Right now "shutdown" is the
  only action accepted by on_exit, but theoretically more "on_exit"
  actions could be added later. Example: <executable cmd="ls"
  on_exit="shutdown"/> * Added tests for yaml

* Improve launch file parsing error messages (#626)

* Contributors: Matthew Elwin, Steve Peters, Timon Engelke

launch_yaml
===========

* Fix flake8 warnings in launch_yaml. (#756)

* Let XML executables/nodes be "required" (like in ROS 1) (#751) * Let
  XML nodes be "required" Essentially on_exit="shutdown" is equivalent
  to ROS 1 required="true". This feature is implemented using the
  python launchfile on_exit mechanism. Right now "shutdown" is the
  only action accepted by on_exit, but theoretically more "on_exit"
  actions could be added later. Example: <executable cmd="ls"
  on_exit="shutdown"/> * Added tests for yaml
