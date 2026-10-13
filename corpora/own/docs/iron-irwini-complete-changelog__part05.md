# Iron Irwini Changelog (part 5 of 5)

* Update rosidl_typesupport_fastrtps to C++17. (#94)

* [rolling] Update maintainers - 2022-11-07 (#93)

* Replace rosidl_cmake imports with rosidl_pycommon (#91)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Jacob Perron, Tyler Weaver

rosidl_typesupport_interface
============================

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Contributors: Audrow Nash, Brian

rosidl_typesupport_introspection_c
==================================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Expose type hash on typesupports (rep2011) (#729)

* Type hash in interface codegen (rep2011) (#722)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Move rosidl_cmake Python module to a new package rosidl_pycommon
  (#696) Deprecate the Python module in rosidl_cmake and move the
  implementation to the new package rosidl_pycommon.

* Fix build export dependencies in C introspection package (#695)

* Add namespaced ALIAS target to easily consume generated libraries
  via add_subdirectory (#605)

* Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron,
  Silvio Traversaro

rosidl_typesupport_introspection_cpp
====================================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Expose type hash on typesupports (rep2011) (#729)

* Type hash in interface codegen (rep2011) (#722)

* Make sure to add the event message to typesupport introspection cpp.
  (#724)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Move rosidl_cmake Python module to a new package rosidl_pycommon
  (#696) Deprecate the Python module in rosidl_cmake and move the
  implementation to the new package rosidl_pycommon.

* Add namespaced ALIAS target to easily consume generated libraries
  via add_subdirectory (#605)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Jacob Perron, Silvio Traversaro

rosidl_typesupport_introspection_tests
======================================

* Fix a few more clang analysis problems. (#731) In particular, make
  sure to mark the fact that we are C++17 (as the emplace_back
  signature changed), and also add in a few more (void)_ for benchmark
  tests.

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Contributors: Audrow Nash, Brian, Chris Lalancette

rosidl_typesupport_tests
========================

* typesupport_tests needs to be updated to C++17 (#137)

* Fix Typesupport Introspection tests (#133)

* Make rosidl_typesupport_tests depend on rosidl_generator_cpp. (#132)

* Service introspection (#127)

* Contributors: Brian, Chris Lalancette, Cristóbal Arroyo, Lucas
  Wendland

rpyutils
========

* [rolling] Update maintainers - 2022-11-07 (#10)

* Mirror rolling to master

* updating maintainer

* Contributors: Audrow Nash, Dharini Dutia

rqt
===

* fix build of "rqt" with "setuptools>=v61.0.0" (#271)

* [rolling] Update maintainers - 2022-11-07 (#283)

* Fix up the package description. (#250)

* Contributors: Audrow Nash, Chris Lalancette, Daniel Reuter, Dharini
  Dutia, quarkytale

rqt_action
==========

* [rolling] Update maintainers - 2022-11-07 (#14)

* Small cleanups to the rqt_action plugin (#13)

* Mirror rolling to ros2

* Contributors: Audrow Nash, Chris Lalancette

rqt_bag
=======

* Use default storage id (#140)

* Use rosbag2_py API instead of direct bag parsing

* [rolling] Update maintainers - 2022-11-07 (#132)

* For get_entry_after, bump by 1 nanosecond otherwise always get the
  same message equal to the timestamp

* Use rosbag2_py.reader for all message queries, remove sqlite3 direct
  usage

* Cleanup for review

* Improved logging

* Use a rosbag2_py.Reader to get bag metadata

* Disable reading from bag while recording - use direct caching to
  index for timeline

* Increase publishing checkbox size (#122)

* Fix toggle thumbnails button (#117)

* ensure data types match what PyQt expects (#118)

* Visualize topics being published and highlight topic being selected
  (#116)

* Be able to scroll up and down, not only zoom-in and out the timeline
  (#114)

* [Fixes] Fix crash when no qos metadata, make scroll bar appear if
  needed, add gitignore (#113)

* Fix the types being passed into QFont and QColor. (#109)

* Fix tuples for bisect calls (#67) (#76)

* fix long topic names (#114)

* fix zoom behavior (#76)

* Contributors: Audrow Nash, Chris Lalancette, Emerson Knapp, Ivan
  Santiago Paunovic, Kenji Brameld, Yadunund

rqt_bag_plugins
===============

* Changes the use of __slots__ for the field and field type getter
  (#138)

* [rolling] Update maintainers - 2022-11-07 (#132)

* Contributors: Audrow Nash, Eloy Briceno

rqt_console
===========

* [rolling] Update maintainers - 2022-11-07 (#39)

* added new maintainer

* Contributors: Arne Hitzmann, Audrow Nash

rqt_graph
=========

* Refresh rosgraph when params checkbox is clicked (#87)

* [rolling] Update maintainers - 2022-11-07 (#83)

* Minor cleanup (#80)

* Mirror rolling to galactic-devel

* graph load/save into DOT file corrections for py3 (#78)

* Remove repeated prefixes from buttons

* Contributors: Audrow Nash, Chris Lalancette, David V. Lu!!,
  Yadunund, mergify[bot]

rqt_gui
=======

* [rolling] Update maintainers - 2022-11-07 (#283)

* Display basic help information when no plugins are loaded (#268)

* Contributors: Audrow Nash, Dharini Dutia, Michael Jeronimo,
  quarkytale

rqt_gui_cpp
===========

* Update rqt to C++17. (#285)

* [rolling] Update maintainers - 2022-11-07 (#283)

* Contributors: Audrow Nash, Chris Lalancette, Dharini Dutia,
  quarkytale

rqt_gui_py
==========

* Fix an exception raised when terminating with Ctrl+c (#292)

* [rolling] Update maintainers - 2022-11-07 (#283)

* Contributors: Audrow Nash, Chen Lihui, Dharini Dutia, quarkytale

rqt_msg
=======

* [rolling] Update maintainers - 2022-11-07 (#17)

* Contributors: Audrow Nash

rqt_plot
========

* Fix regression from #87 (#91)

* Changes the use of __slots__ for the field and field type getter
  (#87)

* [rolling] Update maintainers - 2022-11-07 (#83)

* Fix fixed-size Array visualization (#81)

* Contributors: Audrow Nash, Eloy Briceno, Jacob Perron, Michael
  Jeronimo, Yadunund

rqt_publisher
=============

* Changes the use of __slots__ for the field and field type getter

* [rolling] Update maintainers - 2022-11-07 (#36)

* Minor cleanups in rqt_publisher for ROS 2 (#35)

* Delete sync to foxy-devel workflow

* Merge pull request #33 from NBadyal/improve-evaluation-of-types

* Use regex matching to strip errors from input

* Change slot_type verification strategy

* Mirror rolling to foxy-devel

* Contributors: Audrow Nash, Chris Lalancette, Geoffrey Biggs, Michael
  Jeronimo, Nicholas Badyal, Voldivh

rqt_py_common
=============

* Changes the use of __slots__ for the field and field type getter
  (#289)

* [rolling] Update maintainers - 2022-11-07 (#283)

* Contributors: Audrow Nash, Dharini Dutia, Eloy Briceno, quarkytale

rqt_py_console
==============

* [rolling] Update maintainers - 2022-11-07 (#13)

* Contributors: Audrow Nash, Jacob Perron

rqt_reconfigure
===============

* reorder imports to fix flake8 warning (#129)

* Fixed validator locale when float value is not bound in a range.
  (#121)

* get parameter type from descriptor

* [rolling] Update maintainers - 2022-11-07 (#122)

* Cleanup mislabeled BSD license (#66)

* Add support for array types (#108)

* Fix float slider step size (#117)

* update maintainer

* Fixed package to run with ros2 run (#81)

* fix updating range limits (#108)

* Improvement; "GUI hangs for awhile or completely, when any one of
  nodes doesn't return any value" (#81)

* Contributors: Aris Synodinos, Audrow Nash, Christian Rauch, Dharini
  Dutia, Florian Vahl, Jacob Perron, Shrijit Singh, Tully Foote,
  quarkytale

rqt_service_caller
==================

* [rolling] Update maintainers - 2022-11-07 (#25)

* Contributors: Audrow Nash, Jacob Perron

rqt_shell
=========

* [rolling] Update maintainers - 2022-11-07 (#17)

* Contributors: Audrow Nash, Jacob Perron

rqt_srv
=======

* [rolling] Update maintainers - 2022-11-07 (#10)

* Contributors: Audrow Nash, Jacob Perron

rqt_topic
=========

* [rolling] Update maintainers - 2022-11-07 (#43)

* Implement bandwidth monitoring (#40)

* Fix the display of array type elements. (#41)

* Fix removal of topics while they are being monitored. (#39)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

rti_connext_dds_cmake_module
============================

* Use unified approach for checking the existence of environment
  variables (#117)

* Contributors: Christopher Wecht

rttest
======

* [rolling] Update maintainers - 2022-11-07 (#121)

* Addressing issues found in Humble testing (#116)

* Contributors: Audrow Nash, Michael Carroll

rviz2
=====

* Make rviz1_to_rviz2.py accept configs with missing values (#945)

* Update rviz to C++17. (#939)

* [rolling] Update maintainers - 2022-11-07 (#923)

* Add rviz1_to_rviz2.py conversion script (#882)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

rviz_assimp_vendor
==================

* If vendored assimp is present, always prefer that (#970)

* [rolling] Update maintainers - 2022-11-07 (#923)

* Fixes policy CMP0135 warning for CMake >= 3.24 (#898)

* Contributors: Audrow Nash, Cristóbal Arroyo, Scott K Logan

rviz_common
===========

* Update Frame shortcut (#958) * Update Frame shortcut

* Update rviz to C++17. (#939)

* [rolling] Update maintainers - 2022-11-07 (#923)

* Remove YAML_CPP_DLL define (#831)

* Document getTransform() time behavior (#893)

* Ogre 1.12.10 upgrade (#878)

* Add RVIZ_COMMON_PUBLIC macro (#865)

* Add time jump handler (#752) (#791)

* Make sure not to dereference a null Renderable pointer. (#850)

* Contributors: Akash, Audrow Nash, Chris Lalancette, David V. Lu!!,
  Kenji Brameld, Marcel Zeilinger, Shane Loretz, juchajam

rviz_default_plugins
====================

* Fix ODR errors with gmock (#967)

* Update Frame shortcut (#958)

* point_marker: fix bug where the number of rendered points
  accumulates over time (#949)

* Update rviz to C++17. (#939)

* Fix tolerance calculation precision (#934)

* Fix MeshResourceMarker for mesh with color-based embedded material
  (#928)

* [rolling] Update maintainers - 2022-11-07 (#923)

* Add Map Display binary option (#846)

* Delete frame_locked_markers when reusing marker (#907)

* Consider region of interest in CameraDisplay (#864)

* std::copy fix - OccupancyGridUpdate - Data is not being processed
  correctly (#895)

* Set error status when duplicate markers are in the same MarkerArray
  (#891)

* Make Axes display use latest transform (#892)

* Show link names in inertia error message (#874)

* Ogre 1.12.10 upgrade (#878)

* Use make_shared to construct PointCloud2 (#869)

* Fix include order (#858)

* Contributors: AndreasR30, Audrow Nash, Chris Lalancette, David V.
  Lu!!, Eric, Hunter L. Allen, Jacob Perron, Kenji Brameld, Patrick
  Roncagliolo, Shane Loretz, Timon Engelke, Xavier BROQUERE, Xenofon
  Karamanos, methylDragon

rviz_ogre_vendor
================

* Fix build failures on macOS + Apple Silicon (#944)

* [rolling] Update maintainers - 2022-11-07 (#923)

* Remove broken rviz_ogre_vendor::RenderSystem_GL target (#920)

* Fixes policy CMP0135 warning for CMake >= 3.24 (#898)

* Ogre 1.12.10 upgrade (#878)

* Make resource file paths relative (#862)

* Use CMAKE_STAGING_PREFIX for staging OGRE installation (#861)

* Contributors: Audrow Nash, Cristóbal Arroyo, Kenji Brameld, Scott K
  Logan, Shane Loretz, Yadu

rviz_rendering
==============

* [rolling] Update maintainers - 2022-11-07 (#923)

* add test to ensure binary STL files from SOLIDWORKS get imported
  without a warning (#917)

* Ogre 1.12.10 upgrade (#878)

* Stop using glsl150 resources for now. (#851)

* Contributors: Audrow Nash, Chris Lalancette, Kenji Brameld

rviz_rendering_tests
====================

* [rolling] Update maintainers - 2022-11-07 (#923)

* add test to ensure binary STL files from SOLIDWORKS get imported
  without a warning (#917)

* Contributors: Audrow Nash, Kenji Brameld

rviz_visual_testing_framework
=============================

* Update rviz to C++17. (#939)

* [rolling] Update maintainers - 2022-11-07 (#923)

* Ogre 1.12.10 upgrade (#878)

* Contributors: Audrow Nash, Chris Lalancette, Kenji Brameld

sensor_msgs
===========

* update YUV format codes and documentation (#214)

* sensor_msgs/Range lacks variance field (#181)

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Replaced non-ASCII dash symbol with ASCII dash (#208)

* Add NV21 and NV24 to colour formats (#205)

* Update BatteryState.msg (#206)

* use regex for matching cv types (#202)

* Fix outdated file path for image_encodings (#200)

* Use uint32_t for pointcloud2 resize method (#195)

* Retain width and height after resize for master (#193)

* Contributors: Audrow Nash, Borong Yuan, Chris Lalancette, Christian
  Rauch, El Jawad Alaa, Geoffrey Biggs, Ivan Zatevakhin, Kenji
  Brameld, Tianyu Li

sensor_msgs_py
==============

* Add missing dep for sensor_msgs_py (#217)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Add support for non standard point step sizes (#199)

* Remove reference to old implementation (#198)

* Contributors: Audrow Nash, Florian Vahl, Yadu

service_msgs
============

* Update common_interfaces to C++17. (#215) (#151)

* Add service_msgs package (#143)

* Contributors: Brian, Chris Lalancette

shape_msgs
==========

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Fix SolidPrimitive.msg to contain a single Polygon (#189)

* Contributors: Audrow Nash, Chris Lalancette, M. Fatih Cırıt

shared_queues_vendor
====================

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Fixes policy CMP0135 warning for CMake >= 3.24 (#1084)

* Contributors: Cristóbal Arroyo, Michael Orlov

spdlog_vendor
=============

* Update to spdlog 1.9.2 (#33)

* [rolling] Update maintainers - 2022-11-07 (#31)

* Update to spdlog 1.9.1 (#27)

* Fixes policy CMP0135 warning for CMake >= 3.24 (#30)

* build shared lib only if BUILD_SHARED_LIBS is set (#29)

* Mirror rolling to master

* xml tag order

* updating maintainer

* Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo,
  Dharini Dutia, Scott K Logan, hannes09

sqlite3_vendor
==============

* Update to sqlite3 3.37.2 (#1274) This matches version distributed in
  Ubuntu Jammy.

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Fixes policy CMP0135 warning for CMake >= 3.24 (#1084)

* Contributors: Cristóbal Arroyo, Michael Orlov, Scott K Logan

sros2
=====

* Fix SSH commands in SROS2_Linux.md (#286)

* Make type of get_package_share_directory apparent for sphinx (#284)

* Contributors: Boris Boutillier, Yadu

statistics_msgs
===============

* Update common_interfaces to C++17. (#215) (#151)

* [rolling] Update maintainers - 2022-11-07 (#150)

* Contributors: Audrow Nash, Chris Lalancette

std_msgs
========

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Contributors: Audrow Nash, Chris Lalancette

std_srvs
========

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Contributors: Audrow Nash, Chris Lalancette

stereo_msgs
===========

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Contributors: Audrow Nash, Chris Lalancette

tango_icons_vendor
==================

* [rolling] Update maintainers - 2022-11-07 (#10)

* Mirror rolling to master

* Contributors: Audrow Nash

test_cli
========

* Update the system tests to C++17. (#510)

* [rolling] Update maintainers - 2022-11-07 (#509)

* Contributors: Audrow Nash, Chris Lalancette

test_cli_remapping
==================

* Update the system tests to C++17. (#510)

* [rolling] Update maintainers - 2022-11-07 (#509)

* Contributors: Audrow Nash, Chris Lalancette

test_communication
==================

* Update the system tests to C++17. (#510)

* [rolling] Update maintainers - 2022-11-07 (#509)

* Revert "Replace deprecated spin_until_future_complete with
  spin_until_complete (#499)" (#504)

* Replace deprecated spin_until_future_complete with
  spin_until_complete (#499)

* Contributors: Audrow Nash, Chris Lalancette, Hubert Liberacki,
  William Woodall

test_interface_files
====================

* [rolling] Update maintainers - 2022-11-07 (#21)

* Mirror rolling to master

* Contributors: Audrow Nash

test_launch_ros
===============

* Enable document generation using rosdoc2 (#359)

* Fix normalize_parameters_dict for multiple nodes in the same
  namespace (#347)

* Implement None check for ComposableNodeContainer (#341)

* Add LifecyleTransition action (#317)

* Ensure load_composable_nodes respects condition (#339)

* [rolling] Update maintainers - 2022-11-07 (#331)

* RosTimer -> ROSTimer and PushRosNamespace -> PushROSNamespace, to
  follow PEP8 (#326)

* add SetROSLogDir action (#325)

* Support default values in parameter substitution (#313)

* Run condition for composable nodes (#311)

* Load composable nodes in sequence (#315)

* Contributors: Aditya Pande, Alexey Merzlyakov, Audrow Nash,
  Christoph Hellmann Santos, Kenji Miyake, Shane Loretz, William
  Woodall, Yadu, methylDragon

test_launch_testing
===================

* [rolling] Update maintainers - 2022-11-07 (#671)

* Contributors: Audrow Nash

test_msgs
=========

* Update common_interfaces to C++17. (#215) (#151)

* [rolling] Update maintainers - 2022-11-07 (#150)

* Depend on rosidl_core_generators for packages required by actions
  (#144)

* Make the functions in the header static inline (#140)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

test_osrf_testing_tools_cpp
===========================

* Changing C++ Compile Version (#76)

* Update maintainers (#74)

* Contributors: Audrow Nash, Lucas Wendland

test_quality_of_service
=======================

* Fix ODR errors with gtest (#514)

* Avoid flaky test (#513)

* Update the system tests to C++17. (#510)

* [rolling] Update maintainers - 2022-11-07 (#509)

* Pass rclcpp::QoS to create_service (#507)

* Pass rclcpp::QoS to create_client (#506)

* Remove Werror from test_quality_of_service. (#503)

* Revert "Replace deprecated spin_until_future_complete with
  spin_until_complete (#499)" (#504)

* Replace deprecated spin_until_future_complete with
  spin_until_complete (#499)

* Add tests for 'best available' QoS policies (#501)

* Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Hubert
  Liberacki, Jacob Perron, Shane Loretz, William Woodall, methylDragon

test_rclcpp
===========

* Update the system tests to C++17. (#510)

* [rolling] Update maintainers - 2022-11-07 (#509)

* Pass rclcpp::QoS to create_service (#507)

* Pass rclcpp::QoS to create_client (#506)

* Revert "Replace deprecated spin_until_future_complete with
  spin_until_complete (#499)" (#504)

* Replace deprecated spin_until_future_complete with
  spin_until_complete (#499)

* Contributors: Audrow Nash, Chris Lalancette, Hubert Liberacki, Shane
  Loretz, William Woodall

test_rmw_implementation
=======================

* Add tests for rmw matched event (#216)

* Update rmw_implementation to C++17. (#214)

* [rolling] Update maintainers - 2022-11-07 (#212)

* Add rmw_get_gid_for_client & tests (#206)

* Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette

test_ros2trace
==============

* Move ros2trace tests to new test_ros2trace package (#63)

* Contributors: Christophe Bedard

test_security
=============

* [rolling] Update maintainers - 2022-11-07 (#509)

* Contributors: Audrow Nash

test_tf2
========

* Update the demos to C++17. (#578)

* Update maintainers (#560)

* Contributors: Audrow Nash, Chris Lalancette

test_tracetools
===============

* Disable tracing on Android (#72)

* Add intra-process tracepoints (#30)

* Allow requiring minimum lttng package version for is_lttng_installed
  (#59)

* Disable tracing on macOS (#53)

* Include tracepoints by default on Linux (#31)

* Fix memory leak in tracetools::get_symbol() (#43)

* Update tracing to C++17. (#33)

* Contributors: Chris Lalancette, Christophe Bedard, Przemysław
  Dąbrowski, ymski

test_tracetools_launch
======================

* Error out if trace already exists unless 'append' option is used
  (#58)

* Make subbuffer size configurable with Trace action (#51)

* Allow requiring minimum lttng package version for is_lttng_installed
  (#59)

* Enable document generation using rosdoc2 for ament_python pkgs (#50)

* Contributors: Christophe Bedard, Christopher Wecht, Yadu

tf2
===

* Fix error code returned in BufferCore::walkToTopParent (#602)

* Depend on ament_cmake_ros to default SHARED to ON (#591)

* Fix a potential crash in TimeCache::findClosest (#592)

* Extend TimeCache API to provide rich ExtrapolationException infos
  (#586)

* Update geometry2 to C++17 (#584)

* Include required header Scalar.h (#559)

* Update maintainers (#560)

* Contributors: Audrow Nash, Chris Lalancette, Patrick Roncagliolo,
  Shane Loretz, Tyler Weaver

tf2_bullet
==========

* Update the demos to C++17. (#578)

* Update maintainers (#560)

* Contributors: Audrow Nash, Chris Lalancette

tf2_eigen
=========

* Update the demos to C++17. (#578)

* Update maintainers (#560)

* Contributors: Audrow Nash, Chris Lalancette

tf2_eigen_kdl
=============

* Update geometry2 to C++17 (#584)

* Update maintainers (#560)

* Use orocos_kdl_vendor and orocos-kdl target (#534)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

tf2_geometry_msgs
=================

* Add do_transform_polygon_stamped (#582)

* Update the demos to C++17. (#578)

* Update maintainers (#560)

* Add torque due to force offset (#538)

* Use orocos_kdl_vendor and orocos-kdl target (#534)

* Contributors: Audrow Nash, Chris Lalancette, Paul Gesel, Scott K
  Logan, Tony Najjar

tf2_kdl
=======

* Update the demos to C++17. (#578)

* Update maintainers (#560)

* Use orocos_kdl_vendor and orocos-kdl target (#534)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

tf2_msgs
========

* Update geometry2 to C++17 (#584)

* Update maintainers (#560)

* Remove action_msgs dependency (#547)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

tf2_py
======

* Update geometry2 to C++17 (#584)

* Update maintainers (#560)

* Contributors: Audrow Nash, Chris Lalancette

tf2_ros
=======

* Destroy callback group before node (#595)

* Enable TransformListener node-based constructor in Intra-process
  enabled components (#572)

* Fix use-after-free bug in BufferServer::cancelCB (#579)

* Update the demos to C++17. (#578)

* add constructor to static tf broadcaster accepting node interfaces
  (#576)

* Update maintainers (#560)

* Switching from sstream to c string formatting to fix ros arg issue
  (#557)

* allow construction of tf broadcaster from node object (not a
  pointer) (#555)

* Allow to construct "TransformBroadcaster" and "TransformListener"
  from node interfaces (#552)

* Suppress spam from calling canTransform (#529)

* Contributors: Alberto Soragna, Alexander Hans, Audrow Nash, Chris
  Lalancette, Gonzo, Michael Carroll, Patrick Roncagliolo

tf2_ros_py
==========

* Update sys.path with wokring directory (#594)

* Enable document generation using rosdoc2 for ament_python pkgs
  (#587)

* Update maintainers (#560)

* Use pytest rather than unittest to enable repeat (#558)

* Contributors: Audrow Nash, Michael Carroll, Yadu

tf2_sensor_msgs
===============

* Update the demos to C++17. (#578)

* Update maintainers (#560)

* feat: export tf2 sensor msgs target (#536)

* tf2_sensor_msgs find the right Python executable. (#525)

* Add missing ament_cmake_pytest package needed because of newly-
  enabled test (#520)

* Port point cloud transformation to numpy (#507)

* Contributors: Audrow Nash, Chris Lalancette, Daisuke Nishimatsu,
  Florian Vahl, Jorge Perez, Michael Jeronimo

tf2_tools
=========

* Enable document generation using rosdoc2 for ament_python pkgs
  (#587)

* Update maintainers (#560)

* Contributors: Audrow Nash, Yadu

tlsf
====

* [rolling] Update maintainers - 2022-11-07 (#13)

* Update maintainers (#12)

* Contributors: Audrow Nash, methylDragon

tlsf_cpp
========

* Update realtime support to C++17. (#122)

* [rolling] Update maintainers - 2022-11-07 (#121)

* Addressing issues found in Humble testing (#116)

* Contributors: Audrow Nash, Chris Lalancette, Michael Carroll

topic_monitor
=============

* update launch file name format to match documentation (#588)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Patrick Wspanialy

topic_statistics_demo
=====================

* Update the demos to C++17. (#594)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Chris Lalancette

tracetools
==========

* Disable tracing on Android (#72)

* Add intra-process tracepoints (#30)

* Improve tracetools rosdoc2/doxygen output (#57)

* Update README and other documentation (#55)

* Disable tracing on macOS (#53)

* Include tracepoints by default on Linux (#31)

* Explicitly link against dl for dladdr() (#48)

* Fix memory leak in tracetools::get_symbol() (#43)

* Add TRACEPOINT_ENABLED() and DO_TRACEPOINT() macros (#46)

* Update tracing to C++17. (#33)

* Add new rclcpp_subscription_init tracepoint to support new intra-
  process comms

* Contributors: Chris Lalancette, Christophe Bedard, Przemysław
  Dąbrowski, ymski

tracetools_launch
=================

* Error out if trace already exists unless 'append' option is used
  (#58)

* Improve 'ros2 trace' command error handling & add end-to-end tests
  (#54)

* Make subbuffer size configurable with Trace action (#51)

* Enable document generation using rosdoc2 for ament_python pkgs (#50)

* Remove deprecated context_names parameter (#38)

* Contributors: Christophe Bedard, Christopher Wecht, Yadu

tracetools_trace
================

* Error out if trace already exists unless 'append' option is used
  (#58)

* Improve 'ros2 trace' command error handling & add end-to-end tests
  (#54)

* Make subbuffer size configurable with Trace action (#51)

* Add intra-process tracepoints (#30)

* Allow requiring minimum lttng package version for is_lttng_installed
  (#59)

* Include tracepoints by default on Linux (#31)

* Enable document generation using rosdoc2 for ament_python pkgs (#50)

* Replace distutils.version.StrictVersion with
  packaging.version.Version (#42)

* Remove deprecated context_names parameter (#38)

* Contributors: Christophe Bedard, Christopher Wecht, Yadu, ymski

trajectory_msgs
===============

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Contributors: Audrow Nash, Chris Lalancette

turtlesim
=========

* Remove the range constraints from the holonomic parameter. (#150)
  (#151)

* Add icon (#148) (#149)

* Update turtlesim to C++17. (#146)

* [rolling] Update maintainers - 2022-11-07 (#145)

* Add parameter to enable holonomic motion (#131)

* Add humble turtle (#140)

* Contributors: Audrow Nash, Chris Lalancette, Daisuke Sato,
  mergify[bot]

type_description_interfaces
===========================

* Add GetTypeDescription.srv (rep2011) (#153)

* new package and interfaces for describing other types (#146)

* Contributors: Emerson Knapp, William Woodall

unique_identifier_msgs
======================

* [rolling] Update maintainers - 2022-11-07 (#26)

* Depend on rosidl_core instead of rosidl_defaults (#24)

* Mirror rolling to master

* Update maintainers (#22)

* Contributors: Audrow Nash, Jacob Perron, methylDragon

urdf
====

* [rolling] Update maintainers - 2022-11-07 (#35)

* [urdf] package.xml: add missing exec_depend to urdf_parser_plugin
  (#34)

* Provide copy and move constructors for "model" (#33)

* Add linter tests and fix errors (#30)

* fix #30

* Contributors: Audrow Nash, Daniel Reuter, Tobias Neumann

urdf_parser_plugin
==================

* [rolling] Update maintainers - 2022-11-07 (#35)

* Contributors: Audrow Nash

visualization_msgs
==================

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Contributors: Audrow Nash, Chris Lalancette

yaml_cpp_vendor
===============

* [rolling] Update maintainers - 2022-11-07 (#40)

* Export YAML_CPP_DLL define on Windows (#30) (#38)

* Sets CMP0135 policy behavior to NEW (#36)

* Fixes policy CMP0135 warning for CMake >= 3.24 (#35)

* build shared lib only if BUILD_SHARED_LIBS is set (#34)

* Mirror rolling to master

* Contributors: Audrow Nash, Cristóbal Arroyo, Jacob Perron, hannes09

zstd_vendor
===========

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Bump zstd to 1.4.8 in zstd_vendor package (#1132)

* Fix/zstd vendor does not find system zstd (#1111)

* Contributors: DasRoteSkelett, Michael Orlov
