# Humble Hawksbill changelog (part 1 of 5)

Humble Hawksbill changelog
**************************

This page is a list of the complete changes in all ROS 2 core packages
since the previous release.

Table of Contents
^^^^^^^^^^^^^^^^^

* action_msgs

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

* ament_cmake_nose

* ament_cmake_pclint

* ament_cmake_pep257

* ament_cmake_pycodestyle

* ament_cmake_pyflakes

* ament_cmake_pytest

* ament_cmake_python

* ament_cmake_ros

* ament_cmake_target_dependencies

* ament_cmake_test

* ament_cmake_uncrustify

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

* builtin_interfaces

* camera_calibration_parsers

* camera_info_manager

* class_loader

* common_interfaces

* composition

* composition_interfaces

* demo_nodes_cpp

* demo_nodes_cpp_native

* demo_nodes_py

* diagnostic_msgs

* domain_coordinator

* dummy_map_server

* dummy_robot_bringup

* dummy_sensors

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

* fastrtps_cmake_module

* geometry_msgs

* google_benchmark_vendor

* image_tools

* image_transport

* interactive_markers

* intra_process_demo

* kdl_parser

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

* libcurl_vendor

* libstatistics_collector

* libyaml_vendor

* lifecycle

* lifecycle_msgs

* lifecycle_py

* logging_demo

* message_filters

* mimick_vendor

* nav_msgs

* pendulum_control

* pendulum_msgs

* pluginlib

* pybind11_vendor

* python_cmake_module

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

* rmw_implementation_cmake

* robot_state_publisher

* ros2action

* ros2bag

* ros2cli

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

* ros2run

* ros2service

* ros2test

* ros2topic

* ros2trace

* rosbag2

* rosbag2_compression

* rosbag2_compression_zstd

* rosbag2_cpp

* rosbag2_interfaces

* rosbag2_performance_benchmarking

* rosbag2_py

* rosbag2_storage

* rosbag2_storage_default_plugins

* rosbag2_test_common

* rosbag2_tests

* rosbag2_transport

* rosgraph_msgs

* rosidl_adapter

* rosidl_cli

* rosidl_cmake

* rosidl_default_generators

* rosidl_default_runtime

* rosidl_generator_c

* rosidl_generator_cpp

* rosidl_generator_dds_idl

* rosidl_generator_py

* rosidl_parser

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

* rpyutils

* rqt_gui

* rqt_gui_cpp

* rqt_gui_py

* rqt_py_common

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

* sqlite3_vendor

* sros2

* statistics_msgs

* std_msgs

* std_srvs

* stereo_msgs

* test_cli

* test_cli_remapping

* test_communication

* test_interface_files

* test_launch_ros

* test_launch_testing

* test_msgs

* test_quality_of_service

* test_rclcpp

* test_rmw_implementation

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

* tracetools_test

* tracetools_trace

* trajectory_msgs

* turtlesim

* urdf

* urdf_parser_plugin

* visualization_msgs

* yaml_cpp_vendor

* zstd_vendor

action_msgs
===========

* Update maintainers to Chris Lalancette (#130)

* Contributors: Audrow Nash

action_tutorials_cpp
====================

* Update maintainers to Audrow Nash and Michael Jeronimo (#543)

* Contributors: Audrow Nash

action_tutorials_interfaces
===========================

* Update maintainers to Audrow Nash and Michael Jeronimo (#543)

* Contributors: Audrow Nash

action_tutorials_py
===================

* Update maintainers to Audrow Nash and Michael Jeronimo (#543)

* Contributors: Audrow Nash

actionlib_msgs
==============

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash, Grey

ament_clang_format
==================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_clang_tidy
================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* remove google style from clang-tidy default settings, removing need
  for default config file (#337)

* Improvements to ament_lint_clang_tidy. (#316)

* Contributors: Audrow Nash, Steven! Ragnarök, William Woodall

ament_cmake
===========

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Add ament_cmake_gen_version_h package (#198)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz, serge-
  nikulin

ament_cmake_auto
================

* Update forthcoming version in changelog

* Fix typo in ament_auto_find_test_dependencies (#363)

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Add ament_auto_add_gtest (#344)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Daisuke Nishimatsu,
  Joshua Whitley, Shane Loretz

ament_cmake_clang_format
========================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_cmake_clang_tidy
======================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Improvements to ament_lint_clang_tidy. (#316)

* Contributors: Audrow Nash, Steven! Ragnarök

ament_cmake_copyright
=====================

* Increase the ament_cmake_copyright default timeout. (#355)

* Update forthcoming version in changelogs

* [ament_cmake_copyright] Add file exclusion support (#328) *
  [ament_cmake_copyright] Add file exclusion support In the
  "ament_copyright" CMake function, the optional list argument
  "EXCLUDE" can now be used as an exclusion specifier. *
  [ament_cmake_copyright] Fix function header typo Remove reference to
  "cppcheck" in the "EXCLUDE" arg description.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette

ament_cmake_core
================

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Support commands with executable targets (#352)

* doc/resource_index: Indent list subitems correctly (#342)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Michal Sojka, Scott K
  Logan, Shane Loretz

ament_cmake_cppcheck
====================

* Update forthcoming version in changelogs

* [ament_cmake_cppcheck] Fix file exclusion behavior (#329) The
  "EXCLUDE" argument of the "ament_cppcheck" CMake function is a list,
  i.e. a multi-value keyword. As such, it needs to be placed out of
  the one-value keywords from the "cmake_parse_arguments" function
  call.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Add cppcheck libraries option (#323) * adding ament_cppcheck
  libraries option * pass libraries option via CMake Co-authored-by:
  William Wedler <william.wedler@resquared.com>

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Will

ament_cmake_cpplint
===================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_cmake_export_definitions
==============================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_export_dependencies
===============================

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane
  Loretz

ament_cmake_export_include_directories
======================================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_export_interfaces
=============================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_export_libraries
============================

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Add note regarding interface libraries (#339)

* Update maintainers (#336)

* Contributors: Audrow Nash, Bjar Ne, Chris Lalancette, Scott K Logan,
  Shane Loretz

ament_cmake_export_link_flags
=============================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_export_targets
==========================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_flake8
==================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Add custom config file support for flake8 (#331)

* Contributors: Audrow Nash, Kenji Miyake

ament_cmake_gen_version_h
=========================

* Add ament_generate_version_header and deprecate
  ament_cmake_gen_version_h (#377)

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Add ament_cmake_gen_version_h package (#198)

* Contributors: Audrow Nash, Shane Loretz, serge-nikulin

ament_cmake_gmock
=================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_google_benchmark
============================

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane
  Loretz

ament_cmake_gtest
=================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_include_directories
===============================

* Update forthcoming version in changelog

* Make ament_include_directories_order a function to allow paths with
  backslashes on windows. (#371) * Repalce backslashes with forward
  slashes on Windows * Typo * Replace slashes in ARGN * Don't quote *
  Check ARGN has values before trying to string(REPLACE them * Make
  ament_include_directories_order a function

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_libraries
=====================

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane
  Loretz

ament_cmake_lint_cmake
======================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_cmake_mypy
================

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N

ament_cmake_nose
================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Support commands with executable targets (#352)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_pclint
==================

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N

ament_cmake_pep257
==================

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N

ament_cmake_pycodestyle
=======================

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N

ament_cmake_pyflakes
====================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_cmake_pytest
==================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Fix misleading comment (#361)

* Use FindPython3 instead of FindPythonInterp (#355)

* Support commands with executable targets (#352)

* Mention other platforms in 'pytest/pytest-cov not found' warning
  (#337)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Christophe Bedard,
  Shane Loretz

ament_cmake_python
==================

* Use sysconfig directly to determine python lib dir (#378)

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Make ament_cmake_python symlink for symlink installs only (#357)

* Use FindPython3 instead of FindPythonInterp (#355)

* Make ament_python_install_package() match setuptools' egg names.
  (#338)

* Drop ament_cmake_python outdated tests. (#340)

* Update maintainers (#336)

* Make ament_python_install_package() install console_scripts (#328)

* Contributors: Audrow Nash, Chris Lalancette, Michel Hidalgo, Scott K
  Logan, Shane Loretz

ament_cmake_ros
===============

* Refactor domain_coordinator API to use a context manager (#12)

* Contributors: Timo Röhling

ament_cmake_target_dependencies
===============================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Fix bug packages with multiple configurations (#318)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_test
================

* Update forthcoming version in changelog

* Resolve various ament_lint linter violations (#360) We can't add
  ament_lint linters in ament_cmake in the traditional way without
  creating a circular dependency between the repositories. Even though
  we can't automatically enforce linting, it's still a good idea to
  try to keep conformance where possible.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane
  Loretz

ament_cmake_uncrustify
======================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* [ament_cmake_uncrustify] Add file exclude support (#330) In the
  "ament_uncrustify" CMake function, the optional list argument
  "EXCLUDE" can now be used as an exclusion specifier.

* Contributors: Abrar Rahman Protyasha, Audrow Nash

ament_cmake_version
===================

* Update forthcoming version in changelog

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#362)

* Use FindPython3 instead of FindPythonInterp (#355)

* Update maintainers (#336)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ament_cmake_xmllint
===================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_copyright
===============

* Fix importlib_metadata warning on Python 3.10. (#365)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* [ament_copyright] Fix file exclusion behavior (#327) *
  [ament_copyright] Fix file exclusion behavior This commit fixes the
  faulty file exclusion behavior reported in
  https://github.com/ament/ament_lint/issues/326. Specifically, the
  exclusion list is matched against traversed files in the "crawler"
  module. Changes inspired by
  https://github.com/ament/ament_lint/pull/299/. * Update excluded
  file path in copyright tests Since file names are not
  indiscriminately matched throughout the search tree anymore, the
  excluded files listed in the copyright tests need to be updated
  relative to the root of the package. * Add test cases to check
  exclusion behavior Specifically, these tests check for: - Incorrect
  exclusion of single filenames. - Correct exclusion of
  relatively/absolutely addressed filenames. - Correct exclusion of
  wildcarded paths. * Add unit tests for crawler module These unit
  tests make sure both search and exclusion behaviors are correctly
  demonstrated by the "ament_copyright.crawler" module.

* Add SPDX identifiers to the licenses. (#315)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette

ament_cppcheck
==============

* Disable cppcheck 2.x. (#345)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Add cppcheck libraries option (#323) * adding ament_cppcheck
  libraries option * pass libraries option via CMake Co-authored-by:
  William Wedler <william.wedler@resquared.com>

* Contributors: Audrow Nash, Chris Lalancette, Will

ament_cpplint
=============

* ignore NOLINT comments with categories that come from clang-tidy
  (#339)

* Update forthcoming version in changelogs

* Reapply patches Reapply parts of
  232428752251de61e84ef013bcd643e35eb9038d that are still relevant.

* Update cpplint version Point to the fork
  https://github.com/cpplint/cpplint Contains updates for modern C++
  standards (e.g. C++14 and C++17).

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* [ament_copyright] Fix file exclusion behavior (#327) *
  [ament_copyright] Fix file exclusion behavior This commit fixes the
  faulty file exclusion behavior reported in
  https://github.com/ament/ament_lint/issues/326. Specifically, the
  exclusion list is matched against traversed files in the "crawler"
  module. Changes inspired by
  https://github.com/ament/ament_lint/pull/299/. * Update excluded
  file path in copyright tests Since file names are not
  indiscriminately matched throughout the search tree anymore, the
  excluded files listed in the copyright tests need to be updated
  relative to the root of the package. * Add test cases to check
  exclusion behavior Specifically, these tests check for: - Incorrect
  exclusion of single filenames. - Correct exclusion of
  relatively/absolutely addressed filenames. - Correct exclusion of
  wildcarded paths. * Add unit tests for crawler module These unit
  tests make sure both search and exclusion behaviors are correctly
  demonstrated by the "ament_copyright.crawler" module.

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Dirk Thomas,
  Jacob Perron, William Woodall

ament_flake8
============

* Remove use of distutils.version.LooseVersion. (#346)

* Update forthcoming version in changelogs

* Ignore .*/_* dirs in ament_flake8 (#335) Other ament_* linters
  specifically ignore directories starting with a dot or underscore
  when crawling for files to lint. They also do so implicitly, so this
  change mimics that same pattern so that the behavior is consistent.

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Ignore flake8-blind-except B902 (#292)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

ament_index_cpp
===============

* Install includes to include/ (#83)

* Remove ament_export_include_directories and ament_export_libraries
  (#81)

* Contributors: Shane Loretz

ament_index_python
==================

* Print warning when get_package_share_directory() does not exist (Fix
  #74) (#77)

* Fail lookups on invalid resource names (#69)

* Add get_package_share_path method (#73)

* Contributors: David V. Lu, rob-clarke

ament_lint
==========

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_lint_auto
===============

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_lint_cmake
================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* [ament_copyright] Fix file exclusion behavior (#327) *
  [ament_copyright] Fix file exclusion behavior This commit fixes the
  faulty file exclusion behavior reported in
  https://github.com/ament/ament_lint/issues/326. Specifically, the
  exclusion list is matched against traversed files in the "crawler"
  module. Changes inspired by
  https://github.com/ament/ament_lint/pull/299/. * Update excluded
  file path in copyright tests Since file names are not
  indiscriminately matched throughout the search tree anymore, the
  excluded files listed in the copyright tests need to be updated
  relative to the root of the package. * Add test cases to check
  exclusion behavior Specifically, these tests check for: - Incorrect
  exclusion of single filenames. - Correct exclusion of
  relatively/absolutely addressed filenames. - Correct exclusion of
  wildcarded paths. * Add unit tests for crawler module These unit
  tests make sure both search and exclusion behaviors are correctly
  demonstrated by the "ament_copyright.crawler" module.

* Contributors: Abrar Rahman Protyasha, Audrow Nash

ament_lint_common
=================

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Fix typo in ament_lint_common/package.xml (#336)

* Contributors: Audrow Nash, Kenji Miyake

ament_mypy
==========

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N

ament_package
=============

* Set forthcoming for previous version

* Add support for appending to environment variables (#130) This works
  largely the same as 'prepend-non-duplicate', but instead puts the
  candidate value at the end of the target variable.

* Update maintainers to Audrow Nash (#135)

* Make python executable variable ament_package specific (#134)

* Contributors: Audrow Nash, Scott K Logan, Shane Loretz

ament_pclint
============

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* [ament_copyright] Fix file exclusion behavior (#327) *
  [ament_copyright] Fix file exclusion behavior This commit fixes the
  faulty file exclusion behavior reported in
  https://github.com/ament/ament_lint/issues/326. Specifically, the
  exclusion list is matched against traversed files in the "crawler"
  module. Changes inspired by
  https://github.com/ament/ament_lint/pull/299/. * Update excluded
  file path in copyright tests Since file names are not
  indiscriminately matched throughout the search tree anymore, the
  excluded files listed in the copyright tests need to be updated
  relative to the root of the package. * Add test cases to check
  exclusion behavior Specifically, these tests check for: - Incorrect
  exclusion of single filenames. - Correct exclusion of
  relatively/absolutely addressed filenames. - Correct exclusion of
  wildcarded paths. * Add unit tests for crawler module These unit
  tests make sure both search and exclusion behaviors are correctly
  demonstrated by the "ament_copyright.crawler" module.

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Bi0T1N

ament_pep257
============

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Remove use of distutils.version.LooseVersion. (#346)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N, Chris Lalancette

ament_pycodestyle
=================

* Improve documentation by clarifying the purpose of different tools
  (#357)

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash, Bi0T1N

ament_pyflakes
==============

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

ament_uncrustify
================

* Update forthcoming version in changelogs

* [ament_uncrustify] Fix file exclusion behavior (#334) *
  [ament_uncrustify] Fix file exclusion behavior This PR fixes the
  file exclusion behavior reported in #326. Specifically, the
  exclusion list is matched against files/directories as the search
  path is traversed. Tries to maintain consistency with #327. *
  [ament_uncrustify] Add file exclusion tests * [ament_uncrustify]
  Remove erroneous pytest marker

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* [ament_uncrustify] Add ament_lint tests (#338) * Add "ament_lint"
  tests on "ament_uncrustify" * Address linter warnings in
  "ament_uncrustify"

* Contributors: Abrar Rahman Protyasha, Audrow Nash

ament_xmllint
=============

* Update forthcoming version in changelogs

* Update maintainers to Michael Jeronimo and Michel Hidalgo (#340)

* Contributors: Audrow Nash

builtin_interfaces
==================

* Update maintainers to Chris Lalancette (#130)

* Contributors: Audrow Nash

camera_calibration_parsers
==========================

* Tests depend on rcpputils (#236)

* Remove YAML_CPP_DLL define (#231)

* Export a modern CMake target instead of variables and install
  includes to include/${PROJECT_NAME} (#218)

* Update maintainers (#173)

* Contributors: Akash, Alejandro Hernández Cordero, Shane Loretz

camera_info_manager
===================

* Export a modern CMake target instead of variables and install
  includes to include/${PROJECT_NAME} (#218)

* Update maintainers (#173)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

class_loader
============

* Install includes to include/ (#191)

* Fix include order for cpplint (#192)
