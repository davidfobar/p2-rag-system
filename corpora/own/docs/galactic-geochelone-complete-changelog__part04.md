# Galactic Geochelone changelog (part 4 of 8)

* Add lifecycle node state transition instrumentation (#804)

* Update maintainers (#825)

* Improve error messages in rcl_lifecycle (#742)

* Fix test_rcl_lifecycle (#788)

* Add fault injection macros and unit tests to rcl_lifecycle (#731)

* Remove std::cout line from test_rcl_lifecycle.cpp (#773)

* Set transition_map->states/transition size to 0 on fini (#729)

* Topic fix rcl lifecycle test issue (#715)

* Removed doxygen warnings (#712)

* Update quality declaration and coverage (#674)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Barry Xu,
  Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Karsten
  Knese, Lei Liu, Stephen Brawner, brawner, shonigmann

rcl_logging_interface
=====================

* Update QD to QL 1 (#66)

* Use rcutils_expand_user in rcl_logging_get_logging_directory (#59)

* Allow configuring logging directory through environment variables
  (#53)

* Update the maintainers. (#55)

* Add new package with rcl logging interface (#41)

* Contributors: Chris Lalancette, Christophe Bedard, Stephen Brawner

rcl_logging_log4cxx
===================

* Allow configuring logging directory through environment variables
  (#53)

* Update the maintainers. (#55)

* Remove unused pytest dependency. (#43)

* Use new package with rcl logging interface (#41)

* Contributors: Chris Lalancette, Christophe Bedard

rcl_logging_noop
================

* Make internal dependencies private (#60)

* Update the maintainers. (#55)

* Remove unused pytest dependency. (#43)

* Use new package with rcl logging interface (#41)

* Contributors: Chris Lalancette, Shane Loretz

rcl_logging_spdlog
==================

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#73)

* Include what you use (#71)

* Update QD to QL 1 (#66)

* Make sure to check return value from external_initialize. (#65)

* updated QD section 3.i and 3ii and spelling error (#63)

* rcl_logging_spdlog: Increased QL to 2 in QD

* Updated spdlog QL in QD

* Make internal dependencies private (#60)

* [rcl_logging_spdlog] Add warnings (#54)

* Allow configuring logging directory through environment variables
  (#53)

* Update the maintainers. (#55)

* Added benchmark test to rcl_logging_spdlog (#52)

* Used current_path() function from rcpputils (#51)

* Add fault injection unittest to increase coverage (#49)

* Bump QD to level 3 and updated QD (#44)

* Added Doxyfile and fixed related warnings (#42)

* Use new package with rcl logging interface (#41)

* Increased test coverage (#40)

* Add Security Vulnerability Policy pointing to REP-2006.

* Rename Quality_Declaration.md -> QUALITY_DECLARATION.md

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris
  Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Scott K
  Logan, Shane Loretz, Stephen Brawner, ahcorde, brawner, shonigmann

rcl_yaml_param_parser
=====================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#909)

* Enable compiler warnings (#831)

* Update QDs to QL 1 (#866)

* Rearrange test logic to avoid reference to null (#862)

* Update QL (#858)

* Make sure to initialize the end_mark for yaml_event_t (#849)

* Check for valid node names in parameters files (#809)

* Update maintainers (#825)

* Updated performance section QD (#817)

* Several memory-related fixes for rcl_variant_t benchmarks (#813)

* Improved rcl_yaml_param_parser benchmark test (#810)

* Added benchmark test to rcl_yaml_param_parser (#803)

* Remove MAX_NUM_PARAMS_PER_NODE and MAX_NUM_NODE_ENTRIES limitation.
  (#802)

* Add mocking unit tests for rcl_yaml_param_parser (coverage part 3/3)
  (#772)

* Add fault-injection unit tests (coverage part 2/3) (#766)

* Add basic unit tests for refactored functions in
  rcl_yaml_param_parser (coverage part 1/3) (#771)

* Fix yaml parser error when meets .nan (refactor on #754) (#781)

* Refactor parser.c for better testability (#754)

* Don't overwrite cur_ns pointer if reallocation fails (#780)

* Fix mem leaks in unit test from 776 (#779)

* Fix rcl_parse_yaml_file() error handling. (#776)

* Don't overwrite string_array pointer on reallocation failure (#775)

* Set yaml_variant values to NULL on finalization (#765)

* Remove debugging statements. (#755)

* Removed doxygen warnings (#712)

* Update quality declaration and coverage (#674)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chen Lihui,
  Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Scott K
  Logan, Stephen Brawner, brawner, shonigmann, tomoya

rclcpp
======

* Use OnShutdown callback handle instead of OnShutdown callback
  (#1639) (#1650)

* use dynamic_pointer_cast to detect allocator mismatch in intra
  process manager (#1643) (#1644)

* Increase cppcheck timeout to 500s (#1634)

* Clarify node parameters docs (#1631)

* Avoid returning loan when none was obtained. (#1629)

* Use a different implementation of mutex two priorities (#1628)

* Do not test the value of the history policy when testing the
  get_publishers/subscriptions_info_by_topic() methods (#1626)

* Check first parameter type and range before calling the user
  validation callbacks (#1627)

* Restore test exception for Connext (#1625)

* Fix race condition in TimeSource clock thread setup (#1623)

* remove deprecated code which was deprecated in foxy and should be
  removed in galactic (#1622)

* Change index.ros.org -> docs.ros.org. (#1620)

* Unique network flows (#1496)

* Add spin_some support to the StaticSingleThreadedExecutor (#1338)

* Add publishing instrumentation (#1600)

* Create load_parameters and delete_parameters methods (#1596)

* refactor AnySubscriptionCallback and add/deprecate callback
  signatures (#1598)

* Add generic publisher and generic subscription for serialized
  messages (#1452)

* use context from "node_base\_" for clock executor. (#1617)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#1615)

* Initialize integers in test_parameter_event_handler.cpp to avoid
  undefined behavior (#1609)

* Namespace tracetools C++ functions (#1608)

* Revert "Namespace tracetools C++ functions (#1603)" (#1607)

* Namespace tracetools C++ functions (#1603)

* Clock subscription callback group spins in its own thread (#1556)

* Remove rmw_connext_cpp references. (#1595)

* Add API for checking QoS profile compatibility (#1554)

* Document misuse of parameters callback (#1590)

* use const auto & to iterate over parameters (#1593)

* Guard against integer overflow in duration conversion (#1584)

* get_parameters service should return empty if undeclared parameters
  are allowed (#1514)

* Made 'Context::shutdown_reason' function a const function (#1578)

* Document design decisions that were made for statically typed
  parameters (#1568)

* Fix doc typo in CallbackGroup constructor (#1582)

* Enable qos parameter overrides for the /parameter_events topic
  (#1532)

* Add support for rmw_connextdds (#1574)

* Remove 'struct' from the rcl_time_jump_t. (#1577)

* Add tests for declaring statically typed parameters when undeclared
  parameters are allowed (#1575)

* Quiet clang memory leak warning on "DoNotOptimize". (#1571)

* Add ParameterEventsSubscriber class (#829)

* When a parameter change is rejected, the parameters map shouldn't be
  updated. (#1567)

* Fix when to throw the NoParameterOverrideProvided exception. (#1567)

* Fix SEGV caused by order of destruction of Node sub-interfaces
  (#1469)

* Fix benchmark test failure introduced in #1522 (#1564)

* Fix documented example in create_publisher (#1558)

* Enforce static parameter types (#1522)

* Allow timers to keep up the intended rate in MultiThreadedExecutor
  (#1516)

* Fix UBSAN warnings in any_subscription_callback. (#1551)

* Fix runtime error: reference binding to null pointer of type (#1547)

* Reference test resources directly from source tree (#1543)

* clear statistics after window reset (#1531) (#1535)

* Fix a minor string error in the topic_statistics test. (#1541)

* Avoid "Resource deadlock avoided" if use intra_process_comms (#1530)

* Avoid an object copy in parameter_value.cpp. (#1538)

* Assert that the publisher_list size is 1. (#1537)

* Don't access objects after they have been std::move (#1536)

* Update for checking correct variable (#1534)

* Destroy msg extracted from LoanedMessage. (#1305)

* Add instrumentation for linking a timer to a node (#1500)

* Fix error when using IPC with StaticSingleThreadExecutor (#1520)

* Change to using unique_ptrs for DummyExecutor. (#1517)

* Allow reconfiguring 'clock' topic qos (#1512)

* Allow to add/remove nodes thread safely in rclcpp::Executor (#1505)

* Call rclcpp::shutdown in test_node for clean shutdown on Windows
  (#1515)

* Reapply "Add get_logging_directory method to rclcpp::Logger (#1509)"
  (#1513)

* use describe_parameters of parameter client for test (#1499)

* Revert "Add get_logging_directory method to rclcpp::Logger (#1509)"
  (#1511)

* Add get_logging_directory method to rclcpp::Logger (#1509)

* Better documentation for the QoS class (#1508)

* Modify excluding callback duration from topic statistics (#1492)

* Make the test of graph users more robust. (#1504)

* Make sure to wait for graph change events in test_node_graph.
  (#1503)

* add timeout to SyncParametersClient methods (#1493)

* Fix wrong test expectations (#1497)

* Update create_publisher/subscription documentation, clarifying when
  a parameters interface is required (#1494)

* Fix string literal warnings (#1442)

* support describe_parameters methods to parameter client. (#1453)

* Add getters to rclcpp::qos and rclcpp::Policy enum classes (#1467)

* Change nullptr checks to use ASSERT_TRUE. (#1486)

* Adjust logic around finding and erasing guard_condition (#1474)

* Update QDs to QL 1 (#1477)

* Add performance tests for parameter transport (#1463)

* Move ownership of shutdown_guard_condition to
  executors/graph_listener (#1404)

* Add options to automatically declare qos parameters when creating a
  publisher/subscription (#1465)

* Add "take_data" to "Waitable" and "data" to "AnyExecutable" (#1241)

* Add benchmarks for node parameters interface (#1444)

* Remove allocation from executor::remove_node() (#1448)

* Fix test crashes on CentOS 7 (#1449)

* Bump rclcpp packages to Quality Level 2 (#1445)

* Added executor benchmark tests (#1413)

* Add fully-qualified namespace to WeakCallbackGroupsToNodesMap
  (#1435)

* Deprecate Duration(rcl_duration_value_t) in favor of static
  Duration::from_nanoseconds(rcl_duration_value_t) (#1432)

* Avoid parsing arguments twice in
  "rclcpp::init_and_remove_ros_arguments" (#1415)

* Add service and client benchmarks (#1425)

* Set CMakeLists to only use default rmw for benchmarks (#1427)

* Update tracetools' QL in rclcpp's QD (#1428)

* Add missing locking to the rclcpp_action::ServerBase. (#1421)

* Initial benchmark tests for rclcpp::init/shutdown create/destroy
  node (#1411)

* Refactor test CMakeLists in prep for benchmarks (#1422)

* Add methods in topic and service interface to resolve a name (#1410)

* Update deprecated gtest macros (#1370)

* Clear members for StaticExecutorEntitiesCollector to avoid
  shared_ptr dependency (#1303)

* Increase test timeouts of slow running tests with rmw_connext_cpp
  (#1400)

* Avoid self dependency that not destoryed (#1301)

* Update maintainers (#1384)

* Add clock qos to node options (#1375)

* Fix NodeOptions copy constructor (#1376)

* Make sure to clean the external client/service handle. (#1296)

* Increase coverage of WaitSetTemplate (#1368)

* Increase coverage of guard_condition.cpp to 100% (#1369)

* Add coverage statement (#1367)

* Tests for LoanedMessage with mocked loaned message publisher (#1366)

* Add unit tests for qos and qos_event files (#1352)

* Finish coverage of publisher API (#1365)

* Finish API coverage on executors. (#1364)

* Add test for ParameterService (#1355)

* Add time API coverage tests (#1347)

* Add timer coverage tests (#1363)

* Add in additional tests for parameter_client.cpp coverage.

* Minor fixes to the parameter_service.cpp file.

* reset rcl_context shared_ptr after calling rcl_init sucessfully
  (#1357)

* Improved test publisher - zero qos history depth value exception
  (#1360)

* Covered resolve_use_intra_process (#1359)

* Improve test_subscription_options (#1358)

* Add in more tests for init_options coverage. (#1353)

* Test the remaining node public API (#1342)

* Complete coverage of Parameter and ParameterValue API (#1344)

* Add in more tests for the utilities. (#1349)

* Add in two more tests for expand_topic_or_service_name. (#1350)

* Add tests for node_options API (#1343)

* Add in more coverage for expand_topic_or_service_name. (#1346)

* Test exception in spin_until_future_complete. (#1345)

* Add coverage tests graph_listener (#1330)

* Add in unit tests for the Executor class.

* Allow mimick patching of methods with up to 9 arguments.

* Improve the error messages in the Executor class.

* Add coverage for client API (#1329)

* Increase service coverage (#1332)

* Make more of the static entity collector API private.

* Const-ify more of the static executor.

* Add more tests for the static single threaded executor.

* Many more tests for the static_executor_entities_collector.

* Get one more line of code coverage in memory_strategy.cpp

* Bugfix when adding callback group.

* Fix typos in comments.

* Remove deprecated executor::FutureReturnCode APIs. (#1327)

* Increase coverage of publisher/subscription API (#1325)

* Not finalize guard condition while destructing
  SubscriptionIntraProcess (#1307)

* Expose qos setting for /rosout (#1247)

* Add coverage for missing API (except executors) (#1326)

* Include topic name in QoS mismatch warning messages (#1286)

* Add coverage tests context functions (#1321)

* Increase coverage of node_interfaces, including with mocking rcl
  errors (#1322)

* Make node_graph::count_graph_users() const (#1320)

* Add coverage for wait_set_policies (#1316)

* Only exchange intra_process waitable if nonnull (#1317)

* Check waitable for nullptr during constructor (#1315)

* Call vector.erase with end iterator overload (#1314)

* Use best effort, keep last, history depth 1 QoS Profile for '/clock'
  subscriptions (#1312)

* Add tests type_support module (#1308)

* Replace std_msgs with test_msgs in executors test (#1310)

* Add set_level for rclcpp::Logger (#1284)

* Remove unused private function (rclcpp::Node and
  rclcpp_lifecycle::Node) (#1294)

* Adding tests basic getters (#1291)

* Adding callback groups in executor (#1218)

* Refactor Subscription Topic Statistics Tests (#1281)

* Add operator!= for duration (#1236)

* Fix clock thread issue (#1266) (#1267)

* Fix topic stats test, wait for more messages, only check the ones
  with samples (#1274)

* Add get_domain_id method to rclcpp::Context (#1271)

* Fixes for unit tests that fail under cyclonedds (#1270)

* initialize_logging_ should be copied (#1272)

* Use static_cast instead of C-style cast for instrumentation (#1263)

* Make parameter clients use template constructors (#1249)

* Ability to configure domain_id via InitOptions. (#1165)

* Simplify and fix allocator memory strategy unit test for connext
  (#1252)

* Use global namespace for parameter events subscription topic (#1257)

* Increase timeouts for connext for long tests (#1253)

* Adjust test_static_executor_entities_collector for rmw_connext_cpp
  (#1251)

* Fix failing test with Connext since it doesn't wait for discovery
  (#1246)

* Fix node graph test with Connext and CycloneDDS returning actual
  data (#1245)

* Warn about unused result of add_on_set_parameters_callback (#1238)

* Unittests for memory strategy files, except
  allocator_memory_strategy (#1189)

* EXPECT_THROW_EQ and ASSERT_THROW_EQ macros for unittests (#1232)

* Add unit test for static_executor_entities_collector (#1221)

* Parameterize test executors for all executor types (#1222)

* Unit tests for allocator_memory_strategy.cpp part 2 (#1198)

* Unit tests for allocator_memory_strategy.hpp (#1197)

* Derive and throw exception in spin_some spin_all for
  StaticSingleThreadedExecutor (#1220)

* Make ring buffer thread-safe (#1213)

* Add missing RCLCPP_PUBLIC to ~StaticExecutorEntitiesCollector
  (#1227)

* Document graph functions don't apply remap rules (#1225)

* Remove recreation of entities_collector (#1217)

* Fix rclcpp::NodeOptions::operator= (#1211)

* Link against thread library where necessary (#1210)

* Unit tests for node interfaces (#1202)

* Remove usage of domain id in node options (#1205)

* Remove deprecated set_on_parameters_set_callback function (#1199)

* Fix conversion of negative durations to messages (#1188)

* Fix implementation of NodeOptions::use_global_arguments() (#1176)

* Bump to QD to level 3 and fixed links (#1158)

* Fix pub/sub count API tests (#1203)

* Update tracetools' QL to 2 in rclcpp's QD (#1187)

* Fix exception message on rcl_clock_init (#1182)

* Throw exception if rcl_timer_init fails (#1179)

* Unit tests for some header-only functions/classes (#1181)

* Callback should be perfectly-forwarded (#1183)

* Add unit tests for logging functionality (#1184)

* Add create_publisher include to create_subscription (#1180)

* Check period duration in create_wall_timer (#1178)

* Fix get_node_time_source_interface() docstring (#988)

* Add message lost subscription event (#1164)

* Add spin_all method to Executor (#1156)

* Reorganize test directory and split CMakeLists.txt (#1173)

* Check if context is valid when looping in spin_some (#1167)

* Add check for invalid topic statistics publish period (#1151)

* Fix spin_until_future_complete: check spinning value (#1023)

* Fix doxygen warnings (#1163)

* Fix reference to rclcpp in its Quality declaration (#1161)

* Allow spin_until_future_complete to accept any future like object
  (#1113)

* Contributors: Ada-King, Alejandro Hernández Cordero, Ananya
  Muddukrishna, Andrea Sorbini, Audrow Nash, Barry Xu, BriceRenaudeau,
  Chen Lihui, Chris Lalancette, Christophe Bedard, Claire Wang, Colin
  MacKenzie, Daisuke Sato, Devin Bonnie, Dirk Thomas, DongheeYe, Ivan
  Santiago Paunovic, Jacob Perron, Jannik Abbenseth, Johannes Meyer,
  Jorge Perez, Karsten Knese, Louise Poubel, Miaofei Mei, Michel
  Hidalgo, Miguel Company, Morgan Quigley, Nikolai Morin, Pedro Pena,
  Sarthak Mittal, Scott K Logan, Shane Loretz, Stephen Brawner,
  Steven! Ragnarök, Tomoya Fujita, William Woodall, anaelle-sw,
  bpwilcox, brawner, eboasson, hsgwa, mauropasse, shonigmann,
  suab321321, tomoya

rclcpp_action
=============

* Returns CancelResponse::REJECT while goal handle failed to transit
  to CANCELING state (#1641) (#1653)

* Fix action server deadlock issue that caused by other mutexes locked
  in CancelCallback (#1635) (#1646)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#1615)

* Add support for rmw_connextdds (#1574)

* node_handle must be destroyed after client_handle to prevent memory
  leak (#1562)

* Finalize rcl_handle to prevent leak (#1528) (#1529)

* Fix #1526. (#1527)

* Fix action server deadlock (#1285) (#1313)

* Goal response callback compatibility shim with deprecation of old
  signature (#1495)

* [rclcpp_action] Add warnings (#1405)

* Update QDs to QL 1 (#1477)

* Add "take_data" to "Waitable" and "data" to "AnyExecutable" (#1241)

* Fix test crashes on CentOS 7 (#1449)

* Bump rclcpp packages to Quality Level 2 (#1445)

* Add rclcpp_action action_server benchmarks (#1433)

* Benchmark rclcpp_action action_client (#1429)

* Add missing locking to the rclcpp_action::ServerBase. (#1421)

* Increase test timeouts of slow running tests with rmw_connext_cpp
  (#1400)

* Update maintainers (#1384)

* Increase coverage rclcpp_action to 95% (#1290)

* Pass goal handle to goal response callback instead of a future
  (#1311)

* Remove deprecated client goal handle method for getting result
  (#1309)

* Increase test timeout necessary for Connext (#1256)

* Bump to QD to level 3 and fixed links (#1158)

* Add rcl_action_client_options when creating action client. (#1133)

* Fix doxygen warnings (#1163)

* Increase rclcpp_action test coverage (#1153)

* Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Audrow
  Nash, Chris Lalancette, Daisuke Sato, Dirk Thomas, Ivan Santiago
  Paunovic, Jacob Perron, Kaven Yau, Louise Poubel, Michel Hidalgo,
  Stephen Brawner, Tomoya Fujita, William Woodall, brawner,
  shonigmann, tomoya, y-okumura-isp

rclcpp_components
=================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#1615)

* Use std compliant non-method std::filesystem::exists function
  (#1502)

* Fix string literal warnings (#1442)

* Update QDs to QL 1 (#1477)

* Add benchmarks for components (#1476)

* Bump rclcpp packages to Quality Level 2 (#1445)

* Update maintainers (#1384)

* ComponentManager: switch off parameter services and event publisher
  (#1333)

* Bump to QD to level 3 and fixed links (#1158)

* Include original exception in ComponentManagerException (#1157)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Ivan
  Santiago Paunovic, Josh Langsfeld, Louise Poubel, Martijn Buijs,
  Scott K Logan, Stephen Brawner, Tomoya Fujita, shonigmann

rclcpp_lifecycle
================

* Add generic publisher and generic subscription for serialized
  messages (#1452)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#1615)

* Fix flaky lifecycle node tests (#1606)

* Clock subscription callback group spins in its own thread (#1556)

* Delete debug messages (#1602)

* add automatically_add_executor_with_node option (#1594)

* make rcl_lifecyle_com_interface optional in lifecycle nodes (#1507)

* Add support for rmw_connextdds (#1574)

* Fix SEGV caused by order of destruction of Node sub-interfaces
  (#1469)

* Enforce static parameter types (#1522)

* add LifecycleNode::get_transition_graph to match services. (#1472)

* Update QDs to QL 1 (#1477)

* Benchmark lifecycle features (#1462)

* Reserve vector capacities and use emplace_back for constructing
  vectors (#1464)

* [rclcpp_lifecycle] Change uint8_t iterator variables to size_t
  (#1461)

* Bump rclcpp packages to Quality Level 2 (#1445)

* Increase test timeouts of slow running tests with rmw_connext_cpp
  (#1400)

* Update maintainers (#1384)

* Add clock qos to node options (#1375)

* Increase test coverage of rclcpp_lifecycle to 96% (#1298)

* Log error instead of throwing exception in Transition and State
  reset(), mark no except (#1297)

* Remove unused private function (rclcpp::Node and
  rclcpp_lifecycle::Node) (#1294)

* Remove rmw-dependent unit-test checks (#1293)

* Added missing tests for rclcpp lifecycle (#1240)

* Warn about unused result of add_on_set_parameters_callback (#1238)

* Remove deprecated set_on_parameters_set_callback function (#1199)

* Bump to QD to level 3 and fixed links (#1158)

* Fix race in test_lifecycle_service_client (#1204)

* Fix doxygen warnings (#1163)

* Contributors: Alejandro Hernández Cordero, Andrea Sorbini,
  BriceRenaudeau, Claire Wang, Colin MacKenzie, Dirk Thomas, Ivan
  Santiago Paunovic, Jacob Perron, Karsten Knese, Louise Poubel,
  Nikolai Morin, Stephen Brawner, anaelle-sw, brawner, shonigmann,
  tomoya

rclpy
=====

* Break log function execution ASAP if configured severity is too high
  (#776) (#783)

* typo fix. (#768)

* Restore exceptions for Connext and message timestamps on Windows
  (#765)

* Use correct type when creating test publisher (#764)

* Add a test for destroy_node while spinning (#663)

* Add __enter__ and __exit__ to Waitable (#761)

* Check if shutdown callback weak method is valid before calling it
  (#754)

* Change index.ros.org -> docs.ros.org. (#755)

* Use py::class_ for rcl_event_t (#750)

* Convert Clock to use a C++ Class (#749)

* Convert Service to use C++ Class (#747)

* Fix windows warning by using consistent types (#753)

* Use py::class_ for rmw_service_info_t and rmw_request_id_t (#748)

* Convert Timer to use a C++ Class (#745)

* Add PythonAllocator (#746)

* Use py::class_ for rmw_qos_profile_t (#741)

* Combine pybind11 modules into one (#743)

* Use py::class_ for rcl_duration_t (#744)

* Fix bug in unique_ptr type argument (#742)

* Convert Client to use C++ Class (#739)

* Converting last of _rclpy.c to pybind11 (#738)

* Make sure only non-empty std::vector of arguments are indexed (#740)

* Use py::class_ for rcl_time_point_t (#737)

* Convert logging mutex functions to pybind11 (#735)

* Document misuse of of parameter callbacks (#734)

* Convert QoS APIs to pybind11 (#736)

* Add API for checking QoS profile compatibility (#708)

* Replace rmw_connext_cpp with rmw_connextdds (#698)

* Convert last of pub/sub getters to pybind11 (#733)

* Pybind 11: count_subscribers and count_publishers (#732)

* Convert more node accessors to pybind11 (#730)

* Pybind11-ify rclpy_get_node_parameters (#718)

* Modify parameter service behavior when allow_undeclared_parameters
  is false and the requested parameter doesn't exist (#661)

* Include pybind11 first to fix windows debug warning (#731)

* Convert init/shutdown to pybind11 (#715)

* Convert take API to pybind11 (#721)

* Migrate qos event APIs to pybind11 (#723)

* Remove pybind11 from rclpy common (#727)

* Look up pybind11 package once (#726)

* typo fix. (#729)

* [pybind11] Node Accessors (#719)

* Convert serialize/deserialize to pybind11 (#712)

* Convert names_and_types graph APIs to pybind11 (#717)

* Use Pybind11 for name functions (#709)

* Better checks for valid msg and srv types (#714)

* Convert duration to pybind11 (#716)

* Convert wait_set functions to pybind11 (#706)

* Explicitly populate tuple with None (#711)

* Change the time jump time type to just rcl_time_jump_t. (#707)

* Convert rclpy service functions to pybind11 (#703)

* Bump the cppcheck timeout by 2 minutes (#705)

* Convert subscription functions to pybind11 (#696)

* Convert rclpy client functions to pybind11 (#701)

* Fix static typing when allow undeclared (#702)

* Convert publisher functions to pybind11 (#695)

* Convert clock and time functions to pybind11 (#699)

* Set destructor on QoS Profile struct (#700)

* Convert timer functions to pybind11 (#693)

* Convert guard conditions functions to pybind11 (#692)

* Convert service info functions to pybind11 (#694)

* Enforce static parameter types when dynamic typing is not specified
  (#683)

* rclpy_ok and rclpy_create_context to pybind11 (#691)

* Include Pybind11 before Python.h (#690)

* Clean up exceptions in _rclpy_action (#685)

* Clean windows flags on _rclpy_pybind11 and _rclpy_action (#688)

* Use pybind11 for _rclpy_handle (#668)

* Split rclpy module for easier porting to pybind11 (#675)

* Use Pybind11 to generate _rclpy_logging (#659)

* Copy windows debug fixes for pybind11 (#681)

* Use pybind11 for _rclpy_action (#678)

* Update just pycapsule lib to use pybind11 (#652)

* remove maintainer (#682)

* Use Pybind11's CMake code (#667)

* Don't call destroy_node while spinning (#674)

* Check the rcl_action return value on cleanup. (#672)

* Fix the NULL check for destroy_ros_message. (#677)

* Use Py_XDECREF for pynode_names_and_namespaces (#673)

* Use Py_XDECREF for pyresult_list. (#670)

* Fix dead stores. (#669)

* Fix two clang static analysis warnings. (#664)

* Add method to get the current logging directory (#657)

* Fix docstring indent error in create_node (#655)

* use only True to avoid confusion in autodoc config

* document QoS profile constants

* Merge pull request #649 from ros2/clalancette/dont-except-while-
  sleep

* Fixes from review/CI.

* Make sure to catch the ROSInterruptException when calling
  rate.sleep.

* memory leak (#643) (#645)

* Don't throw an exception if timer canceled while sleeping.

* Wake executor in Node.create_subscription() (#647)

* Fix Enum not being comparable with ints in get_parameter_types
  service

* Qos configurability (#635)

* Use Py_XDECREF for pytopic_names_and_types. (#638)

* qos_policy_name_from_kind() should accept either a QoSPolicyKind or
  an int (#637)

* Add method in Node to resolve a topic or service name (#636)

* Deprecate verbose qos policy value names (#634)

* Remove deprecated set_parameters_callback (#633)

* Make sure to use Py_XDECREF in rclpy_get_service_names_and_types
  (#632)

* Update maintainers (#627)

* Add in semicolon on RCUTILS_LOGGING_AUTOINIT. (#624)

* Add in the topic name when QoS events are fired. (#621)

* Use best effort, keep last, history depth 1 QoS Profile for '/clock'
  subscriptions (#619)

* PARAM_REL_TOL documentation fix (#559)

* Node get fully qualified name (#598)

* MultiThreadedExecutor spin_until_future complete should not continue
  waiting when the future is done (#605)
