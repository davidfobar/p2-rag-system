# ROS 2 Kilted Kaiju Complete Changelog (part 3 of 5)

* Shut down context during init if logging config fails (#2594)

* Make more of the Waitable API abstract (#2593)

* Only compile the tests once. (#2590)

* Updated rcpputils path API (#2579)

* Make the subscriber_triggered_to_receive_message test more reliable.
  (#2584) * Make the subscriber_triggered_to_receive_message test more
  reliable. In the current code, inside of the timer we create the
  subscription and the publisher, publish immediately, and expect the
  subscription to get it immediately. But it may be the case that
  discovery hasn't even happened between the publisher and the
  subscription by the time the publish call happens. To make this more
  reliable, create the subscription and publish *before* we ever
  create and spin on the timer. This at least gives 100 milliseconds
  for discovery to happen. That may not be quite enough to make this
  reliable on all platforms, but in my local testing this helps a lot.
  Prior to this change I can make this fail one out of 10 times, and
  after the change I've run 100 times with no failures.

* Have the EventsExecutor use more common code (#2570) * move notify
  waitable setup to its own function * move mutex lock to
  retrieve_entity utility * use entities_need_rebuild_ atomic bool in
  events-executors * remove duplicated set_on_ready_callback for
  notify_waitable * use mutex from base class rather than a new
  recursive mutex * use current_collection_ member in events-executor
  * delay adding notify waitable to collection * postpone clearing the
  current collection * commonize notify waitable and collection *
  commonize add/remove node/cbg methods * fix linter errors ---------

* Removed deprecated methods and classes (#2575)

* Release ownership of entities after spinning cancelled (#2556) *
  Release ownership of entities after spinning cancelled * Move
  release action to every exit point in different spin functions *
  Move wait_result_.reset() before setting spinning to false * Update
  test code * Move test code to test_executors.cpp ---------

* Split test_executors.cpp even further. (#2572) That's because it is
  too large for Windows Debug to compile, so split into smaller bits.
  Even with this split, the file is too big; that's likely because we
  are using TYPED_TEST here, which generates multiple symbols per test
  case. To deal with this, without further breaking up the file, also
  add in the /bigobj flag when compiling on Windows Debug.

* avoid adding notify waitable twice to events-executor collection
  (#2564) * avoid adding notify waitable twice to events-executor
  entities collection * remove redundant mutex lock ---------

* Remove unnecessary msg includes in tests (#2566)

* Fix copy-paste errors in function docs (#2565)

* Fix typo in function doc (#2563)

* Add test creating two content filter topics with the same topic name
  (#2546) (#2549)

* add impl pointer for ExecutorOptions (#2523)

* Fixup Executor::spin_all() regression fix (#2517)

* Add 'mimick' label to tests which use Mimick (#2516)

* Contributors: Abhishek Kashyap, Alberto Soragna, Alejandro Hernández
  Cordero, Alexis Pojomovsky, Barry Xu, Chris Lalancette, Christophe
  Bedard, Hsin-Yi, Janosch Machowinski, Jeffery Hsu, Kang, Leander
  Stephen D'Souza, Patrick Roncagliolo, Pedro de Azeredo, Romain
  DESILLE, Scott K Logan, Steve Macenski, Tanishq Chaudhary, Tomoya
  Fujita, William Woodall, Yuyuan Yuan, jmachowinski

rclcpp_action
=============

* Use std::recursive_mutex for action requests. (#2798)

* Remove warning (#2790)

* Harden rclcpp_action::convert(). (#2786)

* Add new interfaces to enable introspection for action (#2743)

* use maybe_unused attribute for the portability. (#2758)

* fix: Expose timers used by rclcpp::Waitables (#2699)

* Collect log messages from rcl, and reset. (#2720)

* Make ament_cmake a buildtool dependency (#2689)

* Fix documentation typo in server_goal_handle.hpp (#2669)

* Increase the timeout for the cppcheck on rclcpp_action. (#2640)

* add smart pointer macros definitions to action server and client
  base classes (#2631)

* Fix typo in function doc (#2563)

* Add 'mimick' label to tests which use Mimick (#2516)

* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Barry
  Xu, Chris Lalancette, Christophe Bedard, Janosch Machowinski, Nathan
  Wiebe Neufeldt, Scott K Logan, Tomoya Fujita, YR

rclcpp_components
=================

* Removed trailing whitespace from the codebase. (#2791)

* add NO_UNDEFINED_SYMBOLS to rclcpp_components_register_node cmake
  macro (#2746) (#2764)

* use maybe_unused attribute for the portability. (#2758)

* ComponentManager should just ignore unknown extra argument in the
  bas… (#2723)

* Add parsing for rest of obvious boolean extra arguments and throw
  for unsupported ones (#2685)

* Shutdown the context before context's destructor is invoked in tests
  (#2633)

* Fix typo in rclcpp_components benchmark_components (#2602)

* Updated rcpputils path API (#2579)

* remove deprecated APIs from component_manager.hpp (#2585)

* Contributors: Alberto Soragna, Alejandro Hernández Cordero,
  Christophe Bedard, Jonas Otto, Leander Stephen D'Souza, Tomoya
  Fujita, rcp1

rclcpp_lifecycle
================

* should pull valid transition before trying to change the state.
  (#2774)

* use maybe_unused attribute for the portability. (#2758)

* Collect log messages from rcl, and reset. (#2720)

* Update docstring for "rclcpp::Node::now()" (#2696)

* Fix error message in rclcpp_lifecycle::State::reset() (#2647)

* Shutdown the context before context's destructor is invoked in tests
  (#2633)

* LifecycleNode bugfix and add test cases (#2562)

* Properly test get_service_names_and_types_by_node in
  rclcpp_lifecycle (#2599)

* Removed deprecated methods and classes (#2575)

* Fix the lifecycle tests on RHEL-9. (#2583) * Fix the lifecycle tests
  on RHEL-9. The full explanation is in the comment, but basically
  since RHEL doesn't support mocking_utils::inject_on_return, we have
  to split out certain tests to make sure resources within a process
  don't collide. Co-authored-by: Alejandro Hernández Cordero
  <ahcorde@gmail.com>

* revert call shutdown in LifecycleNode destructor (#2557)

* LifecycleNode shutdown on dtor only with valid context. (#2545)

* call shutdown in LifecycleNode dtor to avoid leaving the device in
  unknown state (2nd) (#2528)

* rclcpp::shutdown should not be called before LifecycleNode dtor.
  (#2527)

* Revert "call shutdown in LifecycleNode dtor to avoid leaving the
  device in un… (#2450)" (#2522)

* Add 'mimick' label to tests which use Mimick (#2516)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Patrick Roncagliolo, Scott K Logan, Tomoya Fujita

rclpy
=====

* Update parameter types (#1441)

* Add TypeError string arg for better clarity (#1442)

* Fix loading parameter behavior from yaml file. (#1193)

* Update "lifecycle" types (#1440)

* Update _rclpy_pybind11.pyi order and add EventsExecutor (#1436)

* Update Clock Types (#1433)

* Introduce EventsExecutor implementation (#1391)

* Fix Duration, Clock, and QoS Docs (#1428)

* Add exception doc for configure_introspection. (#1434)

* Fix Task constructor type bug (#1431)

* Add new interfaces to enable intropsection for action (#1413)

* Check parameter callback signature during registration. (#1425)

* Fix function params indentation (#1426)

* Update Service and Action Protocols (#1409)

* Remove "SHARED" from "pybind11_add_module" (#1305)

* Publish action goal status once accepted before execution. (#1228)

* Add missing dependencies so that rosdoc2 shows Node (#1408)

* add QoS Profile/Depth support to Node. (#1376)

* Various typing fixes (#1402)

* Add types to Action with rhel roscli fix (#1361)

* Check if Task(Future) is canceled. (#1377)

* Executors types (#1370)

* event_handler.py types (#1340)

* Add support for operator overloading of "Duration" (#1387)

* Service/Client Implementation types (#1384)

* avoid lifecycle node transition exception (#1319)

* Client:call generates TimeoutError exception when it is timed out.
  (#1271)

* Add in python3-dev build dependency. (#1380)

* Fix the race condition while calling rcl_shutdown (#1353)

* Use @deprecated to mark deprecated APIs for type checkers. (#1350)

* init (#1358)

* Avoid redundant done callbacks of the future while repeatedly
  calling spin_until_future_complete (#1374)

* Clean qos zenoh tests (#1369)

* adjust warn message that requested goal is already expired. (#1363)

* Adds types to Lifecycle Objects (#1338)

* Remove python_cmake_module use (#1220)

* TestClient.test_service_timestamps failing consistently. (#1364)

* Revert "Add types to Action Server and Action Client (#1349)"
  (#1359)

* Revert "Executors types (#1345)" (#1360)

* remove mock_compat (#1357)

* Executors types (#1345)

* Add types to Action Server and Action Client (#1349)

* Remove TODO for OpenSplice DDS issue. (#1354)

* Add types to parameter_client.py (#1348)

* Add types to Node.py (#1346)

* Add types to signals.py (#1344)

* Fixes spin_until_future_complete inside callback (#1316)

* add types (#1339)

* Add types to wait_for_message.py and moves Handles into type stubs
  (#1325)

* Add types to waitable.py (#1328)

* Replace rclpyHandle with type stubs (#1326)

* Fix time subtraction (#1312)

* Adds types to TypeDescriptionService. (#1329)

* Import DurationHandle not DurationType (#1332)

* Creates PublisherHandle and updates publisher.py (#1310)

* Subscription types (#1281)

* Add types to qos.py (#1255)

* minor improvements (#1330)

* Initialize signal handlers after context (#1331)

* shutdown ThreadPoolExecutor in MultiThreadedExecutor. (#1309)

* Generics Services and Clients (#1275)

* Add types to ParameterService (#1262)

* Add types to timer.py (#1260)

* Add types to rcutils_logger.py (#1249)

* Add types to topic_endpoint_info.oy (#1253)

* Add types to parameter.py. (#1246)

* Guard condition types. (#1252)

* Add types to callback_groups.py (#1251)

* Utilities.py types. (#1250)

* reduce result_timeout to 10 secs from 15 mins. (#1171)

* Add TimerInfo to timer callback. (#1292)

* Add types to task.py (#1254)

* Fix a bad bug in fetching the lifecycle transitions. (#1321)

* Fix a bug when using multiple rclpy.init context managers. (#1314)

* Executor executes the tasks in FIFO order. (#1304)

* Add top-level try_shutdown method. (#1302)

* Make rclpy initialization context-manager aware. (#1298)

* Docstring specifying proper destruction and creation of Rate, Timer
  and GuardCondition (#1286)

* Make timers context-aware. (#1296)

* Make service lients context-aware. (#1295)

* Make service servers context-manager aware. (#1294)

* Make nodes context-manager aware. (#1293)

* Make subscriptions context-manager aware. (#1291)

* Make publishers context-manager aware. (#1289)

* (NumberOfEntities) improve performance (#1285)

* Using Generics for messages (#1239)

* Contributors: Alejandro Hernández Cordero, Arjo Chakravarty, Barry
  Xu, Brad Martin, Chris Lalancette, Christophe Bedard, Elian NEPPEL,
  Jonathan, Matthijs van der Burgh, Michael Carlstrom, Nadav Elkabets,
  R Kent James, Shane Loretz, Tomoya Fujita, Wolf Vollprecht, Zahi
  Kakish

rcpputils
=========

* Switch to ament_cmake_ros_core package (#211)

* Added marco to disable deprecation warnings (#210)

* Added missing include (#207)

* Clear the rcutils error when throwing an exception. (#206)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#204)

* fix memory leak for remove_all(). (#201)

* Suppress clang error because of deprecation (#199)

* Deprecated path class (#196)

* Replace create_temp_directory with the new
  create_temporary_directory (#198) * Replace create_temp_directory
  with the new create_temporary_directory - The newly added
  "create_temporary_directory(..)" uses std::filesystem::path and
  doesn't have platform-specific code. - Also deprecated
  "create_temp_directory(..)" and "temp_directory_path"

* Removed deprecated header get_env.hpp (#195)

* Removed rolling mean accumulator deprecated header (#194)

* Removed deprecated clamp methods (#193)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Janosch
  Machowinski, Michael Carroll, Michael Orlov, Tomoya Fujita

rcutils
=======

* Handle spaces in start_process arguments on Windows (#494)

* Add utility functions for invoking a subprocess (#491) (#492)

* Add rcutils_join function for concatenating strings (#490)

* Switch to ament_cmake_ros_core package (#489)

* Cleanup error handling in rcutils. (#485)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#483)

* Fix setting allocator to NULL. (#478)

* Add new API to set envar while specifying overwrite (#473)

* Remove completely unnecessary use of CLASSNAME. (#471)

* load dll built by MINGW with lib prefix (#470)

* add mingw support (#468)

* Fix filesystem iteration on Windows (#469)

* Add 'mimick' label to tests which use Mimick (#466)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Felix F
  Xu, Michael Carroll, Scott K Logan, Yadu

resource_retriever
==================

* Fixed clang compile error (#112)

* Removed windows warnings (#111)

* Add a plugin mechanism to resource_retriever (#103)

* uniform MinCMakeVersion (#108)

* Stop using python_cmake_module. (#94)

* Allow spaces (#100)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael
  Carroll, mosfet80

rmw
===

* Switch to ament_cmake_ros_core package (#397)

* Added rmw_event_type_is_supported (#395)

* add enclave option functions. (#393)

* a couple of typo fixes for doc section. (#391)

* update cmake version (#389)

* get_zero_initialized_xxx functions return zero initialized
  structure. (#380) * get_zero_initialized_xxx functions return zero
  initialized structure. * introduce RMW_EVENT_TYPE_MAX in
  rmw_event_type_t. * add a comment and more tests for rmw_event_type.
  ---------

* move qos_profile_rosout_default from rcl. (#381)

* Fix ugly overwritten warning messages on error paths. (#387) This
  mostly has to do with calling rmw_reset_error() in the proper time
  in the tests, but we also change one test for an allocator to
  properly check for a valid allocator.

* Fix rmw_validate_namespace{_with_size} error handling. (#386) * Fix
  rmw_validate_namespace{_with_size} error handling. It should always
  set an error, even on invalid arguments.

* Fix arg name in rmw_take_response() doc (#384)

* Initialize the NULL strucutre with static value. (#378)

* remove rmw_localhost_only_t. (#376)

* Fix typo with RMW_DURATION_UNSPECIFIED (#375)

* Fix typo in rmw_validate_*_with_size() doc (#374)

* removed deprecated rmw_node_assert_liveliness() (#373)

* add mingw support (#370)

* Minor typo fix (#368)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Felix F Xu, G.A. vd. Hoorn, Michael Carroll,
  Tomoya Fujita

rmw_connextdds
==============

* Switch buildtool to ament_cmake package (#183)

* Export a modern CMake target (#179)

* Added rmw_event_type_is_supported (#173)

* Contributors: Alejandro Hernández Cordero, Scott K Logan, Shane
  Loretz

rmw_connextdds_common
=====================

* Address cpplit and gcc warnings. (#184)

* Support topic instances (#178)

* Switch buildtool to ament_cmake package (#183)

* Discovery race condition mitigation (#174)

* Added rmw_event_type_is_supported (#173)

* use rmw_enclave_options_xxx APIs instead. (#172)

* fix security certificate error message format. (#171)

* Use rmw_security_common (#167)

* Use target_link_libraries instead of ament_target_dependencies
  (#169)

* introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. (#162)

* Instrument client/service for end-to-end request/response tracking
  (#163)

* fix: "Failed to parse type hash" message was overly spammy (ros2-50)
  (#149)

* remove rmw_localhost_only_t. (#156)

* Make rmw_service_server_is_available return RMW_RET_INVALID_ARGUMENT
  (#150)

* Use rmw_namespace_validation_result_string() in rmw_create_node
  (#151)

* Make rmw_destroy_wait_set return RMW_RET_INVALID_ARGUMENT (#152)

* Contributors: Alejandro Hernández Cordero, Christophe Bedard,
  Francisco Gallego Salido, Scott K Logan, Shane Loretz, Taxo Rubio
  RTI, Tomoya Fujita

rmw_connextddsmicro
===================

* Mark the package rmw_connextddsmicro as deprecated (#182)

* Switch buildtool to ament_cmake package (#183)

* Added rmw_event_type_is_supported (#173)

* Contributors: Alejandro Hernández Cordero, Francisco Gallego Salido,
  Scott K Logan

rmw_cyclonedds_cpp
==================

* Switch to ament_cmake_ros_core package (#538)

* Added rmw_event_type_is_supported (#532)

* use rmw_enclave_options_xxx APIs instead. (#531)

* use rmw_security_common (#529)

* introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. (#518)

* Reset the error before setting a new one. (#526)

* Instrument client/service for end-to-end request/response tracking
  (#521)

* Drop support for float128. (#522)

* use RMW_GID_STORAGE_SIZE to client_service_id_t. (#515)

* remove rmw_localhost_only_t. (#508)

* Fix the triggering of guard conditions. (#504) When a guard
  condition goes active, we have to remember to increase the trig_idx
  so we look at the next trigger. Otherwise, we can get into
  situations where we skip a triggered member.

* Make rmw_service_server_is_available return RMW_RET_INVALID_ARGUMENT
  (#496)

* Use rmw_namespace_validation_result_string() in rmw_create_node
  (#497)

* Make rmw_destroy_wait_set return RMW_RET_INVALID_ARGUMENT (#498)

* Set received_timestamp to system_clock::now() in message_info (#491)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Erik Boasson, Joe Speed, Jose Tomas Lorente,
  Michael Orlov, Scott K Logan, Tomoya Fujita

rmw_dds_common
==============

* Deprecated security methods (#77)

* Contributors: Alejandro Hernández Cordero

rmw_fastrtps_cpp
================

* Address RHEL warnings and missing includes. (#819)

* Support topic instances (#753)

* Switch to ament_cmake_ros_core package (#818)

* Added rmw_event_type_is_supported (#809)

* use rmw_enclave_options_xxx APIs instead. (#808)

* Add deprecation warning for FASTRTPS_DEFAULT_PROFILES_FILE (#806)

* Export a modern CMake target (#805)

* Changes to build against Fast DDS 3.0 (#776)

* Fix some overwritten errors in rmw_fastrtps. (#799)

* Instrument client/service for end-to-end request/response tracking
  (#787)

* Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto,
  Chris Lalancette, Christophe Bedard, Miguel Company, Scott K Logan,
  Shane Loretz, Tomoya Fujita

rmw_fastrtps_dynamic_cpp
========================

* Address RHEL warnings and missing includes. (#819)

* Support topic instances (#753)

* Switch to ament_cmake_ros_core package (#818)

* Make rmw_fastrtps_dynamic_cpp export a modern CMake target (#814)

* Added rmw_event_type_is_supported (#809)

* use rmw_enclave_options_xxx APIs instead. (#808)

* Add deprecation warning for FASTRTPS_DEFAULT_PROFILES_FILE (#806)

* Changes to build against Fast DDS 3.0 (#776)

* Fix some overwritten errors in rmw_fastrtps. (#799)

* Instrument client/service for end-to-end request/response tracking
  (#787)

* Add tracing instrumentation to rmw_fastrtps_dynamic_cpp (#772)

* Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto,
  Chris Lalancette, Christophe Bedard, Miguel Company, Scott K Logan,
  Shane Loretz, Tomoya Fujita

rmw_fastrtps_shared_cpp
=======================

* Address RHEL warnings and missing includes. (#819)

* Support topic instances (#753)

* Switch to ament_cmake_ros_core package (#818)

* Added rmw_event_type_is_supported (#809)

* use rmw_enclave_options_xxx APIs instead. (#808)

* Add deprecation warning for FASTRTPS_DEFAULT_PROFILES_FILE (#806)

* Use rmw_security_common (#803)

* introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. (#785)

* Changes to build against Fast DDS 3.0 (#776)

* Cleanup one test in rmw_fastrtps_shared_cpp. (#794)

* Instrument client/service for end-to-end request/response tracking
  (#787)

* Drop support for float128. (#788)

* Keep reference to "DomainParticipantFactory" (#770)

* Use client's reader guid for service introspection event gid (#781)

* Revert "Unique Client GID for Service Introspectino Event. (#779)"
  (#780)

* Unique Client GID for Service Introspectino Event. (#779)

* remove rmw_localhost_only_t. (#773)

* Make rmw_service_server_is_available return RMW_RET_INVALID_ARGUMENT
  (#763)

* Use rmw_namespace_validation_result_string() in rmw_create_node
  (#765)

* Make rmw_destroy_wait_set return RMW_RET_INVALID_ARGUMENT (#766)

* Use unique mangled names when creating Content Filter Topics (#762)

* Add support for data representation (#756)

* Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto,
  Chris Lalancette, Christophe Bedard, Jorge J. Perez, Mario Domínguez
  López, Miguel Company, Scott K Logan, Tomoya Fujita

rmw_implementation
==================

* Added rmw_event_type_is_supported (#250)

* Make sure to find_package(rmw) in rmw_implementation. (#242)

* Add mechanism to disable workaround for dependency groups (#229)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Scott K
  Logan

rmw_implementation_cmake
========================

* update cmake version (#389)

* Contributors: Alejandro Hernández Cordero

rmw_security_common
===================

* Export rmw dependency (#400)

* Added rmw_security_common (#388)

* Contributors: Alejandro Hernández Cordero, yadunund

rmw_test_fixture
================

* Resolve windows warnings in rmw_test_fixture (#22)

* Add rmw_test_fixture for supporting RMW-isolated testing (#21)

* Contributors: Alejandro Hernández Cordero, Scott K Logan

rmw_test_fixture_implementation
===============================

* Don't set ROS_AUTOMATIC_DISCOVERY_RANGE in rmw_test_fixture (#33)

* Fix rmw_test_fixture DLL import on Windows (#32)

* Fix range for rmw_test_fixture_default port locking (#31)

* Stop loading RMW to load the test fixture (#30)

* Add 'default' rmw_test_fixture based on domain_coordinator (#26)

* Install run_rmw_isolated executable to lib subdirectory (#25)

* Ignore Ctrl-C in run_rmw_isolated on Windows (#24)

* Resolve windows warnings in rmw_test_fixture (#22)

* Add rmw_test_fixture for supporting RMW-isolated testing (#21)

* Contributors: Alejandro Hernández Cordero, Scott K Logan

rmw_zenoh_cpp
=============

* Change serialization format in attachment_helpers.cpp (#601)

* Bump Zenoh to v1.3.2 and improve e2e reliability with
  HeartbeatSporadic (#591)

* Implement rmw_test_fixture to start the Zenoh router (#583)

* Add quality declaration (#483)

* Trigger qos event callback if there are changes before registration
  (#587)

* Set wait_set->triggered flag to false (#575)

* Add space after "id" token in "rmw_zenohd" log string (#576)

* Use "std::unique_lock" to unlock correctly on Windows (#570)

* Switch to std::map for TopicTypeMap (#546)

* Support zenoh config override (#551)

* Align the config with the latest Zenoh. (#556)

* Added documentation note in the code (#540)

* fix: unlock the mutex before making get (#537)

* Take wait_set_lock before condition_variable notification for
  subscriptions (#528)

* Switch default durability to volatile (#521)

* Added rmw_event_type_is_supported (#502)

* Fixed windows warning (#500)

* Config: tune some values for ROS use case, especially with large
  number of Nodes (>200) (#509)

* Honor ignore_local_publications in subscription options (#508)

* Bump zenoh-cpp to 2a127bb, zenoh-c to 3540a3c, and zenoh to f735bf5
  (#503)

* Fix calculation of current_count_change when event status is updated
  (#504)

* Fix checks for invalid arguments (#497)

* Fail creation of entities if qos contains unknown settings (#494)

* use rmw_enclave_options_xxx APIs instead. (#491)

* Enable Zenoh UDP transport (#486)

* fix: use the default destructor that automatically drops the zenoh
  reply/query and hence sends the final signal (#473)

* Introduce the advanced publisher and subscriber (#368)

* Switch to debug log if topic_name not in topic_map (#454)

* Bump Zenoh to commit id 3bbf6af (1.2.1 + few commits) (#456)

* Bump Zenoh to commit id e4ea6f0 (1.2.0 + few commits) (#446)

* Inform users that peers will not discover and communicate with one
  another until the router is started (#440)

* Clear the error after rmw_serialized_message_resize() (#435)

* Fix "ZENOH_ROUTER_CHECK_ATTEMPTS" which was not respected (#427)

* fix: use the default destructor to drop the member "Payload" (#419)

* Remove "gid_hash\_" from "AttachmentData" (#416)

* Sync the config with the default config in Zenoh. (#396)

* fix: check the context validity before accessing the session (#403)

* Fix wan't typo (#400)

* An alternative middleware for ROS 2 based on Zenoh.

* Contributors: Alejandro Hernández Cordero, Alex Day, Bernd Pfrommer,
  ChenYing Kuo (CY), Chris Lalancette, Christophe Bedard,
  CihatAltiparmak, Esteve Fernandez, Franco Cipollone, Geoffrey Biggs,
  Hans-Martin, Hugal31, James Mount, Julien Enoch, Luca Cominardi,
  Mahmoud Mazouz, Morgan Quigley, Nate Koenig, Patrick Roncagliolo,
  Scott K Logan, Shivang Vijay, Tim Clephas, Tomoya Fujita, Yadunund,
  Yuyuan Yuan, methylDragon, yadunund, yellowhatter

robot_state_publisher
=====================

* Use "emplace()" with "std::map" (#231)

* Remove CODEOWNERS and mirror-rolling-to-main workflow (#229)

* update urdf model header (#223)

* Contributors: Alejandro Hernández Cordero, Patrick Roncagliolo

ros2action
==========

* Allow zenoh tests to run with multicast (#992)

* Support 'ros2 action echo' (#978)

* Correct the license content (#979)

* Maintaining consistency of automatically putting time stamps in the
  service and action calls similiar to publishing in rostopics. (#961)

* ros2action: add SIGINT handler to manage cancel request. (#956)

* node name print bug fix with ros2 action info. (#926)

* Switch to using rclpy.init context manager. (#918)

* support 'ros2 action find'. (#917)

* Contributors: Barry Xu, Chris Lalancette, Michael Carroll, Sukhvansh
  Jain, Tomoya Fujita

ros2bag
=======

* Add actions replay feature (#1955)

* Implement actions recording and displaying information about
  recorded actions features (#1939)

* Fix for failing test_record_qos_profiles on Windows (#1949)

* Progress bar for ros2 bag play (#1836)

* Update CLI play verb metavar (#1906)

* Add test_xmllint.py to python packages. (#1879)

* Add support for replaying based on publication timestamp (#1876)

* Publish clock after delay is over and disable delay on next loops
  (#1861)

* Support replaying multiple bags (#1848)

* Rename rclpy.qos.QoS*Policy to rclpy.qos.*Policy (#1832)

* Add "--sort" CLI option to the "ros2 bag info" command (#1804)

* Add cli option compression-threads-priority (#1768)

* Add computation of size contribution to info verb (#1726)

* fix(start-offset): allow specifying a start offset of 0 (#1682)

* Exclude recorded /clock topic when --clock option is specified
  (#1646)

* Sweep cleanup in rosbag2 recorder CLI args verification code (#1633)

* Add --log-level to ros2 bag play and record (#1625)

* Add optional '--topics' CLI argument for 'ros2 bag record' (#1632)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Christophe Bedard, Kosuke Takeuchi, Michael Orlov,
  Nicola Loi, Patrick Roncagliolo, Rein Appeldoorn, Roman, Sanoronas

ros2cli
=======

* Allow zenoh tests to run with multicast (#992)

* Rename the test_{daemon,direct}.py tests. (#959)

* replace removeprefix with string slicing. (#953)

* Fix instability in the ros2 daemon. (#947)

* Drop dependency on python3-pkg-resources (#946)

* NodeStrategy supports node name argument. (#941)

* Switch to using the rclpy.init context manager. (#920)

* Contributors: Chris Lalancette, Michael Carroll, Scott K Logan,
  Tomoya Fujita

ros2doctor
==========

* Allow zenoh tests to run with multicast (#992)

* Skip QoS compatibility test on Zenoh (#985)

* New flag and code update for its use (#942)

* Switch to using rclpy.init context manager. (#918)

* Revamp how we get network information in ros2doctor. (#910)

* Contributors: Alejandro Hernández Cordero, Angel LoGa, Chris
  Lalancette, Michael Carroll

ros2launch
==========

* Add ament_xmllint to the ament_python packages. (#423)

* Fix url in setup.py (#413)

* Add mechanism to disable workaround for dependency groups (#397)

* Contributors: Chris Lalancette, Scott K Logan, Wei HU

ros2lifecycle
=============

* Allow zenoh tests to run with multicast (#992)

* Contributors: Michael Carroll

ros2lifecycle_test_fixtures
===========================

* Use target_link_libraries instead of ament_target_dependencies
  (#973)

* Contributors: Shane Loretz

ros2node
========

* Allow zenoh tests to run with multicast (#992)

* ros2node requires fully qualified node name. (#923)

* Switch to using rclpy.init context manager. (#918)

* Contributors: Chris Lalancette, Michael Carroll, Tomoya Fujita

ros2param
=========

* Fix loading parameter behavior from yaml file (#864)

* Allow zenoh tests to run with multicast (#992)

* cosmetic fixes for ros2param dump command. (#933)

* Switch to using rclpy.init context manager. (#918)

* Contributors: Chris Lalancette, Michael Carroll, Tomoya Fujita

ros2pkg
=======

* Use modern C++17 syntax. (#982)

* Use target_link_libraries instead of ament_target_dependencies
  (#973)

* Try to use the git global user.name for maintainer-name (#968)
