# ROS 2 Lyrical Luth Complete Changelog (part 4 of 6)

* Harden ros2doctor system calls. (#1118)

* Add error handling when parsing package locally (#1108)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* [ros2doctor] Environment Report (#1045)

* Restore environment variables after launch tests (#1086)

* add warning notice for ros2 doctor --report. (#1079)

* [ros2doctor] Add Action Report (#1076)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Add Service report similar to topic report (#1059)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* Fix stringifying InterfaceFlags when the flags are empty. (#1026)

* Allow zenoh tests to run with multicast (#992)

* Skip QoS compatibility test on Zenoh (#985)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K
  Logan, Tomoya Fujita, mini-1235, mosfet80

ros2interface
=============

* Add fzf-based interactive selection to ros2cli commands (#1151)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* Contributors: Christophe Bedard, Michael Carlstrom, Tony Najjar,
  mosfet80

ros2launch
==========

* correct typos (#524)

* fix setuptools deprecations (#475)

* user control of log file base names, in ros2 launch (#461) Co-
  authored-by: Katherine Scott <katherineAScott@gmail.com>

* Contributors: Auguste Lalande, Tanishq Chaudhary, mosfet80

ros2lifecycle
=============

* Add timeout arguments to "ros2 service call", "ros2 action
  send_goal", "ros2 component", "ros2 lifecycle", and "ros2 param"
  (#1185)

* ros2interface output the contents for each node. (#1163)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* Restore environment variables after launch tests (#1086)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Relax the check from exact to partial match. (#1055)

* Export Typing information (#1041)

* Allow zenoh tests to run with multicast (#992)

* Contributors: Christophe Bedard, Michael Carlstrom, Michael Carroll,
  Scott K Logan, Tomoya Fujita, mosfet80

ros2lifecycle_test_fixtures
===========================

* fix cmake deprecation (#1082)

* Use target_link_libraries instead of ament_target_dependencies
  (#973)

* Contributors: Shane Loretz, mosfet80

ros2multicast
=============

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* Contributors: Christophe Bedard, Michael Carlstrom, mosfet80

ros2node
========

* Add fzf-based interactive selection to ros2cli commands (#1151)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* Restore environment variables after launch tests (#1086)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* Allow zenoh tests to run with multicast (#992)

* Contributors: Christophe Bedard, Michael Carlstrom, Michael Carroll,
  Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80

ros2param
=========

* Add timeout arguments to "ros2 service call", "ros2 action
  send_goal", "ros2 component", "ros2 lifecycle", and "ros2 param"
  (#1185)

* ros2 param set /node_name <param1 value1 param2 value2...> support.
  (#1204)

* ros2 param get /node_name <param1 param2 param3...> support. (#1203)

* Add per-node timeout option to ros2 param list (#1170)

* Fix Bash completion (#1182)

* Add fzf-based interactive selection to ros2cli commands (#1151)

* Support "ros2 param get <parameter>" across all nodes. (#1174)

* Fix ParameterNameCompleter. (#1172)

* Output node parameters upon each receipt (#1162)

* skip test_verb_load_wildcard for rmw_connextdds. (#1150)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* Restore environment variables after launch tests (#1086)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Relax the check from exact to partial match. (#1055)

* Export Typing information (#1041)

* fix misspelling. (#1035)

* catch ConnectionRefusedError, so that it can fall back to
  DirectNode. (#1014)

* fails the test properly to avoid TypeError exception. (#1016)

* Fix loading parameter behavior from yaml file (#864)

* Allow zenoh tests to run with multicast (#992)

* Contributors: Barry Xu, Christophe Bedard, Michael Carlstrom,
  Michael Carroll, Scott K Logan, Taiga Arai, Tomoya Fujita, Tony
  Najjar, mosfet80

ros2pkg
=======

* Remove "rclrs" duplicate dependency (#1197)

* Fix future flake8 regressions (#1196)

* Add Native ROS2 Rust Package Create Capability (#1107)

* Remove importlib packages (#1117)

* add mypy (#1109)

* fix cmake deprecation (#1082)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Reduce boilerplate in install(TARGETS for library (#1056)

* Export Typing information (#1041)

* Use modern C++17 syntax. (#982)

* Use target_link_libraries instead of ament_target_dependencies
  (#973)

* Try to use the git global user.name for maintainer-name (#968)

* Update minimum CMake version CMakeLists.txt.em (#969)

* Contributors: Bartlomiej Styczen, Christophe Bedard, Larry Gezelius,
  Michael Carlstrom, Parth Patel, Sebastian Castro, Shane Loretz,
  Shynur, Silvio Traversaro, mosfet80

ros2plugin
==========

* Implement package option (#293)

* Improve logging when unable to parse the plugin (#285)

* Add ros2plugin (#165)

* Contributors: Alejandro Hernández Cordero, Jeremie Deray, mini-1235

ros2run
=======

* Fix Bash completion (#1182)

* Add fzf-based interactive selection to ros2cli commands (#1151)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* Add signal handler SIGIN/SIGTERM to ros2run (#899)

* Contributors: Christophe Bedard, Michael Carlstrom, Tomoya Fujita,
  Tony Najjar, mosfet80

ros2service
===========

* Add timeout arguments to "ros2 service call", "ros2 action
  send_goal", "ros2 component", "ros2 lifecycle", and "ros2 param"
  (#1185)

* Fix Bash completion (#1182)

* Add fzf-based interactive selection to ros2cli commands (#1151)

* add verbose in service-info verb (#916)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* Restore environment variables after launch tests (#1086)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Relax the check from exact to partial match. (#1055)

* Export Typing information (#1041)

* move QoS methods from ros2topic.api to ros2cli.qos. (#1053)

* add QoS option to ros2service/ros2action echo commands. (#1036)

* Use "get_service" in "ros2service call" (#994)

* Allow zenoh tests to run with multicast (#992)

* Support QoS options for "ros2 service call" (#966)

* Contributors: Christophe Bedard, Lee, Michael Carlstrom, Michael
  Carroll, Minju, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80

ros2test
========

* fix setuptools deprecations (#16)

* Contributors: mosfet80

ros2topic
=========

* Improve test isolation and suppress Connext license noise (#1225)

* Add fzf-based interactive selection to ros2cli commands (#1151)

* add "--all/-a" option to "ros2 topic bw" with screen refresh.
  (#1130)

* return explicitly from internal functions. (#1128)

* support multiple topics for "ros2 topic bw". (#1124)

* add "--all/-a" option to "ros2 topic hz" with screen refresh.
  (#1122)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* wait for the publisher before test command is executed. (#1094)

* Enable test isolation on a few remaining ros2topic tests (#1087)

* Restore environment variables after launch tests (#1086)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* move QoS methods from ros2topic.api to ros2cli.qos. (#1053)

* Custom Completion Finder for fetching topic prototype (#995)

* Documented now and auto keywords (#1008)

* Conditional deserialization of message for "ros2 topic hz" (#1005)

* Enable "ros2 topic echo" with entries of array fields (#996)

* Allow zenoh tests to run with multicast (#992)

* Adapt tests to Zenoh (#988)

* Adjust topic hz and bw command description (#987)

* Add support for topic QOS for ros2topic bw, delay and hz (#935)

* Start the simulation from 1 second for the test (#975)

* Support QoS options for "ros2 service call" (#966)

* Support ros2 topic pub yaml file input (#925)

* Contributors: Alejandro Hernández Cordero, Anthony Welte, Christophe
  Bedard, Fabian Thomsen, Florencia, Kostubh Khandelwal, Leander
  Stephen D'Souza, Martin Pecka, Michael Carlstrom, Michael Carroll,
  Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80, nomumu

ros2trace
=========

* Ignore A0005 (#237)

* Update trace command's doc-string (#213)

* Allow creating snapshot sessions (#195)

* Add support for starting tracing at runtime (#191)

* fix setuptools deprecation (#189)

* Address typing issues reported by mypy in tracetools_launch (#184)

* Contributors: Christophe Bedard, Michael Carlstrom, Shravan Deva,
  mosfet80

ros_environment
===============

* Change default ROS_DISTRO from 'rolling' to 'lyrical'

* fix cmake deprecation (#42)

* Remove CODEOWNERS. (#40)

* Contributors: Chris Lalancette, Shane Loretz, mosfet80

ros_testing
===========

* fix cmake deprecation (#17)

* Contributors: mosfet80

rosbag2
=======

* Fix CMAKE deprecation (#2067)

* Contributors: mosfet80

rosbag2_compression
===================

* Add validation for empty file path in compression process (#2398)

* Fix a possible race condition in compression writer on close (#2362)

* Update Rosbag2 filename format to "index+name+timestamp" (#2265)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Make topics persistent between writer's close() and open() API calls
  (#2229)

* Address recorder test flakiness by increasing cache size (#2203)

* Fix CMAKE deprecation (#2067)

* Add message loss statistics callbacks and logging (#2039)

* Introduce new "BaseWriteInterface" methods "write_messages" and
  "write_message" to provide operation status, deprecating old write
  APIs (#2030)

* Bugfix: "ros2 bag convert" dropping messages with compression mode
  message (#1975)

* Contributors: Daisuke Sato, DangitBen, Luke Sy, Michael Orlov,
  mosfet80

rosbag2_compression_zstd
========================

* Replace "zstd_vendor" with "zstd_cmake_module" (#2166)

* Fix CMAKE deprecation (#2067)

* Contributors: Alejandro Hernández Cordero, mosfet80

rosbag2_cpp
===========

* Removed clang warning (#2404)

* Implement "transient-local topic" repetition for Writer API and
  split/snapshot integration (#2386)

* Add "TransientLocalMessagesCache" and "RecordOptions" for repeating
  transient-local topics (#2385)

* Use new ROSIDL aggregate CMake target (#2384)

* Fix a possible race condition in compression writer on close (#2362)

* Fix incorrect serialization format in metadata (#2372)

* Update Rosbag2 filename format to "index+name+timestamp" (#2265)

* Support relative includes for IDL in local message definition
  (#2241)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Workaround flaky "bagsize_split_is_at_least_specified_size" test
  (#2311)

* Incorporate upstream minor fixes from Apex.AI (#2240)

* Update deprecated ament_index_cpp API (#2268)

* Make topics persistent between writer's close() and open() API calls
  (#2229)

* Add nullptr check when pushing new messages to the message cache
  (#2219)

* Address recorder test flakiness by increasing cache size (#2203)

* Log reasoning for not found message definition only in debug log
  (#2183)

* Improve error handling in rosbag2_cpp with null checks and exception
  throwing (#2127)

* Add null pointer checks in "Reader" constructor and "open()" method
  (#2135)

* Use "rclcpp typesupport helpers" in "rosbag2_cpp" (#2017)

* Fix callback not called for MESSAGES_LOST event (#2105)

* Improve recorder's MessageCache performance (#2104)

* Fix reindex duration bug when bag file durations overlap (#2036)

* Fix CMAKE deprecation (#2067)

* Add support for searching message definitions in nested
  subdirectories (#2055)

* Add message loss statistics callbacks and logging (#2039)

* Use cache to determine action interface inner types (#2052)

* Fix service/action message definition issue (#2041)

* Introduce new "BaseWriteInterface" methods "write_messages" and
  "write_message" to provide operation status, deprecating old write
  APIs (#2030)

* Improve message publishing timing by avoiding sporadic wakeups and
  fixing incorrect intervals on player start (#2025)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Address clang warning in the "TimeControllerClock::wakeup()" (#1962)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe
  Bedard, Chui Vanfleet, Daisuke Sato, Emerson Knapp, Hunter L. Allen,
  José Faria, Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar,
  YuJin Hong, mosfet80

rosbag2_examples_cpp
====================

* Use new ROSIDL aggregate CMake target (#2384)

* Update subscription callback signatures (#2225)

* Fix CMAKE deprecation (#2067)

* Add examples for compressing bag files (#1956)

* Contributors: Emerson Knapp, Maxime Fleury, mini-1235, mosfet80

rosbag2_examples_py
===================

* Fix setuptools deprecation by removing "tests_require" (#2092)

* Add examples for compressing bag files (#1956)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Add a simple example showing how to convert bags to the csv file
  (#1974)

* Contributors: Christophe Bedard, Maxime Fleury, Michael Orlov,
  mosfet80

rosbag2_interfaces
==================

* Add support for time based Resume service (#2357)

* Allow pause/resume service calls while not in recording (#2349)

* Implement delayed and time-based recorder and player services,
  adding new bag split modes (#2330)

* Add error return code to the "~/stop" service request (#2312)

* Add Record, Stop, StartDiscovery, StopDiscovery, and
  IsDiscoveryRunning services for Recorder (#2248)

* Publish messages lost statistics to 'events/messages_lost' topic
  (#2150)

* Fix CMAKE deprecation (#2067)

* Contributors: Michael Orlov, carlos-apex, mosfet80

rosbag2_performance_benchmarking
================================

* Use new ROSIDL aggregate CMake target (#2384)

* Remove unnecessary dependencies on "yaml_cpp_vendor" (#2353)

* Fix warning by initializing "number_of_threads" (#2121)

* Enable "rosbag2_performance_benchmarking" package to be built by
  default (#2093)

* Fix performance benchmarking data generation and environment
  variable handling (#2078)

* Fix failure in "benchmark_launch" when calling "Process.wait()"
  twice (#2076)

* Fix incorrect results from "prosbag2_performance_benchmarking" for
  high-frequency topics (#2077)

* Fix CMAKE deprecation (#2067)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Contributors: Chris Lalancette, Christophe Bedard, Cristóbal Arroyo,
  Emerson Knapp, Michael Orlov, mosfet80

rosbag2_performance_benchmarking_msgs
=====================================

* Enable "rosbag2_performance_benchmarking" package to be built by
  default (#2093)

* Fix CMAKE deprecation (#2067)

* Contributors: Michael Orlov, mosfet80

rosbag2_py
==========

* Add "--repeat-all-transient-local" flag for automatic transient-
  local topic detection (#2391)

* Repeat transient-local topics: Recorder, CLI, and Python bindings
  (#2387)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Move to "build_depend" (#2332)

* Improve "ros2 bag convert" performance for fragment cutting and add
  "--input-options" (#2325)

* Add static topics feature for recorder (#2319)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Incorporate upstream minor fixes from Apex.AI (#2240)

* Add "input_serialization_format" and "output_serialization_format"
  to "RecordOptions", deprecating "rmw_serialization_format" (#2215)

* Use pybind11 from deb or pixi (#2154)

* Publish messages lost statistics to 'events/messages_lost' topic
  (#2150)

* Ensure test topic discovery by recorder in "rosbag2_py" test (#2132)

* Fix CMake list append for env vars in rosbag2_py with clang (#2116)

* Add public API for player's starting time and playback duration
  (#2095)

* Expose more of the player and recorder API to Python, and improve
  signal handling (#2062)

* Add "send_timestamp" to Python interface for reading serialized
  messages (#2061)

* Refactor Python player and recorder APIs into classes (#2047)

* Fix service/action message definition issue (#2041)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Bugfix: "ros2 bag convert" dropping messages with compression mode
  message (#1975)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe
  Bedard, DangitBen, Luke Sy, Michael Carlstrom, Michael Orlov, Om
  Shivam Verma, Tony Najjar

rosbag2_storage
===============

* Add "TransientLocalMessagesCache" and "RecordOptions" for repeating
  transient-local topics (#2385)

* Implement delayed and time-based recorder and player services,
  adding new bag split modes (#2330)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Improve "ros2 bag convert" performance for fragment cutting and add
  "--input-options" (#2325)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Throw "YAML::Exception" during conversion if the data type
  mismatches (#2262)

* Fix decoder and encode mismatch in YAML deserialization (#2277)

* Incorporate upstream minor fixes from Apex.AI (#2240)

* Fix memory leak on "make_empty_serialized_message()" (#2253)

* Fix CMAKE deprecation (#2067)

* Introduce new "BaseWriteInterface" methods "write_messages" and
  "write_message" to provide operation status, deprecating old write
  APIs (#2030)

* Fix undefined behavior in the "rosbag2_storage" and
  "rosbag2_storage_sqlite3" packages (#1997)

* Use DDS queue depth for subscriptions as a maximum value across
  publishers (#1960)

* Contributors: Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar,
  carlos-apex, mosfet80

rosbag2_storage_default_plugins
===============================

* Fix CMAKE deprecation (#2067)

* Contributors: mosfet80

rosbag2_storage_mcap
====================

* Use new ROSIDL aggregate CMake target (#2384)

* Remove unnecessary dependencies on "yaml_cpp_vendor" (#2353)

* Fix MCAPStorage::seek(time) to advance when timestamp matches
  current time (#2157)

* Fix CMAKE deprecation (#2067)

* Introduce new "BaseWriteInterface" methods "write_messages" and
  "write_message" to provide operation status, deprecating old write
  APIs (#2030)

* Update "index.ros.org/p/" links for "rosbag2_storage_mcap" (#2034)

* Contributors: Chris Lalancette, Christophe Bedard, Emerson Knapp,
  Michael Orlov, mosfet80

rosbag2_storage_sqlite3
=======================

* Use new ROSIDL aggregate CMake target (#2384)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Fix vulnerable string concatenation by using parameterized queries
  (#2290)

* Remove sqlite3_vendor (#2164)

* Fix CMAKE deprecation (#2067)

* Introduce new "BaseWriteInterface" methods "write_messages" and
  "write_message" to provide operation status, deprecating old write
  APIs (#2030)

* Fix undefined behavior in the "rosbag2_storage" and
  "rosbag2_storage_sqlite3" packages (#1997)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Contributors: Alejandro Hernández Cordero, Christophe Bedard,
  Emerson Knapp, Luke Sy, Michael Orlov, Tomoya Fujita, mosfet80

rosbag2_test_common
===================

* Reduce flakiness in rosbag2 recorder end-to-end tests (#2370)

* Use new ROSIDL aggregate CMake target (#2384)

* Update Rosbag2 filename format to "index+name+timestamp" (#2265)

* Update subscription callback signatures (#2225)

* Fix CMAKE deprecation (#2067)

* Address test flakiness by waiting for executor spin (#2001)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Use DDS queue depth for subscriptions as a maximum value across
  publishers (#1960)

* Contributors: Christophe Bedard, Daisuke Sato, Emerson Knapp,
  Michael Orlov, mini-1235, mosfet80

rosbag2_test_msgdefs
====================

* Support relative includes for IDL in local message definition
  (#2241)

* Fix CMAKE deprecation (#2067)

* Add support for searching message definitions in nested
  subdirectories (#2055)

* Contributors: Hunter L. Allen, Michael Orlov, mosfet80

rosbag2_tests
=============

* Use new ROSIDL aggregate CMake target (#2384)

* Update Rosbag2 filename format to "index+name+timestamp" (#2265)

* Add static topics feature for recorder (#2319)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Workaround flaky "bagsize_split_is_at_least_specified_size" test
  (#2311)

* Add "input_serialization_format" and "output_serialization_format"
  to "RecordOptions", deprecating "rmw_serialization_format" (#2215)

* Address recorder test flakiness by increasing cache size (#2203)

* Use "rclcpp typesupport helpers" in "rosbag2_cpp" (#2017)

* Expose more of the player and recorder API to Python, and improve
  signal handling (#2062)

* Fix CMAKE deprecation (#2067)

* Fix deadlocks in Rosbag2 player when calling stop API (#2057)

* Introduce new "BaseWriteInterface" methods "write_messages" and
  "write_message" to provide operation status, deprecating old write
  APIs (#2030)

* Address test flakiness by waiting for executor spin (#2001)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Contributors: Christophe Bedard, Daisuke Sato, Emerson Knapp,
  Michael Orlov, mosfet80

rosbag2_transport
=================

* Apply /bigobj to all MSVC builds in rosbag2_transport (#2424)
  (#2428)

* fix: Fixed compile errors in rosbag2_transport for MSVC 2022 and
  C++20 (#2407)

* Fix QoS overrides ignored when topic name has no leading slash
  (#2394)

* Refactor transient-local topic detection and logging in RecorderImpl
  (#2395)

* Fix race condition in "RecordSrvsSimTimeTest" by waiting for clock
  subscriber (#2396)

* Add "--repeat-all-transient-local" flag for automatic transient-
  local topic detection (#2391)

* Repeat transient-local topics: Recorder, CLI, and Python bindings
  (#2387)

* Implement "transient-local topic" repetition for Writer API and
  split/snapshot integration (#2386)

* Add "TransientLocalMessagesCache" and "RecordOptions" for repeating
  transient-local topics (#2385)

* Use new ROSIDL aggregate CMake target (#2384)

* Address flakiness in the "rosbag2_transport::test_record_services"
  tests (#2368)

* Add support for time based Resume service (#2357)

* Address race condition in the "wait_for_playback_to_start()"
  function (#2344)

* Add "set_on_start_recording_callback()" to set the callback for when
  recording starts (#2340)

* Remove unnecessary dependencies on "yaml_cpp_vendor" (#2353)

* Allow pause/resume service calls while not in recording (#2349)

* Implement delayed and time-based recorder and player services,
  adding new bag split modes (#2330)

* Update Rosbag2 filename format to "index+name+timestamp" (#2265)

* Address a possible deadlock in "seek(timestamp)" (#2345)

* Add missing fields to "RecordOptions" YAML encode/decode functions
  and include a compile-time safeguard (#2334)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Improve "ros2 bag convert" performance for fragment cutting and add
  "--input-options" (#2325)

* Add static topics feature for recorder (#2319)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Fix the flaky "can_record_again_after_stop" test (#2313)

* Add error return code to the "~/stop" service request (#2312)

* Add Record, Stop, StartDiscovery, StopDiscovery, and
  IsDiscoveryRunning services for Recorder (#2248)

* Use QoS override settings for inner Rosbag2 publishing topics
  (#2286)

* Fix decoder and encode mismatch in YAML deserialization (#2277)

* Incorporate upstream minor fixes from Apex.AI (#2240)

* Fix macOS build: Disable thread-safety annotations in
  "locked_priority_queue.hpp" (#2245)

* Fix C++ Recorder failure when stop() then record() are called with
  the same bag name (#2224)

* Add a direct API for "rosbag2_transport::Recorder" (#2221)

* Add "input_serialization_format" and "output_serialization_format"
  to "RecordOptions", deprecating "rmw_serialization_format" (#2215)

* Enable RMW communication isolation in rosbag2_transport tests
  (#2190)

* Add topic name and type delimiter for hash map keys to avoid
  collisions (#2210)

* Add cache for "TopicFilter" to avoid performance burden on discovery
  (#1486)

* Address recorder test flakiness by increasing cache size (#2203)

* Reduce CPU overhead in Rosbag2 recorder discovery by improving
  discovery logic (#2201)

* Fix data races in "PlayerProgressBar" using atomic variables (#2194)

* Fix data races in tests with "MockSequentialWriter" (#2192)

* Player now respects original message order for same timestamps
  (#2172)

* Return player storage options by value in "get_storage_options()" to
  avoid dangling reference (#2181)

* Fix player not playing when "read_ahead_queue_size" equals 1 (#2174)

* Fix multiple race conditions and a deadlock in the player (#2171)

* Fix multibag replay stagnation and improve playback performance by
  managing chronological message order with "ReadersManager" (#2158)

* Fix MCAPStorage::seek(time) to advance when timestamp matches
  current time (#2157)

* Publish messages lost statistics to 'events/messages_lost' topic
  (#2150)

* Add "RecorderEventNotifier" class (#2144)

* Resolve deadlock during multibag replay and update
  "wait_for_playback_to_start" (#2143)

* Use "rclcpp typesupport helpers" in "rosbag2_cpp" (#2017)

* Fix callback not called for MESSAGES_LOST event (#2105)

* Add public API for player's starting time and playback duration
  (#2095)

* Fix CMAKE deprecation (#2067)

* Fix deadlocks in Rosbag2 player when calling stop API (#2057)

* Add message loss statistics callbacks and logging (#2039)

* Skip flaky "can_record_again_after_stop" test (#2031)

* Fix "cout" output when progress bar is disabled (#2024)

* Improve message publishing timing by avoiding sporadic wakeups and
  fixing incorrect intervals on player start (#2025)

* Fix "playing_respects_delay" test flakiness (#2016)

* Address test flakiness by waiting for executor spin (#2001)

* Avoid sending non-existent cancel requests (#2005)

* Fix a maybe-uninitialized warning in player_action_client.cpp
  (#1969)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Bugfix: "ros2 bag convert" dropping messages with compression mode
  message (#1975)

* Use DDS queue depth for subscriptions as a maximum value across
  publishers (#1960)

* Contributors: Barry Xu, Chris Lalancette, Christophe Bedard, Daisuke
  Sato, DangitBen, Dhruv Patel, Emerson Knapp, Janosch Machowinski,
  Luke Sy, Michael Carroll, Michael Orlov, Sahil Lakhmani, Scott K
  Logan, Shane Loretz, Tomoya Fujita, Tony Najjar, baranbologur,
  carlos-apex, mergify[bot], mosfet80

rosgraph_msgs
=============

* Actually build the new graph description messages (#192) (#198)

* Add Graph description messages to "rosgraph_msgs" (#188)

* Fix cmake deprecation (#180)

* Contributors: Emerson Knapp, mergify[bot], mosfet80

rosidl_adapter
==============

* Fix future regressions on flake8 (#936)

* Fix @optional for string literals (#905)

* Export typing Information (#903)

* Add Optional Parsing (#883)

* Uniform cmake minVersion (#849)

* Contributors: Michael Carlstrom, mosfet80

rosidl_buffer
=============

* Add missing std::vector compatible APIs to rosidl::Buffer (#959)

* Bump rosidl_buffer min CMake version (#956)

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* Add cstdint include to c_helpers.cpp (#953)

* Add rosidl_buffer and rosidl_buffer_backend for native Buffer type
  support (#941)

* Contributors: CY Chen, Shane Loretz, mosfet80

rosidl_buffer_backend
=====================

* Clarify return of get_descriptor_type_support() (#958)

* Bump rosidl_buffer min CMake version (#956)

* Add rosidl_buffer and rosidl_buffer_backend for native Buffer type
  support (#941)

* Contributors: CY Chen, Shane Loretz

rosidl_buffer_backend_registry
==============================

* Add missing ament_cmake_gtest dep (#960)

* Bump rosidl_buffer min CMake version (#956)

* Add rosidl_buffer_backend_registry (#944)

* Contributors: CY Chen, Scott K Logan, Shane Loretz

rosidl_buffer_py
================

* Bump rosidl_buffer min CMake version (#956)

* Fix pybind11 rosdep key (#955)

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* Contributors: CY Chen, Christoph Fröhlich, Shane Loretz

rosidl_cli
==========

* Fix future regressions on flake8 (#936)

* remove importlib-metadata (#917)

* Export typing Information (#903)

* fix setuptools deprecations (#877)

* rosidl_cli: Add type description support (#857)

* Contributors: Francisco Rossi, Michael Carlstrom, mosfet80

rosidl_cmake
============

* Install interface files to same folder as idl (#935)

* Create an aggregate target for rosidl generated interfaces targets
  (#947)

* Add "rosidl_auto_generate_interfaces" function (#918)

* Export typing Information (#903)

* remove deprecated rosidl_target_interfaces. (#898)

* fix cmake <3.10 deprecation (#875)

* Contributors: Emerson Knapp, Kotaro Yoshimoto, Michael Carlstrom,
  Tim Wendt, Tomoya Fujita, mosfet80

rosidl_core_generators
======================

* Revert "Revert "Added rosidl_generator_rs (#7)" (#8)" (#9)

* fix cmake deprecation (#10)

* Contributors: Esteve Fernandez, mosfet80

rosidl_core_runtime
===================

* Add rosidl_buffer_py as build_export_depend with explicit group
  resolution (#14)

* fix cmake deprecation (#10)

* Contributors: CY Chen, mosfet80
