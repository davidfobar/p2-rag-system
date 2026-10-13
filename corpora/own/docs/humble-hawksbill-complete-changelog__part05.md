# Humble Hawksbill changelog (part 5 of 5)

* Set the output size unconditionally when copying sequences (#669)

* De-duplicate Quality Level from README and QUALITY_DECLARATION
  (#661)

* Install headers to include/${PROJECT_NAME} (#658)

* Implement copy function for C messages (#650)

* Implement equality operator function for C messages. (#648)

* Set CXX standard to 17 (#635)

* Update package maintainers (#624)

* Use RCUtils allocators in rosidl_generator_c (#584)

* Contributors: Jose Luis Rivero, Michel Hidalgo, Nikolai Morin, Pablo
  Garrido, Shane Loretz, Øystein Sture

rosidl_runtime_cpp
==================

* Add missing dependency on rosidl_runtime_c (#666)

* De-duplicate Quality Level from README and QUALITY_DECLARATION
  (#661)

* Install headers to include/${PROJECT_NAME} (#658)

* Set CXX standard to 17 (#635)

* Update package maintainers (#624)

* Contributors: Jose Luis Rivero, Michel Hidalgo, Shane Loretz,
  Øystein Sture

rosidl_runtime_py
=================

* add yaml dump flow style. (#16)

* Update maintainers (#15) * Update maintainers to Shane Loretz *
  Update Shane's email Co-authored-by: Shane Loretz
  <sloretz@openrobotics.org>

* Contributors: Audrow Nash, Tomoya Fujita

rosidl_typesupport_c
====================

* Use target_link_libraries(... PRIVATE ...) in single typesupport
  case (#124)

* rosidl CMake cleanup in rosidl_typesupport_c (#123)

* Install headers to include/${PROJECT_NAME} (#121)

* Use FindPython3 (#118)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#116)

* Support available typesupport specification in CLI extensions (#112)

* Bundle and ensure the exportation of rosidl generated targets (#113)

* Fix C and C++ typesupports CLI extensions (#111)

* Contributors: Michel Hidalgo, Shane Loretz

rosidl_typesupport_cpp
======================

* Use target_link_libraries(... PRIVATE ...) in single typesupport
  case (#124)

* rosidl CMake cleanup in rosidl_typesupport_cpp (#123)

* Install headers to include/${PROJECT_NAME} (#121)

* Make sure to check typesupport handles against nullptr properly
  (#119)

* Use FindPython3 (#118)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#116)

* Support available typesupport specification in CLI extensions (#112)

* Bundle and ensure the exportation of rosidl generated targets (#113)

* Fix C and C++ typesupports CLI extensions (#111)

* Contributors: Chris Lalancette, Michel Hidalgo, Shane Loretz

rosidl_typesupport_fastrtps_c
=============================

* Install generated headers to include/${PROJECT_NAME} (#88)

* Misc fastrtps typesupport generator cleanup (#87)

* Install headers to include/${PROJECT_NAME} (#86)

* Fix include order for cpplint (#84)

* Update maintainers to Shane Loretz (#83)

* Use FindPython3 explicitly instead of PythonInterp implicitly (#78)

* Revert rosidl targets and dependencies exportation (#76) * Revert
  "Export rosidl_typesupport_fastrtps_c* dependencies (#75)" * Revert
  "Bundle and ensure the exportation of rosidl generated targets
  (#73)"

* Correctly inform that a BoundedSequence is bounded (#71)

* Export rosidl_typesupport_fastrtps_c* dependencies (#75)

* Bundle and ensure the exportation of rosidl generated targets (#73)

* Fix Fast-RTPS C++ typesupport CLI extension (#72)

* Fastdds type support extensions (#67)

* Remove fastrtps dependency (#68)

* Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Michel
  Hidalgo, Miguel Company, Shane Loretz

rosidl_typesupport_fastrtps_cpp
===============================

* Install generated headers to include/${PROJECT_NAME} (#88)

* Misc fastrtps typesupport generator cleanup (#87)

* Install headers to include/${PROJECT_NAME} (#86)

* Fix include order for cpplint (#84) * Fix include order for cpplint
  Relates to https://github.com/ament/ament_lint/pull/324 * Use
  double-quotes for other includes This is backwards compatible with
  older versions of cpplint.

* Update maintainers to Shane Loretz (#83)

* Re-introduce improvements to serialization of primitive bounded
  sequences for C++ type support (#81)

* Revert "Improve serialization of ... (#79)" (#80)

* Improve serialization of primitive bounded sequences in C++ type
  support (#79)

* Use FindPython3 explicitly instead of PythonInterp implicitly (#78)

* Revert rosidl targets and dependencies exportation (#76) * Revert
  "Export rosidl_typesupport_fastrtps_c* dependencies (#75)" * Revert
  "Bundle and ensure the exportation of rosidl generated targets
  (#73)"

* Correctly inform that a BoundedSequence is bounded (#71)

* Export rosidl_typesupport_fastrtps_c* dependencies (#75)

* Bundle and ensure the exportation of rosidl generated targets (#73)

* Fix Fast-RTPS C++ typesupport CLI extension (#72)

* Fastdds type support extensions (#67)

* Remove fastrtps dependency (#68)

* Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Jorge
  Perez, Michel Hidalgo, Miguel Company, Shane Loretz

rosidl_typesupport_interface
============================

* De-duplicate Quality Level from README and QUALITY_DECLARATION
  (#661)

* Install headers to include/${PROJECT_NAME} (#658)

* Add ROSIDL_TYPESUPPORT_INTERFACE__LIBRARY_NAME() macro (#649)

* Set CXX standard to 17 (#635)

* Update package maintainers (#624)

* Contributors: Jose Luis Rivero, Michel Hidalgo, Shane Loretz,
  Øystein Sture

rosidl_typesupport_introspection_c
==================================

* Install generated headers to include/${PROJECT_NAME} (#670)

* Misc cleanup in the rosidl generator extensions (#662)

* De-duplicate Quality Level from README and QUALITY_DECLARATION
  (#661)

* Update Quality declaration to level 1 in README for instrospection
  pkgs (#659)

* Install headers to include/${PROJECT_NAME} (#658)

* Move rosidl_typesupport_introspection_cpp quality declaration to Q1
  (#657)

* Move rosidl_typesupport_introspection_c quality declaration to Q1
  (#656)

* add documentation for generators and API (#646)

* Rework nested types' items introspection in C and C++ (#652)

* Fix up the documentation for rosidl_typesupport_introspection_c
  (#628)

* Update package maintainers (#624)

* Quality Declaration for typesupport_introspection (#621)

* Make rosidl packages use FindPython3 instead of FindPythonInterp
  (#612)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#611)

* Bundle and ensure the exportation of rosidl generated targets (#601)

* Update function prefix (#596)

* Contributors: Chris Lalancette, Jose Luis Rivero, Michel Hidalgo,
  Pablo Garrido, Shane Loretz, eboasson

rosidl_typesupport_introspection_cpp
====================================

* Install generated headers to include/${PROJECT_NAME} (#670)

* Misc cleanup in the rosidl generator extensions (#662)

* De-duplicate Quality Level from README and QUALITY_DECLARATION
  (#661)

* Update Quality declaration to level 1 in README for instrospection
  pkgs (#659)

* Install headers to include/${PROJECT_NAME} (#658)

* Move rosidl_typesupport_introspection_cpp quality declaration to Q1
  (#657)

* add documentation for generators and API (#646)

* Rework nested types' items introspection in C and C++ (#652)

* Set CXX standard to 17 (#635)

* Fix up the documentation for rosidl_typesupport_introspection_cpp
  (#627)

* Update package maintainers (#624)

* Quality Declaration for typesupport_introspection (#621)

* Make rosidl packages use FindPython3 instead of FindPythonInterp
  (#612)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#611)

* Bundle and ensure the exportation of rosidl generated targets (#601)

* Contributors: Chris Lalancette, Jose Luis Rivero, Michel Hidalgo,
  Shane Loretz, eboasson, Øystein Sture

rosidl_typesupport_introspection_tests
======================================

* Bump "rosidl_typesupport_introspection_tests" coverage (#655)

* Add introspection typesupport tests for C/C++ services (#653)

* Add introspection typesupport tests for C/C++ messages (#651)

* Contributors: Michel Hidalgo

rpyutils
========

* Make sure to call abspath when adding Windows DLL directories. (#8)

* Update troubleshooting links to docs.ros.org (#6)

* Contributors: Chris Lalancette, Christophe Bedard

rqt_gui
=======

* Changed getiter to iter (#1) (#241)

* Update maintainers (#233) (#237)

* add missing dependencies: rospkg-modules, python_qt_binding, rospy
  (#227)

* bump CMake minimum version to avoid CMP0048 warning (#219)

* use catkin_install_python for Python script (#206)

* Contributors: Michael Jeronimo, sven-herrmann

rqt_gui_cpp
===========

* Update maintainers (#233) (#237)

* bump CMake minimum version to avoid CMP0048 warning (#219)

* [Windows] fix rqt_gui_cpp install path (#190)

* [Windows] fix building (#189)

* Contributors: Michael Jeronimo

rqt_gui_py
==========

* Update maintainers (#233) (#237)

* bump CMake minimum version to avoid CMP0048 warning (#219)

rqt_py_common
=============

* Update maintainers (#233) (#237)

* bump CMake minimum version to avoid CMP0048 warning (#219)

* fix missing import bugs (#139)

* Contributors: Michael Jeronimo

rti_connext_dds_cmake_module
============================

* Update rti-connext-dds dependency to 6.0.1. (#71)

* Contributors: Steven! Ragnarök

rttest
======

* Install includes to include/${PROJECT_NAME} (#114)

* Fix include order for cpplint (#113)

* Fixes for uncrustify 0.72 (#111)

* Mark dependent targets as PRIVATE (#112)

* Export modern CMake targets (#110)

* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

rviz2
=====

* Change links index.ros.org -> docs.ros.org. (#698)

* Contributors: Chris Lalancette

rviz_assimp_vendor
==================

* Make sure to pass compiler and flags down to assimp (#844)

* Fix support for assimp 5.1.0 (#817)

* Contributors: Chris Lalancette, Silvio Traversaro

rviz_common
===========

* Add implementation for cancel interface (#809)

* Install headers to include/${PROJECT_NAME} (#829)

* Remove definition of PLUGINLIB_DISABLE_BOOST. (#821)

* Fix support for assimp 5.1.0 (#817)

* Fix cpplint errors (#818)

* Set message type for ros topic display (#800)

* Fixes for uncrustify 0.72 (#807)

* Do not block visualization manager updates when opening the display
  panel dialog (#795)

* Switch to using Qt::MiddleButton for RViz. (#802)

* Removed traces in renderPanel (#777)

* move yaml_config_writer.hpp to public includes (#764)

* Update displays_panel.cpp (#745)

* Robot: Report mesh loading issues (#744)

* Exposed tool_manager header file. (#767)

* refactor: make const getter methods const (#756)

* Efficiently handle 3-bytes pixel formats (#743)

* Report sample lost events (#686)

* Update window close icon (#734)

* Fix missing "X" icon in panel close button (#731)

* Add rviz_rendering dependency to rviz_common (#727)

* Remove the word "Alpha" from the splash screen. (#696)

* Removed some memory leaks in rviz_rendering and rviz_rendering_tests
  (#710)

* Contributors: ANDOU Tetsuo, Alejandro Hernández Cordero, Chen Lihui,
  Chris Lalancette, Daisuke Nishimatsu, Gonzo, Ivan Santiago Paunovic,
  Jacob Perron, Joseph Schornak, Rebecca Butler, Shane Loretz, Silvio
  Traversaro, davidorchansky

rviz_default_plugins
====================

* Add far plane distance property to camera (#849)

* Drop ignition-math6 from rviz_default_plugins link interface (#833)

* add implementation for cancel interface (#809)

* Install headers to include/${PROJECT_NAME} (#829)

* Remove definition of PLUGINLIB_DISABLE_BOOST. (#821)

* Remove TF filter from ImageTransportDisplay (#788)

* Add underscores to material names (#811)

* Export image_transport dependency (#813)

* Fixes for uncrustify 0.72 (#807)

* Switch to using Qt::MiddleButton for RViz. (#802)

* Add a tf_buffer_cache_time_ns to tf_wrapper (#792)

* Make libraries to avoid compiling files multiple times (#774)

* Computed inertia with ignition-math (#751)

* Fixed crash when changing rendering parameters for pointcloud2 while
  'Selectable' box is unchecked (#768)

* Robot: Report mesh loading issues (#744)

* Handle NaN values for Wrench msgs (#746)

* Triangle lists support textures (#719)

* Report sample lost events (#686)

* Fix path message orientation error (#736)

* Set topic namespace in interactive markers display (#725)

* mass property visualization (#714)

* Export InteractiveMarker (#718)

* Yuv to rgb changes (#701)

* Extract message type in ImageTransportDisplay (#711)

* Duplicated code RobotJoint (#702)

* Don't attempt to moc generate files that don't have QOBJECT. (#690)

* Switch to including tf2_geometry_msgs.hpp (#689)

* Export Qt5 dependencies properly (#687)

* Add support for namespace-scoped DELETEALL action in Marker displays
  (#685)

* Use image_transport to subscribe to image messages (#523)

* Contributors: Akash, Alejandro Hernández Cordero, Audrow Nash, Chen
  Lihui, Chris Lalancette, Cory Crean, Gonzo, Greg Balke, Ivan
  Santiago Paunovic, Jacob Perron, Martin Idel, Michel Hidalgo, Paul,
  Rebecca Butler, Scott K Logan, Shane Loretz, bailaC, brian soe,
  cturcotte-qnx, ketatam

rviz_ogre_vendor
================

* Fix interface link libraries in ogre vendor (#761)

* Fix the build for Ubuntu Jammy arm64. (#828)

* Strip RPATH from installed Ogre binaries (#688)

* Contributors: Chris Lalancette, Laszlo Turanyi, Michel Hidalgo

rviz_rendering
==============

* Make getVerticesPerPoint method public and improve tests (#843)

* Disable class-memaccess warnings for Eigen (#838)

* Disable a warning when including Eigen. (#835)

* Install headers to include/${PROJECT_NAME} (#829)

* Fix support for assimp 5.1.0 (#817)

* Fix cpplint errors (#818)

* Fixes for uncrustify 0.72 (#807)

* Suppress assimp warnings in rviz_rendering build (#775)

* Fix for ogre failing when material already exists (#729)

* Removed some memory leaks in rviz_rendering and rviz_rendering_tests
  (#710)

* Export Qt5 dependencies properly (#687)

* Putting glsl 1.50 resources back in RenderSystem (#668)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob
  Perron, Jorge Perez, Michel Hidalgo, Piotr Jaroszek, Scott K Logan,
  Shane Loretz, Silvio Traversaro, Wolf Vollprecht

rviz_rendering_tests
====================

* Removed some memory leaks in rviz_rendering and rviz_rendering_tests
  (#710)

* Contributors: Alejandro Hernández Cordero

rviz_visual_testing_framework
=============================

* Install headers to include/${PROJECT_NAME} (#829)

* Fixes for uncrustify 0.72 (#807)

* Update includes after rcutils/get_env.h deprecation (#677)

* Contributors: Chris Lalancette, Christophe Bedard, Shane Loretz

sensor_msgs
===========

* Move the find_package statements for BUILD_TESTING (#186)

* Feedback on conditional sensor_msgs_library target (#1) (#183)

* [Fix] Fix image_encodings.hpp's URL in README (#184)

* [Fix] Fix fill_image.hpp's URL in README (#182)

* Add sensor_msgs_library target and install headers to
  include/${PROJECT_NAME} (#178)

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Add YUV420 and YUV444 to image encodings (#172)

* Cleanup mislabeled BSD license (#83)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Fix rosdoc2 warnings in sensor_msgs. (#162)

* Add equidistant distortion model (#160)

* Use rosidl_get_typesupport_target() (#156)

* Update CompressedImage documentation: add 'tiff' as a supported
  format (#154)

* Contributors: Audrow Nash, Chris Lalancette, Grey, Hemal Shah,
  Homalozoa X, Ivan Santiago Paunovic, Martin Günther, Michael
  Jeronimo, Pablo Garrido, Shane Loretz, Tully Foote

sensor_msgs_py
==============

* Add in a compatibility layer for older versions of numpy. (#185)

* Port pointcloud creation to numpy. (#175)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash, Chris Lalancette, Florian Vahl

shape_msgs
==========

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Add prism type to the SolidPrimitive.msg (#166) (#167)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash, Grey, M. Fatih Cırıt

shared_queues_vendor
====================

* Bump version number to avoid conflict

* Update package maintainers (#899)

* Contributors: Chris Lalancette, Michel Hidalgo

sqlite3_vendor
==============

* Bump version number to avoid conflict

* Update package maintainers (#899)

* Contributors: Chris Lalancette, Michel Hidalgo

sros2
=====

* Increase the shutdown timeout for test_generate_policy_no_nodes.
  (#278)

* Contributors: Chris Lalancette

statistics_msgs
===============

* Update maintainers to Chris Lalancette (#130)

* Contributors: Audrow Nash

std_msgs
========

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash, Grey

std_srvs
========

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash

stereo_msgs
===========

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash, Grey

test_cli
========

* Updated maintainers (#489)

* Add changelogs (#473)

* Merge pull request #356 from ros2/issue/321_enhance_parameter_api

* Contributors: Aditya Pande, Ivan Santiago Paunovic

test_cli_remapping
==================

* Update python nodes SIGINT handling (#490)

* Updated maintainers (#489)

* Add changelogs (#473)

* Contributors: Aditya Pande, Ivan Santiago Paunovic

test_communication
==================

* Split test_subscriber into multiple compilation units. (#500)

* Add test_msgs dependency (#497)

* Update python nodes SIGINT handling (#490)

* Updated maintainers (#489)

* Fix deprecated subscriber callback warnings (#483)

* Add tests for BoundedPlainSequences (#481)

* Use rosidl_get_typesupport_target() (#480)

* Use rcpputils/scope_exit.hpp instead of rclcpp/scope_exit.hpp (#479)

* Add changelogs (#473)

* Contributors: Abrar Rahman Protyasha, Aditya Pande, Chris
  Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz

test_interface_files
====================

* Revert "Update package.xml (#18)" (#19)

* Update package.xml (#18)

* Update maintainers to Audrow Nash (#17)

* Added BoundedPlainSequences messages (#14)

* Contributors: Audrow Nash, Chris Lalancette, Miguel Company, Nikolai
  Morin

test_launch_ros
===============

* Increase test time tolerance (#305)

* Use correct namespace when evaluating parameter files for composable
  nodes (#303)

* Handle empty strings when evaluating parameters (#300)

* Add parameter substitution (#297)

* More Helpful Error Messages (#275)

* Update maintainers in setup.py (#287)

* Set parameters from file for composable nodes (#281)

* Update package maintainers (#284)

* Update node name matcher (#282)

* Support both parameter file configurations for composable nodes
  (#259)

* Shutdown context after test (#267)

* Handle substitutions in RosTimer (#264)

* Add SetParametersFromFile action (#260)

* Properly support ros_args attribute through launch frontends (#253)

* Add 'push_ros_namespace' alias to 'push-ros-namespace' (#250)

* Add ros_arguments option to Node action (#249)

* ROS Timer Action (#244)

* Support container in frontend (#235)

* Added normalize_remap_rule and types. (launch #173)

* Fixed setup.py versions (launch #155)

* Fixed a bug to ensure that shutdown event is handled correctly
  (launch #154)

* Made various fixes and added tests for remappings passed to Node
  actions (launch #137)

* Contributors: Aditya Pande, Audrow Nash, Christophe Bedard, David V.
  Lu!!, Jacob Perron, Jorge Perez, Kenji Miyake, Michel Hidalgo,
  Rebecca Butler

test_launch_testing
===================

* Update maintainers to Aditya Pande and Michel Hidalgo (#559)

* Updated maintainers (#555)

* Contributors: Aditya Pande, Audrow Nash

test_msgs
=========

* Install headers to include/${PROJECT_NAME} and Depend on
  rosidl_typesupport_* targets directly (#133)

* Update maintainers to Chris Lalancette (#130)

* Add test fixures for BoundedPlainSequences (#125)

* Added BoundedPlainSequences to test_msgs (#123)

* Contributors: Audrow Nash, Miguel Company, Shane Loretz

test_quality_of_service
=======================

* Update maintainers to Aditya Pande and Shane Loretz (#491)

* Updated maintainers (#489)

* Fix deprecated subscriber callback warnings (#483)

* Add changelogs (#473)

* Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash,
  Ivan Santiago Paunovic

test_rclcpp
===========

* Fix include order for cpplint (#493)

* Fix test (#488)

* Updated maintainers (#489)

* Add tests for rclcpp sigterm handler (#485)

* Fix deprecated subscriber callback warnings (#483)

* Fix deprecation warnings and failures after client API update (#482)

* Use rosidl_get_typesupport_target() (#480)

* Use rcpputils/scope_exit.hpp instead of rclcpp/scope_exit.hpp (#479)

* Add test for defered service callback signature (#478)

* Add changelogs (#473)

* Merge pull request #357 from ros2/ros2_658_leftovers

* Contributors: Abrar Rahman Protyasha, Aditya Pande, Christophe
  Bedard, Ivan Santiago Paunovic, Jacob Perron, Mauro Passerino, Shane
  Loretz

test_rmw_implementation
=======================

* add content-filtered-topic interfaces (#181)

* Fix linter issues (#200)

* Add client/service QoS getters. (#196)

* Added tests for bounded sequences serialization (#193)

* Add RMW_DURATION_INFINITE basic compliance test. (#194)

* Test SubscriptionOptions::ignore_local_publications. (#192)

* Add rmw_publisher_wait_for_all_acked. (#188)

* Wait for server in test_rmw_implementation service tests. (#191)

* Contributors: Barry Xu, Chen Lihui, Emerson Knapp, Jorge Perez, Jose
  Antonio Moral, Michel Hidalgo, Miguel Company, mauropasse

test_security
=============

* Updated maintainers (#489)

* Fix deprecated subscriber callback warnings (#483)

* Add changelogs (#473)

* Simplify the test_secure_subscriber code. (#471)

* Update includes after rcutils/get_env.h deprecation (#472)

* Contributors: Abrar Rahman Protyasha, Aditya Pande, Chris
  Lalancette, Christophe Bedard, Ivan Santiago Paunovic

test_tf2
========

* Fix more instances of Eigen problems on RHEL. (#515)

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* Fix precision loss from using rclcpp::Time::seconds() (#511)

* More Intuitive CLI for Static Transform Publisher (#392)

* Conversion tests for toMsg() (#423)

* Deprecate tf2_geometry_msgs.h (#418)

* Deprecate tf2_kdl.h (#414)

* Deprecate tf2_bullet.h (#412)

* Contributors: Bjar Ne, Chris Lalancette, Hunter L. Allen, Kenji
  Brameld, Shane Loretz

test_tracetools
===============

* Introduce constants for tracepoint names

* Move actual tests out of tracetools_test to new test_tracetools
  package

* Contributors: Christophe Bedard

test_tracetools_launch
======================

* Add support for preloading pthread and dl instrumentation shared
  libs

* Remove profile_fast option and consider LD_PRELOADing both libs

* Fix multiple LdPreload actions not working and add test

* Deprecate 'context_names' param and replace with 'context_fields'

* Move some tests from tracetools_launch to test_tracetools_launch

* Contributors: Christophe Bedard, Ingo Lütkebohle

tf2
===

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* forward declare fromMsg to avoid missing symbols in downstream
  libraries (#485)

* tf2: Enable common linter tests (#469)

* Move time functions into time.cpp.

* Change a for loop to a while loop.

* Switch to C++-style casts.

* Remove totally unused (and unreachable) code.

* Replace NULL with nullptr.

* Fix up some comments.

* Use std::make_shared where we can.

* Replace two comparisons with empty string to empty().

* Make sure to include-what-you-use.

* Remove unnecessary internal method.

* Remove long-deprecated walkToTopParent overload.

* Remove unnecessary test dependencies.

* Remove some references to the ROS 1 wiki.

* Add rosidl_runtime_cpp as build_depend and build_export_depend.

* Minor cleanups in CMakeLists.txt.

* Remove include directory that doesn't exist.

* Remove completely unnecessary target_link_libraries.

* Remove unused speed_test from tf2.

* Suppress clang warnings about enumerator attributes. (#463)

* Change TF2Error names to be a bit more descriptive. (#349)

* Fixed errors due to missing header link. (#432)

* Deprecate tf2_geometry_msgs.h (#418)

* Speedup covariance unwrapping (#399)

* Contributors: Abrar Rahman Protyasha, Chris Lalancette, Dima
  Dorezyuk, João C. Monteiro, Shane Loretz, Shivam Pandey

tf2_bullet
==========

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* Export a tf2_bullet::tf2_bullet target (#495)

* Fix cpplint errors (#497)

* Remove some references to the ROS 1 wiki.

* Fix tf2_bullet dependency export (#428)

* Deprecate tf2_bullet.h (#412)

* Contributors: Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz

tf2_eigen
=========

* Workaround broken RHEL FindEigen3.cmake (#513)

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* Disable mem-access warnings on aarch64. (#506)

* Fix cpplint errors (#497)

* Remove some references to the ROS 1 wiki.

* Add doTransform function for twists or wrenches (#406)

* Reenable stamped eigen tests (#429)

* Deprecate tf2_eigen.h (#413)

* Contributors: AndyZe, Bjar Ne, Chris Lalancette, Jacob Perron, Shane
  Loretz

tf2_eigen_kdl
=============

* Fix more instances of Eigen problems on RHEL. (#515)

* Depend on orocos_kdl_vendor (#473)

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* Fix cpplint errors (#497)

* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

tf2_geometry_msgs
=================

* Make sure to find the right Python executable. (#514)

* Depend on orocos_kdl_vendor (#473)

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* Drop PyKDL dependency in tf2_geometry_msgs (#509)

* Fix cpplint errors (#497)

* Export a tf2_geometry_msgs::tf2_geometry_msgs target (#496)

* Feature: Add doTransform for Wrench messages (#476)

* Remove some references to the ROS 1 wiki.

* Style fixes in tf2_geometry_msgs. (#464)

* Fix for issue #431 - Covariance is not transformed in
  do_transform_pose_with_covariance_stamped (#453)

* doTransform non stamped msgs (#452)

* "tf2_geometry_msgs": Fixing covariance transformation in
  "doTransform<PoseWithCovarianceStamped, TransformStamped>" (#430)

* Geometry nitpicks (#426)

* Conversion tests for toMsg() (#423)

* Deprecate tf2_geometry_msgs.h (#418)

* Contributors: Abrar Rahman Protyasha, Bjar Ne, Chris Lalancette,
  Denis Štogl, Florian Vahl, Jacob Perron, Khasreto, Shane Loretz,
  vineet131

tf2_kdl
=======

* Depend on orocos_kdl_vendor (#473)

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* KDL python formatting and licenses (#425)

* Deprecate tf2_kdl.h (#414)

* Contributors: Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz

tf2_msgs
========

* Remove dead file from tf2_msgs (#415)

* Contributors: Chris Lalancette

tf2_py
======

* Make sure to finalize tf2_py BufferCore. (#505)

* Make tf2_py Use FindPython3 (#494)

* Change TF2Error names to be a bit more descriptive. (#349)

* Remove python_compat.h (#417)

* Contributors: Chris Lalancette, Shane Loretz

tf2_ros
=======

* Install includes to include/${PROJECT_NAME} and use modern CMake
  (#493)

* use dedicated callback group and executor to isolate timer (#447)

* Adding shared pointer definition to tf2 buffer (#508)

* fix for a basic logic (#510)

* Fix precision loss from using rclcpp::Time::seconds() (#511)

* clear relative callback of Buffer if MessageFilter is destroyed
  (#490)

* More info in tf2_echo output (#468)

* Fix cpplint errors (#497)

* Fixes for uncrustify 0.72 (#486)

* More Intuitive CLI for Static Transform Publisher (#392)

* Reduce transform listener nodes (#442)

* "tf2_ros": Fix deprecated subscriber callbacks (#448)

* Fix tf2_echo does not work with ros-args (#407) (#408)

* Contributors: Abrar Rahman Protyasha, Chen Lihui, Chris Lalancette,
  Hunter L. Allen, Jacob Perron, Kenji Brameld, PGotzmann, Shane
  Loretz, Steve Macenski, Zhenpeng Ge, gezp, simulacrus

tf2_ros_py
==========

* Drop PyKDL dependency in tf2_geometry_msgs (#509)

* Add in one more destroy call that was missed in testing. (#504)

* Be much more careful about cleanup in the tf2_ros_py tests. (#499)

* Use the correct type for BufferClient timeout_padding. (#498) It
  should be a duration, not a float.

* Update maintainers to Alejandro Hernandez Cordero and Chris
  Lalancette (#481)

* Fix buffer_client.py using default timeout_padding (#437)

* Use underscores instead of dashes in setup.cfg. (#403)

* Contributors: Audrow Nash, Carlos Andrés Álvarez Restrepo, Chris
  Lalancette, Florian Vahl

tf2_sensor_msgs
===============

* Disable mem-access warnings on aarch64. (#506)

* Fix cpplint errors (#497)

* Reenable sensor_msgs test (#422)

* Deprecate tf2_sensor_msgs.h (#416)

* Contributors: Bjar Ne, Chris Lalancette, Jacob Perron

tf2_tools
=========

* Update maintainers to Alejandro Hernandez Cordero and Chris
  Lalancette (#481)

* Remove unused import (#465)

* Adding date-time to frames filename (#454)

* Use underscores instead of dashes in setup.cfg. (#403)

* Contributors: Audrow Nash, Hannu Henttinen, Nisala Kalupahana

tlsf
====

* Install headers to include/${PROJECT_NAME} (#11)

* Export a modern CMake target instead of old-style variables (#10)

* Contributors: Shane Loretz

tlsf_cpp
========

* Install includes to include/${PROJECT_NAME} (#114)

* Export modern CMake targets (#110)

* Remove the use of malloc hooks from the tlsf_cpp tests. (#109)

* Contributors: Chris Lalancette, Shane Loretz

topic_monitor
=============

* Update maintainers to Audrow Nash and Michael Jeronimo (#543)

* Small cleanups to the topic monitor. (#517)

* Fix topic_monitor for high publication rate (#461)

* Use is_alive for threads. (#510)

* Contributors: Audrow Nash, Chris Lalancette, Elias De Coninck

topic_statistics_demo
=====================

* Install includes to include/${PROJECT_NAME} (#548)

* Additional fixes for documentation in demos. (#538)

* Fixing deprecated subscriber callback warnings (#532)

* Contributors: Abrar Rahman Protyasha, Chris Lalancette, Shane Loretz

tracetools
==========

* Install headers to include/${PROJECT_NAME}

* Merge branch 'update-mentions-of-tracetools-test' into 'master'
  Update applicable mentions of tracetools_test to test_tracetools See
  merge request ros-tracing/ros2_tracing!259

* Update applicable mentions of tracetools_test to test_tracetools

* Merge branch 'version-3-1-0' into 'master' Version 3.1.0 See merge
  request ros-tracing/ros2_tracing!256

* Correctly handle calls to TRACEPOINT() macro with no tracepoint args

* Move publisher handle tracepoint argument from rclcpp_publish to
  rcl_publish

* Add support for rmw init/pub, take, and executor instrumentation

* Export target on Windows and export an interface if
  TRACETOOLS_DISABLED

* Remove deprecated utility functions

* Contributors: Christophe Bedard, Ivan Santiago Paunovic, Shane
  Loretz

tracetools_launch
=================

* Disable kernel tracing by default

* Don't require kernel tracer and detect when it's not installed

* Add support for preloading pthread and dl instrumentation shared
  libs

* Remove profile_fast option and consider LD_PRELOADing both libs

* Improve event matching for shared lib preloading

* Improve LdPreload action's lib-finding function and add proper tests

* Fix multiple LdPreload actions not working and add test

* Deprecate 'context_names' param and replace with 'context_fields'

* Support per-domain context fields for the Trace action

* Improve LdPreload.get_shared_lib_path() for when a static lib may
  exist

* Move some tests from tracetools_launch to test_tracetools_launch

* Expose Trace action as frontend action and support substitutions

* Contributors: Christophe Bedard, Ingo Lütkebohle

tracetools_test
===============

* Allow providing additional actions for TraceTestCase

* Remove default value for 'package' kwarg for TraceTestCase

* Move actual tests out of tracetools_test to new test_tracetools
  package

* Add tests for rmw init/pub, take, and executor instrumentation

* Add field type assertion utilities to TraceTestCase

* Fixing deprecated subscriber callback warnings

* Contributors: Abrar Rahman Protyasha, Christophe Bedard

tracetools_trace
================

* Disable kernel tracing by default

* Don't require kernel tracer and detect when it's not installed

* Introduce constants for tracepoint names

* Optimize default tracing session channel config values

* Deprecate 'context_names' param and replace with 'context_fields'

* Support per-domain context fields for the Trace action

* Add support for rmw init/pub, take, and executor tracepoints

* Contributors: Christophe Bedard

trajectory_msgs
===============

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Contributors: Audrow Nash, Grey

turtlesim
=========

* Use "double" when handling "qreal orient\_" (#114)

* Add Rolling Icon (#133)

* Update maintainers to Audrow Nash and Michael Jeronimo (#137)

* Fixing deprecated subscriber callback warnings (#134)

* Use rosidl_get_typesupport_target() (#132)

* Print out the correct node name on startup. (#122)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette,
  Katherine Scott, Seulbae Kim, Shane Loretz

urdf
====

* Install headers to include/${PROJECT_NAME} (#31)

* Add linter tests and fix errors (#30)

* Add in a Doxyfile to predefine macros. (#28)

* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

urdf_parser_plugin
==================

* Install headers to include/${PROJECT_NAME} (#31)

* Add linter tests and fix errors (#30)

* Contributors: Jacob Perron, Shane Loretz

visualization_msgs
==================

* Interface packages should fully <depend> on the interface packages
  that they depend on (#173)

* Update maintainers to Geoffrey Biggs and Tully Foote (#163)

* Marker Textures (#153)

* Document namespace scoped marker deletion. (#151)

* Contributors: Audrow Nash, Greg Balke, Grey, Michel Hidalgo

yaml_cpp_vendor
===============

* Add missing dependency on yaml-cpp (#32)

* Upgrade to yaml-cpp 0.7.0 (#25)

* Contributors: Chris Lalancette, Scott K Logan

zstd_vendor
===========

* Bump version number to avoid conflict

* Use git hash for zstd vendor (#969)

* Update package maintainers (#899)

* Declare missing dependency on 'git' in zstd_vendor (#890)

* Switch to using 'git apply' for zstd_vendor patches (#846)

* Contributors: Chris Lalancette, Christophe Bedard, Michel Hidalgo,
  Scott K Logan, Shane Loretz
