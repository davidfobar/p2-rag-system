# Iron Irwini Changelog (part 2 of 5)

* Update the demos to C++17. (#594)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Chris Lalancette, Gary Bey, Yadunund

kdl_parser
==========

* Switch some tests to use unique pointers instead of raw pointers.
  (#74)

* log link children as DEBUG instead of INFO (#71)

* Enable the kdl_parser tests in ROS 2 (#68)

* Add in a LICENSE file and fix up copyright headers (#66)

* Use orocos_kdl_vendor and orocos-kdl target (#64)

* Use the rcutils logger instead of printf (#65)

* Contributors: Chris Lalancette, Joseph Schornak, Scott K Logan,
  yuraSomatic

keyboard_handler
================

* Force exit from main thread on signal handling in "keyboard_handler"
  (#23)

* Contributors: Michael Orlov

laser_geometry
==============

* Update laser_geometry to C++17. (#90)

* Update Maintainers (#88)

* Mirror rolling to ros2

* Contributors: Audrow Nash, Chris Lalancette

launch
======

* Document LaunchService.{run,run_async}() return value (#702)

* [rosdoc2] Fix document generation on buildfarm (#701)

* Enable document generation using rosdoc2 for ament_python pkgs
  (#697)

* Remove the import of Literal from entity.py. (#694)

* Fix flake8 errors. (#695)

* add symlink to latest log directory (#686)

* Improve type checking (#679)

* Fixed typos (#692)

* Pass modules to PythonExpression (#655)

* Allow ReadyToTest() usage in event handler (#665)

* Expose emulate_tty to xml and yaml launch (#669)

* Expose sigterm_timeout and sigkill_timeout to xml frontend (#667)

* [rolling] Update maintainers - 2022-11-07 (#671)

* Expect deprecation warnings in tests (#657)

* Fix the restoring of os.environ to maintain type. (#656)

* Implement Any, All, Equals, and NotEquals substitutions (#649)

* add LaunchLogDir substitution, replacing log_dir frontend only
  substitution (#652)

* Add special cases to coerce "1" and "0" to bool when using bool
  coercion only (#651)

* Update launch/test/launch/test_execute_local.py

* Added unit test ensuring that output dictionary works with
  ExecuteLocal

* Addresses issue #588, allowing dict for 'output'

* Remove unused variables. (#612)

* Expose shutdown action to xml frontend (#611)

* Contributors: Aditya Pande, Alejandro Hernández Cordero, Audrow
  Nash, Blake Anderson, Chris Lalancette, Christophe Bedard, Hervé
  Audren, Jacob Perron, Matthew Elwin, Michael Jeronimo, Nikolai
  Morin, Welte, William Woodall, Yadu, methylDragon

launch_pytest
=============

* Fixed typos (#692)

* Drop unused data_files entry for example_processes (#680)

* Spelling correction

* [rolling] Update maintainers - 2022-11-07 (#671)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Geoffrey
  Biggs, Scott K Logan

launch_ros
==========

* Use SomeEntitiesType for type checking. (#358)

* Fix normalize_parameters_dict for multiple nodes in the same
  namespace (#347)

* Implement None check for ComposableNodeContainer (#341)

* Add LifecyleTransition action (#317)

* Improve evaluate_paramenter_dict exceptions error message (#320)

* Ensure load_composable_nodes respects condition (#339)

* fix: return text value to avoid exception (#338)

* [rolling] Update maintainers - 2022-11-07 (#331)

* RosTimer -> ROSTimer and PushRosNamespace -> PushROSNamespace, to
  follow PEP8 (#326)

* add SetROSLogDir action (#325)

* Support default values in parameter substitution (#313)

* Run condition for composable nodes (#311)

* Contributors: Aditya Pande, Alexey Merzlyakov, Audrow Nash, Chris
  Lalancette, Christoph Hellmann Santos, Daisuke Nishimatsu, Felipe
  Gomes de Melo, Kenji Miyake, William Woodall, methylDragon

launch_testing
==============

* Improve type checking (#679)

* Fixed typos (#692)

* Allow ReadyToTest() usage in event handler (#665)

* Inherit markers from generate_test_description (#670)

* [rolling] Update maintainers - 2022-11-07 (#671)

* Fix Typo (#641)

* ReadyToTest action timeout using decorator (#625)

* Switch to using a comprehension for process_names. (#614)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris
  Lalancette, Deepanshu Bansal, Hervé Audren, Kenji Brameld, Nikolai
  Morin, Scott K Logan

launch_testing_ament_cmake
==========================

* [rolling] Update maintainers - 2022-11-07 (#671)

* Contributors: Audrow Nash

launch_testing_examples
=======================

* Enable document generation using rosdoc2 for ament_python pkgs
  (#357)

* increase the timeout for window platform to avoid flaky test (#355)

* [rolling] Update maintainers - 2022-11-07 (#352)

* Increase the WaitForNode timeout. (#350)

* Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Yadu

launch_testing_ros
==================

* Increase the timeouts in wait_for_topic_launch_test. (#360)

* Enable document generation using rosdoc2 (#359)

* exit() methods should not reraise the passed-in exception (#357)

* Inherit markers from generate_test_description (#330)

* [rolling] Update maintainers - 2022-11-07 (#331)

* Fix long wait during shutdown in WaitForTopics (#314)

* Contributors: Audrow Nash, Chris Lalancette, Giorgio Pintaudi,
  Keng12, Scott K Logan, Yadu

launch_xml
==========

* Fixed typos (#692)

* Expose emulate_tty to xml and yaml launch (#669)

* Expose sigterm_timeout and sigkill_timeout to xml frontend (#667)

* [rolling] Update maintainers - 2022-11-07 (#671)

* Contributors: Aditya Pande, Alejandro Hernández Cordero, Audrow Nash

launch_yaml
===========

* Expose emulate_tty to xml and yaml launch (#669)

* Expose sigterm_timeout and sigkill_timeout to xml frontend (#667)

* [rolling] Update maintainers - 2022-11-07 (#671)

* Contributors: Aditya Pande, Audrow Nash

libcurl_vendor
==============

* merge libcurl_vendor build instructions (#81)

* Sets CMP0135 policy behavior to NEW (#79)

* Fixes policy CMP0135 warning for CMake >= 3.24

* Contributors: Cristóbal Arroyo, Crola1702, schrodinbug

libstatistics_collector
=======================

* Bump hmarr/auto-approve-action from 3.2.0 to 3.2.1

* Mark benchmark _ as unused. (#158)

* Bump hmarr/auto-approve-action from 3.1.0 to 3.2.0

* Bump ros-tooling/action-ros-ci from 0.2 to 0.3

* Bump pascalgn/automerge-action from 0.15.5 to 0.15.6

* Update libstatistics_collector to C++17. (#154)

* Remove unnecessary build dependency on std_msgs. (#145)

* Bump pascalgn/automerge-action from 0.15.2 to 0.15.3

* Cleanup the CI jobs on this repository. (#146)

* Check if message has a "header" field with a stamp subfield of type
  builtin_interfaces::msg::Time (#54)

* Mirror rolling to master

* Contributors: Audrow Nash, Chris Lalancette, Scott Mende,
  dependabot[bot]

libyaml_vendor
==============

* Fix system package dependency (#54)

* Update libyaml_vendor to C++17. (#55)

* [rolling] Update maintainers - 2022-11-07 (#53)

* Remove a warning message. (#51)

* check if libyaml is already present before building it (take 2)
  (#45)

* Mirror rolling to master

* Support WindowsStore builds for ROS2 (#50) * libyaml for uwp

* Contributors: Audrow Nash, Chris Lalancette, Lou Amadio, Scott K
  Logan, Silvio Traversaro

lifecycle
=========

* update launch file name format to match documentation (#588)

* Update the demos to C++17. (#594)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Chris Lalancette, Patrick Wspanialy

lifecycle_msgs
==============

* Update common_interfaces to C++17. (#215) (#151)

* [rolling] Update maintainers - 2022-11-07 (#150)

* lifecycle_msgs: remove non-ASCII chars from field comments (#147)

* Contributors: Audrow Nash, Chris Lalancette, G.A. vd. Hoorn

lifecycle_py
============

* Enable document generation using rosdoc2 (#606)

* update launch file name format to match documentation (#588)

* Cleanup lifecycle_py to conform to ROS 2 standards. (#604)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Install the launch file for lifecycle_py. (#586)

* Contributors: Audrow Nash, Chris Lalancette, Patrick Wspanialy, Yadu

logging_demo
============

* Update the demos to C++17. (#594)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Change dependency from 'rosidl_cmake' to 'rosidl_default_generators'
  (#578)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

map_msgs
========

* Update maintainers

* Contributors: Audrow Nash, Steve Macenski

mcap_vendor
===========

* mcap_vendor: add readme with versioning procedure (#1230)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* mcap_vendor: only install public headers (#1207)

* Fixes policy CMP0135 warning for CMake >= 3.24 for mcap_vendor
  (#1208)

* mcap_vendor: download MCAP source via tarball (#1204)

* rosbag2_cpp: test more than one storage plugin (#1196)

* rosbag2_storage_mcap: merge into rosbag2 repo (#1163)

* Fix Windows build (#73) Update mcap version to newest windows-
  compatible release. Add visibility macros for tests. Add clang-
  format preprocessor indentation for visibility_control to be
  readable.

* mcap_vendor: update to v0.6.0 (#69)

* Cleanup in "mcap_vendor" package (#62)

* Switch to using the vendored zstd library. (#59)

* Support timestamp-ordered playback (#50)

* Support regex topic filtering

* Add all lz4 sources to fix undefined symbols at runtime (#46)

* Upgrade mcap to fix LZ4 error and segfault (#42) Incorporates fixes
  from https://github.com/foxglove/mcap/pull/478 and
  https://github.com/foxglove/mcap/pull/482

* Add missing buildtool_depend on git (#37) This vendor package uses
  git to fetch sources for other packages. It should declare a
  dependency on that build tool. This should address the current cause
  of RPM build failures for RHEL: https://build.ros2.org/view/Rbin_rh
  el_el864/job/Rbin_rhel_el864__mcap_vendor__rhel_8_x86_64__binary/

* Test Foxy & Galactic in CI, fix missing test_depends in
  mcap_vendor/package.xml (#33)

* fix: minor issues (#31) * remove unnecessary block * use
  target_link_libraries instead of ament_target_dependencies * remove
  ros environment * add prefix to compile definition

* Update email address for Foxglove maintainers (#32)

* Added mcap_vendor package. Updated CMakeLists.txt to fetch
  dependencies with FetchContent rather than Conan.

* Contributors: Chris Lalancette, Cristóbal Arroyo, Daisuke
  Nishimatsu, Emerson Knapp, Jacob Bandes-Storch, James Smith, Michael
  Orlov, Scott K Logan, james-rms

message_filters
===============

* Update message_filters to C++17. (#88)

* Fix cache.h std::placeholder namespace (#87)

* [rolling] Update maintainers - 2022-11-07 (#85)

* Add a simpler aproximate time sync policy: ApproximateEpsilonTime
  (#84)

* Add latest time zero-order-hold sync policy (#73)

* Fix python examples and add a new example in documentation (#79)

* Mirror rolling to master

* Adding fix to subscribe() call with raw node pointer and subscriber
  options (#76)

* Corrected function arguments in example description (#35)

* Changed invocation to "add" to conform template syntax (#1388)

* fix sphinx warning (#1371)

* change invocation to "add" to conform template syntax (#1388)

* fix sphinx warning (#1371)

* Contributors: Audrow Nash, Carlos Andrés Álvarez Restrepo, Chris
  Lalancette, Haoru Xue, Ivan Santiago Paunovic, Martin Ganeff, Steve
  Macenski, andermi

mimick_vendor
=============

* [rolling] Update maintainers - 2022-11-07 (#29)

* Mirror rolling to master

* Contributors: Audrow Nash

nav_msgs
========

* Update common_interfaces to C++17. (#215)

* [rolling] Update maintainers - 2022-11-07 (#210)

* Contributors: Audrow Nash, Chris Lalancette

orocos_kdl_vendor
=================

* Make sure to quote orocos variables when setting targets. (#12)

* Ensure orocos-kdl is available as a target (#10)

* Ensure orocos-kdl target references Eigen (#6)

* Contributors: Chris Lalancette, Scott K Logan

osrf_pycommon
=============

* [master] Update maintainers - 2022-11-07 (#89)

* Declare test dependencies in [test] extra (#86)

* Contributors: Audrow Nash, Scott K Logan

osrf_testing_tools_cpp
======================

* Fix mpark/variant conditional for MSVC (#77)

* Changing C++ Compile Version (#76)

* Update maintainers (#74)

* Sets CMP0135 policy behavior to NEW (#73)

* Fixes policy CMP0135 warning in CMake 3.24 (#71)

* Add cstring include. (#70)

* Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo, Lucas
  Wendland, Scott K Logan

pendulum_control
================

* Update the demos to C++17. (#594)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Chris Lalancette

pendulum_msgs
=============

* Change all ROS2 -> ROS 2. (#610)

* A couple more upgrades to C++17. (#609)

* Added README.md for pendulum_msgs. (#577)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Chris Lalancette, Gary Bey

performance_test_fixture
========================

* Resolve use-after-free compiler warnings (#24)

* Update performance_test_fixture to C++17. (#21)

* [rolling] Update maintainers - 2022-11-07 (#20)

* Mirror rolling to main

* Add "cstring" to the list of includes (#19)

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

pluginlib
=========

* Update maintainers

* Contributors: Audrow Nash

pybind11_vendor
===============

* Add a modified patch from upstream to support Python 3.11 (#22)

* Add missing buildtool dependency on git (#19)

* Update maintainers (#17)

* Force pybind11 to find Python 3. (#15)

* Mirror rolling to master

* Update maintainers (#14)

* Update to pybind11 2.9.1.

* Rename patch file for history continuity.

* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Steven!
  Ragnarök, methylDragon

python_cmake_module
===================

* [rolling] Update maintainers - 2022-11-07 (#13)

* Mirror rolling to master

* Contributors: Audrow Nash

python_orocos_kdl_vendor
========================

* Fixes policy CMP0135 warning for CMake >= 3.24 (#16)

* Workaround pybind11 CMake error (#9)

* Contributors: Cristóbal Arroyo, Jacob Perron

python_qt_binding
=================

* Fix to allow ninja to use make for generators (#123)

* Fix flake8 linter regression (#125)

* Remove pyqt from default binding order for macOS (#118)

* Demote missing SIP message from WARNING to STATUS (#122)

* [rolling] Update maintainers - 2022-11-07 (#120)

* Contributors: Audrow Nash, Christoph Hellmann Santos, Cristóbal
  Arroyo, Michael Carroll, Rhys Mainwaring, Scott K Logan

qt_dotgraph
===========

* Add in LICENSE file

* Cast drawLine input arguments to int (#264) (#265)

* Contributors: Chris Lalancette, mergify[bot]

qt_gui
======

* Add in LICENSE file

* Fix flake8 errors introduced by the previous commit. (#262)

* Enable basic help information if no plugins are running (#261)

* Contributors: Chris Lalancette, Michael Jeronimo

qt_gui_app
==========

* Add in LICENSE file

* Contributors: Chris Lalancette

qt_gui_core
===========

* Add in LICENSE file

* Contributors: Chris Lalancette

qt_gui_cpp
==========

* Fix ClassLoader warning by unloading plugin providers. (#275)

* Chen Lihui

* fix shiboken error (#267)

* Conditionally run import tests when generators are built (#269)

* Add in LICENSE file

* Contributors: Chris Lalancette, Christoph Hellmann Santos, Michael
  Carroll, Rhys Mainwaring, Scott K Logan

qt_gui_py_common
================

* Add in LICENSE file

* Contributors: Chris Lalancette

quality_of_service_demo_cpp
===========================

* Update the demos to C++17. (#594)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Contributors: Audrow Nash, Chris Lalancette

quality_of_service_demo_py
==========================

* Use non-deprecated rclpy import. (#617)

* Change all ROS2 -> ROS 2. (#610)

* Enable document generation using rosdoc2 (#606)

* [rolling] Update maintainers - 2022-11-07 (#589)

* Exit with code 0 if ExternalShutdownException is raised (#581)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, Yadu

rcl
===

* Honor ROS_LOCALHOST_ONLY if enabled. (#1071)

* fix flaky test (#1063)

* Add enable_type_description_service node option - API only (#1060)

* Dynamic Subscription (BONUS: Allocators): rcl (#1057)

* Runtime Interface Reflection: rcl (#1025)

* [rcl] Improve handling of dynamic discovery (#1023)

* Use get_type_hash_func for typesupports (#1055)

* publish for rosout topic multiple times to avoid flaky test (#1054)

* Switch to target_link_libraries in rcl. (#1051)

* Calculate type hash from TypeDescription (rep2011) (#1027)

* Implement matched event (#1033)

* use user-defined allocator to configure logging. (#1047)

* user defined allocator should be used for rosout publisher. (#1044)

* Add in inconsistent_topic implementation. (#1024)

* doc update, ROS message accessibility depends on RMW implementation.
  (#1043)

* Fix some warnings from clang. (#1042)

* avoid unnecessary copy for rcutils_char_array_vsprintf. (#1035)

* Service introspection (#997)

* Cache disable flag to avoid reading environmental variable. (#1029)

* use parent logger (#921)

* Add timer on reset callback (#995)

* Update rcl to C++17. (#1031)

* Make sure to check the return value of rcl_clock_init in tests.
  (#1030)

* Implement rcl_clock_time_started (#1021)

* Make sure to reset errors more places in the tests. (#1020) This
  makes it so we don't get as many warnings when the tests are
  running.

* [rolling] Update maintainers - 2022-11-07 (#1017)

* Small cleanups to rcl (#1013)

* use int64_t for period. (#1010)

* fixed rcl_wait return error when timer cancelled (#1003)

* remove duplicate packages in find_package and reorder (#994)

* Fix buffer overflow in argument parsing caused by lexer returning
  length beyond length of string (#979)

* Fix leak in test_subscription_content_filter_options.cpp (#978)

* Contributors: Audrow Nash, Barry Xu, Brian, Chen Lihui, Chris
  Lalancette, Emerson Knapp, Geoffrey Biggs, Shane Loretz, Tomoya
  Fujita, mauropasse, methylDragon, 정찬희

rcl_action
==========

* doc update, ROS message accessibility depends on RMW implementation.
  (#1043)

* Update rcl to C++17. (#1031)

* Reduce result_timeout to 10 seconds. (#1012)

* [rolling] Update maintainers - 2022-11-07 (#1017)

* Contributors: Audrow Nash, Chris Lalancette, Tomoya Fujita

rcl_interfaces
==============

* Add interfaces for logging service. (#154)

* Update common_interfaces to C++17. (#215) (#151)

* [rolling] Update maintainers - 2022-11-07 (#150)

* Contributors: Audrow Nash, Chris Lalancette, Lei Liu

rcl_lifecycle
=============

* Update rcl to C++17. (#1031)

* [rolling] Update maintainers - 2022-11-07 (#1017)

* Contributors: Audrow Nash, Chris Lalancette

rcl_logging_interface
=====================

* Update rcl_logging to C++17. (#98)

* Updated maintainers - 2022-11-07 (#96)

* Contributors: Audrow Nash, Chris Lalancette

rcl_logging_noop
================

* Update rcl_logging to C++17. (#98)

* Updated maintainers - 2022-11-07 (#96)

* Contributors: Audrow Nash, Chris Lalancette

rcl_logging_spdlog
==================

* Mark the benchmark _ as unused. (#99)

* Update rcl_logging to C++17. (#98)

* change flushing behavior for spdlog log files, and add env var to
  use old style (no explicit flushing) (#95) * now flushes every ERROR
  message and periodically every 5 seconds * can set
  "RCL_LOGGING_SPDLOG_EXPERIMENTAL_OLD_FLUSHING_BEHAVIOR=1" to get old
  behavior

* Updated maintainers - 2022-11-07 (#96)

* Disable cppcheck for rcl_logging_spdlog. (#93)

* ament_export_dependencies any package with targets we linked against
  (#89)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz, William
  Woodall

rcl_yaml_param_parser
=====================

* Fix some warnings from clang. (#1042)

* Cleanup the dependencies in rcl_yaml_param_parser. (#1014)

* Update rcl to C++17. (#1031)

* Support yaml string tag '!!str' (#999)

* [rolling] Update maintainers - 2022-11-07 (#1017)

* Contributors: Audrow Nash, Barry Xu, Chris Lalancette

rclcpp
======

* Fix delivered message kind (#2175) (#2178)

* Add support for logging service. (#2122)

* Picking ABI-incompatible executor changes (#2170)

* add events-executor and timers-manager in rclcpp (#2155)

* Create common structures for executors to use (#2143)

* Implement deliver message kind (#2168)

* applied tracepoints for ring_buffer (#2091)

* Dynamic Subscription (REP-2011 Subset): Stubs for rclcpp (#2165)

* Add type_hash to cpp TopicEndpointInfo (#2137)

* Trigger the intraprocess guard condition with data (#2164)

* Minor grammar fix (#2149)

* Fix unnecessary allocations in executor.cpp (#2135)

* add Logger::get_effective_level(). (#2141)

* Remove deprecated header (#2139)

* Implement matched event (#2105)

* use allocator via init_options argument. (#2129)

* Fixes to silence some clang warnings. (#2127)

* Documentation improvements on the executor (#2125)

* Avoid losing waitable handles while using MultiThreadedExecutor
  (#2109)

* Hook up the incompatible type event inside of rclcpp (#2069)

* Update all rclcpp packages to C++17. (#2121)

* Fix clang warning: bugprone-use-after-move (#2116)

* Fix memory leak in tracetools::get_symbol() (#2104)

* Service introspection (#1985)

* Allow publishing borrowed messages with intra-process enabled
  (#2108)

* to fix flaky test about TestTimeSource.callbacks (#2111)

* to create a sublogger while getting child of Logger (#1717)

* Fix documentation of Context class (#2107)

* fixes for rmw callbacks in qos_event class (#2102)

* Add support for timers on reset callback (#1979)

* Topic node guard condition in executor (#2074)

* Fix bug on the disorder of calling shutdown callback (#2097)

* Add default constructor to NodeInterfaces (#2094)

* Fix clock state cached time to be a copy, not a reference. (#2092)

* Fix -Wmaybe-uninitialized warning (#2081)

* Fix the keep_last warning when using system defaults. (#2082)

* Add in a fix for older compilers. (#2075)

* Implement Unified Node Interface (NodeInterfaces class) (#2041)

* Do not throw exception if trying to dequeue an empty intra-process
  buffer (#2061)

* Move event callback binding to PublisherBase and SubscriptionBase
  (#2066)

* Implement validity checks for rclcpp::Clock (#2040)

* Explicitly set callback type (#2059)

* Fix logging macros to build with msvc and cpp20 (#2063)

* Add clock type to node_options (#1982)

* Fix nullptr dereference in prune_requests_older_than (#2008)

* Remove templating on to_rcl_subscription_options (#2056)

* Fix SharedFuture from async_send_request never becoming valid
  (#2044)

* Add in a warning for a KeepLast depth of 0. (#2048)

* Mark rclcpp::Clock::now() as const (#2050)

* Fix a case that did not throw ParameterUninitializedException
  (#2036)

* Update maintainers (#2043)

* MultiThreadExecutor number of threads is at least 2+ in default.
  (#2032)

* Fix bug that a callback not reached (#1640)

* Set the minimum number of threads of the Multithreaded executor to 2
  (#2030)

* check thread whether joinable before join (#2019)

* Set cpplint test timeout to 3 minutes (#2022)

* Make sure to include-what-you-use in the node_interfaces. (#2018)

* Do not clear entities callbacks on destruction (#2002)

* fix mismatched issue if using zero_allocate (#1995)

* Make ParameterService and Sync/AsyncParameterClient accept
  rclcpp::QoS (#1978)

* support regex match for parameter client (#1992)

* operator+= and operator-= for Duration (#1988)

* Revert "Revert "Add a create_timer method to Node and
  "LifecycleNode" classes (#1975)" (#2009) (#2010)

* force compiler warning if callback handles not captured (#2000)

* Revert "Add a "create_timer" method to "Node" and "LifecycleNode"
  classes (#1975)" (#2009)

* Add a "create_timer" method to "Node" and "LifecycleNode" classes
  (#1975)

* [docs] add note about callback lifetime for {on,
  post}_set_parameter_callback (#1981)

* fix memory leak (#1994)

* Support pre-set and post-set parameter callbacks in addition to on-
  set-parameter-callback. (#1947)

* Make create_service accept rclcpp::QoS (#1969)

* Make create_client accept rclcpp::QoS (#1964)

* Fix the documentation for rclcpp::ok to be accurate. (#1965)

* use regex for wildcard matching (#1839)

* Revert "Introduce executors new spin_for method, replace
  spin_until_future_complete with spin_until_complete. (#1821)
  (#1874)" (#1956)

* Introduce executors new spin_for method, replace
  spin_until_future_complete with spin_until_complete. (#1821) (#1874)

* test adjustment for LoanedMessage. (#1951)

* fix virtual dispatch issues identified by clang-tidy (#1816)

* Remove unused on_parameters_set_callback_ (#1945)

* Fix subscription.is_serialized() for callbacks with message info
  (#1950)

* wait for subscriptions on another thread. (#1940)

* Fix documentation of "RCLCPP\_[INFO,WARN,...]" (#1943)

* Always trigger guard condition waitset (#1923)

* Add statistics for handle_loaned_message (#1927)

* Drop wrong template specialization (#1926)

* Update get_parameter_from_event to follow the function description
  (#1922)

* Add 'best available' QoS enum values and methods (#1920)

* use reinterpret_cast for function pointer conversion. (#1919)

* Contributors: Alberto Soragna, Alexander Hans, Alexis Paques, Andrew
  Symington, Audrow Nash, Barry Xu, Brian, Chen Lihui, Chris
  Lalancette, Christophe Bedard, Christopher Wecht, Cristóbal Arroyo,
  Daniel Reuter, Deepanshu Bansal, Emerson Knapp, Hubert Liberacki,
  Ivan Santiago Paunovic, Jacob Perron, Jeffery Hsu, Jochen
  Sprickerhof, Lei Liu, Mateusz Szczygielski, Michael Carroll, Miguel
  Company, Nikolai Morin, Shane Loretz, Silvio Traversaro, Tomoya
  Fujita, Tyler Weaver, William Woodall, Yadu, andrei, mauropasse,
  mergify[bot], methylDragon, schrodinbug, uupks, ymski

rclcpp_action
=============

* extract the result response before the callback is issued. (#2132)

* Update all rclcpp packages to C++17. (#2121)

* Fix the GoalUUID to_string representation (#1999)

* Explicitly set callback type (#2059)

* Update maintainers (#2043)

* Do not clear entities callbacks on destruction (#2002)

* Revert "Introduce executors new spin_for method, replace
  spin_until_future_complete with spin_until_complete. (#1821)
  (#1874)" (#1956)

* Introduce executors new spin_for method, replace
  spin_until_future_complete with spin_until_complete. (#1821) (#1874)

* Contributors: Audrow Nash, Chris Lalancette, Hubert Liberacki,
  Nathan Wiebe Neufeldt, Tomoya Fujita, William Woodall, mauropasse

rclcpp_components
=================

* Update all rclcpp packages to C++17. (#2121)

* Improve component_manager_isolated shutdown (#2085)

* Update maintainers (#2043)

* use unique ptr and remove unuseful container (#2013)

* Revert "Introduce executors new spin_for method, replace
  spin_until_future_complete with spin_until_complete. (#1821)
  (#1874)" (#1956)

* Introduce executors new spin_for method, replace
  spin_until_future_complete with spin_until_complete. (#1821) (#1874)

* Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Hubert
  Liberacki, Michael Carroll, William Woodall

rclcpp_lifecycle
================

* Add support for logging service. (#2122)

* Support publishing loaned messages in LifecyclePublisher (#2159)

* Fixes to silence some clang warnings. (#2127)

* Update all rclcpp packages to C++17. (#2121)

* Use the correct macro for LifecycleNode::get_fully_qualified_name
  (#2117)

* add get_fully_qualified_name to rclcpp_lifecycle (#2115)

* Implement Unified Node Interface (NodeInterfaces class) (#2041)

* Add clock type to node_options (#1982)

* Update maintainers (#2043)

* LifecycleNode on_configure doc fix. (#2034)

* Bugfix 20210810 get current state (#1756)

* Make lifecycle impl get_current_state() const. (#2031)

* Cleanup the lifecycle implementation (#2027)

* Cleanup the rclcpp_lifecycle dependencies. (#2021)

* Revert "Revert "Add a create_timer method to Node and
  "LifecycleNode" classes (#1975)" (#2009) (#2010)

* Revert "Add a "create_timer" method to "Node" and "LifecycleNode"
  classes (#1975)" (#2009)

* Add a "create_timer" method to "Node" and "LifecycleNode" classes
  (#1975)

* Support pre-set and post-set parameter callbacks in addition to on-
  set-parameter-callback. (#1947)

* Make create_service accept rclcpp::QoS (#1969)

* Make create_client accept rclcpp::QoS (#1964)

* Contributors: Andrew Symington, Audrow Nash, Chris Lalancette,
  Deepanshu Bansal, Ivan Santiago Paunovic, Jeffery Hsu, Lei Liu,
  Michael Babenko, Shane Loretz, Steve Macenski, Tomoya Fujita,
  methylDragon

rclpy
=====

* Fix type in Node init args (#1115) (#1122)

* Logging service support (#1102)

* Use custom sourcedir for conf.py (#1109)

* ServerGoalHandle should be destroyed before removing. (#1113)

* Fix unnecessary list comprehension flake8 (#1112)

* Stub type hash value line in TopicEndpointInfo string (#1110)

* Support documentation generation using rosdoc2 (#1103)

* Fix Time and Duration raising exception when compared to another
  type (#1007)

* Make rcl_interfaces a build and exec dependency. (#1100)

* Solving Atomic undefined on OSX with clang (#1096)

* Implement matched event (#1083)

* Update service.py documentation (#1094)

* Allow space or empty strings when using ros2 param set (#1093)

* Hook up the incompatible type event inside of rclpy (#1058)

* Switch to using module instead of module_ (#1090)

* Add in subscription.get_publisher_count() (#1089)
