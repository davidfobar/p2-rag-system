# ROS 2 Kilted Kaiju Complete Changelog (part 1 of 5)

ROS 2 Kilted Kaiju Complete Changelog
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

* ament_cmake_auto

* ament_cmake_core

* ament_cmake_gen_version_h

* ament_cmake_gtest

* ament_cmake_pytest

* ament_cmake_ros

* ament_cmake_ros_core

* ament_cmake_target_dependencies

* ament_cmake_vendor_package

* ament_copyright

* ament_cppcheck

* ament_cpplint

* ament_flake8

* ament_index_python

* ament_lint_auto

* ament_lint_cmake

* ament_mypy

* ament_package

* ament_pclint

* ament_pycodestyle

* ament_pyflakes

* ament_uncrustify

* ament_xmllint

* builtin_interfaces

* camera_calibration_parsers

* camera_info_manager

* camera_info_manager_py

* composition

* demo_nodes_cpp

* demo_nodes_cpp_native

* demo_nodes_py

* domain_coordinator

* dummy_map_server

* dummy_robot_bringup

* dummy_sensors

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

* google_benchmark_vendor

* gtest_vendor

* gz_cmake_vendor

* gz_math_vendor

* gz_utils_vendor

* image_tools

* image_transport

* image_transport_py

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

* liblz4_vendor

* libstatistics_collector

* libyaml_vendor

* lifecycle

* lifecycle_py

* logging_demo

* lttngpy

* mcap_vendor

* message_filters

* mimick_vendor

* nav_msgs

* orocos_kdl_vendor

* osrf_pycommon

* osrf_testing_tools_cpp

* pendulum_control

* pendulum_msgs

* performance_test_fixture

* pluginlib

* point_cloud_transport

* point_cloud_transport_py

* python_orocos_kdl_vendor

* python_qt_binding

* qt_dotgraph

* qt_gui_cpp

* quality_of_service_demo_cpp

* quality_of_service_demo_py

* rcl

* rcl_action

* rcl_lifecycle

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

* rmw_security_common

* rmw_test_fixture

* rmw_test_fixture_implementation

* rmw_zenoh_cpp

* robot_state_publisher

* ros2action

* ros2bag

* ros2cli

* ros2doctor

* ros2launch

* ros2lifecycle

* ros2lifecycle_test_fixtures

* ros2node

* ros2param

* ros2pkg

* ros2run

* ros2service

* ros2test

* ros2topic

* ros2trace

* ros_environment

* rosbag2

* rosbag2_compression

* rosbag2_cpp

* rosbag2_examples_cpp

* rosbag2_examples_py

* rosbag2_py

* rosbag2_storage

* rosbag2_storage_mcap

* rosbag2_storage_sqlite3

* rosbag2_test_common

* rosbag2_test_msgdefs

* rosbag2_tests

* rosbag2_transport

* rosidl_adapter

* rosidl_cli

* rosidl_core_generators

* rosidl_core_runtime

* rosidl_default_runtime

* rosidl_dynamic_typesupport

* rosidl_dynamic_typesupport_fastrtps

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

* rqt_bag

* rqt_bag_plugins

* rqt_console

* rqt_graph

* rqt_gui

* rqt_gui_cpp

* rqt_gui_py

* rqt_plot

* rqt_publisher

* rqt_py_common

* rqt_py_console

* rqt_service_caller

* rqt_shell

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

* rviz_resource_interfaces

* rviz_visual_testing_framework

* sensor_msgs

* sensor_msgs_py

* service_msgs

* sqlite3_vendor

* sros2

* test_cli

* test_cli_remapping

* test_communication

* test_interface_files

* test_launch_ros

* test_msgs

* test_osrf_testing_tools_cpp

* test_quality_of_service

* test_rclcpp

* test_rmw_implementation

* test_ros2trace

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

* turtlesim

* turtlesim_msgs

* type_description_interfaces

* unique_identifier_msgs

* urdf

* urdf_parser_plugin

* zenoh_cpp_vendor

* zenoh_security_tools

action_msgs
===========

* Add missing build_export_depend on rosidl_core_runtime (#165)

* Contributors: Scott K Logan

action_tutorials_cpp
====================

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Update action cpp demos to support setting introspection (#709) *
  Update action cpp demos to support setting introspection * Add the
  missing header file declaration ---------

* Remove action_tutorials_interfaces. (#701)

* Removed outdated comment (#699)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, mosfet80

action_tutorials_py
===================

* Update action python demos to support setting introspection (#708) *
  Update action python demos to support setting introspection *
  Correct the errors in the document ---------

* Add test_xmllint.py to all of the ament_python packages. (#704)

* Remove action_tutorials_interfaces. (#701)

* Change all of the demos to use the new rclpy context manager. (#694)

* Contributors: Barry Xu, Chris Lalancette

ament_clang_format
==================

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_clang_tidy
================

* Add ament_xmllint testing for all packages that we can. (#508)

* ament_clang_tidy - Fix Reporting when WarningsAsErrors is specified
  in config (#397)

* Contributors: Chris Lalancette, Matt Condino

ament_cmake_auto
================

* Fix headers destination installed by ament_auto_package (#540)

* Add ament_auto_depend_on_packages to replace
  ament_target_dependencies (#571)

* More specific prefix in some cmake_parse_argument calls (#523)

* Contributors: Kevin Egger, Kotaro Yoshimoto, Shane Loretz

ament_cmake_core
================

* Create destination directory during symlink install (#569)

* Support generator expressions when symlinking install(FILES) (#560)

* Always symlink TARGET_{LINKER,SONAME}_FILE on libraries (#535)

* Fix symlink install of versioned libs on macOS (#558)

* More specific prefix in some cmake_parse_argument calls (#523)

* Contributors: Ezra Brooks, Kevin Egger, Scott K Logan

ament_cmake_gen_version_h
=========================

* Add ALL target for ament_generate_version_header target. (#526)

* Contributors: Chris Lalancette

ament_cmake_gtest
=================

* set search path args and then append (#543)

* Contributors: Will

ament_cmake_pytest
==================

* Don't write Python bytecode when invoking pytest (#533)

* Contributors: Scott K Logan

ament_cmake_ros
===============

* Add ament_add_ros_isolated_{gmock,gtest}_test macros (#29)

* Switch from 'domain_coordinator' to 'rmw_test_fixture' (#28)

* Add ament_add_ros_isolated_test function (#27)

* Split generic parts of ament_cmake_ros into _core package (#20)

* Contributors: Scott K Logan

ament_cmake_ros_core
====================

* Add missing build_export_depend on ament_cmake_libraries (#37)

* Split generic parts of ament_cmake_ros into _core package (#20)

* Contributors: Scott K Logan

ament_cmake_target_dependencies
===============================

* Deprecate ament_target_dependencies() (#572)

* Contributors: Shane Loretz

ament_cmake_vendor_package
==========================

* Add explicit git dependency from ament_cmake_vendor_package (#554)

* Contributors: Scott K Logan

ament_copyright
===============

* Improve ament_copyright performance drastically. (#515)

* Fix error path for search_copyright_information. (#491)

* Contributors: Chris Lalancette

ament_cppcheck
==============

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_cpplint
=============

* Enable a quiet mode for cpplint (#532)

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette, Nils-Christian Iseke

ament_flake8
============

* Add the rest of the flake8 plugins as dependencies. (#503)

* Contributors: Chris Lalancette

ament_index_python
==================

* Add py.typed to package_data (#100)

* Add test_xmllint to ament_index_python. (#96)

* Add ament_mypy unit test and export types (#95)

* Contributors: Chris Lalancette, Michael Carlstrom

ament_lint_auto
===============

* Add docu for AMENT_LINT_AUTO_EXCLUDE (#524)

* Contributors: Alexander Reimann

ament_lint_cmake
================

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_mypy
==========

* Fix Windows Regression by removing removesuffix() (#530)

* Export typing information (#487)

* Add support for type stubs (#516)

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette, Michael Carlstrom

ament_package
=============

* Simplify removing leading and trailing separators (#152)

* Remove CODEOWNERS and mirror-rolling-to-master. (#149)

* Always consider .dsv files, even when no shell specific script
  exists (#147)

* Contributors: Addisu Z. Taddese, Chris Lalancette, Rob Woolley

ament_pclint
============

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_pycodestyle
=================

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_pyflakes
==============

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_uncrustify
================

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

ament_xmllint
=============

* Add ament_xmllint testing for all packages that we can. (#508)

* Contributors: Chris Lalancette

builtin_interfaces
==================

* Add missing build_export_depend on rosidl_core_runtime (#165)

* Contributors: Scott K Logan

camera_calibration_parsers
==========================

* Use target_link_libraries instead of ament_target_dependencies
  (#345)

* Added common linters to camera_calibration_parsers (#317)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

camera_info_manager
===================

* Add optional namespace to /set_camera_info service in
  CameraInfoManager (#324)

* Added common test to camera info manager (#318)

* Contributors: Alejandro Hernández Cordero, Jan Hernas

camera_info_manager_py
======================

* Cleanup of camera_info_manager_py. (#340)

* Add "camera_info_manager_py" (#335)

* Bump package version to synchronize with image_common

* Ros2 (#2) * Run magic converter * Ament_python package * Fix some
  imports * Remove references to cpp camera info manager. Disable
  tests * Linting * Fully Remove old tests * Add lint tests * Final
  tests * Remove pep257 from depends

* changelog

* added CPR maintainer

* Release to Melodic and Noetic

* Only use rostest when testing enabled, thanks to Lukas Bulwahn.

* Move repository to ros-perception.

* Add namespace parameter to constructor, so a driver can handle
  multiple cameras. Enhancement thanks to Martin Llofriu.

* Make unit tests conditional on "CATKIN_ENABLE_TESTING".

* Release to Groovy and Hydro.

* Set null calibration even when URL invalid (#7).

* Release to Groovy and Hydro.

* Convert to catkin.

* Remove roslib dependency.

* Release to Groovy and Hydro.

* Initial Python camera_info_manager release to Fuerte.

* Contributors: Alejandro Hernández Cordero, Chris Iverach-Brereton,
  Chris Lalancette, Jack O'Quin, José Mastrangelo, Lucas Walter, Lukas
  Bulwahn, Martin Pecka, Michael Hosmar, mllofriu

composition
===========

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Fix typo in composition comment (#703)

* Change references from "jazzy" to "rolling" on the rolling branch.
  (#687)

* [composition] add launch action console output in the verify section
  (#677)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Mikael Arguedas, Shane Loretz, mosfet80

demo_nodes_cpp
==============

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* [demo_nodes_cpp] some readme and executable name fixups (#678)

* Fix gcc warnings when building with optimizations. (#672)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Mikael
  Arguedas, mosfet80

demo_nodes_cpp_native
=====================

* Uniform CMAKE min VERSION (#714)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Shane Loretz, mosfet80

demo_nodes_py
=============

* Revert "Revert "fix loading parameter behavior from yaml file.
  (#656)" (#660)" (#661)

* Add test_xmllint.py to all of the ament_python packages. (#704)

* Change all of the demos to use the new rclpy context manager. (#694)

* Contributors: Chris Lalancette, Tomoya Fujita

domain_coordinator
==================

* Add test_xmllint to domain_coordinator. (#17)

* Contributors: Chris Lalancette

dummy_map_server
================

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Shane Loretz, mosfet80

dummy_robot_bringup
===================

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Contributors: mosfet80

dummy_sensors
=============

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Update dummy_sensors readme to echo the correct topic (#675)

* Contributors: Shane Loretz, jmackay2, mosfet80

examples_rclcpp_async_client
============================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_cbg_executor
============================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_minimal_action_client
=====================================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Removed outdated comment (#388)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

examples_rclcpp_minimal_action_server
=====================================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Removed outdated comment (#388)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

examples_rclcpp_minimal_client
==============================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_minimal_composition
===================================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_minimal_publisher
=================================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_minimal_service
===============================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_minimal_subscriber
==================================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_minimal_timer
=============================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_multithreaded_executor
======================================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclcpp_wait_set
========================

* Use target_link_libraries instead of ament_target_dependencies
  (#404)

* Contributors: Shane Loretz

examples_rclpy_executors
========================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_rclpy_guard_conditions
===============================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_rclpy_minimal_action_client
====================================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_rclpy_minimal_action_server
====================================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Add guard on Python single goal action server example (#380)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette, Ruddick Lawrence

examples_rclpy_minimal_client
=============================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Use a single executor instance for spinning in
  client_async_callback. (#382)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_rclpy_minimal_publisher
================================

* Address flake8 errors for examples_rclpy_minimal_publisher (#410)

* Add publisher_member_function_with_wait_for_all_acked.py (#407)

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette, Tomoya Fujita

examples_rclpy_minimal_service
==============================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_rclpy_minimal_subscriber
=================================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_rclpy_pointcloud_publisher
===================================

* Add in ament_xmllint for the ament_python packages. (#397)

* Switch to using the rclpy context manager everywhere. (#389)

* Update the shutdown handling in all of the Python examples. (#379)

* Contributors: Chris Lalancette

examples_tf2_py
===============

* Add in test_xmllint for geometry2 python packages. (#725)

* Switch to using a context manager for the python examples. (#700)
  That way we can be sure to always clean up, but use less code doing
  so.

* Contributors: Chris Lalancette

foonathan_memory_vendor
=======================

* Improve mechanism to find an installation of foonathan_memory (#67)

geometry2
=========

* Uniform cmake min version (#764)

* Contributors: mosfet80

geometry_msgs
=============

* Complete Removal of PoseStampedArray (#270)

* Move geometry_msgs/PoseStampedArray to nav_msgs/Goals (#269)

* Add PoseStampedArray (#262)

* Contributors: Tony Najjar, Tully Foote

gmock_vendor
============

* Bump minimum CMake version to 3.15 (#31)

* Contributors: mosfet80

google_benchmark_vendor
=======================

* Bump minimum CMake version to 3.10 (#35)

* Remove CODEOWNERS and mirror-rolling-to-main workflow. (#31)

* Contributors: Chris Lalancette, mosfet80

gtest_vendor
============

* Bump minimum CMake version to 3.15 (#33)

* Contributors: mosfet80

gz_cmake_vendor
===============

* Bump version to 4.1.1 (#13)

* Bump version to 4.1.0 (#11)

* Bump version to 4.0.0 (#10)

* Fixes the cmake-config used during find_package (#8) The provided
  cmake-config was not actually working if one did "`
  find_package(gz_cmake_vendor) find_package(gz-cmake) `" This because
  the config file tried to create aliases to targets that don't exist.
  For example, gz-cmake4::gz-cmake4 is not exported by gz-cmake.

* Remove the BUILD_DOCS cmake argument. (#9) It is apparently
  deprecated in newer Gazebo.

* Apply prerelease suffix and remove patch (#7)

* Upgrade to Ionic

* Contributors: Addisu Z. Taddese, Chris Lalancette, Steve Peters

gz_math_vendor
==============

* Bump version to 8.1.1 (#10)

* Bump version to 8.1.0 (#8) * This is a rerelease since #7 did not
  actually bump the version of the vendored package.

* Bump version to 8.1.0 (#7)

* Bump version to 8.0.0 (#5)

* Apply prerelease suffix (#4)

* Upgrade to Ionic

* Update vendored package version to 7.5.0

* Contributors: Addisu Z. Taddese, Carlos Agüero, Michael Carroll

gz_utils_vendor
===============

* Bump version to 3.1.1 (#10)

* Bump version to 3.1.0 (#8)

* Bump version to 3.0.0 (#7)

* Add in a dependency on spdlog_vendor. (#6) * Add in a dependency on
  spdlog_vendor. That way when building on e.g. Windows, the paths to
  spdlog will be setup properly before trying to build this vendor
  package. * Also remove the spdlog dependency. That's because we will
  just depend on the vendor package to provide that dependency for us
  as necessary. ---------

* Remove the BUILD_DOCS cmake argument. (#5) It is apparently
  deprecated in newer Gazebo.

* Apply prerelease suffix (#4)

* Upgrade to Ionic

* Contributors: Addisu Z. Taddese, Carlos Agüero, Chris Lalancette,
  Michael Carroll

image_tools
===========

* Uniform CMAKE min VERSION (#714)

* Lint image_tools/CMakeLists.txt (#712)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Contributors: Alejandro Hernández Cordero, mosfet80, yadunund

image_transport
===============

* Remove windows warnings (#350)

* Add "rclcpp::shutdown" (#347)

* Use target_link_libraries instead of ament_target_dependencies
  (#345)

* feat: python bindings for image_transport and publish (#323) Co-
  authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>

* Apply remappings to base topic before creating transport-specific
  topics (#326)

* Add lazy subscription to republisher (#325)

* Fix node name (#321)

* Updated deprecated message filter headers (#320)

* Removed outdated comment (#319)

* Preparing for qos deprecation (#315)

* Removed warning (#312)

* Support zero-copy intra-process publishing (#306)

* Add missing sub and pub options (#308) Co-authored-by: Angsa
  Deployment Team <team@angsa-robotics.com>

* Contributors: Alejandro Hernández Cordero, Błażej Sowa, Földi Tamás,
  Lucas Wendland, Michal Sojka, Shane Loretz, Tony Najjar, Yuyuan Yuan

image_transport_py
==================

* Add in python3-dev build dependency (#334)

* feat: python bindings for image_transport and publish (#323) Co-
  authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>

* Contributors: Chris Lalancette, Földi Tamás

interactive_markers
===================

* Deprecating tf2 C Headers (#109)

* Remove CODEOWNERS and mirror-rolling-to-main workflow (#110)

* Use non deprecated API (#108)

* Contributors: Alejandro Hernández Cordero, Lucas Wendland

intra_process_demo
==================

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Removed pre-compiler check for opencv3 (#695)

* [intra_process_demo] executable name in README.md fix-up (#690)

* Contributors: Alejandro Hernández Cordero, Trushant Adeshara,
  mosfet80

kdl_parser
==========

* update urdf model header (#85)

* Contributors: Alejandro Hernández Cordero

laser_geometry
==============

* Deprecating tf2 C Headers (#98)

* Remove CODEOWNERS and mirror-rolling-to-main workflow (#100)

* Stop using python_cmake_module. (#93)

* Added common linters (#96)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Lucas
  Wendland

launch
======

* Provide copy of launch configs to TimerAction's entities (#836)

* Allow concatenating each path component of PathJoinSubstitution
  (#838)

* Add StringJoinSubstitution substitution (#843)

* Add missing test_depend for launch (#850)

* Document substitutions concatenation in architecture doc (#845)

* Update docs to use proper RST literals (#837)

* Fix function params indentation (#833)

* Add ForEach action to repeat entities using iteration-specific
  values (#802)

* Create py.typed (#828)

* Improve error reporting by adding file locations to exceptions
  (#823)

* add test coverage for substitution edgecases involving E notation
  (#824)

* Cleanup the launch dependencies. (#819)

* Fix 'set up' typo (#813)

* Add test_xmllint to all of the ament_python packages. (#804)

* Fix typo in comment (#783)

* Contributors: Chris Lalancette, Christian Ruf, Christophe Bedard,
  Michael Carlstrom, Roland Arsenault, danielcranston

launch_pytest
=============

* Cleanup the launch dependencies. (#819)

* Add test_xmllint to all of the ament_python packages. (#804)

* Switch to using an rclpy context manager. (#787)

* Contributors: Chris Lalancette

launch_ros
==========

* Remove the slash stripping since leading slash matters (#456)

* Fixing lifecycle node autostart issue #445 (#449)

* Change docstring markdown code blocks to RST (#450)

* Autostarting lifecycle nodes and example launch file demo (#430)

* Add YAML dumper representator for str type to keep quotes always.
  (#436)

* Mock launch components causing rosdoc2 to fail Python API (#425)

* Add ament_xmllint to the ament_python packages. (#423)

* Fix url in setup.py (#413)

* Contributors: Chris Lalancette, Christophe Bedard, Olivia/F.F., R
  Kent James, Steve Macenski, Tomoya Fujita, Wei HU

launch_testing
==============

* Fix function params indentation (#833)

* Cleanup the launch dependencies. (#819)

* Add test_xmllint to all of the ament_python packages. (#804)

* Add mechanism to disable workaround for dependency groups (#775)

* Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan

launch_testing_ament_cmake
==========================

* Add CMake parameter to override launch_testing module (#854)

* Stop using python_cmake_module. (#760)

* Don't write Python bytecode when invoking launch tests (#785)

* Contributors: Chris Lalancette, Scott K Logan

launch_testing_examples
=======================

* Add test_xmllint.py. (#401)

* Contributors: Chris Lalancette

launch_testing_ros
==================

* "WaitForTopics": let the user inject a trigger function to be
  executed after starting the subscribers (#356)

* Add EnableRmwIsolation action for starting rmw_test_fixture (#459)

* Fix function params indentation (#446)

* Add ament_xmllint to the ament_python packages. (#423)

* Switch to use rclpy.init context manager. (#402)

* Contributors: Chris Lalancette, Christophe Bedard, Giorgio Pintaudi,
  Scott K Logan

launch_xml
==========

* Add ForEach action to repeat entities using iteration-specific
  values (#802)

* Stop loading extensions during launch_{xml,yaml} tests. (#820)

* Cleanup the launch dependencies. (#819)

* Add test_xmllint to all of the ament_python packages. (#804)

* Contributors: Chris Lalancette, Christophe Bedard

launch_yaml
===========

* Add ForEach action to repeat entities using iteration-specific
  values (#802)

* Stop loading extensions during launch_{xml,yaml} tests. (#820)

* Cleanup the launch dependencies. (#819)

* Add test_xmllint to all of the ament_python packages. (#804)

* Contributors: Chris Lalancette, Christophe Bedard

libcurl_vendor
==============

* uniform MinCMakeVersion (#108)

* Add "lib" to the Windows curl search path. (#96) In CMake 3.3, a
  commit made it so that the find_package module in CMake had a
  compatibility mode where it would automatically search for packages
  in a <prefix>/lib subdirectory. In CMake 3.6, this compatibility
  mode was reverted for all platforms *except* Windows. That means
  that since CMake 3.3, we haven't actually been using the path as
  specified in "curl_DIR", but we have instead been inadvertently
  relying on that fallback behavior. In CMake 3.28, that compatibilty
  mode was also removed for Windows, meaning that we are now failing
  to find_package(curl) in downstream packages (like
  resource_retriever). Fix this by adding in the "lib" directory that
  always should have been there. I'll note that this *only* affects
  our Windows builds, because this code is in a if(WIN32) block.

* Contributors: Chris Lalancette, mosfet80

liblz4_vendor
=============

* Add in a library prefix for lz4 from conda on Windows. (#1846)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

libstatistics_collector
=======================

* Bump codecov/codecov-action from 4.5.0 to 4.6.0

* Fix MovingAverageStatistics::max_ Default Value (#201)

* Removed deprecated classes (#200)

* fix: add void annotation (#194)

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu,
  Jeffery Hsu, dependabot[bot]

libyaml_vendor
==============

* Only set CRT_SECURE_NO_WARNINGS if it hasn't already been set. (#64)

* Contributors: Chris Lalancette

lifecycle
=========

* Uniform CMAKE min VERSION (#714)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Shane Loretz, mosfet80

lifecycle_py
============

* Add test_xmllint.py to all of the ament_python packages. (#704)

* Change all of the demos to use the new rclpy context manager. (#694)

* Contributors: Chris Lalancette

logging_demo
============

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Alejandro Hernández Cordero, Shane Loretz, mosfet80

lttngpy
=======

* Remove SHARED from pybind11_add_module (#154)

* Add python3-dev build_depend to lttngpy. (#146)

* Don't try to build on BSD (#142)

* Allow enabling syscalls through "ros2 trace" or the Trace action
  (#137)

* Remove python_cmake_module use. (#91)

* Add missing dependency on pkg-config to lttngpy (#130)

* Contributors: Chris Lalancette, Christophe Bedard, Nathan Wiebe
  Neufeldt, Scott K Logan, Silvio Traversaro

mcap_vendor
===========

* Update mcap (#1774) Update mcap cpp to last version
