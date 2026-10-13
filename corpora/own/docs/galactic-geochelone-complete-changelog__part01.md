# Galactic Geochelone changelog (part 1 of 8)

Galactic Geochelone changelog
*****************************

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

* cyclonedds

* demo_nodes_cpp

* demo_nodes_cpp_native

* demo_nodes_py

* diagnostic_msgs

* domain_coordinator

* dummy_map_server

* dummy_robot_bringup

* dummy_sensors

* example_interfaces

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

* geometry2

* geometry_msgs

* google_benchmark_vendor

* image_common

* image_tools

* image_transport

* interactive_markers

* intra_process_demo

* kdl_parser

* laser_geometry

* launch

* launch_ros

* launch_testing

* launch_testing_ament_cmake

* launch_testing_ros

* launch_xml

* launch_yaml

* libcurl_vendor

* libstatistics_collector

* libyaml_vendor

* lifecycle

* lifecycle_msgs

* logging_demo

* map_msgs

* message_filters

* mimick_vendor

* nav_msgs

* osrf_pycommon

* osrf_testing_tools_cpp

* pendulum_control

* pendulum_msgs

* performance_test_fixture

* pluginlib

* pybind11_vendor

* python_cmake_module

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

* rcl_logging_log4cxx

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

* ros1_bridge

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

* ros2run

* ros2service

* ros2test

* ros2topic

* ros_testing

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

* rqt_top

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

* test_quality_of_service

* test_rclcpp

* test_rmw_implementation

* test_security

* test_tf2

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

* unique_identifier_msgs

* urdf

* urdf_parser_plugin

* visualization_msgs

* yaml_cpp_vendor

* zstd_vendor

action_msgs
===========

* Change index.ros.org -> docs.ros.org. (#122)

* Updating Quality Declaration (#120)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  brawner, shonigmann

action_tutorials_cpp
====================

* Update logging macros (#476)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Update goal response callback signature (#463)

* Contributors: Audrow Nash, Jacob Perron, Michael Jeronimo

action_tutorials_interfaces
===========================

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo

action_tutorials_py
===================

* Use underscores instead of dashes in setup.cfg (#502)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Ivan Santiago Paunovic, Michael Jeronimo

actionlib_msgs
==============

* Update package maintainers. (#132)

* Contributors: Michel Hidalgo

ament_clang_format
==================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Add clang-format-version option to ament_clang_format (#282)

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan, Tyler Weaver

ament_clang_tidy
================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Add multiprocessing support to ament_clang_tidy (#288) * add
  multiprocessing support * fix stylistic lint issues

* Add --packages-select argument to ament_clang_tidy (#287) Add
  comment explaining handling quoted list of space separated package
  names Update documentation for ament_clang_tidy

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, M. Mei,
  Tyler Weaver

ament_cmake
===========

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_auto
================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_clang_format
========================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_cmake_clang_tidy
======================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* add TIMEOUT argument to ament_cmake_clang_tidy (#298)

* Add Audrow as a maintainer (#294)

* Fix documentation for ament_cmake_clang_tidy (#285)

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, M. Mei,
  Tyler Weaver

ament_cmake_copyright
=====================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* increase default timeout for CMake copyright linter to 120s (#261)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Dirk
  Thomas, Scott K Logan

ament_cmake_core
================

* Merge pull request #287 from ament/mjeronimo/add-condition-support *
  Check condition attr in package.xml dependencies The condition
  attribute was already parsed when reading the XML file. Just needed
  to check the condition when adding dependencies to the list for a
  particular key/target. Fixes #266 * Address Dirk's code review
  feedback

* Address Dirk's code review feedback

* Check condition attr in package.xml dependencies The condition
  attribute was already parsed when reading the XML file. Just needed
  to check the condition when adding dependencies to the list for a
  particular key/target. Fixes #266

* Update package maintainers. (#286)

* Contributors: Michael Jeronimo, Michel Hidalgo

ament_cmake_cppcheck
====================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Increase the ament_cppcheck timeout to 5 minutes. (#271) This will
  avoid timeouts on some slower platforms that we've started to see.

* parse LANGUAGE argument case insensitive (#255)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Karsten
  Knese, Scott K Logan

ament_cmake_cpplint
===================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_cmake_export_definitions
==============================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_export_dependencies
===============================

* fix cmake list(TRANSFORM ) is only available from version 3.12,
  (#296) convert to string instead

* fix imported targets with multiple configuration (#290) * fix
  imported targets with multiple configuration * taking into account
  DEBUG_CONFIGURATIONS global variable

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo, siposcsaba89

ament_cmake_export_include_directories
======================================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_export_interfaces
=============================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_export_libraries
============================

* Fix variable name in ament_export_libraries.cmake (#314)

* Update package maintainers. (#286)

* Contributors: Alejandro Hernández Cordero, Michel Hidalgo

ament_cmake_export_link_flags
=============================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_export_targets
==========================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_flake8
==================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang

ament_cmake_gmock
=================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_google_benchmark
============================

* Serialize benchmarks within CTest by default (#308)

* Handle runtime failures in Google Benchmark (#294) This change will
  handle runtime failures in Google Benchmark by propagating error
  information from Google Benchmark to both CTest and the Jenkins
  benchmark plugin.

* Use consistent string format and resolve flake8 (#295) Follow-up to
  a5fb3112b5c46c42b1824c96af4171d469eb13bf

* Make ament_cmake_test a dep of ament_cmake_google_benchmark (#293)

* Catch JSONDecodeError and printout some debug info (#291)

* Update package maintainers. (#286)

* Make AMENT_RUN_PERFORMANCE_TESTS a CMake option (#280)

* Skip performance tests using a CMake variable (#278) These tests can
  be fairly heavy, so we don't want to run them by default. It would
  be better if there was a way to skip the tests by default in such a
  way that they could be specifically un-skipped at runtime, but I
  can't find a mechanism in CMake or CTest that would allow us to
  achieve that behavior without leveraging environment variables.

* Handle Google Benchmark 'aggregate' results (#276) Previously, I
  assumed all results generated by Google Benchmark were of
  'iteration' type. Now that I have more experience with Google
  Benchmark, I've started generating aggregate results, which contain
  some different properties. This change adds support for aggregate
  results and should make it easy to add any other result schemas we
  encounter in the future. For forward-compatibility, unsupported
  types will generate a warning message but will not fail the test.
  This makes the conversion tolerant to Google Benchmark adding new
  measures for existing mechanisms.

* Initial Google Benchmark results conversion (#275)

* Handle missing results file for Google Benchmark (#265)

* Initial ament_cmake_google_benchmark package (#261)

* Contributors: Michel Hidalgo, Scott K Logan, brawner

ament_cmake_gtest
=================

* Disable gtest warning when building in Release (#298)
  https://github.com/google/googletest/issues/1303

* Update package maintainers. (#286)

* [ament_cmake_gtest] ensure gtest to consume the correct headers.
  (#267) * ensure gtest to consume the correct headers. * add another
  patch.

* Contributors: Michel Hidalgo, Sean Yen, Victor Lopez

ament_cmake_include_directories
===============================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_libraries
=====================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_lint_cmake
======================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* ament_lint_cmake: default linelength in argumentparser for
  consistency (#306)

* 0.10.3

* Fix ament_lint_cmake line length expression (#236) This regular
  expression is using the re.VERBOSE flag, meaning that characters
  after an un-escaped '#' character are interpreted as a comment and
  are not part of the expression. Also set the default maximum line
  length to 140 columns.

* Add Audrow as a maintainer (#294)

* Make CMake linter line length configurable (#235) Co-authored-by:
  Miaofei <miaofei@amazon.com>

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Emerson
  Knapp, Scott K Logan

ament_cmake_mypy
================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang

ament_cmake_nose
================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_pclint
==================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_cmake_pep257
==================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_cmake_pycodestyle
=======================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_cmake_pyflakes
====================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_cmake_pytest
==================

* Fix ament_get_pytest_cov_version for newer versions of pytest (#315)

* Update package maintainers. (#286)

* Contributors: Christophe Bedard, Michel Hidalgo

ament_cmake_python
==================

* Symlink setup.cfg and sources before building Python egg-info (#327)

* Simplify ament_python_install_package() macro. (#326) Do not
  delegate to setuptools, install egg-info manually.

* Escape $ENV{DESTDIR} everywhere in ament_python_install_package()
  (#324) Follow up after f80071e2216e766f7bf1b0792493a5f6523e9226

* Use DESTDIR on ament_python_install_package() (#323) * Use DESTDIR
  on ament_python_install_package()

* Make ament_python_install_package() install a flat Python egg (#316)

* [ament_cmake_python] ament_cmake_python_get_python_install_dir
  public (#300) * [ament_cmake_python] make the
  ament_cmake_python_get_python_install_dir a public interface.

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo, Naveau

ament_cmake_ros
===============

* Update package maintainers. (#11)

* Contributors: Michel Hidalgo

ament_cmake_target_dependencies
===============================

* Force SYSTEM keyword in ament_target_dependencies() at the start.
  (#303)

* Add SYSTEM keyword option to ament_target_dependencies (#297) * Add
  SYSTEM keyword option to ament_target_dependencies * Add
  documentation of SYSTEM keyword for ament_target_dependencies

* Update package maintainers. (#286)

* ordered interface include dirs and use privately to ensure workspace
  order (#260)

* Contributors: Andre Nguyen, Dirk Thomas, Michel Hidalgo

ament_cmake_test
================

* Update package maintainers. (#286)

* Fix skipped test reporting in CTest (#279) This is a follow-up to
  c67cdf2. When the SKIP_RETURN_CODE gets set to 0, the value is
  interpreted as 'false', and the test property is never actually
  added.

* limit test time to three decimals (#271)

* Add actual test time to xUnit result files (#270) * Add actual test
  time to xUnit result files Fixes #269 * Report test_time even with
  skipped test * Set time attribute for testcase element

* Add SKIP_RETURN_CODE argument to ament_add_test (#264) This makes
  the "run_test.py" wrapper aware of the "SKIP_RETURN_CODE" property
  on CTest tests. In the existing implementation, the wrapper detects
  that no result file was generated and overrides the special return
  code coming from the test, making the the CTest feature fail
  completely. This change makes the wrapper script aware of the
  special return code, and when detected, will write a 'skipped'
  result file instead of a 'failed' result file, and pass along the
  special return code as-is. Now the gtest result and the ctest
  results both show the test as 'skipped' when the special return flag
  is used. Note that none of this behavior is enabled by default,
  which is important because we wouldn't want a test to fail and
  return a code which we've decided is the special 'skip' return code.
  Only tests which are aware of this feature should use it.

* Contributors: Dirk Thomas, Michel Hidalgo, Ruffin, Scott K Logan

ament_cmake_uncrustify
======================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* parse LANGUAGE argument case insensitive (#255)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Karsten
  Knese, Scott K Logan

ament_cmake_version
===================

* Update package maintainers. (#286)

* Contributors: Michel Hidalgo

ament_cmake_xmllint
===================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_copyright
===============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* Use non-blind except for open() (#307)

* Add optional file header style (#304) * Add optional file header
  style * Fix test on ament_copyright

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* add mit-0 as a valid license to ament_copyright (#284)

* Support Python 3.8-provided importlib.metadata (#290) The
  importlib_metadata package is a backport of the importlib.metadata
  module from Python 3.8. Fedora (and possibly others) no longer
  package importlib_metadata because they ship Python versions which
  have the functionality built-in.

* Update maintainer (#274) * update maintainer * add authors

* added bsd 2 clause simplified license to ament_copyright (#267) *
  added bsd 2 clause simplified license to ament_copyright

* Remove use of pkg_resources from ament_lint. (#260) Replace it with
  the use of the more modern importlib_metadata library. There are a
  couple of reasons to do this: 1. pkg_resources is quite slow to
  import; on my machine, just firing up the python interpreter takes
  ~35ms, while firing up the python interpreter and importing
  pkg_resources takes ~175ms. Firing up the python interpreter and
  importing importlib_metadata takes ~70ms. Removing 100ms per
  invocation of the command-line both makes it speedier for users, and
  will speed up our tests (which call out to the command-line quite a
  lot). 2. pkg_resources is somewhat deprecated and being replaced by
  importlib. https://importlib-
  metadata.readthedocs.io/en/latest/using.html describes some of it
  Note: By itself, this change is not enough to completely remove our
  dependence on pkg_resources. We'll also have to do something about
  the console_scripts that setup.py generates. That will be a
  separate effort.

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Alfi Maulana, Audrow Nash, Chris Lalancette,
  Christophe Bedard, Claire Wang, Evan Flynn, M. Mei, Scott K Logan

ament_cppcheck
==============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Fix file exclusion behavior in ament_cppcheck and ament_cpplint
  (#299) * fix exclude behavior in ament_cppcheck and ament_cpplint *
  fix flake8 errors * add missing realpath() conversion

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Suppress unknownMacro (#268) cppcheck creates an unknownMacro error
  when it cannot resolve a macro. Since we don't pass in all dependent
  headers, we don't expect all macros to be discoverable by cppcheck.

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Dan Rose,
  M. Mei, Scott K Logan

ament_cpplint
=============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Fix file exclusion behavior in ament_cppcheck and ament_cpplint
  (#299) * fix exclude behavior in ament_cppcheck and ament_cpplint *
  fix flake8 errors * add missing realpath() conversion

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, M. Mei,
  Scott K Logan

ament_flake8
============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang

ament_index_cpp
===============

* Remove Claire as the maintainer. (#71)

* Change links from index.ros.org -> docs.ros.org (#70)

* Add Audrow as a maintainer (#68)

* update maintainers (#67)

* Update QD to Quality Level 1 (#66)

* add rational why ament_index pkgs don't have explicit performance
  tests (#65)

* Fixed Doxygen warnings (#63)

* Remove the Quality Level from the README.md. (#62)

* Update QD ament_index_cpp to QL 2 (#59)

* Add Security Vulnerability Policy pointing to REP-2006. (#57)

* [Quality Declaration] Update Version Stability to stable version
  (#58)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris
  Lalancette, Claire Wang, Dirk Thomas, brawner

ament_index_python
==================

* Remove Claire as the maintainer. (#71)

* Change links from index.ros.org -> docs.ros.org (#70)

* Add Audrow as a maintainer (#68)

* update maintainers (#67)

* add rational why ament_index pkgs don't have explicit performance
  tests (#65)

* Remove the Quality Level from the README.md. (#62)

* Fix document link (#61)

* [Quality Declaration] Update Version Stability to stable version
  (#58)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris
  Lalancette, Claire Wang, Dirk Thomas, Matthijs van der Burgh
