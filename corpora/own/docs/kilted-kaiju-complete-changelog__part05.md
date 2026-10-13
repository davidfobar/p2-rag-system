# ROS 2 Kilted Kaiju Complete Changelog (part 5 of 5)

* Contributors: Chris Lalancette

test_communication
==================

* Use EnableRmwIsolation in launch tests (#571)

* Switch to isolated test fixture macros (#571)

* Add tests for Keyed types (#568)

* Remove use of ament_target_dependencies (#566)

* Skip all multi-vendor pub/sub tests with zenoh (#560)

* Stop using python_cmake_module. (#536)

* Use rclpy.init context manager where we can. (#547) This allows us
  to cleanup, while using a lot less code to try and track it.

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Francisco Gallego Salido, Scott K Logan, Shane Loretz, yadunund

test_interface_files
====================

* Drop long double from the IDL. (#22)

* Contributors: Chris Lalancette

test_launch_ros
===============

* Add python3-pytest-timeout to test_launch_ros. (#454)

* Autostarting lifecycle nodes and example launch file demo (#430)

* Add ament_xmllint to the ament_python packages. (#423)

* Add in a timeout for test_launch_ros. (#417)

* Fix url in setup.py (#413)

* Revamp the test_load_composable_nodes test. (#403)

* Switch to use rclpy.init context manager. (#402)

* Contributors: Chris Lalancette, Steve Macenski, Tomoya Fujita, Wei
  HU

test_msgs
=========

* Added test messages with keys (#173)

* Contributors: Francisco Gallego Salido

test_osrf_testing_tools_cpp
===========================

* Update CMakeLists.txt (#85)

* Contributors: mosfet80

test_quality_of_service
=======================

* Switch to isolated test fixture macros (#571)

* Use rmw_event_type_is_supported to skip tests (#563)

* Fixed some qos test related with Zenoh (#551)

* Contributors: Alejandro Hernández Cordero, Scott K Logan

test_rclcpp
===========

* Use EnableRmwIsolation in launch tests (#571)

* Ensure test verifies the existence of all spawning nodes (#558)

* chore: Adopted to API changes in rclcpp (#556)

* Implement the pure-virtual functions in the Waitable class. (#548)

* Update deprecated methods (#546)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Janosch
  Machowinski, Scott K Logan, Yuyuan Yuan

test_rmw_implementation
=======================

* Added rmw_event_type_is_supported (#250) * Added
  rmw_event_check_compatible * fix return typoe * updated name and use
  in wait_set test ---------

* Update expectations of tests to remain compatible with non-DDS
  middlewares (#248)

* use rmw_enclave_options_xxx APIs instead. (#247)

* Fix up some overwritten errors. (#246) That is, make sure to clear
  out errors where we should. We also slightly rewrite some of the
  testing around unsupported APIs, so that they make more sense.

* Do not deref msg ptr for rmw_{publish,return}_loaned_message*()
  (#240)

* remove rmw_localhost_only_t. (#239)

* Expect rmw_service_server_is_available to ret
  RMW_RET_INVALID_ARGUMENT (#231)

* Expect rmw_destroy_wait_set to ret RMW_RET_INVALID_ARGUMENT (#234)

* Add test creating two content filter topics with the same topic name
  (#230) (#233)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Tomoya Fujita, yadunund

test_ros2trace
==============

* Add timeout to test_ros2trace tests that wait on stdout (#167)

* Allow enabling syscalls through "ros2 trace" or the Trace action
  (#137)

* Contributors: Christophe Bedard

test_tf2
========

* Uniform cmake min version (#764)

* Add "rclcpp::shutdown" (#762)

* Remove many extra conversions from Matrix3x3 to Quaternion (#741)
  Co-authored-by: jmachowinski <jmachowinski@users.noreply.github.com>
  Co-authored-by: Katherine Scott <katherineAScott@gmail.com>

* Deprecate C Headers (#720)

* Switch to using a context manager for the python examples. (#700)
  That way we can be sure to always clean up, but use less code doing
  so.

* Contributors: Chris Lalancette, Lucas Wendland, Yuyuan Yuan, kyle-
  basis, mosfet80

test_tracetools
===============

* Run test_tracetools tests against rmw_zenoh_cpp (#140)

* Use ament_add_ros_isolated_* in test_tracetools (#159)

* Instrument client/service for end-to-end request/response tracking
  (#145)

* Don't try to build on BSD (#142) The 'BSD' variable was added in
  CMake 3.25. Note that variables which are not defined will evaluate
  to 'False', so this shouldn't regress platforms using CMake versions
  older than 3.25.

* Refactor and split test_service into test_{service,client} (#144)

* Change expected rmw GID array size to 16 bytes (#138)

* Run test_tracetools tests against rmw_fastrtps_dynamic_cpp too
  (#127)

* Make test_tracetools ping pubs/subs transient_local (#125)

* Run relevant test_tracetools tests with all instrumented rmw impls
  (#116)

* Contributors: Christophe Bedard, Scott K Logan

test_tracetools_launch
======================

* Fix or ignore new mypy issues (#161)

* Allow enabling syscalls through "ros2 trace" or the Trace action
  (#137)

* Contributors: Christophe Bedard

tf2
===

* Add isnan support (#780)

* Overflow Issue in durationFromSec() Function when Handling Extremely
  Large or Small Values (#785)

* Do not clobber callback handles when cancelling pending
  transformable requests (#779)

* Uniform cmake min version (#764)

* Remove many extra conversions from Matrix3x3 to Quaternion (#741)
  Co-authored-by: jmachowinski <jmachowinski@users.noreply.github.com>
  Co-authored-by: Katherine Scott <katherineAScott@gmail.com>

* Cleanup deprecation warnings. (#744) The deprecation warnings were
  not printing out properly on GCC, at least; it would warn that
  #warning was not standard, and it would also not print out the
  actual warning. Also "deprecated" was spelled wrong. Fix all of
  these issues here.

* Deprecate C Headers (#720)

* Removed unused var in tf2 (#735)

* Error String Filled (#715)

* Removed deprecated enuns (#699)

* [TimeCache] Improve performance for insertData() and pruneList()
  (#680) Co-authored-by: Chris Lalancette <clalancette@gmail.com>

* Removed warning (#682)

* Add cache_benchmark (#679) * Add cache_benchmark Co-authored-by:
  Chris Lalancette <clalancette@gmail.com>

* [cache_unittest] Add direct implementation testing on ordering,
  pruning (#678) * [cache_unittest] Add direct implementation testing
  on ordering, pruning * do getAllItems() approach * Return a
  reference instead. * mark getAllItems as internal * Fix warning on
  Windows. Co-authored-by: Chris Lalancette <clalancette@gmail.com>

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Eric
  Cousineau, Lucas Wendland, Michael Carlstrom, Timo Röhling, cramke,
  kyle-basis, mosfet80

tf2_bullet
==========

* Uniform cmake min version (#764)

* Deprecate C Headers (#720)

* Contributors: Lucas Wendland, mosfet80

tf2_eigen
=========

* Uniform cmake min version (#764)

* Deprecate C Headers (#720)

* Contributors: Lucas Wendland, mosfet80

tf2_eigen_kdl
=============

* Uniform cmake min version (#764)

* Deprecate C Headers (#720)

* Contributors: Lucas Wendland, mosfet80

tf2_geometry_msgs
=================

* Remove many extra conversions from Matrix3x3 to Quaternion (#741)
  Co-authored-by: jmachowinski <jmachowinski@users.noreply.github.com>
  Co-authored-by: Katherine Scott <katherineAScott@gmail.com>

* Deprecate C Headers (#720)

* Add a python3-dev dependency to tf2_py. (#733)

* Fix tf2_geometry_msgs_INCLUDE_DIRS. (#729)

* Remove use of python_cmake_module (#651)

* Contributors: Chris Lalancette, Lucas Wendland, kyle-basis,
  rkeating-planted

tf2_kdl
=======

* Uniform cmake min version (#764)

* Fix external docs mappings (#757)

* tf2_kdl: add python_orocos_kdl_vendor dependency (#745) * tf2_kdl:
  add python_orocos_kdl_vendor dependency The tf2_kdl Python API
  depends on PyKDL, which is provided by python_orocos_kdl_vendor. *
  tf2_kdl: remove tf2_msgs test dependency This dependency is not
  needed.

* Deprecate C Headers (#720)

* Contributors: Ben Wolsieffer, Emmanuel, Lucas Wendland, mosfet80

tf2_msgs
========

* Uniform cmake min version (#764)

* Contributors: mosfet80

tf2_py
======

* Deprecate C Headers (#720)

* Add a python3-dev dependency to tf2_py. (#733)

* Remove use of python_cmake_module (#651)

* Contributors: Chris Lalancette, Lucas Wendland

tf2_ros
=======

* Uniform cmake min version (#764)

* Add "rclcpp::shutdown" (#762)

* Fix external docs mappings (#757)

* Deprecate C Headers (#720)

* specified quaternion order to be xyzw (#718)

* Add configurable TF topics (#709)

* Adding static transform listener (#673)

* Updated deprecated message filter headers (#702)

* Update qos for deprecation (#695)

* Cli tools documentation (#653)

* Contributors: Abhishek Kashyap, Alejandro Hernández Cordero,
  Emmanuel, Lucas Wendland, Ryan, Tom Moore, Yuyuan Yuan, mosfet80

tf2_ros_py
==========

* Fix external docs mappings (#757)

* Add in the linters for tf2_ros_py. (#740)

* Adding StaticTransformListener in Python (#719)

* Add in test_xmllint for geometry2 python packages. (#725)

* Add configurable TF topics (#709)

* Fix the time_jump_callback signature. (#711)

* Switch to using a context manager for the python examples. (#700)
  That way we can be sure to always clean up, but use less code doing
  so.

* Contributors: Chris Lalancette, Emmanuel, Lucas Wendland, Ryan

tf2_sensor_msgs
===============

* Deprecate C Headers (#720)

* Add a python3-dev dependency to tf2_py. (#733)

* Remove use of python_cmake_module (#651)

* Contributors: Chris Lalancette, Lucas Wendland

tf2_tools
=========

* Add in test_xmllint for geometry2 python packages. (#725)

* Add configurable TF topics (#709)

* [view_frames] log filenames after it's been determined (#674)

* Contributors: Chris Lalancette, Mikael Arguedas, Ryan

tlsf
====

* Fixed link (#15)

* Contributors: Alejandro Hernández Cordero

tlsf_cpp
========

* Explicitly shutdown context before test exits (#129)

* Reduce the number of files we compile. (#125)

* Contributors: Chris Lalancette, yadunund

topic_monitor
=============

* Add test_xmllint.py to all of the ament_python packages. (#704)

* Contributors: Chris Lalancette

topic_statistics_demo
=====================

* Uniform CMAKE min VERSION (#714)

* Contributors: mosfet80

tracetools
==========

* Switch to ament_cmake_ros_core package (#162)

* Instrument client/service for end-to-end request/response tracking
  (#145)

* Don't try to build on BSD (#142)

* Change expected rmw GID array size to 16 bytes (#138)

* Fix up two different C problems. (#129)

* Ignore zero-variadic-macro-arguments warnings from lttng-ust macros
  (#126)

* Remove deprecated TRACEPOINT macros (#123)

* Fix type for buffer index argument in tracepoint event declaration.
  (#117)

* Contributors: Chris Lalancette, Christophe Bedard, Mattis Kieffer,
  Michael Carroll, Scott K Logan

tracetools_launch
=================

* Fix or ignore new mypy issues (#161)

* Improve Python typing annotations (#152)

* Expose types for tracing tools (#153)

* Allow enabling syscalls through "ros2 trace" or the Trace action
  (#137)

* Contributors: Christophe Bedard, Michael Carlstrom

tracetools_read
===============

* Improve Python typing annotations (#152)

* Expose types for tracing tools (#153)

* Contributors: Christophe Bedard, Michael Carlstrom

tracetools_test
===============

* Fix or ignore new mypy issues (#161)

* Improve Python typing annotations (#152)

* Expose types for tracing tools (#153)

* Run relevant test_tracetools tests with all instrumented rmw impls
  (#116)

* Contributors: Christophe Bedard, Michael Carlstrom

tracetools_trace
================

* Improve Python typing annotations (#152)

* Expose types for tracing tools (#153)

* Remove unnecessary 'type: ignore' comments in tracetools_trace
  (#151)

* Instrument client/service for end-to-end request/response tracking
  (#145)

* Allow enabling syscalls through "ros2 trace" or the Trace action
  (#137)

* Contributors: Christophe Bedard, Michael Carlstrom

turtlesim
=========

* Create turtlesim_msgs (#169)

* Add icon for Jazzy. (#167)

* [teleop_turtle_key] update usage string to match keys captured by
  keyboard (#165)

* Contributors: Alejandro Hernández Cordero, Marco A. Gutierrez,
  Mikael Arguedas

turtlesim_msgs
==============

* Create turtlesim_msgs (#169)

* Contributors: Alejandro Hernández Cordero

type_description_interfaces
===========================

* Add missing build_export_depend on rosidl_core_runtime (#165)

* Contributors: Scott K Logan

unique_identifier_msgs
======================

* Add missing build_export_depend on rosidl_core_runtime (#30)

* Contributors: Scott K Logan

urdf
====

* make linters happy (#45)

* Added documentation with rosdoc2 (#40)

* Added commom linters (#39)

* Use rcutils to log (#37)

* Enable test_robot_model_parser test (#38)

* Contributors: Alejandro Hernández Cordero

urdf_parser_plugin
==================

* Added commom linters (#39)

* Contributors: Alejandro Hernández Cordero

zenoh_cpp_vendor
================

* Bump Zenoh to v1.3.2 and improve e2e reliability with
  HeartbeatSporadic (#591)

* Add quality declaration (#483)

* Fix liveliness crash in debug mode (#544)

* Bump zenoh-cpp to 2a127bb, zenoh-c to 3540a3c, and zenoh to f735bf5
  (#503)

* Enable Zenoh UDP transport (#486)

* Bump zenoh-c to 261493 and zenoh-cpp to 5dfb68c (#463)

* Bump Zenoh to commit id 3bbf6af (1.2.1 + few commits) (#456)

* Bump Zenoh to commit id e4ea6f0 (1.2.0 + few commits) (#446)

* Bump zenoh-c and zenoh-cpp to 1.1.1 (#424)

* Update Zenoh version (#405)

* Vendors zenoh-cpp for rmw_zenoh.

* Contributors: Alejandro Hernández Cordero, ChenYing Kuo (CY), Chris
  Lalancette, Franco Cipollone, Hugal31, Julien Enoch, Luca Cominardi,
  Yadunund, Yuyuan Yuan

zenoh_security_tools
====================

* Add zenoh_security_tools (#595)

* Contributors: yadunund
