# ROS 2 Lyrical Luth Complete Changelog (part 1 of 6)

ROS 2 Lyrical Luth Complete Changelog
*************************************

This page is a list of the complete changes in all ROS 2 core packages
since the previous release.

Table of Contents
^^^^^^^^^^^^^^^^^

* action_msgs

* action_tutorials_cpp

* action_tutorials_py

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

* ament_cmake_export_targets

* ament_cmake_flake8

* ament_cmake_gen_version_h

* ament_cmake_gmock

* ament_cmake_gtest

* ament_cmake_libraries

* ament_cmake_lint_cmake

* ament_cmake_mypy

* ament_cmake_pclint

* ament_cmake_pep257

* ament_cmake_pycodestyle

* ament_cmake_pyflakes

* ament_cmake_python

* ament_cmake_python_test

* ament_cmake_ros

* ament_cmake_ros_core

* ament_cmake_target_dependencies

* ament_cmake_uncrustify

* ament_cmake_vendor_package

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

* builtin_interfaces

* camera_calibration_parsers

* camera_info_manager

* camera_info_manager_py

* class_loader

* common_interfaces

* composition

* composition_interfaces

* console_bridge_vendor

* demo_nodes_cpp

* demo_nodes_cpp_native

* demo_nodes_py

* diagnostic_msgs

* domain_coordinator

* dummy_map_server

* dummy_robot_bringup

* dummy_sensors

* eigen3_cmake_module

* example_interfaces

* examples_rclcpp_async_client

* examples_rclcpp_cbg_executor

* examples_rclcpp_minimal_action_client

* examples_rclcpp_minimal_action_server

* examples_rclcpp_minimal_client

* examples_rclcpp_minimal_composition

* examples_rclcpp_minimal_publisher

* examples_rclcpp_minimal_service

* examples_rclcpp_minimal_subscriber

* examples_rclcpp_minimal_timer

* examples_rclcpp_multithreaded_executor

* examples_rclcpp_wait_set

* examples_rclpy_executors

* examples_rclpy_guard_conditions

* examples_rclpy_minimal_action_client

* examples_rclpy_minimal_action_server

* examples_rclpy_minimal_client

* examples_rclpy_minimal_publisher

* examples_rclpy_minimal_service

* examples_rclpy_minimal_subscriber

* examples_rclpy_pointcloud_publisher

* examples_tf2_py

* foonathan_memory_vendor

* geometry2

* geometry_msgs

* gmock_vendor

* gtest_vendor

* gz_cmake_vendor

* gz_math_vendor

* gz_utils_vendor

* image_common

* image_tools

* image_transport

* image_transport_py

* interactive_markers

* intra_process_demo

* kdl_parser

* keyboard_handler

* laser_geometry

* launch

* launch_pytest

* launch_ros

* launch_testing

* launch_testing_ament_cmake

* launch_testing_examples

* launch_testing_ros

* launch_xml

* launch_yaml

* libstatistics_collector

* libyaml_vendor

* lifecycle

* lifecycle_msgs

* lifecycle_py

* logging_demo

* lttngpy

* map_msgs

* mcap_vendor

* message_filters

* mimick_vendor

* nav_msgs

* osrf_testing_tools_cpp

* pendulum_control

* pendulum_msgs

* performance_test_fixture

* pluginlib

* point_cloud_transport

* point_cloud_transport_py

* python_qt_binding

* qt_dotgraph

* qt_gui

* qt_gui_app

* qt_gui_core

* qt_gui_cpp

* qt_gui_py_common

* quality_of_service_demo_cpp

* quality_of_service_demo_py

* rcl

* rcl_action

* rcl_interfaces

* rcl_lifecycle

* rcl_logging_implementation

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

* resource_retriever_interfaces

* resource_retriever_service

* resource_retriever_service_plugin

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

* rmw_test_fixture

* rmw_test_fixture_implementation

* rmw_zenoh_cpp

* robot_state_publisher

* ros2action

* ros2bag

* ros2cli

* ros2cli_common_extensions

* ros2cli_test_interfaces

* ros2component

* ros2doctor

* ros2interface

* ros2launch

* ros2lifecycle

* ros2lifecycle_test_fixtures

* ros2multicast

* ros2node

* ros2param

* ros2pkg

* ros2plugin

* ros2run

* ros2service

* ros2test

* ros2topic

* ros2trace

* ros_environment

* ros_testing

* rosbag2

* rosbag2_compression

* rosbag2_compression_zstd

* rosbag2_cpp

* rosbag2_examples_cpp

* rosbag2_examples_py

* rosbag2_interfaces

* rosbag2_performance_benchmarking

* rosbag2_performance_benchmarking_msgs

* rosbag2_py

* rosbag2_storage

* rosbag2_storage_default_plugins

* rosbag2_storage_mcap

* rosbag2_storage_sqlite3

* rosbag2_test_common

* rosbag2_test_msgdefs

* rosbag2_tests

* rosbag2_transport

* rosgraph_msgs

* rosidl_adapter

* rosidl_buffer

* rosidl_buffer_backend

* rosidl_buffer_backend_registry

* rosidl_buffer_py

* rosidl_cli

* rosidl_cmake

* rosidl_core_generators

* rosidl_core_runtime

* rosidl_default_generators

* rosidl_default_runtime

* rosidl_dynamic_typesupport

* rosidl_dynamic_typesupport_fastrtps

* rosidl_generator_c

* rosidl_generator_cpp

* rosidl_generator_dds_idl

* rosidl_generator_py

* rosidl_generator_rs

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

* rosidl_typesupport_interface

* rosidl_typesupport_introspection_c

* rosidl_typesupport_introspection_cpp

* rosidl_typesupport_introspection_tests

* rosidl_typesupport_tests

* rpyutils

* rqt

* rqt_action

* rqt_bag

* rqt_bag_plugins

* rqt_console

* rqt_graph

* rqt_gui

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

* rviz_common

* rviz_default_plugins

* rviz_ogre_vendor

* rviz_rendering

* rviz_rendering_tests

* rviz_visual_testing_framework

* sensor_msgs

* sensor_msgs_py

* service_msgs

* shape_msgs

* spdlog_vendor

* sros2

* sros2_cmake

* statistics_msgs

* std_msgs

* std_srvs

* stereo_msgs

* tango_icons_vendor

* test_cli

* test_cli_remapping

* test_communication

* test_interface_files

* test_launch_ros

* test_launch_testing

* test_msgs

* test_osrf_testing_tools_cpp

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

* tf2_msgs

* tf2_py

* tf2_ros

* tf2_ros_py

* tf2_sensor_msgs

* tf2_tools

* tlsf

* tlsf_cpp

* topic_monitor

* topic_statistics_demo

* tracetools

* tracetools_launch

* tracetools_read

* tracetools_test

* tracetools_trace

* trajectory_msgs

* turtlesim

* turtlesim_msgs

* type_description_interfaces

* uncrustify_vendor

* unique_identifier_msgs

* urdf

* urdf_parser_plugin

* urdfdom

* urdfdom_headers

* visualization_msgs

* yaml_cpp_vendor

* zenoh_cpp_vendor

* zenoh_security_tools

action_msgs
===========

* Fix cmake deprecation (#180)

* Contributors: mosfet80

action_tutorials_cpp
====================

* Use new ROSIDL aggregate CMake target (#781)

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Update action cpp demos to support setting introspection (#709) *
  Update action cpp demos to support setting introspection * Add the
  missing header file declaration ---------

* Contributors: Barry Xu, Emerson Knapp, mosfet80

action_tutorials_py
===================

* action_tutorials_py: add ament_mypy support (#775)

* fix setuptools deprecations (#733)

* support cancel handler in action_tutorials_py action server. (#727)

* Update action python demos to support setting introspection (#708) *
  Update action python demos to support setting introspection *
  Correct the errors in the document ---------

* Contributors: Barry Xu, Tomoya Fujita, mohit, mosfet80

ament_clang_format
==================

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_clang_tidy
================

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_cmake
===========

* Removed deprecated ament_cmake_export_interfaces package (#581)

* Contributors: Alejandro Hernández Cordero

ament_cmake_auto
================

* Do not error on USE_SCOPED_HEADER_INSTALL_DIR (#596)

* Contributors: Tim Clephas

ament_cmake_clang_format
========================

* Fix cmake deprecation (#539)

* Allow overriding clang-format version via CMake (#536)

* Contributors: Nathan Wiebe Neufeldt, mosfet80

ament_cmake_clang_tidy
======================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_copyright
=====================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_core
================

* Remove unused AMENT_CMAKE_ENVIRONMENT_GENERATION option (#354)

* Address ament_lint_cmake regressions (#604)

* Respect find_package(QUIET) in chains from ament_cmake_core (#603)

* perf: faster normalize_path implementation using cmake_path (#586)

* Contributors: Nathan Boisard, Scott K Logan, Shane Loretz

ament_cmake_cppcheck
====================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_cpplint
===================

* Fixing EXCLUDE consistency (#481)

* cpplint: update link to upstream cpplint repo (#538)

* Fix cmake deprecation (#539)

* Contributors: Romain Reignier, Tom Moore, mosfet80

ament_cmake_export_targets
==========================

* Address ament_lint_cmake regressions (#604)

* Contributors: Scott K Logan

ament_cmake_flake8
==================

* Fixing EXCLUDE consistency (#481)

* Fix cmake deprecation (#539)

* Contributors: Tom Moore, mosfet80

ament_cmake_gen_version_h
=========================

* Address ament_lint_cmake regressions (#604)

* Update CMake requirement (#589)

* Removed deprecated function ament_cmake_gen_version_h (#582)

* Contributors: Alejandro Hernández Cordero, Scott K Logan, mosfet80

ament_cmake_gmock
=================

* Use libgtest-dev and libgmock-dev (#622)

* Contributors: Shane Loretz

ament_cmake_gtest
=================

* Use libgtest-dev and libgmock-dev (#622)

* Contributors: Shane Loretz

ament_cmake_libraries
=====================

* Address ament_lint_cmake regressions (#604)

* Contributors: Scott K Logan

ament_cmake_lint_cmake
======================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_mypy
================

* [ament_mypy] Add "--ament-strict" flag for more strict type
  checking. (#573)

* Fix cmake deprecation (#539)

* Contributors: Michael Carlstrom, mosfet80

ament_cmake_pclint
==================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_pep257
==================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_pycodestyle
=======================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_pyflakes
====================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_cmake_python
==================

* feature: allow extending a python package in
  "ament_python_install_package" (#587)

* Add missing dependency (#617)

* Contributors: Nadav Elkabets, Robert Haschke

ament_cmake_python_test
=======================

* feature: allow extending a python package in
  "ament_python_install_package" (#587)

* Contributors: Nadav Elkabets

ament_cmake_ros
===============

* fix cmake deprecation (#47)

* Contributors: mosfet80

ament_cmake_ros_core
====================

* Add "ament_ros_defaults" target (#62)

* fix cmake deprecation (#47)

* Contributors: Michael Carlstrom, mosfet80

ament_cmake_target_dependencies
===============================

* Revert "Revert "Removed deprecated function
  ament_cmake_target_dependencies (…" (#614)

* Revert "Removed deprecated function ament_cmake_target_dependencies"
  (#585)

* Removed deprecated function ament_cmake_target_dependencies (#583)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

ament_cmake_uncrustify
======================

* [ament_cmake_uncrustify] Add ament_cmake_uncrustify_LANGUAGE
  variable (#384)

* Fix cmake deprecation (#539)

* Contributors: Abrar Rahman Protyasha, mosfet80

ament_cmake_vendor_package
==========================

* ament_vendor: Propagate additional variables to ExternalProject
  (#593)

* Contributors: Silvio Traversaro

ament_cmake_xmllint
===================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_copyright
===============

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Remove "importlib_metadata" (#564)

* Remove invalid license template. (#209)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, Tully Foote,
  mosfet80

ament_cppcheck
==============

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_cpplint
=============

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* cpplint: update link to upstream cpplint repo (#538)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, Romain
  Reignier, mosfet80

ament_flake8
============

* [ament_mypy] Add "--ament-strict" flag for more strict type
  checking. (#573)

* Drop setuptools from install_requires (#566)

* Drop dependency on python3-flake8-docstrings (#513)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, Scott K Logan,
  mosfet80

ament_index_cpp
===============

* Cleanups (#114)

* Use get_package_share_path just as python (#112)

* Add autogenerated version header (#105)

* Extend API to use std::filesystem (#104)

* Fix CMake deprecation (#102)

* Contributors: Alejandro Hernández Cordero, Eric Lujan, Tim Clephas,
  mosfet80

ament_index_python
==================

* Cleanups ament_index_python (#115)

* fix setuptools deprecations (#101)

* Contributors: Alejandro Hernández Cordero, mosfet80

ament_lint
==========

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_lint_auto
===============

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_lint_cmake
================

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_lint_common
=================

* Fix cmake deprecation (#539)

* Contributors: mosfet80

ament_mypy
==========

* Allow unused ignores (#575)

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* [ament_mypy] Add "--ament-strict" flag for more strict type
  checking. (#573)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_package
=============

* feat: add support for fish (#164)

* Fix flake8 (#163)

* Remove unneeded deps (#161)

* fix setuptools deprecations (#156)

* Contributors: Michael Carlstrom, SPeak, mosfet80

ament_pclint
============

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* clean setup.py (#552)

* fix setuptools deprecation (#551)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_pep257
============

* Skip pydocstyle tests if it can't be imported (#579)

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, Scott K Logan,
  mosfet80

ament_pycodestyle
=================

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_pyflakes
==============

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

ament_uncrustify
================

* [ament_mypy] Fix config for ament_cmake packages and type
  entrypoints (#574)

* Drop setuptools from install_requires (#566)

* Revert "Removed uncrustify_vendor (#556)" (#561)

* Removed uncrustify_vendor (#556)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Alejandro Hernández Cordero, Jochen Sprickerhof,
  Michael Carlstrom, Michael Orlov, mosfet80

ament_xmllint
=============

* [ament_mypy] Add "--ament-strict" flag for more strict type
  checking. (#573)

* xmllint: fetch external schemas via Python (#570)

* Drop setuptools from install_requires (#566)

* Export typing information for ament linters (#553)

* fix setuptools deprecations (#547)

* Contributors: Jochen Sprickerhof, Michael Carlstrom, Michael
  Carroll, mosfet80

builtin_interfaces
==================

* Fix cmake deprecation (#180)

* Add info to duration message and time message comments (#176)

* Contributors: Jimmy McElwain, mosfet80

camera_calibration_parsers
==========================

* Use new ROSIDL aggregate CMake target (#396)

* Delete camera_calibration_parsers/setup.py (#393)

* Update BSD licenses to SPDX identifier (#389) Co-authored-by:
  Alejandro Hernandez Cordero <ahcorde@gmail.com>

* Fix cmake deprecation (#367)

* Use target_link_libraries instead of ament_target_dependencies
  (#345)

* Contributors: Emerson Knapp, Garrett Brown, Michael Carlstrom, Shane
  Loretz, mosfet80

camera_info_manager
===================

* Use new ROSIDL aggregate CMake target (#396)

* Added camera info manager unit test (#358)

* Use get_package_share_path (#391)

* Update BSD licenses to SPDX identifier (#389) Co-authored-by:
  Alejandro Hernandez Cordero <ahcorde@gmail.com>

* Updated deprecated ament_index_cpp API (#388)

* Fix compilation error with clang (#372)

* Support lifecycle node - NodeInterfaces (#352)

* Deprecated rmw_qos_profile_t in favour of rclcpp::QoS (#364)

* Fix cmake deprecation (#367)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Garrett
  Brown, mosfet80

camera_info_manager_py
======================

* Update BSD licenses to SPDX identifier (#389) Co-authored-by:
  Alejandro Hernandez Cordero <ahcorde@gmail.com>

* Cleanup mislabeled BSD license (#382)

* fix setuptools deprecation (#366)

* Fix CameraInfo distortion coefficients and logger (#360)

* Contributors: Alejandro Hernández Cordero, Garrett Brown, Rick-v-E,
  mosfet80

class_loader
============

* Fix compiler error with clang (#227)

* Remove ament_cmake_ros dependency (#226) The dependent
  ament_cmake_ros package transitively pulls in RMW-layer packages
  which is unnecessarily heavy to class_loader that is supposed to be
  an independent plugin loading library. This commit removes the
  ament_cmake_ros dependency and replaces with a plain ament_cmake
  with an explicit SHARED library type to keep the dependency minimal.

* Improvements (#225)

* Clean up tests (#224)

* Add support for passing arguments to constructors (#223)

* Thread and Address Sanitizer CI (#198)

* Update cmake requirement

* Remove CODEOWNERS and mirror-rolling-to-main workflow (#215)

* Contributors: Alejandro Hernández Cordero, CY Chen, Tyler Weaver,
  mosfet80, pum1k

common_interfaces
=================

* Fix CMAKE deprecation (#288)

* Removed deprecated actionlib_msgs (#280)

* Contributors: Alejandro Hernández Cordero, mosfet80

composition
===========

* Use new ROSIDL aggregate CMake target (#781)

* Add tests isolation in test_dlopen_composition.py.in and
  test_linktime_composition.py.in (#764)

* Switching to example_interfaces (#674)

* Log message for linktime composition on Windows (#640)

* correct name of shared libraries and their location (#722) (#726)

* Use EnableRmwIsolation in launch tests (#724)

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Julien
  Enoch, Lucas Wendland, Scott K Logan, Shane Loretz, mergify[bot],
  mosfet80, yadunund

composition_interfaces
======================

* Fix cmake deprecation (#180)

* Contributors: mosfet80

console_bridge_vendor
=====================

* Update CMake version here and console_bridge (#44)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#42)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

demo_nodes_cpp
==============

* Use new ROSIDL aggregate CMake target (#781)

* add child logger under parent node, with different log levels.
  (#772)

* Switching to example_interfaces (#674)

* Update subscription callback signatures (#754)

* Use EnableRmwIsolation in launch tests (#724)

* fix typo in docs demo_nodes_cpp (#715)

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Khaled
  Gabr, Lucas Wendland, Scott K Logan, Tomoya Fujita, mini-1235,
  mosfet80

demo_nodes_cpp_native
=====================

* Use new ROSIDL aggregate CMake target (#781)

* Switching to example_interfaces (#674)

* Removed outdated TODO (#723)

* Uniform CMAKE min VERSION (#714)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas
  Wendland, Shane Loretz, mosfet80

demo_nodes_py
=============

* add child logger under parent node, with different log levels.
  (#772)

* Fix deprecated RcutilsLogger::warn() usage in LoggerServiceNode
  (#773)

* Ignore A005 (#771)

* Switching to example_interfaces (#674)

* fix setuptools deprecations (#733)

* Revert "Revert "fix loading parameter behavior from yaml file.
  (#656)" (#660)" (#661)

* Contributors: Barry Xu, Lucas Wendland, Michael Carlstrom, Tomoya
  Fujita, mosfet80

diagnostic_msgs
===============

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

domain_coordinator
==================

* fix setuptools deprecations (#49)

* Contributors: mosfet80

dummy_map_server
================

* Use new ROSIDL aggregate CMake target (#781)

* get rid of deprecated rclcpp::spin_some(). (#734)

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80

dummy_robot_bringup
===================

* Fixed launch file (#759)

* Added README.md for dummy_robot_bringup. (#574)

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Contributors: Alejandro Hernández Cordero, Gary Bey, mosfet80

dummy_sensors
=============

* Use new ROSIDL aggregate CMake target (#781)

* get rid of deprecated rclcpp::spin_some(). (#734)

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80

eigen3_cmake_module
===================

* fix cmake deprecation (#10)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#8)

* Contributors: Chris Lalancette, mosfet80

example_interfaces
==================

* fix cmake deprecation (#23)

* Remove .github/ISSUE_TEMPLATE.md (old version of templates) (#21)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#19)

* Contributors: Chris Lalancette, Tomoya Fujita, mosfet80

examples_rclcpp_async_client
============================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclcpp_cbg_executor
============================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclcpp_minimal_action_client
=====================================

* Use new ROSIDL aggregate CMake target (#444)

* get rid of deprecated rclcpp::spin_some(). (#422)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80

examples_rclcpp_minimal_action_server
=====================================

* Use new ROSIDL aggregate CMake target (#444)

* Add rclcpp single goal action server example (#429)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, Taiga Arai, mosfet80

examples_rclcpp_minimal_client
==============================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclcpp_minimal_composition
===================================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclcpp_minimal_publisher
=================================

* Use new ROSIDL aggregate CMake target (#444)

* Improve minimal_publisher README with clearer structure and usage
  guidance (#434)

* get rid of deprecated rclcpp::spin_some(). (#422)

* Fix CMAKE deprecation (#419)

* wait 5 secs until all subscriptions acknowledge the messages. (#414)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita,
  Yadnyeshwar Amol Sakhare, mosfet80

examples_rclcpp_minimal_service
===============================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclcpp_minimal_subscriber
==================================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclcpp_minimal_timer
=============================

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz, mosfet80

examples_rclcpp_multithreaded_executor
======================================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Improve readibility of reported thread ids in the multithreaded
  executor example (#415)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, José Faria, Shane Loretz, mosfet80

examples_rclcpp_wait_set
========================

* Use new ROSIDL aggregate CMake target (#444)

* Fix CMAKE deprecation (#419)

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Emerson Knapp, Shane Loretz, mosfet80

examples_rclpy_executors
========================

* Fix setuptools deprecations (#421)

* Contributors: mosfet80

examples_rclpy_guard_conditions
===============================

* Fix setuptools deprecations (#421)

* Contributors: mosfet80

examples_rclpy_minimal_action_client
====================================

* Fix setuptools deprecations (#421)

* Contributors: mosfet80

examples_rclpy_minimal_action_server
====================================

* Fix setuptools deprecations (#421)

* Contributors: mosfet80

examples_rclpy_minimal_client
=============================

* flake8 fixes (#445)

* Fix setuptools deprecations (#421)

* Contributors: Michael Carlstrom, mosfet80

examples_rclpy_minimal_publisher
================================

* Fix setuptools deprecations (#421)

* Address flake8 errors for examples_rclpy_minimal_publisher (#410)

* Add publisher_member_function_with_wait_for_all_acked.py (#407)

* Contributors: Tomoya Fujita, mosfet80

examples_rclpy_minimal_service
==============================

* flake8 fixes (#445)

* Fix setuptools deprecations (#421)

* Contributors: Michael Carlstrom, mosfet80

examples_rclpy_minimal_subscriber
=================================

* flake8 fixes (#445)

* Fix setuptools deprecations (#421)

* Contributors: Michael Carlstrom, mosfet80

examples_rclpy_pointcloud_publisher
===================================

* Fix setuptools deprecations (#421)

* Contributors: mosfet80

examples_tf2_py
===============

* fix typos (#921)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Fix Setuptools deprecations (#809)

* Contributors: Auguste Lalande, R Kent James, mosfet80

foonathan_memory_vendor
=======================

* Change upstream to fix build with clang (#80)

* Change upstream to eProsima fork to avoid patch command (#80)

* Update upstream to release 0.7-4 (#75)

* Remove installer CMake patches (#75)

* Improve mechanism to find an installation of foonathan_memory (#67)

* Fix ament_lint_cmake errors (#68)

* Add FORCE_BUILD option to cmake (#69)

* Shorten new option description (#70)

geometry2
=========

* Uniform cmake min version (#764)

* Contributors: mosfet80

geometry_msgs
=============

* Clarify "Inertia.msg" expresses inertia about the center of mass
  (#313)

* Fix CMAKE deprecation (#288)

* Removed deprecated geometry_msgs/Pose2d (#283)

* Contributors: Alejandro Hernández Cordero, Andrew Symington,
  mosfet80

gmock_vendor
============

* Deprecate gtest_vendor and gmock_vendor (#41)

* Contributors: Shane Loretz

gtest_vendor
============

* Deprecate gtest_vendor and gmock_vendor (#41)

* Contributors: Shane Loretz

gz_cmake_vendor
===============

* Bump version to 5.1.0 (#24)

* Merge pull request #23 Bump version to 5.0.2 ---------

* Bump version to 5.0.1 (#20)

* Bump version to 5.0.0 (#19)

* Jetty support: bump to 5.0.0, fix package names (#16) * Jetty
  support: bump to 5.0.0, fix package names Major version numbers have
  been removed from package names in Gazebo Jetty, so extra cmake
  config files are no longer needed. * Add option
  VENDOR_FROM_LIB_VCS_REF This allows vendoring from a specified vcs
  ref instead of the hard-coded tag. When this option is set to true,
  a branch, tag, or commit can be specified in the LIB_VCS_REF
  variable. If LIB_VCS_REF is unspecified, vendoring will use main. *
  remove unused cmake config template * use lowercase to fix linter
  complaint * 5.0.0~pre1 ---------

* Bump version to 4.2.0 (#15)

* Contributors: Addisu Z. Taddese, Jose Luis Rivero, Steve Peters

gz_math_vendor
==============

* Bump version to 9.1.0 (#20)

* Bump version to 9.0.0 (#17)

* Set PYTHONPATH for Jetty packages (#14) * Set PYTHONPATH for
  unversioned packages * Bump to 9.0.0-pre2 * Set PYTHONPATH in
  separate dsv file ---------

* Bump to 9.0.0-pre2 (#16)

* Jetty support: bump to 9.0.0, fix package names (#12) * Jetty
  support: bump to 9.0.0, fix package names Major version numbers have
  been removed from package names in Gazebo Jetty, so extra cmake
  config files are no longer needed. * Add option
  VENDOR_FROM_LIB_VCS_REF This allows vendoring from a specified vcs
  ref instead of the hard-coded tag. When this option is set to true,
  a branch, tag, or commit can be specified in the LIB_VCS_REF
  variable. If LIB_VCS_REF is unspecified, vendoring will use main. *
  remove unused cmake config file * use lowercase to fix linter
  complaint * build python bindings * 9.0.0~pre1 ---------

* Bump version to 8.2.0 (#11)

* Contributors: Addisu Z. Taddese, Ian Chen, Jose Luis Rivero, Steve
  Peters

gz_utils_vendor
===============

* Bump version to 4.0.0 (#12)

* Add dsv for PYTHONPATH for Jetty packages (#13)

* Jetty support: bump to 4.0.0, fix package names (#11) * Jetty
  support: bump to 4.0.0, fix package names Major version numbers have
  been removed from package names in Gazebo Jetty, so extra cmake
  config files are no longer needed. * Add option
  VENDOR_FROM_LIB_VCS_REF This allows vendoring from a specified vcs
  ref instead of the hard-coded tag. When this option is set to true,
  a branch, tag, or commit can be specified in the LIB_VCS_REF
  variable. If LIB_VCS_REF is unspecified, vendoring will use main. *
  remove unused cmake config file * use lowercase to fix linter
  complaint * Add dependency on cli11 * 4.0.0~pre1 * Use vendored
  version of CLI11 --------- Co-authored-by: Addisu Z. Taddese
  <addisu@openrobotics.org>
