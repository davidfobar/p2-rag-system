# Galactic Geochelone changelog (part 8 of 8)

sqlite3_vendor
==============

* Explicitly add emersonknapp as maintainer (#692)

* Always preserve source permissions in vendor packages (#645)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* use interface_include_directories (#426)

* Contributors: Emerson Knapp, Karsten Knese, Michael Jeronimo, Scott
  K Logan

sros2
=====

* Skip mypy test on platforms using importlib_resources (#258)

* Enable topic "ros_discovery_info" for rmw_connextdds (#253)

* Declare missing dependency on python3-importlib-resources (#249) Co-
  authored-by: <mikael.arguedas@gmail.com>

* Fix namedtuple names. (#250)

* parameter_events topic is now absolute (#233) Signed-off-by: Mikael
  Arguedas <mikael.arguedas@gmail.com>

* Expose keystore operations in public API (#241)

* add cyclonedds to the list of rmw using graph info topics (#231)

* Add scope parameter (#230)

* Fix name of argument passed to NodeStrategy (#227)

* Remove the use of pkg_resources. (#225)

* Make use of ros_testing to test policy generation. (#214)

* Add pytest.ini so local tests don't display warning (#224)

* Fix list keys verb (#219)

* Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron, Jose
  Luis Rivero, Kyle Fazzari, Michel Hidalgo, Mikael Arguedas, Scott K
  Logan

statistics_msgs
===============

* Updating Quality Declaration (#120)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  brawner, shonigmann

std_msgs
========

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145) Co-authored-by: Simon Honigmann <shonigmann@blueorigin.com>

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

std_srvs
========

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

stereo_msgs
===========

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

tango_icons_vendor
==================

* Add exec_depend on tango-icon-theme system package (#8)

* Added common linters (#7) * Added common linters * Fixed license in
  package.xml

* Remaned package qt_gui_icons -> tango_icons_vendor (#4) * Remaned
  package qt_gui_icons -> tango_icons_vendor * Updated CMake var to
  install tango icons: INSTALL_TANGO_ICONS * Added cmake option
  INSTALL_TANGO_ICONS * Fixed logic * set
  INSTALL_TANGO_ICONS_DEFAULT_VALUE to option * Make linters happy

* Updated link on the description (#6)

* Updated the maintainer (#5)

* Version 0.0.0 this package was never released (#3)

* Install icons by default on macOS too (#1)

* Updating package.xml

* fixup! Install tango icons

* Adding icons

* Install tango icons

* Contributors: Alejandro Hernández Cordero, Scott K Logan, Stephen,
  Stephen Brawner

test_cli
========

* Update maintainers. (#450)

* Enable -Wall, -Wextra, and -Wpedantic. (#447)

* Contributors: Audrow Nash, Jacob Perron

test_cli_remapping
==================

* Fix test_cli_remapping flaky test. (#470)

* Update maintainers. (#450)

* Enable -Wall, -Wextra, and -Wpedantic. (#448)

* Contributors: Audrow Nash, Jacob Perron, Shane Loretz

test_communication
==================

* Add support for rmw_connextdds. (#463)

* Kill off the ros2 daemon before running tests. (#460)

* Remove Opensplice from test_communication. (#460)

* Make TestMessageSerialization robust to missed messages. (#456)

* Add corresponding rclcpp::shutdown. (#455)

* Update maintainers. (#450)

* Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron,
  Stephen Brawner

test_interface_files
====================

* Update maintainer (#13)

* Contributors: Jacob Perron

test_launch_ros
===============

* Add a package marker to test_launch_ros. (#226)

* Re-order shutdown vs node destruction (#213)

* Increase test_composable_node_container timeout (#195)

* Remove constructors arguments deprecated since Foxy (#190)

* Merge pull request #183 from ros2/update-maintainers

* Move previous maintainer to <author>

* Update the package.xml files with the latest Open Robotics
  maintainers

* Handle any substitution types for SetParameter name argument (#182)

* Address security bug in yaml loading (#175)

* Resolve TODO in test (#172)

* Fix case where list of composable nodes is zero (#173)

* Do not use event handler for loading composable nodes (#170)

* Fix race with launch context changes when loading composable nodes
  (#166)

* Substitutions in parameter files (#168)

* Fix problems when parsing a "Command" "Substitution" as a parameter
  value (#137)

* Drop double single-quoted params. (#164)

* Add a way to set remapping rules for all nodes in the same scope
  (#163)

* Fix ComposableNode ignoring PushRosNamespace actions (#162)

* Add a SetParameter action that sets a parameter to all nodes in the
  same scope (#158)

* Make namespace parameter mandatory in LifecycleNode constructor
  (#157)

* Avoid using a wildcard to specify parameters if possible (#154)

* Remove the loop parameter from async.sleep. (#155)

* Fix no specified namespace (#153)

* Fix test_node_frontend (#146)

* Add pytest.ini so local tests don't display warning (#152)

* Contributors: Chris Lalancette, Dan Rose, Ivan Santiago Paunovic,
  Jacob Perron, Michael Jeronimo, Michel Hidalgo, Scott K Logan,
  Víctor Mayoral Vilches

test_launch_testing
===================

* Update package maintainers (#465)

* Add pytest.ini to test_launch_testing so tests succeed locally.
  (#431)

* Contributors: Chris Lalancette, Michel Hidalgo

test_msgs
=========

* Update package maintainers. (#112)

* Contributors: Chris Lalancette

test_quality_of_service
=======================

* Add support for rmw_connextdds. (#463)

* Run QoS tests. (#441)

* Update maintainers. (#450)

* Contributors: Andrea Sorbini, Jacob Perron, Michel Hidalgo

test_rclcpp
===========

* Reenable test that used to be flaky. (#467)

* Get_parameters_service_ should return empty if allow_undeclared_ is
  false. (#466)

* Make test pass after rclcpp#1532. (#465)

* Adapt tests to statically typed parameters. (#462)

* Guard against TOCTTOU with rclcpp::ok and rclcpp:spin_some. (#459)

* Update parameter client test with timeout. (#457)

* Call rclcpp::init and rclcpp::shutdown in each test for test_rclcpp.
  (#454)

* Set cppcheck timeout to 400 seconds. (#453)

* Modify to match Waitable interface adding take_data. (#444)

* Update maintainers. (#450)

* Fix rclcpp timeout subscriber test. (#440) * Use nonzero lower bound
  for timeout checks. * Relax time tolerance.

* Show numbers of nanseconds in EXPECT with durations. (#438) * Show
  numbers of nanseconds in expect with durations * Fix syntax

* Remove ament_pytest dependency from test_rclcpp. (#437) It is not
  used in test_rclcpp anywhere.

* Contributors: Audrow Nash, Chris Lalancette, Dirk Thomas, Ivan
  Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz,
  Stephen Brawner, Tomoya Fujita, tomoya

test_rmw_implementation
=======================

* Implement test for subscription loaned messages (#186)

* Remove rmw_connext_cpp. (#183)

* Add support for rmw_connextdds (#182)

* Add function for checking QoS profile compatibility (#180)

* Make sure to initialize the rmw_message_sequence after init. (#175)

* Set the value of is_available before entering the loop (#173)

* Set the return value of rmw_ret_t before entering the loop. (#171)

* Add some additional checking that cleanup happens. (#168)

* Add test to check rmw_send_response when the client is gone (#162)

* Update maintainers (#154)

* Add fault injection tests to construction/destroy APIs. (#144)

* Add tests bad type_support implementation (#152)

* Add tests for localhost-only node creation (#150)

* Added rmw_service_server_is_available tests (#140)

* Use 10x the intraprocess delay to wait for sent requests. (#148)

* Added rmw_wait, rmw_create_wait_set, and rmw_destroy_wait_set tests
  (#139)

* Add tests service/client request/response with bad arguments (#141)

* Added test for rmw_get_serialized_message_size (#142)

* Add service/client construction/destruction API test coverage.
  (#138)

* Added rmw_publisher_allocation and rmw_subscription_allocation
  related tests (#137)

* Add tests take serialized with info bad arguments (#130)

* Add gid API test coverage. (#134)

* Add tests take bad arguments (#125)

* Bump graph API test coverage. (#132)

* Add tests take sequence serialized with bad arguments (#129)

* Add tests take sequence + take sequence with bad arguments (#128)

* Add tests take with info bad arguments (#126)

* Add tests for non-implemented rmw_take_* functions (#131)

* Add tests publish serialized bad arguments (#124)

* Add tests publish bad arguments (#123)

* Add tests non-implemented functions + loan bad arguments (#122)

* Add missing empty topic name tests. (#136)

* Add rmw_get_serialization_format() smoke test. (#133)

* Complete publisher/subscription QoS query API test coverage. (#120)

* Remove duplicate assertions (#121)

* Add publisher/subscription matched count API test coverage. (#119)

* Add serialize/deserialize API test coverage. (#118)

* Add subscription API test coverage. (#117)

* Extend publisher API test coverage (#115)

* Add node construction/destruction API test coverage. (#112)

* Check that rmw_init() fails if no enclave is given. (#113)

* Add init options API test coverage. (#108)

* Complete init/shutdown API test coverage. (#107)

* Add dependency on ament_cmake_gtest (#109)

* Add test_rmw_implementation package. (#106)

* Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Chris
  Lalancette, Geoffrey Biggs, Ivan Santiago Paunovic, Jacob Perron,
  Jose Tomas Lorente, José Luis Bueno López, Michel Hidalgo, Miguel
  Company, Shane Loretz

test_security
=============

* Add support for rmw_connextdds. (#463)

* Update deprecated gtest macros. (#449)

* Update maintainers. (#450)

* Run test_security on CycloneDDS as well. (#408)

* Remove invalid cert folder to force regeneration of certificates.
  (#434)

* Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Mikael
  Arguedas

test_tf2
========

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Fix a TOCTTOU race in tf2. (#307)

* Fixed memory leak in Buffer::waitForTransform (#281)

* relax test timings to pass with Connext (#304)

* Explicitly initialize instances of tf2::Duration (#291)

* Generate callbacks after updating message_ (#274)

* fix test_static_publisher in macos (#284)

* Fix up the dependencies in test_tf2. (#277)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk
  Thomas, Ivan Santiago Paunovic, Martin Ganeff, Michael Carroll, ymd-
  stella

tf2
===

* Change index.ros.org -> docs.ros.org. (#394)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Active usual compiler warnings in tf2 (#322)

* Cleanups in buffer_core.cpp. (#301)

* Add PoseWithCovarianceStamped transform support (#312)

* Fix a TOCTTOU race in tf2. (#307)

* Fixed memory leak in Buffer::waitForTransform (#281)

* Add common linters to tf2. (#258)

* Provide more available error messaging for nonexistent and invalid
  frames in canTransform (ros2 #187)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ivan
  Santiago Paunovic, Joshua Whitley, Martin Ganeff

tf2_bullet
==========

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Suppress compiler warning on Centos (#290)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michael
  Carroll

tf2_eigen
=========

* Fix linter errors (#385)

* Fix up the style in tf2_eigen. (#378)

* Fix doTransform with Eigen Quaternion (#369)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Contributors: Audrow Nash, Bjar Ne, Chris Lalancette, Ivan Santiago
  Paunovic

tf2_eigen_kdl
=============

* fix order of find eigen3_cmake_module & find eigen3 (#344)

* Update package.xml (#333)

* Port eigen_kdl.h/cpp to ROS2 (#311)

* Contributors: Ahmed Sobhy, Jafar Abdi

tf2_geometry_msgs
=================

* Fix doTransform with Eigen Quaternion (#369)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Add PoseWithCovarianceStamped transform support (#312)

* Don't install python tf2_geometry_msgs (#299) It hasn't been ported
  yet. Closes https://github.com/ros2/geometry2/issues/285

* Split tf2_ros in tf2_ros and tf2_ros_py (#210) * Split tf2_ros in
  tf2_ros and tf2_ros_py

* Contributors: Alejandro Hernández Cordero, Bjar Ne, Chris
  Lalancette, Ivan Santiago Paunovic, Joshua Whitley, Shane Loretz

tf2_kdl
=======

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ivan
  Santiago Paunovic

tf2_msgs
========

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic

tf2_py
======

* Adapt to Python 3.9 (#362)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Add in pytest.ini so tests succeed locally. (#280)

* Contributors: Chris Lalancette, Homalozoa X

tf2_ros
=======

* Guard against access to null node pointer (#393)

* Allow to reconfigure durability for /tf topic broadcaster/listener
  (#383)

* Fix the rcl type used in the time jump. (#391)

* Fix linter errors (#385)

* fix accessing freed resources (#386)

* Allow reconfiguring qos of tf and tf_static topics through
  parameters (#381)

* Replace ROS_* logging macros and use RCLCPP_* instead (#380)

* Improve message filters error messages (#364)

* Clarify the role of child_frame_id and header.frame_id in the
  documentation. (#345)

* Remove usage of deprecated rclcpp::Duration constructor (#340)

* Remove messages_count member from tf2_ros::MessageFilter. (#335)

* Style fixup in tf2_ros. (#325)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Update goal response callback signature (#323)

* Activate usual compiler warnings and fix errors (#270)

* Fixed memory leak in Buffer::waitForTransform (#281)

* fix time-reset test with Connext (#306)

* reenable FrameGraph server (#198)

* Use the usual style of parameters for static_transform_program
  (#300)

* Make static_transform_broadcaster consistent with its command line
  description (#294)

* Avoid using invalid std::list iterators (#293)

* Generate callbacks after updating message_ (#274)

* Moved unique_lock of messages_mutex_ to guarantee pointer (#279)

* Fix dependencies in tf2_ros. (#269)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris
  Lalancette, Dirk Thomas, Hunter L. Allen, Ivan Santiago Paunovic,
  Jacob Perron, Kazunari Tanaka, Martin Ganeff, Michael Carroll, Vikas
  Dhiman, ymd-stella

tf2_ros_py
==========

* Use underscores instead of dashes in setup.cfg. (#403) (#404)

* Use global namespace for TransformListener topics (#390)

* Fix indentation of a comment in buffer.py (#371)

* Update rclpy.Rate TODO with url to issue (#324)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Add deprecation warnings to lookup_transform to handle the passing
  of the incorrect Time object. (#319)

* change signature to show true arguments (#321)

* Handle when None passed to qos argument in the constructor of
  TransformBroadcaster. (#320)

* Add type hints to tf2_ros_py code(#275) (#315)

* Clear callbacks_to_remove variable after removing (#303)

* Fix cache_time None check in buffer.py (#297)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob
  Perron, Matthijs den Toom, ScottMcMichael, surfertas

tf2_sensor_msgs
===============

* Update maintainers of the ros2/geometry2 fork. (#328)

* Activate usual compiler warnings and fix errors (#270)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ivan
  Santiago Paunovic

tf2_tools
=========

* Use underscores instead of dashes in setup.cfg. (#403) (#404)

* Add wait time option to view_frames (#374)

* Cleanup tf2_tools to be more modern. (#351)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Address security bug in yaml loading (#313)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob
  Perron, Víctor Mayoral Vilches

tlsf
====

* Switch to standard __VA_ARGS__. (#9)

* Enable basic warnings (#8)

* Contributors: Audrow Nash, Chris Lalancette

tlsf_cpp
========

* Add in the Apache license to tlsf_cpp. (#108)

* Contributors: Chris Lalancette

topic_monitor
=============

* Use is_alive for threads. (#510) (#513)

* Use underscores instead of dashes in setup.cfg (#502)

* Change index.ros.org -> docs.ros.org. (#496)

* Update deprecated qos policy value names (#468)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michael
  Jeronimo

topic_statistics_demo
=====================

* Change index.ros.org -> docs.ros.org. (#496)

* Update logging macros (#476)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Create new topic statistics demo package (#454)

* Contributors: Audrow Nash, Chris Lalancette, Michael Jeronimo,
  Prajakta Gokhale

tracetools
==========

* Update QD to be more specific about public API

* Namespace tracetools C++ functions and macros and deprecate current
  ones

* Add support for rcl_publish and rclcpp_publish tracepoints

* Add instrumentation support for linking a timer to a node

* Bring tracetools up to quality level 1

* Add lifecycle node state transition instrumentation

* Do not export tracetools if empty

* Allow disabling tracetools status app

* Contributors: Christophe Bedard, Ingo Lütkebohle, José Antonio Moral

tracetools_launch
=================

* Allow configuring tracing directory through environment variables

* Contributors: Christophe Bedard

tracetools_test
===============

* Update after namespacing C++ tracetools functions and macros

* Add tests for rcl_publish and rclcpp_publish tracepoints

* Allow asserting order of list of events

* Allow skipping test trace cleanup by setting an environment variable

* Add test for timer-node linking instrumentation

* Increased code coverage > 94% as part of QL1

* Add lifecycle node state transition instrumentation test

* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Ingo
  Lütkebohle

tracetools_trace
================

* Add support for rcl_publish and rclcpp_publish tracepoints

* Fix flake8 blind except error by using more concrete types

* Allow configuring tracing directory through environment variables

* Cleanly stop ros2trace/tracetools_trace tracing on SIGINT

* Add instrumentation support for linking a timer to a node

* Add lifecycle node state transition instrumentation

* Contributors: Christophe Bedard, Ingo Lütkebohle

trajectory_msgs
===============

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Finish up API documentation (#123)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

turtlesim
=========

* Ignore key up events in teleop_turtle_key on Windows (#118)

* Update maintainers (#106)

* Update goal response callback signature (#100)

* add holonomic motion for turtlesim (#98)

* add step value to turtlesim color parameters (#91)

* update Foxy turtle (#90)

* Contributors: Jacob Perron, Michel Hidalgo, Shane Loretz

unique_identifier_msgs
======================

* Change index.ros.org -> docs.ros.org (#21)

* Update QD to QL 1 (#17)

* Update Quality Declaration to QL2. (#15)

* Update Quality level to level 3 (#13)

* Add Security Vulnerability Policy pointing to REP-2006. (#11)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  brawner

urdf
====

* Work around Windows min/max bug. (#21)

* Enable -Wall -Wextra -Wpedantic (#20)

* Add dependency on TinyXML2 (#19)

* Remove TinyXML dependency from urdf. (#17)

* Make urdf plugable and revive urdf_parser_plugin (#13)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

urdf_parser_plugin
==================

* Export urdfdom_headers as urdf_parser_plugin dependency. (#25)

* Make urdf plugable and revive urdf_parser_plugin (#13)

* Contributors: Michel Hidalgo, Shane Loretz

visualization_msgs
==================

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

yaml_cpp_vendor
===============

* Always preserve source permissions in vendor packages (#22)

* Add an override flag to force vendored build (#21)

* Reapply "Use system installed yaml-cpp 0.6 if available (#8)" (#16)

* Revert "Use system installed yaml-cpp 0.6 if available (#8)" (#15)

* Use system installed yaml-cpp 0.6 if available (#8)

* Contributors: Ivan Santiago Paunovic, Scott K Logan, Sean Yen

zstd_vendor
===========

* Explicitly add emersonknapp as maintainer (#692)

* Always preserve source permissions in vendor packages (#645)

* Zstd should not install internal headers - some of them try include
  others that aren't installed. We don't use them. Avoid the situation
  (#631)

* Patch zstd 1.4.4 to include cmake_minimum_version bump to 2.8.12
  (#579)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Contributors: Emerson Knapp, Michael Jeronimo, Scott K Logan
