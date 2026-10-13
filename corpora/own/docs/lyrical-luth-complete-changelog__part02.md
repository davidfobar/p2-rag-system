# ROS 2 Lyrical Luth Complete Changelog (part 2 of 6)

* Contributors: Addisu Z. Taddese, Steve Peters

image_common
============

* Update BSD licenses to SPDX identifier (#389) Co-authored-by:
  Alejandro Hernandez Cordero <ahcorde@gmail.com>

* Fix cmake deprecation (#367)

* Contributors: Garrett Brown, mosfet80

image_tools
===========

* Use new ROSIDL aggregate CMake target (#781)

* Don't use "libopencv-dev" for exec (#760)

* Switching to example_interfaces (#674)

* Use EnableRmwIsolation in launch tests (#724)

* Uniform CMAKE min VERSION (#714)

* Lint image_tools/CMakeLists.txt (#712)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas
  Wendland, Michael Carlstrom, Scott K Logan, mosfet80, yadunund

image_transport
===============

* Removed clang warning (#399)

* Include message type (#394)

* Use new ROSIDL aggregate CMake target (#396)

* Update BSD licenses to SPDX identifier (#389) Co-authored-by:
  Alejandro Hernandez Cordero <ahcorde@gmail.com>

* properly shut down rclcpp after all tests complete. (#384)

* Fix QoS override tests (#376)

* Fix rclcpp_lifecycle dependency (#373)

* Fix compilation error with clang (#372)

* Support lifecycle node - NodeInterfaces (#352)

* Fixed clang build (#371)

* fixed build (#369)

* Deprecated rmw_qos_profile_t in favour of rclcpp::QoS (#364)

* Removed deprecated code (#356)

* Fix cmake deprecation (#367)

* Fix topic resolution for plugins (#365)

* Remove windows warnings (#350)

* Add "rclcpp::shutdown" (#347)

* Use target_link_libraries instead of ament_target_dependencies
  (#345)

* Contributors: Alejandro Hernández Cordero, Alex Tyshka, Emerson
  Knapp, Garrett Brown, Shane Loretz, Tomoya Fujita, Yuyuan Yuan,
  mosfet80

image_transport_py
==================

* Use new ROSIDL aggregate CMake target (#396)

* Update BSD licenses to SPDX identifier (#389) Co-authored-by:
  Alejandro Hernandez Cordero <ahcorde@gmail.com>

* Use pybind11 from deb or pixi (#374)

* Support lifecycle node - NodeInterfaces (#352)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Garrett
  Brown

interactive_markers
===================

* fix: Fix compilation on MSVC 2022 (#120)

* Use new ROSIDL aggregate CMake target (#119)

* Cleanup mislabeled BSD license (#118)

* Explicit Time comparissons (#105)

* fix cmake deprecation (#113)

* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Emerson
  Knapp, Janosch Machowinski, mosfet80

intra_process_demo
==================

* Use new ROSIDL aggregate CMake target (#781)

* Don't use "libopencv-dev" for exec (#760)

* Switching to example_interfaces (#674)

* fixup image_pipeline_demo (#755)

* Use EnableRmwIsolation in launch tests (#724)

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas
  Wendland, Michael Carlstrom, Scott K Logan, William Woodall,
  mosfet80

kdl_parser
==========

* Removed kdl vendor dependency (#90)

* Cmake requirement (#88)

* Remove kdl_parser_py. (#89)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  mosfet80

keyboard_handler
================

* fix cmake deprecation (#55)

* Contributors: mosfet80

laser_geometry
==============

* Use new ROSIDL aggregate CMake target (#115)

* Use seconds in sensor_msgs::msg::LaserScan msg inside the test
  (#107)

* Use constructor of rclcpp::Time instead of conversion. (#91)

* fix cmake deprecation (#105)

* Remove hard-coded eigen3 header path for linux hosts (#95) Co-
  authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>

* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Emerson
  Knapp, Lukas Schäper, mosfet80

launch
======

* Correct typos (#961)

* hotfix (#950)

* Declare Boolean Launch Argument (#944)

* Support frontends for PathJoinSubstitution (#943)

* test python substitution with submodules (#688)

* Scope launch file dir/path locals to included launch file (#862)

* Capture the environment variables in TimerAction (#728)

* Remove importlib metadata (#932)

* Fix intersphinx_mapping format (#921)

* Make the directory-finding substitutions into a PathSubstitution for
  / operator (#914)

* Expose StringJoinSubstitution to frontend (#857)

* Shared logic for substitutions (#769)

* Use yaml types (#781)

* Switch osrf_pycommon dependency to system package (#817)

* Fix all/any in xml and yaml launch files (#906)

* Allow providing launch args to include using let in frontends (#848)

* Fix Setuptoolsdeprecations (#898)

* Remove LaunchDescriptionArgument (#891)

* Make sure to install py.typed files (#886)

* use custom log_file name as per the user setting (#861)

* Using "TimerAction" with "SetParameter" from launch_ros causes crash
  (#879)

* Fix "log\_*" warnings (#883)

* Updated "launch" typings (#831)

* Allow Path in substitutions, instead of requiring cast to str (#873)

* Add a "/" path join operator for "PathJoinSubstitution" (#868)

* Other Logging Implementations with "getLevelNamesMapping" fix (#866)

* Revert "Add Other Logging Implementations (#858)" (#865) This
  reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.

* Add Other Logging Implementations (#858)

* Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard,
  David V. Lu!!, Emerson Knapp, Harrison Chen, Jonas Otto, Kenji
  Brameld (TRACLabs), Matthijs van der Burgh, Michael Carlstrom, Scott
  K Logan, Sebastian Javier D'Alessandro Szymanowski, Tanishq
  Chaudhary, Will, mosfet80

launch_pytest
=============

* fix regressions (#959)

* fix: add get_launch_test_fixture_scope for pytest compatibility
  (#949)

* Switch osrf_pycommon dependency to system package (#817)

* Fix Setuptoolsdeprecations (#898)

* Make sure to install py.typed files (#886)

* Add remaining "py.typed" (#884)

* Allow Path in substitutions, instead of requiring cast to str (#873)

* fix(launch_pytest): prevent re-wrapping test funtions on re-run
  (#855)

* Contributors: Christophe Bedard, Daisuke Nishimatsu, David Revay,
  Emerson Knapp, Michael Carlstrom, Scott K Logan, mosfet80

launch_ros
==========

* Fix flake8 (#529)

* correct typos (#524)

* Fix regression (#521)

* Fix rhel10 flake8 error (#515)

* Compatiblity with 'Populate Transitions' ros2/rcl#1269 (#495)

* remove importlib (#508)

* Make FindPackage substitutions a Path to get operator / (#494)

* Expose lifecycle_node (#327) (with test) (#482)

* Expose composable_lifecycle_node in front-end (#480)

* Switch osrf_pycommon dependency to system package (#431)

* Fix SetUseSimTime for launch frontends (#488)

* fix setuptools deprecations (#475)

* improve type readability in errors (#469)

* Fix: LoadComposableNodes fails to parse wildcard param files
  correctly (#460) (#465)

* Contributors: Auguste Lalande, Christophe Bedard, Emerson Knapp,
  Emre Kuru, Jasper van Brakel, Kenji Brameld, Michael Carlstrom,
  Scott K Logan, mosfet80

launch_testing
==============

* Correct typos (#961)

* Fix test_io_tests for Ubuntu26 (#960)

* Fix flake8 (#952)

* Switch osrf_pycommon dependency to system package (#817)

* Fix Setuptoolsdeprecations (#898)

* Make sure to install py.typed files (#886)

* Add remaining "py.typed" (#884)

* Updated "launch" typings (#831)

* Contributors: Auguste Lalande, Christophe Bedard, Michael Carlstrom,
  Scott K Logan, mosfet80

launch_testing_ament_cmake
==========================

* Fix CMake deprecation (#899)

* Contributors: mosfet80

launch_testing_examples
=======================

* improve test integrity with rmw_cyclonedds_cpp. (#440)

* Fix setuptools deprecations (#421)

* Contributors: Tomoya Fujita, mosfet80

launch_testing_ros
==================

* Add tests isolation in launch_testing_ros (#528)

* Surpressing multi-threaded process warning from flake8. (#520)

* correct typos (#524)

* Fix launch_ros_testing shutdown race in WaitForTopics (#511)

* Give the option to inject a quality of service profile (#493)

* fix setuptools deprecations (#475)

* "WaitForTopics": wait for publisher-subscriber connection to be
  established (#474)

* Contributors: Auguste Lalande, Giorgio Pintaudi, Julien Enoch,
  Michael Carroll, Tomoya Fujita, mosfet80

launch_xml
==========

* Correct typos (#961)

* Support frontends for PathJoinSubstitution (#943)

* Capture the environment variables in TimerAction (#728)

* Expose StringJoinSubstitution to frontend (#857)

* Fix all/any in xml and yaml launch files (#906)

* Allow providing launch args to include using let in frontends (#848)

* Fix Setuptoolsdeprecations (#898)

* Make sure to install py.typed files (#886)

* Add remaining "py.typed" (#884)

* Fix "log\_*" warnings (#883)

* Allow Path in substitutions, instead of requiring cast to str (#873)

* Other Logging Implementations with "getLevelNamesMapping" fix (#866)

* Revert "Add Other Logging Implementations (#858)" (#865) This
  reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.

* Add Other Logging Implementations (#858)

* Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard,
  Emerson Knapp, Matthijs van der Burgh, Michael Carlstrom, Sebastian
  Javier D'Alessandro Szymanowski, mosfet80

launch_yaml
===========

* Correct typos (#961)

* Support frontends for PathJoinSubstitution (#943)

* Capture the environment variables in TimerAction (#728)

* Expose StringJoinSubstitution to frontend (#857)

* Fix all/any in xml and yaml launch files (#906)

* Allow providing launch args to include using let in frontends (#848)

* Fix Setuptoolsdeprecations (#898)

* Make sure to install py.typed files (#886)

* Add remaining "py.typed" (#884)

* Fix "log\_*" warnings (#883)

* Other Logging Implementations with "getLevelNamesMapping" fix (#866)

* Revert "Add Other Logging Implementations (#858)" (#865) This
  reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.

* Add Other Logging Implementations (#858)

* Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard,
  Matthijs van der Burgh, Michael Carlstrom, Sebastian Javier
  D'Alessandro Szymanowski, mosfet80

libstatistics_collector
=======================

* Use new aggregate rosidl target instead of _TARGETS (#222)

* fix cmake deprecation (#214)

* Bump ros-tooling/action-ros-ci from 0.3 to 0.4

* Bump codecov/codecov-action from 5.3.1 to 5.4.0

* Bump codecov/codecov-action from 5.1.2 to 5.3.1

* Bump codecov/codecov-action from 5.0.7 to 5.1.2

* Bump codecov/codecov-action from 4.6.0 to 5.0.7

* Contributors: Alexis Tsogias, dependabot[bot], mosfet80

libyaml_vendor
==============

* Replace ament_vendor with cmake module (#67)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#65)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

lifecycle
=========

* Use new ROSIDL aggregate CMake target (#781)

* Switching to example_interfaces (#674)

* r-simonelli/demos-lifecycle (#750)

* Uniform CMAKE min VERSION (#714)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Emerson Knapp, Lucas Wendland, Shane Loretz, mosfet80,
  r-simonelli

lifecycle_msgs
==============

* Use builtin_interfaces/Time for TransitionEvent stamp (#185)

* Fix cmake deprecation (#180)

* Contributors: Jasper van Brakel, mosfet80

lifecycle_py
============

* Add "ament_mypy" support and type hints to "lifecycle_py" (#778)

* Revert lifecycle_py accidental merge - ament_mypy (#777)

* action_tutorials_py: add ament_mypy support (#775)

* Switching to example_interfaces (#674)

* fix setuptools deprecations (#733)

* Contributors: Lucas Wendland, Mohit Kumaresan, mohit, mosfet80

logging_demo
============

* Use new ROSIDL aggregate CMake target (#781)

* Switching to example_interfaces (#674)

* Use EnableRmwIsolation in launch tests (#724)

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas
  Wendland, Scott K Logan, Shane Loretz, mosfet80

lttngpy
=======

* Use <lttng/lttng.h> in lttngpy and clean up includes (#222)

* Allow creating snapshot sessions (#195)

* [Fix] compile fail (#194)

* Use pybind11 from deb or pixi (#197)

* Add support for starting tracing at runtime (#191)

* Contributors: Alejandro Hernández Cordero, RHolland, Shravan Deva,
  mosfet80

map_msgs
========

* Change email address associated with maintainer

* fix cmake deprecation

* Contributors: David V. Lu, Steve Macenski, mosfet80

mcap_vendor
===========

* Update mcap dependency to version 2.1.3 (#2355)

* Remove lz4 vendor package (#2165)

* Replace "zstd_vendor" with "zstd_cmake_module" (#2166)

* Fix CMAKE deprecation (#2067)

* Backport missing "cstdint" include (#2008)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, David
  Anthony, mosfet80

message_filters
===============

* Avoid vector assignment in message_filters signal callback (#292)
  (#293)

* Cleanup headers and removed deadcode (#284) (#291)

* feat(python): add python implementation of InputAligner (backport
  #283) (#286)

* C++20 style (#272)

* (#221) Tutorials: Add DeltaFilter Python tutorial (#277)

* DeltaFilter(C++): Add DeltaFilter class. Add tests (#273) (#273)

* Removed dead code

* Improvements and more test coverage

* Use new ROSIDL aggregate CMake target

* Tutorials minor fixers: Replace the TODOs with the actual links to
  other tutorials as required. Rename Approximate-Tyme tutorial to
  Approximate-Time (#266)

* Tutorials: Add LatestTime synchronization policy tutorial (#266)

* Tutorials: Approximate-Synchronizer: Label CMake code blocks with
  the right language markings

* Tutorials: Add C++ tutorial for Approximate Epsilon Time Sync policy

* DeltaFilter(Python): Add DeltaFilter for Python. Add tests. Add
  docstring to filters and comparison handlers (#252)

* remove setup.py (#257)

* (#246, #186) Subscriber(Python): Add callback_group,
  event_callbacks, qos_overriding_options, raw and
  content_filter_options arguments to __init__. (#251)

* Add kwargs passing from Subscriber to node.create_subscription
  (#247) Fixes callers that use callback_group

* Get topic name from base class to propagate remaps (#68)

* #130 add simple filter tutorial for cpp (#239)

* #200 fix inconsistensy between cpp and python exact time
  synchronizer impl (#238)

* Add simple filter tutorials (#226)

* Update subscription callback signatures (#222)

* Add chain tutorial python (#219)

* Change function signature for Python Subscriber class (#220)

* Add Python implementation for a Chain filter (#213)

* Fix comparison of different time sources in C++ TimeSequencer (#202)

* Some fixes to documentation (#208)

* Create a Chain class tutorial for C++ (#203)

* get rid of deprecated rclcpp::spin_some(). (#201)

* Add 'Cache (C++)' tutorial (#196)

* cache.hpp: Add allow_headerless (#195)

* Simplify method call (#194)

* Fix cache tutorial: added tab extension (#190)

* Add tutorial for Cache filter for Python (#185)

* fix cmake deprecation (#182)

* update documentation (#180)

* Removed missing pragma (#179)

* Removed Subscriber deprecation (#177)

* Removed deprecated headers (#176)

* Use warning instead of warn (#178)

* Docs - Remove C++ implementation limit of 9 channels (#174)

* Contributors: Alejandro Hernandez Cordero, Alejandro Hernández
  Cordero, Alex Spitzer, Emerson Knapp, Erwin L., EsipovPA, Johannes
  Böhm, Michael Carlstrom, Patrick Roncagliolo, Pavel Esipov, Samuel
  Foo Enze, Tomoya Fujita, mergify[bot], mini-1235, mosfet80

mimick_vendor
=============

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#40)

* Contributors: Chris Lalancette

nav_msgs
========

* Adding the Trajectory and trajectoryPoint messages (#296)

* Fix CMAKE deprecation (#288)

* Contributors: Steve Macenski, mosfet80

osrf_testing_tools_cpp
======================

* fix cmake min version (#96)

* fix cmake deprecation (#94)

* Contributors: mosfet80

pendulum_control
================

* Use new ROSIDL aggregate CMake target (#781)

* Update subscription callback signatures (#754)

* get rid of deprecated rclcpp::spin_some(). (#734)

* Use EnableRmwIsolation in launch tests (#724)

* Uniform CMAKE min VERSION (#714)

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery
  (#711)

* Use target_link_libraries instead of ament_target_dependencies
  (#707)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K
  Logan, Shane Loretz, Tomoya Fujita, mini-1235, mosfet80

pendulum_msgs
=============

* Uniform CMAKE min VERSION (#714)

* Contributors: mosfet80

performance_test_fixture
========================

* fix cmake deprecation (#31)

* Remove CODEOWNERS and mirror-rolling-to-main workflow. (#28)

* Contributors: Chris Lalancette, mosfet80

pluginlib
=========

* Fix some minor issues (#292)

* Add support for passing arguments to constructors (#291)

* Export includes (#290)

* Updated deprecated ament_index_cpp API (#289)

* refactor: replace regex with find_last_of to split plugin name
  (#271)

* Removed tinyxml2_vendor dependency (#274)

* Add ros2plugin (#165)

* Contributors: Alejandro Hernández Cordero, Jeremie Deray, ipa-fez,
  pum1k

point_cloud_transport
=====================

* Fix exit crash on aarch64 by using leaky singleton for global loader
  (#157)

* Include message type (#152)

* Use new aggregate rosidl target instead of _TARGETS (#153) Co-
  authored-by: Alexis Tsogias <a.tsogias@cellumation.com>

* Improvements (#150)

* Expose original ROS Publishers and Subscription (#146) (#148)

* Fix duplicate component registration for Republisher (#142)

* Removed outdated comment (#138)

* Use standard unsigned int in place of uint for Windows compatibility
  (#134)

* Update subscriber filter (#126)

* Simplify NodeInterface API mehotd call (#129)

* Fixed QOS override tests (#128)

* Deprecated rmw_qos_profile_t (#125)

* Feat/Add LifecycleNode Support (#109)

* Add "rclcpp::shutdown" (#110)

* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, ElSayed
  ElSheikh, Michael Carroll, Silvio Traversaro, Yuyuan Yuan,
  mergify[bot], mini-1235

point_cloud_transport_py
========================

* Use new aggregate rosidl target instead of _TARGETS (#153)

* Python improvements (#151)

* Use pybind11 from deb or pixi (#131)

* Simplify NodeInterface API mehotd call (#129)

* Feat/Add LifecycleNode Support (#109)

* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, ElSayed
  ElSheikh

python_qt_binding
=================

* Pick Qt version at build time, not install time (#161)

* Re-add exec depend on python3 qt bindings rosdep key (#160)

* Remove qt6-base-dev from package.xml (#159)

* Depend on python3-dev (#158)

* Use sip-build and python3_add_library for Qt5/Qt6 (#157)

* fix setuptools deprecation (#151)

* fix cmake deprecation (#150)

* Remove the mirror-rolling-to-main workflow (#145)

* Remove CODEOWNERS (#144)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane
  Loretz, mosfet80

qt_dotgraph
===========

* More qt6 fixes (#334) (#335) (cherry picked from commit
  62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro
  Hernández Cordero <ahcorde@gmail.com>

* Support qt6 (#293)

* Ignore case when asserting snippet presence in tests (#314)

* Fix setupTools deprecations (#308)

* Contributors: Alejandro Hernández Cordero, Scott K Logan,
  mergify[bot], mosfet80

qt_gui
======

* More qt6 fixes (#334) (#335) (cherry picked from commit
  62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro
  Hernández Cordero <ahcorde@gmail.com>

* Support qt6 (#293)

* fix(qt_gui): __builtin__ -> builtins (#315)

* Fix cmake deprecations (#307)

* Contributors: Alejandro Hernández Cordero, Matthijs van der Burgh,
  mergify[bot], mosfet80

qt_gui_app
==========

* Fix cmake deprecations (#307)

* Contributors: mosfet80

qt_gui_core
===========

* Update qt_gui_core to package.xml version 2. (#319)

* Fix cmake deprecations (#307)

* Contributors: Chris Lalancette, mosfet80

qt_gui_cpp
==========

* More qt6 fixes (#334) (#335) (cherry picked from commit
  62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro
  Hernández Cordero <ahcorde@gmail.com>

* find_package(Qt...) in downstream packages (#332)

* Export qt dependencies in package.xml (#331)

* Use qt-base-dev / libqtwidgets (#330)

* Support qt6 (#293)

* Use new aggregate rosidl target instead of _TARGETS (#325)

* remove unsued setup.py (#323)

* Removed tinyxml2_vendor dependency (#309)

* Fix cmake deprecations (#307)

* Removed deprecated headers (#305)

* Use target_link_libraries instead of ament_target_dependencies
  (#302)

* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Michael
  Carlstrom, Shane Loretz, mergify[bot], mosfet80

qt_gui_py_common
================

* More qt6 fixes (#334) (#335)

* Support qt6 (#293)

* remove unsued setup.py (#323)

* Fix cmake deprecations (#307)

* Contributors: Alejandro Hernández Cordero, Michael Carlstrom,
  mergify[bot], mosfet80

quality_of_service_demo_cpp
===========================

* Use new ROSIDL aggregate CMake target (#781)

* Switching to example_interfaces (#674)

* Uniform CMAKE min VERSION (#714) demo_nodes_cpp/CMakeLists.txt
  require cmake min version 3.12 other modules cmake 3.5. It is
  proposed to standardize with version 3.12. This also fixes cmake
  <3.10 deprecation warnings

* Contributors: Emerson Knapp, Lucas Wendland, mosfet80

quality_of_service_demo_py
==========================

* Switching to example_interfaces (#674)

* fix setuptools deprecations (#731)

* Contributors: Lucas Wendland, mosfet80

rcl
===

* feat: Added check for double usage of entities in rcl_waitset
  (#1206)

* Preserve "rmw_create_node" error state in "rcl_node_init" by using
  "RCL_EXPECT_ERROR_IS_SET" (#1313)

* Remove clang warnings (#1315)

* Add RCL_EXPECT_ERROR_IS_SET macro (#1312)

* Improved documentation of rcl_XYZ_set_on_new_XYZ_callback (#1289)

* Add rcl_subscription_options_set_acceptable_buffer_backends with
  proper lifetime management (#1308)

* Added tracepoint to rcl_take_loaned_message (#1300)

* Apply change from "Use new aggregate rosidl target instead of
  _TARGETS (#1302)" on some leftovers (#1309)

* Remove the check for content filter support at the RCL layer (#1304)

* Use new aggregate rosidl target instead of _TARGETS (#1302)

* Add API for client libraries to set action server goal expiration
  callbacks (#1295)

* Fujitatomoya/improve rcl test graph (#1296)

* Add content filtering support check for subscriptions (#1293)

* rcl_logging_implementation package support. (#1276)

* Remove default from switch with enum, so that compiler warns.
  (#1278)

* Add clients servers info (#1161)

* Fix REP url locations (#1271)

* rcl_logging_allocator_initialize() support. (#1049)

* Fix typos: occurrs->occurs, successfull->successful (#1259)

* Refer to 'the middleware' and not 'the DDS implementation' in doc
  (#1260)

* Switch to isolated testing via rmw_test_fixture (#1251)

* Fix Cmake deprecation (#1249)

* Assert HistoryQoS in test_info_by_topic (#1242)

* Add a test for the subscription option 'ignore_local_publications'
  (#1239)

* remove unnecessary test_with_localhost_only. (#1238)

* Address memory leaks in rcl test_timer_init_state (#1236)

* Removed unused nondefault_qos_profile (#1233)

* Removed unused functions (#1230)

* remove rcl_qos_profile_rosout_default. (#1225)

* remove rmw_connext from test. (#1226)

* Fix a dangling pointer discovered by a fresh Clang (#1222)

* Contributors: Akihiko Komada, Alejandro Hernández Cordero, Alexander
  Kornienko, Alexis Tsogias, Barry Xu, CY Chen, Christophe Bedard,
  Emerson Knapp, Janosch Machowinski, Lee, Mario Domínguez López,
  Michael Orlov, Minju, Oren Bell PhD, Rushhaank Sahay, Sai Kishor
  Kothakota, Shane Loretz, Skyler Medeiros, Tim Clephas, Tomoya
  Fujita, mosfet80, yadunund

rcl_action
==========

* fix(rcl_action): use RMW isolation for cross-node tests (#1311)

* Add 2 interfaces for configuring action client feedback subscription
  contents filter (#1287)

* Apply change from "Use new aggregate rosidl target instead of
  _TARGETS (#1302)" on some leftovers (#1309)

* simplify error logging for timer cancellation (#1307)

* fix: Prevent short time endless loop in expire_timer (#1303)

* Add API for client libraries to set action server goal expiration
  callbacks (#1295)

* support rcl_action_count_clients and rcl_action_count_servers.
  (#1294)

* Fix REP url locations (#1271)

* add rcl_action_goal_handle_is_abortable(). (#1257)

* Fix Cmake deprecation (#1249)

* Contributors: Alexis Tsogias, Barry Xu, Janosch Machowinski, Skyler
  Medeiros, Tim Clephas, Tomoya Fujita, William Woodall, Yuyuan Yuan,
  mosfet80

rcl_interfaces
==============

* Fix cmake deprecation (#180)

* Contributors: mosfet80

rcl_lifecycle
=============

* Apply change from "Use new aggregate rosidl target instead of
  _TARGETS (#1302)" on some leftovers (#1309)

* Populate Transitions in Transition Events (continuation) (#1269)

* Fix REP url locations (#1271)

* Fix Cmake deprecation (#1249)

* introduce rcl_lifecycle_get_transition_label_by_id(). (#1229)

* Contributors: Alexis Tsogias, Jasper van Brakel, Tim Clephas, Tomoya
  Fujita, mosfet80

rcl_logging_implementation
==========================

* update rcl_logging_implementation architecture diagram. (#137)

* rcl logging implementation (#135) * 1st draft bring-up for
  rcl_logging_implementation package. * add
  test_logging_implementation to check dynamic loading. * address
  Copilot review comments. * fix: correct visibility macro for DLL
  export in CMakeLists.txt * add visibility control with
  RCL_LOGGING_IMPLEMENTATION_DEFAULT_VISIBILITY. * load the all
  symbols at the initialization. * Use goto pattern to eliminate the
  cleanup duplication. * Add basic design doc of
  rmw_logging_implementation. * use RCPPUTILS_SCOPE_EXIT instead of
  goto statement. * logging visibility macro was incorrect. * logging
  symbols stay until the peocess actually exits. --------- Co-
  authored-by: Barry Xu <barry.xu@sony.com>

* Contributors: Tomoya Fujita

rcl_logging_interface
=====================

* Fix cmake deprecation (#133)

* Contributors: mosfet80

rcl_logging_noop
================

* Fix cmake deprecation (#133)

* Cleanup rcl_logging_noop dependencies. (#132) It shouldn't
  build_export_depend anything (as nothing downstream should link
  against it), and all of its dependencies can be private.

* Contributors: Chris Lalancette, mosfet80

rcl_logging_spdlog
==================

* feat: add env variable to configure flushing interval (#139)

* Fix cmake deprecation (#133)

* Cleanup overwritten warning messages on error. (#128)

* Contributors: Achille Verheye, Chris Lalancette, mosfet80

rcl_yaml_param_parser
=====================

* Remove clang warnings (#1315)

* fix (#1310)

* Use the POSIX locale to parse YAML double (#1292)

* rcl_yaml_node_struct_print print loop interation fix. (#1290)

* rcl_yaml_param_parser: add support for binary tag to load byte
  arrays parameters (#1256)

* Validate name input in add_name_to_ns function (#1281)

* parse_key() should use yaml_map_lvl_t instead of uint_32. (#1279)

* Remove default from switch with enum, so that compiler warns.
  (#1278)

* Add yaml tags support (#1275) Co-authored-by: Lei Liu
  <Lei.Liu.AP@sony.com>

* Fix REP url locations (#1271)

* Fix param file parsing failure with wildcards due to ordering
  (#1253)

* Fix Cmake deprecation (#1249)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Hugal31,
  Michael Carlstrom, Romain Reignier, Tim Clephas, Tomoya Fujita,
  mosfet80

rclcpp
======

* Include EventsCBGExecutor (#3137)

* Fix topic statistics for IPC subscriptions (#3130)

* fix: Fixed MSVC compile errors (#3135)

* feat: Added callback group events executor (#3097)

* Fix wrong dependency (#3133)

* feat: Switch to c++20 and remove resulting compile warnings (#3124)

* fix: Compile fix for MSVC 2022 (#3131)

* Remove warnings on tests (#3125)

* feat: Add per-node log level support via NodeOptions (#3092)

* Improve error message when parameter value is missing (#3093)

* Fix incorrect internal clear inside "RingBufferImplementation"
  (#3116)

* Add acceptable_buffer_backends field in SubscriptionOptionsBase
  (#3098)

* Remove comment about removed StaticSingleThreadedExecutor (#3121)

* Added tracepoint (#3103)

* Add ConstRefCallback in take_shared_method (#3066)

* Replace mispelled "${rcl_interfaces_TARGES}" by
  rcl_interfaces::rcl_interfaces (#3112)

* Use new ROSIDL aggregate CMake target (#3105)

* remove duplicate test cases in
  TestAnySubscriptionCallback::is_serialized_message_callback (#3104)

* keep the event alive throught the assertion, preveiting the race.
  (#3099)

* Add support check for content filter feature in subscription (#3089)

* Expose ServiceType in Service public API (#3088)

* perf: Optimized out shared_ptr copies (#3079)

* avoid stale parameter events in content filter tests. (#3085)

* improve lookup time for matches_any_publishers() (#3084)

* Add tests isolation (#3081)

* Revert "improve lookup time for matches_any_publishers(). (#3068)"
  (#3077)

* improve lookup time for matches_any_publishers(). (#3068)

* fix: Use default rcl allocator if allocator is std::allocator
  (#3058)

* fix: Various data races in test cases (#3057)

* fix: Fix data race in CallbackGroup::size() (#3056)

* remove default: so that compiler can detect the missing case.
  (#3048)

* use weak_ptr for rcl entities in the memory strategy. (#2988)

* remove test_static_executor_entities_collector.cpp (#3041)

* include the 1st spin that might throw the exception. (#3042)

* print warning message on owner node if the parameter operation
  fails. (#3037)

* fix context in wait for message wait set (#3030)

* Revert "construct wait set with passed in context (#3021)" (#3028)

* construct wait set with passed in context (#3021)

* Improve the robustness of the TopicEndpointInfo constructor (#3013)

* Deprecate the shared_ptr<MessageT> subscription callback signatures
  (#2975)

* Updated deprecated ament_index_cpp API (#3011)

* Unified Node Interfaces: Add const version of get_node_x_interface()
  (#3006)

* Parameter Descriptor Simplification (#2179)

* ParameterEventHandler support ContentFiltering (#2971)

* update policy_name_from_kind && test_qos (#2156)

* Add ability to disable and enable subscription's callbacks (#2985)

* Switch to isolated testing via rmw_test_fixture (#2929)

* remove I/O from signal handler. (#2986)

* correct test function descriptions (#2970)

* add : get clients, servers info (#2569)
