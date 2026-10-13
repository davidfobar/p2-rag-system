# Jazzy Jalisco changelog (part 3 of 5)

* fix doxygen syntax for NodeInterfaces (#2428)

* Set hints to find the python version we actually want. (#2426) The
  comment in the commit explains the reasoning behind it.

* Update quality declaration documents (#2427)

* feat: add/minus for msg::Time and rclcpp::Duration (#2419) * feat:
  add/minus for msg::Time and rclcpp::Duration

* Split test_executors up into smaller chunks. (#2421)

* [events executor] - Fix Behavior with Timer Cancel (#2375)

* Removed deprecated header (#2413)

* Make sure to mark RingBuffer methods as 'override'. (#2410)

* Increase the cppcheck timeout to 600 seconds. (#2409)

* Add transient local durability support to publisher and
  subscriptions when using intra-process communication (#2303)

* Stop storing the context in the guard condition. (#2400)

* Updated GenericSubscription to AnySubscriptionCallback (#1928)

* make type support helper supported for service (#2209)

* Adding QoS to subscription options (#2323)

* Switch to target_link_libraries. (#2374)

* aligh with rcl that a rosout publisher of a node might not exist
  (#2357)

* Fix data race in EventHandlerBase (#2349)

* Support users holding onto shared pointers in the message memory
  pool (#2336)

* fix (signal_handler.hpp): spelling (#2356)

* Updates to not use std::move in some places. (#2353)

* rclcpp::Time::max() clock type support. (#2352)

* Serialized Messages with Topic Statistics (#2274)

* Add a custom deleter when constructing rcl_service_t (#2351)

* Disable the loaned messages inside the executor. (#2335)

* Use message_info in SubscriptionTopicStatistics instead of typed
  message (#2337)

* Add missing 'enable_rosout' comments (#2345)

* Adjust rclcpp usage of type description service (#2344)

* address rate related flaky tests. (#2329)

* Fixes pointed out by the clang analyzer. (#2339)

* Remove useless ROSRate class (#2326)

* add clients & services count (#2072)

* remove invalid sized allocation test for SerializedMessage. (#2330)

* Adding API to copy all parameters from one node to another (#2304)

* Add locking to protect the TimeSource::NodeState::node_base_ (#2320)

* Update SignalHandler get_global_signal_handler to avoid complex
  types in static memory (#2316)

* Removing Old Connext Tests (#2313)

* Documentation for list_parameters (#2315)

* Decouple rosout publisher init from node init. (#2174)

* fix the depth to relative in list_parameters (#2300)

* Fix the return type of Rate::period. (#2301)

* Update API docs links in package READMEs (#2302)

* Cleanup flaky timers_manager tests. (#2299)

* Topic correct typeadapter deduction (#2294)

* Fix C++20 allocator construct deprecation (#2292)

* Make Rate to select the clock to work with (#2123)

* Correct the position of a comment. (#2290)

* Remove unnecessary lambda captures in the tests. (#2289)

* Add rcl_logging_interface as an explicit dependency. (#2284)

* Revamp list_parameters to be more efficient and easier to read.
  (#2282)

* Do not crash Executor when send_response fails due to client
  failure. (#2276)

* Adding Custom Unknown Type Error (#2272)

* Add a pimpl inside rclcpp::Node for future distro backports (#2228)

* Remove an unused variable from the events executor tests. (#2270)

* Add spin_all shortcut (#2246)

* Adding Missing Group Exceptions (#2256)

* Change associated clocks storage to unordered_set (#2257)

* associated clocks should be protected by mutex. (#2255)

* Instrument loaned message publication code path (#2240)

* Implement get_node_type_descriptions_interface for lifecyclenode and
  add smoke test for it (#2237)

* Add new node interface TypeDescriptionsInterface to provide
  GetTypeDescription service (#2224)

* Move always_false_v to detail namespace (#2232)

* Revamp the test_subscription.cpp tests. (#2227)

* warning: comparison of integer expressions of different signedness
  (#2219)

* Modifies timers API to select autostart state (#2005)

* Enable callback group tests for connextdds (#2182)

* Fix up misspellings of "receive". (#2208)

* Remove flaky stressAddRemoveNode test (#2206)

* Use TRACETOOLS_ prefix for tracepoint-related macros (#2162)

* remove nolint since ament_cpplint updated for the c++17 header
  (#2198)

* Feature/available capacity of ipm (#2173)

* add mutex to protect events_executor current entity collection
  (#2187)

* Declare rclcpp callbacks before the rcl entities (#2024)

* Fix race condition in events-executor (#2177)

* Add missing stdexcept include (#2186)

* Fix a format-security warning when building with clang (#2171)

* Fix delivered message kind (#2175)

* Contributors: AiVerisimilitude, Alberto Soragna, Alejandro Hernández
  Cordero, Alexey Merzlyakov, Barry Xu, Chen Lihui, Chris Lalancette,
  Christophe Bedard, Christopher Wecht, DensoADAS, Eloy Briceno,
  Emerson Knapp, Homalozoa X, HuaTsai, Jeffery Hsu, Jiaqi Li, Jonas
  Otto, Kotaro Yoshimoto, Lee, Luca Della Vedova, Lucas Wendland, Matt
  Condino, Michael Carroll, Michael Orlov, Minju, Nathan Wiebe
  Neufeldt, Steve Macenski, Tim Clephas, Tomoya Fujita, Tony Najjar,
  Tully Foote, William Woodall, Zard-C, h-suzuki-isp, jmachowinski,
  mauropasse, mergify[bot], methylDragon, Øystein Sture

rclcpp_action
=============

* Remove references to index.ros.org. (#2504)

* Callback after cancel (#2281) * feat(Client): Added function to stop
  callbacks of a goal handle This function allows us to drop the
  handle in a locked context. If we do not do this within a lock,
  there will be a race condition between the deletion of the
  shared_ptr of the handle and the result / feedback callbacks. * fix:
  make Client goal handle recursive This fixes deadlocks due to
  release of goal handles in callbacks etc. * fix(ActionGoalClient):
  Fixed memory leak for nominal case This fixes a memory leak due to a
  self reference in the ClientGoalHandle. Note, this fix will only
  work, if the ClientGoalHandle ever receives a result callback. *
  doc: Updated documentation of rclcpp_action::Client::async_send_goal
  * docs: Made the async_send_goal documentation more explicit Co-
  authored-by: Janosch Machowinski <J.Machowinski@cellumation.com>

* Remake of "fix: Fixed race condition in action server between
  is_ready and take" (#2495) Some background information: is_ready,
  take_data and execute data may be called from different threads in
  any order. The code in the old state expected them to be called in
  series, without interruption. This lead to multiple race conditions,
  as the state of the pimpl objects was altered by the three functions
  in a non thread safe way. Co-authored-by: Janosch Machowinski
  <j.machowinski@nospam.org>

* update rclcpp::Waitable API to use references and const (#2467)

* Do not generate the exception when action service response timeout.
  (#2464) * Do not generate the exception when action service response
  timeout. * address review comment. ---------

* Modify rclcpp_action::GoalUUID hashing algorithm (#2441) * Add unit
  tests for hashing rclcpp_action::GoalUUID's * Use the FNV-1a hash
  algorithm for Goal UUID

* Various cleanups to deal with uncrustify 0.78. (#2439) These should
  also work with uncrustify 0.72.

* Update quality declaration documents (#2427)

* Switch to target_link_libraries. (#2374)

* Update API docs links in package READMEs (#2302)

* fix(ClientGoalHandle): Made mutex recursive to prevent deadlocks
  (#2267)

* Correct the position of a comment. (#2290)

* Fix a typo in a comment. (#2283)

* doc fix: call "canceled" only after goal state is in canceling.
  (#2266)

* Contributors: Chris Lalancette, Christophe Bedard, Jiaqi Li, Tomoya
  Fujita, William Woodall, jmachowinski, mauropasse

rclcpp_components
=================

* Remove references to index.ros.org. (#2504)

* Add EXECUTOR docs (#2440)

* Update quality declaration documents (#2427)

* crash on no class found (#2415) * crash on no class found * error on
  no class found instead of no callback groups Co-authored-by: Chris
  Lalancette <clalancette@gmail.com>

* Switch to target_link_libraries. (#2374)

* feat(rclcpp_components): support events executor in node main
  template (#2366)

* fix(rclcpp_components): increase the service queue sizes in
  component_container (#2363)

* Add missing header required by the rclcpp::NodeOptions type (#2324)

* Update API docs links in package READMEs (#2302)

* Contributors: Adam Aposhian, Chris Lalancette, Christophe Bedard,
  Daisuke Nishimatsu, Ignacio Vizzo, M. Fatih Cırıt, Ruddick Lawrence

rclcpp_lifecycle
================

* Revert "call shutdown in LifecycleNode dtor to avoid leaving the
  device in un… (#2450)" (#2522) (#2524) This reverts commit
  04ea0bb00293387791522590b7347a2282cda290. (cherry picked from commit
  42b0b5775b4e68718c5949308c9e1a059930ded7) Co-authored-by: Chris
  Lalancette <clalancette@gmail.com>

* Remove references to index.ros.org. (#2504)

* call shutdown in LifecycleNode dtor to avoid leaving the device in
  un… (#2450) * call shutdown in LifecycleNode dtor to avoid leaving
  the device in unknown state. * add test to verify
  LifecycleNode::shutdown is called on destructor. ---------

* Update quality declaration documents (#2427)

* Increase timeout for rclcpp_lifecycle to 360 (#2395)

* Fix rclcpp_lifecycle inclusion on Windows. (#2331)

* add clients & services count (#2072)

* Update API docs links in package READMEs (#2302)

* add logger level service to lifecycle node. (#2277)

* Stop using constref signature of benchmark DoNotOptimize. (#2238)

* Implement get_node_type_descriptions_interface for lifecyclenode and
  add smoke test for it (#2237)

* Switch lifecycle to use the RCLCPP macros. (#2233)

* Add new node interface TypeDescriptionsInterface to provide
  GetTypeDescription service (#2224)

* Contributors: Chris Lalancette, Christophe Bedard, Emerson Knapp,
  Jorge Perez, Lee, Minju, Tomoya Fujita, mergify[bot]

rclpy
=====

* Clock.py types. (#1244) * Start typing time.py * Testing out Enum
  wrapper for ClockType * convert to rcl_clock_type_t * Update
  create_time_point * add types to logging_service * Add types to
  duration.py * Add newlines for class definintions * update type
  alias name * Update to use Protocols * Add types to time.py * Add
  types * Fix import order * Started typing clock.py * Move typealias
  import

* pybind11 definition doc typo fixes. (#1270)

* Fix small flake8 error in rclpy. (#1267) Newer versions of flake8
  complain that using 'str' as a variable shadows a builtin. Just
  make it 's'.

* Allow specifying qos (#1225)

* update RCL_RET_TIMEOUT error handling with action service response.
  (#1258)

* Add types to time_source.py (#1259)

* Small fixes for modern flake8. (#1264)

* Add types to qos_overriding_options.py (#1248)

* Add types to context.py (#1240)

* Add back Type hash __slots__ and add test cases. (#1245)

* Revert "Add types to TypeHash and moved away from __slots__ usage
  (#1232)" (#1243)

* Time.py Types (#1237)

* Add types to TypeHash and moved away from __slots__ usage (#1232)

* Add Static Typing to Validate files (#1230)

* Add types to duration.py (#1233)

* added python3-yaml (#1242)

* Add types to exceptions.py (#1241)

* Add types (#1231)

* Creates Enum wrapper for ClockType and ClockChange (#1235)

* Add types to expand_topic_name (#1238)

* Add types to logging_service.py (#1227)

* Add types to logging.py (#1226)

* forbid parameter to be declared statically without initialization.
  (#1216)

* Remove parentheses from assert statements. (#1213)

* Add doc-string warnings for destroy methods for services. (#1205)

* Add doc-string warnings for destroy() methods (#1204)

* Add an optional timeout_sec input to Client.call() to fix issue
  https://github.com/ros2/rclpy/issues/1181 (#1188)

* aligh with rcl that a rosout publisher of a node might not exist
  (#1196)

* call ok() to see if rclpy and context is initialized. (#1198)

* Adjust python usage of the type_description service API (#1192)

* Document that spin_once() should not be called from multiple threads
  (#1079)

* making optional things Optional (#1182)

* Use timeout object to avoid callback losing in
  wait_for_ready_callbacks (#1165)

* Fix to issue https://github.com/ros2/rclpy/issues/1179 (#1180)

* Add count services, clients & test (#1024)

* 1105 parameter event handler (#1135)

* unregister_sigterm_signal_handler should be called. (#1170)

* Handle take failure in wait_for_message (#1172)

* Decouple rosout publisher init from node init. (#1121)

* Fix _list_parameters_callback & test (#1161)

* add list_parameters & test (#1124)

* Support to get remapped service name (#1156)

* a couple of typo fixes. (#1158)

* Fix get_type_description service bug and add a unit test (#1155)

* Fix an inherent race in execution vs. destruction. (#1150)

* Cleanup of test_node.py. (#1153)

* Avoid generating the exception when rcl_send_response times out.
  (#1136)

* Store time source clocks in a set (#1146)

* Fix spin_once_until_future_complete to quit when the future
  finishes. (#1143)

* get_type_description service (#1139)

* Add in the ability to start timers paused. (#1138)

* Modifies ros_timer_init for ros_timer_init2 (#999)

* Fix/param namespace association 894 (#1132)

* Include type hash in topic endpoint info (#1104)

* Fix iteration over modified list (#1129)

* making optional things Optional (#974)

* Fix type signature of Client.wait_for_service (#1128)

* Fix action server crash when the client goes away. (#1114)

* Turn Executor into a ContextManager (#1118)

* Turn Context into a ContextManager (#1117)

* Fix type in Node init args (#1115)

* Contributors: AndyZe, Anton Kesy, Barry Xu, Brian, Chen Lihui, Chris
  Lalancette, Eloy Briceno, Emerson Knapp, EsipovPA, Felix Divo, Hans-
  Joachim Krauch, KKSTB, Lee, Luca Della Vedova, M. Hofstätter,
  Michael Carlstrom, Michael Carroll, Minju, Russ, SnIcK, Steve
  Peters, Tim Clephas, Tomoya Fujita, mhidalgo-bdai

rcpputils
=========

* Generate version header with ament_generate_version_header function
  (#190)

* Update docs for rcpputils::split functions (#188)

* Included tl_expected (#185)

* Switch to using target_link_libraries. (#183)

* Add a missing header due to missing PATH_MAX variable (#181)

* Add unique_lock implementation with clang thread safety annotations
  (#180)

* Add in a missing cstdint. (#178)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard, Emerson Knapp, Sai Kishor Kothakota,
  wojciechmadry

rcutils
=======

* Removed warnings - strict-prototypes (#461) (#465)

* Increase timeout repl_str test (#463) (#464)

* validate the allocator before use. (#455) * validate the allocator
  before use. * address review comments. - validate allocator only if
  the function specifically uses. - argument null check comes before
  validation of value. ---------

* feat: Add human readable date to logging formats (#441)

* Updates for uncrustify 0.78. (#454)

* Set hints to find the python version we actually want. (#451)

* Bring ament_add_gtest/target_link_libraries back together (#452)

* Change 'ROS2' to 'ROS 2' in quality declaration (#453)

* Allow parsing of escape sequence in log format (#443)

* Clean up unused references to mimick/mocking in tests (#450)

* Fix if(TARGET ...) condition for test (#447)

* Zero-initialize rcutils_string_array_t in test_string_array (#446)

* Use rcutils_string_array_init in rcutils_split & handle alloc fail
  (#445)

* Make rcutils_split() return RCUTILS_RET_BAD_ALLOC if alloc fails
  (#444)

* Remove two last uses of ament_target_dependencies. (#440)

* time_win32: Update dead link (#438)

* memmove for overlaping memory (#434)

* make escape characters work (#426)

* Remove unused 'max' functions from sha256.c (#429)

* Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Kaju-
  Bubanja, Marc Bestmann, Silvio Traversaro, Tomoya Fujita, Tyler
  Weaver, mergify[bot]

resource_retriever
==================

* Update resource retreiver to use rule of five (#95)

* Use default ament_lint_auto (#92)

* Switch to target_link_libraries. (#89)

* Update to C++17 (#88)

* Contributors: Chris Lalancette, Michael Carroll

rmw
===

* Removed warnings - strict-prototypes (#365) (#366)

* Switch to target_link_libraries. (#361)

* Remove unnecessary c++14 flag. (#360)

* definition of local means being in the same context. (#359)

* typo fix. (#355)

* Contributors: Chris Lalancette, Tomoya Fujita, mergify[bot]

rmw_connextdds
==============

* Add rmw count clients services impl (#93)

* Cleanup context implementation (#131)

* Update to C++17 (#125)

* Contributors: Chris Lalancette, Lee, Minju

rmw_connextdds_common
=====================

* Revert "Mitigate discovery race condition between clients and
  services (#132)" (#146) This reverts commit
  7c95abbfc4559b293ebf5e94e20250bdd99d3ac6.

* Mitigate discovery race condition between clients and services
  (#132) * Mitigate discovery race condition between clients and
  services.

* Add: tracepoint for subscribe serialized_message (#145) * Add:
  tracepoint for take_serialized_message * Fix: TRACETOOLS_TRACEPOINT
  args * Update rmw_connextdds_common/src/common/rmw_subscription.cpp
  Co-authored-by: Christophe Bedard <bedard.christophe@gmail.com>

* Support Fast CDR v2 (#141)

* Fix the rmw_connextdds_common build with gcc 13.2. (#142) The most
  important fix here is to #include <cstdint>, but also make sure we
  #include for all used STL functions.

* Fix basic request reply mapping for ConnextDDS Pro (#139)

* Add ros2_tracing tracepoints (#120)

* avoid using dds common public mutex directly (#134)

* Fix a couple of warnings pointed out by clang. (#133)

* Add rmw count clients services impl (#93)

* Conditional internal API access to support Connext 7+ (#121)

* Cleanup context implementation (#131)

* Fix RMW_Connext_Client::is_service_available for micro (#130)

* Update to C++17 (#125)

* Pass parameters in the correct order to DDS_DataReader_read in
  rmw_connextdds_count_unread_samples for micro (#129)

* Optimize QoS to improve responsiveness of reliable endpoints (#26)

* Clear out errors once we have handled them. (#126)

* Add support for listener callbacks (#76)

* Contributors: Andrea Sorbini, Chen Lihui, Chris Lalancette,
  Christopher Wecht, Lee, Miguel Company, Minju, h-suzuki-isp

rmw_connextddsmicro
===================

* Add rmw count clients services impl (#93)

* Cleanup context implementation (#131)

* Update to C++17 (#125)

* Contributors: Chris Lalancette, Lee, Minju

rmw_cyclonedds_cpp
==================

* Set received_timestamp to system_clock::now() in message_info (#491)
  (#493) * Set received_timestamp to steady_clock::now() in
  message_info * Use 'system_clock' instead of 'steady_clock' * Also
  update receive_timestamp for services. (cherry picked from commit
  76c9d8f38a03d160b258902af6d1d06f6ed9391e) Co-authored-by: Michael
  Orlov <morlovmr@gmail.com>

* Add tracepoint for publish/subscribe serialized message (#485) Co-
  authored-by: eboasson <eb@ilities.com>

* Remove a bunch of unnecessary macros. (#482)

* compare string contents but string pointer addresses. (#481)

* Add timestamp to rmw_publish tracepoint (#454)

* avoid using dds common public mutex directly (#474)

* Add rmw count clients,services impl (#427)

* Minor revamp of the CMakeLists.txt. (#468)

* Clear out errors once we have handled them. (#464)

* Instrument loaned message publication code path

* Use TRACETOOLS_ prefix for tracepoint-related macros (#450)

* Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard,
  Christopher Wecht, Lee, Minju, Tomoya Fujita, h-suzuki-isp,
  mergify[bot]

rmw_dds_common
==============

* Add pkcs11 support to get_security_files (#66)

* make a new private mutex and add updating graph methods (#73)

* Just remove rcpputils::fs dependency (#72)

* Contributors: Chen Lihui, Kenta Yonekura, Miguel Company

rmw_fastrtps_cpp
================

* Support Fast CDR v2 (#746) * Require fastcdr version 2 * Changes to
  build rmw_fastrtps_shared_cpp * Changes to build rmw_fastrtps_cpp *
  Changes to build rmw_fastrtps_dynamic_cpp

* Capture "std::bad_alloc" on deserializeROSmessage. (#665)

* Switch to target_link_libraries for linking. (#734)

* avoid using dds common public mutex directly (#725)

* Add rmw_count clients,services impl (#641)

* Improve node graph delivery by using a unique listening port (#711)

* Use TRACETOOLS_ prefix for tracepoint-related macros (#686)

* Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Lee,
  Miguel Company, Minju

rmw_fastrtps_dynamic_cpp
========================

* Support Fast CDR v2 (#746) * Require fastcdr version 2 * Changes to
  build rmw_fastrtps_shared_cpp * Changes to build rmw_fastrtps_cpp *
  Changes to build rmw_fastrtps_dynamic_cpp

* compare string contents but string pointer addresses. (#744)

* Improve wide string (de)serialization in rwm_dynamic_fastrtps_cpp
  (#740) * Move type support headers to src * Fix references to moved
  headers * move macros.hpp to src/serialization_helpers.hpp * Move
  other non-api headers * Move common code into serialize_wide_string.
  * Move common code into deserialize_wide_string. * Move
  serialization into serialization_helpers.hpp * Move deserialization
  into serialization_helpers.hpp * Fix header guards * Linters * Do
  not account for extra character on serialized size calculation *
  Remove dependency on rosidl_typesupport_fastrtps_c(pp) ---------

* Capture "std::bad_alloc" on deserializeROSmessage. (#665)

* Switch to target_link_libraries for linking. (#734)

* avoid using dds common public mutex directly (#725)

* Account for alignment on is_plain calculations. (#716)

* Add rmw_count clients,services impl (#641)

* Improve node graph delivery by using a unique listening port (#711)

* Contributors: Chen Lihui, Chris Lalancette, Lee, Miguel Company,
  Minju, Tomoya Fujita

rmw_fastrtps_shared_cpp
=======================

* Allow pkcs11 when calling rmw_dds_common::get_security_files. (#565)
  Co-authored-by: Miguel Company <MiguelCompany@eprosima.com>

* Add tracepoint for publish/subscribe serialized_message (#748) *
  Add: tracepoint for generic pub/sub * Fix: correspond to PR 454 *
  Fix: change write to write_to_timestamp ---------

* Support Fast CDR v2 (#746) * Require fastcdr version 2 * Changes to
  build rmw_fastrtps_shared_cpp * Changes to build rmw_fastrtps_cpp *
  Changes to build rmw_fastrtps_dynamic_cpp

* Remove an unnecessary constructor. (#743) We can just use brace
  initialization here, and this allows us to side-step an uncrustify
  issue with the constructor.

* Add timestamp to rmw_publish tracepoint (#694)

* Switch to Unix line endings. (#736)

* Switch to target_link_libraries for linking. (#734)

* Quiet compiler warning in Release mode. (#730)

* avoid using dds common public mutex directly (#725)

* Add rmw_count clients,services impl (#641)

* Switch to using rclcpp::unique_lock. (#712)

* Use DataWriter Qos to configure max_blocking_time on
  rmw_send_response (#704)

* Clear out errors once we have handled them. (#701)

* Instrument loaned message publication code path (#698)

* Add in a missing data_reader check when creating subscription.
  (#697)

* Use TRACETOOLS_ prefix for tracepoint-related macros (#686)

* typo fix. (#693)

* address clang nightly build error. (#689)

* Check for errors while doing an rmw_discovery_options_copy. (#690)

* Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard,
  Christopher Wecht, IkerLuengo, Lee, Miguel Company, Minju, Tomoya
  Fujita, h-suzuki-isp

rmw_implementation
==================

* Update quality declaration document (#225) (#226)

* Switch to using target_link_libraries everywhere. (#222)

* Add rmw_count_clients,services & test (#208)

* Contributors: Chris Lalancette, Lee, Minju, mergify[bot]

robot_state_publisher
=====================

* Fix reload after a description with a mimic joint (#212)

* Remove ament_target_dependencies. (#209)

* Improve log messages (#206)

* Contributors: Chris Lalancette, Guillaume Doisy, Nick Lamprianidis

ros2action
==========

* call get_action_interfaces() properly. (#898) (#900) (cherry picked
  from commit 305ef763b83e42ebddc4802ac788869d178b6e93) Co-authored-
  by: Tomoya Fujita <Tomoya.Fujita@sony.com>

* support "ros2 action type <action name>". (#894) * support "ros2
  action type <action name>". * add review comments. ---------

* Load a message/request/goal from standard input (#844)

* Contributors: Tomoya Fujita, mergify[bot], ymd-stella

ros2bag
=======

* Add option to disable recorder keyboard controls (#1607)

* Support service 2/2 --- rosbag2 service play (#1481)

* Added exclude-topic-types to record (#1582)

* Overhaul in the rosbag2_transport::TopicFilter class and relevant
  tests (#1585)

* Filter topic by type (#1577)

* Implement service recording and display info about recorded services
  (#1480)

* Add python3-yaml as a dependency (#1490)

* Fix the description of paramter '--topics' for play (#1426)

* When using sim time, wait for /clock before beginning recording
  (#1378)

* Revert "Don't record sim-time messages before first /clock (#1354)"
  (#1377)

* Don't record sim-time messages before first /clock (#1354)

* Fix wrong descritpion for '--ignore-leaf-topics' (#1344)

* Cleanup the help text for ros2 bag record. (#1329)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Bernd Pfrommer,
  Chris Lalancette, Emerson Knapp, Michael Orlov, Michal Sojka

ros2cli
=======

* ros2cli.node.daemon : try getting fdsize from /proc for open fd
  limit (#888)

* Fix the SIGTERM handling in the ros2 daemon. (#887)

* Replace unmaintained "netifaces" library to avoid local wheel builds
  (#875)

* make handles not inheritable to prevent from blocking durning tab-
  completion (#852)

* Add ros2 service info (#771)

* catch ExternalShutdownException ros2cli main. (#854)

* Load a message/request/goal from standard input (#844)

* Fix tests with get_type_description service and param present (#838)

* Add marshalling functions for rclpy.type_hash.TypeHash (rep2011)
  (#816)

* [service introspection] ros2 service echo (#745)

* Contributors: Brian, Chen Lihui, Chris Lalancette, Emerson Knapp,
  Hans-Joachim Krauch, Laurenz, Lee, Minju, Tomoya Fujita, akssri-
  sony, ymd-stella

ros2cli_test_interfaces
=======================

* Update to C++17 (#848)

* Contributors: Chris Lalancette

ros2component
=============

* Warning: get_parameter_value() is deprecated. (#866)

* Contributors: Tomoya Fujita

ros2doctor
==========

* Remove references to https://index.ros.org (#897)

* (ros2doctor) fix PackageCheck (#860) * (ros2doctor)(package) improve
  result string generation

* Shutdown ros2doctor hello when ctrl-c is received (#826)

* Contributors: Chris Lalancette, Matthijs van der Burgh, Michael
  Carroll

ros2interface
=============

* Add interface type filters to ros2 interface package (#765)

* Contributors: David V. Lu!!

ros2param
=========

* ros2 param dump should handle empty list as exception. (#881)

* Warning: get_parameter_value() is deprecated. (#866)

* Fix tests with get_type_description service and param present (#838)

* Update ros2 param dump dosctring. (#837)

* Contributors: Emerson Knapp, Murilo M Marinho, Tomoya Fujita

ros2pkg
=======

* Update the package template for our new include directories. (#847)

* Fix typo in ros2pkg warning message. (#827)

* Contributors: Chris Lalancette, Tomoya Fujita

ros2service
===========

* Add ros2 service info (#771)

* Load a message/request/goal from standard input (#844)

* Fix tests with get_type_description service and param present (#838)

* [service introspection] ros2 service echo (#745)

* Contributors: Brian, Emerson Knapp, Lee, Minju, ymd-stella

ros2topic
=========

* Remove parentheses from assert statement. (#878)

* Load a message/request/goal from standard input (#844)

* Add marshalling functions for rclpy.type_hash.TypeHash (rep2011)
  (#816)

* [service introspection] ros2 service echo (#745)

* Contributors: Brian, Chris Lalancette, Hans-Joachim Krauch, ymd-
  stella

ros2trace
=========

* Replace all occurences of index.ros.org (#114)

* Create start/pause/resume/stop sub-commands for 'ros2 trace' (#70)

* Switch <depend> to <exec_depend> in pure Python packages (#67)

* Contributors: Chris Lalancette, Christophe Bedard

rosbag2_compression
===================

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Use std::filesystem instead of rcpputils::fs (#1576)

* Make some changes for newer versions of uncrustify. (#1578)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Add default initialization for CompressionOptions (#1539)

* Add option to set compression threads priority (#1457)

* Fixes pointed out by clang. (#1493)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* Add in a missing cstdint include. (#1321)

* Fix warning from ClassLoader in sequential compression reader and
  writer (#1299)

* Contributors: Arne B, Chris Lalancette, Michael Orlov, Patrick
  Roncagliolo, Roman Sokolkov, jmachowinski
