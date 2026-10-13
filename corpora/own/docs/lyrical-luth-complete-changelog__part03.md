# ROS 2 Lyrical Luth Complete Changelog (part 3 of 6)

* Fix REP url locations (#2987)

* clear handles before node destruction in test_memory_strategy.
  (#2969)

* Added static assert asserting custom types have no overloaded
  operator new (#2954)

* Store graph listener inside the context instead of the node graph
  (#2952)

* Reapply "Catch the exception from rate.sleep() if the context is
  invalid. (#2956)" (#2963) (#2964)

* Revert "Catch the exception from rate.sleep() if the context is
  invalid. (#2956)" (#2963)

* Catch the exception from rate.sleep() if the context is invalid.
  (#2956)

* update Time documentation (#2955)

* Removed warning (#2949)

* add note about problems with spin_until_future_complete (#2849)

* deprecate rclcpp::spin_some and rclcpp::spin_all (#2848)

* Improve the function extract_type_identifier (#2923)

* Allow for implicitly convertable loggers as well (#2922)

* Fix: improve exception context for parameter_value_from (#2917)

* Fix "start_type_description_service" param handling (#2897)

* Add qos parameter for wait_for_message function (#2903)

* Fujitatomoya/test append parameter override (#2896)

* Expose "typesupport_helpers" API needed for the Rosbag2 (#2858)

* Remove comment about now-removed StaticSingleThreadedExecutor
  (#2893)

* Add overload of "append_parameter_override" (#2891)

* fix: Don't deadlock if removing shutdown callbacks in a shutdown
  callback (#2886)

* Hand-code logging.hpp (#2870)

* Adressed TODO in node_graph (#2877)

* fix test_publisher_with_system_default_qos. (#2881)

* Fix for memory leaks in rclcpp::SerializedMessage (#2861)

* Removed warning test_qos (#2859)

* Added missing chrono includes (#2854)

* get_all_data_impl() does not handle null pointers properly, causing
  segmentation fault (#2840)

* QoSInitialization::from_rmw does not validate invalid history policy
  values, leading to silent failures (#2841)

* remove get_notify_guard_condition from NodeBaseInterface. (#2839)

* Removed deprecated StaticSingleThreadedExecutor (#2835)

* Removed deprecated rcpputils Path (#2834)

* Add range constraints for applicable array parameters (#2828)

* Update RingBufferImplementation to clear internal data. (#2837)

* Removed deprecated cancel_sleep_or_wait (#2836)

* Add missing 's' to 'NodeParametersInterface' in doc/comment (#2831)

* subordinate node consistent behavior and update docstring. (#2822)

* throws std::invalid_argument if ParameterEvent is NULL. (#2814)

* Removed clang warnings (#2823)

* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Alex
  Youngs, Alexis Tsogias, Andrianov Roman, Barry Xu, CY Chen, Chris
  Lalancette, Christophe Bedard, Danil, Emerson Knapp, Ilario A.
  Azzollini, Ivo Ivanov, Janosch Machowinski, Julien Enoch, Lee, Lucas
  Wendland, Maurice Alexander Purnawan, Michael Carlstrom, Michael
  Carroll, Michael Orlov, Michiel Leegwater, Minju, Oren Bell, Patrick
  Roncagliolo, Peng Wang, Rahat Dhande, Skyler Medeiros, Sriharsha
  Ghanta, Tim Clephas, Tomoya Fujita, Yadnyeshwar Amol Sakhare,
  Yuchen966, fabianhirmann, jay, yadunund

rclcpp_action
=============

* publish_feedback should effect only on executing state. (#3118)

* Support to configure feedback subscription content filter for action
  client (#3034)

* Use new ROSIDL aggregate CMake target (#3105)

* Fix expiration of action goals when EventsExecutors are used (#3018)

* perf: Optimized out shared_ptr copies (#3079)

* remove default: so that compiler can detect the missing case.
  (#3048)

* Update exception documentation for goal cancellation in
  ServerGoalHandle (#3019)

* Fix REP url locations (#2987)

* it misses the iterator second to lock the weakptr. (#2958)

* try aborting before canceling 1st on dtor of ServerGoalHandle.
  (#2953)

* deprecate rclcpp::spin_some and rclcpp::spin_all (#2848)

* fix cmake deprecation (#2914)

* Replace std::default_random_engine with std::mt19937 (rolling)
  (#2843)

* Added missing chrono includes (#2854)

* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Andrei
  Costinescu, Barry Xu, Emerson Knapp, Janosch Machowinski, Skyler
  Medeiros, Tim Clephas, Tomoya Fujita, keeponoiro, mosfet80

rclcpp_components
=================

* Refactor component containers + Add option for CBG Executor (#3134)

* feat: Add per-node log level support via NodeOptions (#3092)

* Use new ROSIDL aggregate CMake target (#3105)

* Avoid unecessary creation of MultiThreadedExecutor (#3090)

* Fix component registering in subdirectories (#3064)

* Add library dependency to node executable in
  rclcpp_components_register_node (#3047)

* Updated deprecated ament_index_cpp API (#3011)

* Fix REP url locations (#2987)

* Cleanup the dependencies in rclcpp_components. (#2918)

* fix cmake deprecation (#2914)

* NEW PR: Add component_container for EventsExecutor (#2885)

* make sure that plugin arg includes the double colon. (#2878)

* set thread names by node in component container isolated (#2871)

* Added missing chrono includes (#2854)

* Contributors: Adam Aposhian, Alejandro Hernández Cordero, Chris
  Lalancette, Emerson Knapp, Mihir Rao, Peng Wang, Skyler Medeiros,
  Tim Clephas, Tomoya Fujita, YuJin Hong, mosfet80, pum1k, solo

rclcpp_lifecycle
================

* Use new ROSIDL aggregate CMake target (#3105)

* Compatiblity with 'Populate Transitions' ros2/rcl#1269 (#2967)

* add : get clients, servers info (#2569)

* Fix REP url locations (#2987)

* Add get_parameter_or overload returning value or alternative (#2973)

* deprecate rclcpp::spin_some and rclcpp::spin_all (#2848)

* Clearer warning message, the old one lacked information and was
  perhaps misleading (#2927)

* fix cmake deprecation (#2914) cmake version < then 3.10 is
  deprecated

* Added missing chrono includes (#2854)

* introduce rcl_lifecycle_get_transition_label_by_id(). (#2827)

* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Emerson
  Knapp, Jasper van Brakel, Lee, Minju, Peter Mitrano (AR), Tim
  Clephas, Tomoya Fujita, Zheng Qu, mosfet80

rclpy
=====

* Feature: async node (#1620)

* Refactor: moved TypeDescriptionService, LoggingService,
  ParameterService to BaseNode (#1645)

* Refactor: base node (#1637)

* Bugfix: executor doesn't propagate exception from task that awaited
  a future (#1643)

* Fix: disable flaky executor test (#1648) (#1649)

* Streamline entity destroy (#1629)

* Add acceptable_buffer_backends as subscription option in rclpy
  (#1628)

* publish_feedback should effect only on executing state. (#1639)

* Support to configure feedback subscription content filter for action
  client (#1633)

* fix flaky test_multi_threaded_executor_closes_threads. (#1636)

* Fix violation (#1635)

* Fix test_executor types (#1632)

* Refactor: base clock (#1627)

* Fix future flake8 (#1634)

* Use new ROSIDL aggregate CMake target (#1630)

* Update type hints for parameters (#1631)

* Add support check for content filter feature in subscription (#1618)

* Refactor: base entity classes (#1624)

* Fix more test typings and remove unused type aliases (#1626)

* Add types to test_waitable (#1625)

* Correct typos (#1619)

* Fix incorrect action client/server callback type hints (#1616)

* avoid stale parameter events in content filter tests. (#1615)

* fix violations (#1614)

* Typing Regression Fixes (#1612)

* CFT is only supported rmw_fastrtps and rmw_connextdds. (#1611)

* Prevents the Future result from being set twice. (#1599)

* Wrap up ActionClient construction before spining (#1591)

* Compatiblity with 'Populate Transitions' ros2/rcl#1269 (#1528)

* Drop invalid waitables from wait set (#1590)

* give some time for the discovery for test_on_new_message_callback.
  (#1585)

* print warning message on owner node if the parameter operation
  fails. (#1584)

* Update release version to 10.0.4 (#1583)

* Update "type_support.py" to use new message abstract base classes
  (#1509)

* Fix performance bug in MultiThreadedExecutor (hopefully) (#1547)

* Expose action graph functions as Node class methods. (#1574)

* Improve wildcard parsing and optimize the logic for parsing YAML
  para… (#1571)

* Improve the compatibility of processing YAML parameter files (#1548)

* Fix parameter parsing for unspecified target nodes (#1552)

* Remove default from switch with enum, so that compiler warns.
  (#1566)

* Use unconditional wait when possible. (#1563)

* Increase clock accuracy (#1564)

* Fix issues with resuming async tasks awaiting a future (#1469)

* ParameterEventHandler support ContentFiltering (#1531)

* add : get clients, servers info (#1307)

* Allow action servers without execute callback (#1219)

* Remove accidental tuple (#1542)

* fix(test_events_executor): destroy all nodes before shutdown (#1538)

* Remove duplicate future handling from send_goal_async (#1532)

* remove unused 'param_type' (#1524)

* Fixes Action.*_async futures never complete (#1308)

* add spinning state for the Executor classes. (#1510)

* EventsExecutor: Handle async callbacks for services and
  subscriptions (#1478)

* Added lock to protect futures for multithreaded executor (#1477)

* Add content-filtered-topic interfaces (#1506)

* Fix warnings from gcc. (#1501)

* Feature: expose event callback setter in subscription, service,
  client and timer (#1496)

* Feature: add executor.create_future() (#1495)

* Add More Test Typings (#1472)

* Use pybind11 from deb or pixi (#1497)

* Do not execute the timer if call_timer_with_info() fails (#1488)

* Fix msbuild warnings on "operator==" deprecation for pybind11 >=2.2
  (#1483)

* Cleanup the rclpy dependencies. (#1482)

* Feature: add logger_name property to subscription, publisher,
  service and client (#1471)

* Update "test_node" Types (#1464)

* Add method that get datetime.datetime from Time (#1443)

* add "MessageInfo.publisher_gid" (#1466)

* Add types to "test_action\_\*.py" (#1444)

* Revert "Fix Duration, Clock, and QoS Docs (#1428)" (#1447)

* remove all deprecated classes and methods (#1456)

* [rclpy] Fix spin() incorrectly removing node from executor if
  already attached (#1446)

* Contributors: Alejandro Hernández Cordero, Alon Borenshtein, Auguste
  Lalande, Barry Xu, Brad Martin, Brennan Miller-Klugman, Błażej Sowa,
  CY Chen, Chris Lalancette, Christian Rauch, Clara Berendsen, Emerson
  Knapp, Florian Vahl, Jasper van Brakel, Jean Paul, Jonathan, Lee,
  Michael Carlstrom, Michael Tandy, Minju, Nadav Elkabets, Nathan
  Wiebe Neufeldt, Tim Clephas, Tomoya Fujita, Yuyuan Yuan, mhidalgo-
  rai

rcpputils
=========

* Updated note related with tl_expected (#229)

* Increase test coverage (#222)

* Append copies of BSD and CC0 licenses from the works (#223)

* Use std::filesystem in find_library and add more test (#221)

* Remove -Werror from Clang compile options (#220)

* Remove unnecessary dependencies from rcpputils. (#216) It doesn't
  need to have dependencies on python tests.

* fix cmake deprecation (#214)

* add thread naming utilities (#213)

* Removed deprecated path (#212)

* Contributors: Adam Aposhian, Alejandro Hernández Cordero, Chris
  Lalancette, Tully Foote, William Woodall, mosfet80

rcutils
=======

* Add buildtool_export_depend on ament_cmake_ros_core (#558)

* fix: typo in parameter documentation for overwrite (#557)

* Remove ATOMIC_VAR_INIT (#556)

* Use "ament_set_default_language_standards" from "ament_cmake_core"
  (#548)

* Use uncommon variable name in macro to avoid being overwritten
  (#551)

* Remove "ament_export_link_flags()" for atomic operations (#528)

* Use less common variable name in macro (#550)

* Fix missing include for std::get_time (#549)

* Fix gcc 15.2.1 warning for discarding 'const' qualifier (#547)

* Disable warning C5105 for older Windows SDKs in base64.c (#544)

* Add {short_file_name} as log format option (#541)

* Add base64 encoding and decoding functions with tests (#533)

* remove default: so that compiler can detect the missing case. (#534)

* Check SIZE_MAX for array initialization. (#527)

* Do not export dl in rcutils_LIBRARIES (#522)

* rcutils_logging_allocator_initialize() support. (#419)

* Export -latomic even if BUILD_TESTING is disabled. (#516)

* Add rcutils_raw_steady_time_now method for slew-free clock (#507)

* Revert "use getenv_s instead of getenv for Windows. (#499)" (#504)
  This reverts commit 46ab4d4eeb555a2e9e880157b97f0a867d3a256c.

* Hand-code logging_macros.h (#502)

* Implement rcutils_strnlen. (#430)

* use getenv_s instead of getenv for Windows. (#499)

* Make linters happy

* Clean memory in test_process.cpp (#495)

* Contributors: Alejandro Hernández Cordero, Andrei Kholodnyi, Barry
  Xu, Chris Lalancette, EddyGharib, Miguel Company, Sai Kishor
  Kothakota, Shane Loretz, Tomoya Fujita, Tony Najjar

resource_retriever
==================

* Removed python2 code (#121)

* Delete resource_retriever/setup.py (#120)

* Use get_package_share_path (#119)

* Updated deprecated ament_index_cpp API (#118)

* removed libcurl_vendor package (#116)

* Removed deprecated code (#113)

* Fixed clang compile error (#112)

* Removed windows warnings (#111)

* Add a plugin mechanism to resource_retriever (#103)

* uniform MinCMakeVersion (#108)

* Contributors: Alejandro Hernández Cordero, Michael Carlstrom,
  Michael Carroll, mosfet80

resource_retriever_interfaces
=============================

* Update the plugin license (#17)

* Contributors: Stoyan Gaydarov

resource_retriever_service
==========================

* Update the plugin license (#17)

* Contributors: Stoyan Gaydarov

resource_retriever_service_plugin
=================================

* Update the plugin license (#17)

* Contributors: Stoyan Gaydarov

rmw
===

* find_package ament_cmake_gtest (#417)

* Add acceptable_buffer_backends field in rmw_subscription_options_s
  (#416)

* Add is_cft_supported field to rmw_subscription_t for content
  filtering support (#415)

* Remove default from switch with enum, so that compiler warns. (#414)

* add: get clients, servers info (#371)

* Fix REP url locations (#406)

* Update link to rmw API docs (#405)

* Don't assume a DDS-based implementation in function docs (#402)

* Contributors: Barry Xu, CY Chen, Christophe Bedard, Lee, Minju,
  Shane Loretz, Tim Clephas, Tomoya Fujita

rmw_connextdds
==============

* fix: Fixed compilation on MSVC 2022 (#225)

* Remove default from switch with enum to enable compiler warnings
  (#216)

* add : get clients,servers info (#154)

* fix: remove superflous "buildtool_export_depend" (#206)

* Fix cmake deprecation (#198)

* Contributors: Bas Zalmstra, Janosch Machowinski, Lee, Minju, Tomoya
  Fujita, mosfet80

rmw_connextdds_common
=====================

* Fix content filtering on Windows with modern Connext DDS (#226)
  (#230)

* fix: Fixed compilation on MSVC 2022 (#225)

* Add variable "RMW_CONNEXT_USER_TOPICS_PUBLISH_MODE" and deprecate
  "RMW_CONNEXT_USE_DEFAULT_PUBLISH_MODE" (#224)

* Update Connext from 7.3.0 to 7.7.0, disable monitoring library by
  default, and use synchronous publishing mode (#219)

* Enable property "dds.ros.demangle_topic_and_type_names" to announce
  demangled topic name as topic alias (#221)

* Enable content filtering flag (#223)

* Remove deprecated security properties and use new ones (#217)

* Remove default from switch with enum to enable compiler warnings
  (#216)

* Replace "DDS_ContentFilter_register_filter" with
  "DDS_DomainParticipant_register_contentfilterI" (#215)

* Remove superfluous "buildtool_export_depend" (#210)

* add : get clients,servers info (#154)

* [rmw_connextdds_common]: Remove
  <member_of_group>rosidl_interface_packages (#202)

* Correctly calculate the size of a serialized key (#200)

* Fix cmake deprecation (#198)

* Fixed serialized minimum sample size callback (#196)

* Removed warning (#187)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Francisco Gallego Salido, Janosch Machowinski, Lee,
  Minju, Tomoya Fujita, mergify[bot], mosfet80

rmw_connextddsmicro
===================

* fix: Fixed compilation on MSVC 2022 (#225)

* Remove default from switch with enum to enable compiler warnings
  (#216)

* Remove superfluous "buildtool_export_depend" (#210)

* add : get clients,servers info (#154)

* Fix cmake deprecation (#198)

* Contributors: Janosch Machowinski, Lee, Minju, Tomoya Fujita,
  mosfet80

rmw_cyclonedds_cpp
==================

* Silence unused variable warning in Release builds (#580)

* Add key support and update Cyclone DDS compatibility (#575)

* Explicitly disable content filtering support (#574)

* Add tracepoint to "rmw_take_loan_int" (#566)

* Fix warnings about "may be used uninitialized" (#573)

* Improve MessageTypeSupport performance (#562)

* Improve serialization performance by optimizing "dynamic_cast" usage
  and replacing virtual functions with templates (#553)

* Remove defaults to trigger proper warnings (#549)

* add : get clients, servers info (#499)

* Do not include rosidl_typesupport_{c,cpp} in rmw impl typesupport
  list (#544)

* Update CMake requirement (#539)

* Contributors: Brandon Simoncic, Christophe Bedard, Janosch
  Machowinski, Lee, Minju, Oren Bell PhD, Shane Loretz, Tomoya Fujita,
  eboasson, mosfet80

rmw_dds_common
==============

* If no publishers discovered, make the best available QoS for
  subscription. (#84)

* Add get_clients_info_by_service and get_servers_info_by_service;
  introduce ServiceEntityInfo to handle service type hash in graph
  cache (#82)

* Remove deprecated GraphCache methods without type hash (#83)

* Update cmake requirements (#80)

* Remove deprecated security utilities (#79)

* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Lee,
  Minju, Tomoya Fujita, mosfet80

rmw_fastrtps_cpp
================

* Clean up logs for the rosidl::Buffer path (#886) (#887)

* Change the buffer-aware BUFBE: -> bufbe. (backport #880) (#884)

* Fix UB in accessing the keys (#879) (#882)

* Remove warning when compiling with "lcang" (#876)

* Add support for rosidl::Buffer-aware per-endpoint pub/sub (#867)

* Use new aggregate rosidl target instead of _TARGETS (#870)

* Enable content filtering flag (#869)

* fix: remove superflous buildtool_export_depend. (#852)

* add : get clients, servers info (#771)

* Do not include rosidl_typesupport_{c,cpp} in rmw impl typesupport
  list (#843)

* fix cmake deprecation (#831)

* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Barry Xu,
  CY Chen, Christophe Bedard, Lee, Minju, Tomoya Fujita, mergify[bot],
  mosfet80

rmw_fastrtps_dynamic_cpp
========================

* Fix UB in accessing the keys (#879) (#882)

* Add support for rosidl::Buffer-aware per-endpoint pub/sub (#867)

* Use new aggregate rosidl target instead of _TARGETS (#870)

* fix: remove superflous buildtool_export_depend. (#852)

* add : get clients, servers info (#771)

* Do not include rosidl_typesupport_{c,cpp} in rmw impl typesupport
  list (#843)

* Check remaining size before resizing sequences (#827)

* fix cmake deprecation (#831)

* Contributors: Alexis Tsogias, CY Chen, Christophe Bedard, Lee,
  Miguel Company, Minju, Tomoya Fujita, mergify[bot], mosfet80

rmw_fastrtps_shared_cpp
=======================

* Change the buffer-aware BUFBE: -> bufbe. (backport #880) (#884)

* feat: set collection header element_flags
  TryConstructFailAction::DISCARD instead of 0 (#875)

* Add support for rosidl::Buffer-aware per-endpoint pub/sub (#867)

* Added rmw_take tracepoint, because it wasn't being triggered for
  successful takes (#871)

* Added tracepoint to loaned take (#868)

* fix: remove superflous buildtool_export_depend. (#852)

* add : get clients, servers info (#771)

* Refs #23861. Use key annotation in TypeObject build (#849)

* fix cmake deprecation (#831)

* Retrieve "HistoryQoS" in discovery when available (#829)

* check a local publication to ignore with serialized message. (#823)

* Contributors: CY Chen, Daisuke Nishimatsu, Lee, Mario Domínguez
  López, Miguel Company, Minju, Oren Bell, Oren Bell PhD, Tomoya
  Fujita, mergify[bot], mosfet80

rmw_implementation
==================

* Add rmw_zenoh_cpp as a build dependency (#273)

* Updated deprecated ament_index_cpp API (#272)

* Add rmw_get_clients_info_by_service ,
  rmw_servers_clients_info_by_service (#238)

* fix cmake deprecation (#267)

* Explain rosidl_typesupport_{c,cpp} in rmw impl typesupport list
  (#265)

* Fixed windows warning (#254)

* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Lee,
  Minju, Tony Najjar, mosfet80

rmw_test_fixture
================

* Add missing dependency from rmw_test_fixture to rmw (#53)

* add find_package call (#50)

* fix cmake deprecation (#47)

* Contributors: Matt Condino, Scott K Logan, mosfet80

rmw_test_fixture_implementation
===============================

* Block signals during Python environment reload in
  rmw_test_fixture_implementation (#64)

* Add "ament_ros_defaults" target (#62)

* Drop dependency group dependency on test fixtures (#60)

* Restore ROS_DOMAIN_ID after isolation is finished (#58)

* default to c++17 due to use of newer methods on std::map (#55)

* fix cmake deprecation (#47)

* On start-after-stop, re-check RMW_IMPLEMENTATION for changes (#46)

* Choose random domain IDs during default RMW isolation (#39)

* Ignore SIGINT *after* child process has been spawned (#45)

* Add some smoke tests for rmw_test_fixture_implementation (#42)

* Copy all environment variables explicitly (#43)

* Split the generator expression for each library (#36)

* Removed clang warnings (#34)

* Contributors: Alejandro Hernández Cordero, Michael Carlstrom,
  Michael Carroll, Scott K Logan, Tanishq Chaudhary, William Woodall,
  mosfet80

rmw_zenoh_cpp
=============

* Bump Zenoh to 1.8.0, fix Windows shutdown hang, and resolve
  synchronization with "undeclare" (#964)

* Revert changes to build against rust >= 1.75 and bump zenoh to 1.8.0
  (#960)

* Prevent deadlock by not holding both locks when processing event
  data (#937)

* Bump zenoh to 1.8.0 (#935)

* Explicitly set "false" for the content filtering feature (#938)

* Add deadline/liveliness QoS events to "rmw_zenoh_cpp" (#934)

* Catch "PackageNotFoundError" during default config URI loading to
  prevent crash (#915)

* Populate "reception_sequence_number" and "advertise_sequence_number"
  features (#920)

* Use "get_package_share_path" (#913)

* Address outstanding TODO items (#896)

* Expose zenoh session (#865)

* Fix config loading with incorrect path variable (#898)

* Fix build binary workflow (#895)

* Fix line ending in session open error message (#888)

* Update deprecated "ament_index_cpp" API (#879)

* Remove "default" from switch with enum to enable compiler warnings
  (#871)

* Use shared SHM transport provider instead of creating a new instance
  (#857)

* Bump "zenoh" to 1.7.1 (#870)

* Add rmw_get_clients_info_by_service and
  rmw_get_servers_info_by_service (#679)

* Fix REP url locations (#858)

* Restore ZENOH_CONFIG_OVERRIDE after isolation is finished (#855)

* Fix typo in 'triggered' (#844)

* Log details at SHM creation (alloc and threashold sizes) (#835)

* Change default value of ZENOH_SHM_ALLOC_SIZE to 48 MiB (#830)

* config: increase queries_default_timeout to 10min (#820)

* Fix compile with clang (#819)

* feat(logging): add contextual information to log messages (#809)

* Align the config with upstream Zenoh. (#785)

* fix: resolve memory leak when publishing with the default allocator
  (#797)

* Recycle serialization buffers on transmission (#342)

* refactor: avoid redundant key expression creation when replying
  (#732)

* Do not include rosidl_typesupport_{c,cpp} in rmw impl typesupport
  list (#748)

* fixing typo flow to flows in config files (#740)

* Shared Memory on C++ API (#363)

* Bump Zenoh to v1.5.0 (#728)

* rmw_zenoh_cpp: Include algorithm for std::find_if (#723)

* Use rfind to avoid issues with service types ending in Request or
  Response (#719)

* Remove the extra copy on the publisher side (#711)

* Avoid ambiguity with variable shadowing (#706)

* Only configure the timeout of the action-related service
  "get_result" to maximum value. (#685)

* Use Zenoh Querier to replace Session.get (#694)

* Use data() to avoid potentially dereferencing an empty vector (#667)

* Bump Zenoh to 1.4.0 (#652)

* fix(comment): correct the QoS incompatibilities (#644)

* fix rmw_take_serialized_message. (#638)

* Update CMakeLists.txt (#617)

* Contributors: Alejandro Hernandez Cordero, Alejandro Hernández
  Cordero, ChenYing Kuo (CY), Chris Lalancette, Christophe Bedard,
  Faseel Chemmadan, Filip, Hervé Audren, Jan Vermaete, Julien Enoch,
  Lee, Mahmoud Mazouz, Minju, Nikola Banović, Scott K Logan, Shane
  Loretz, Skyler Medeiros, Steven Palma, Tim Clephas, Tomoya Fujita,
  Yadunund, Yuyuan Yuan, jordanburklund, milidam, mosfet80, yadunund,
  yellowhatter, Øystein Sture

robot_state_publisher
=====================

* Use new ROSIDL aggregate CMake target (#246)

* Improvements (#245)

* Update subscription callback signatures (#241)

* Add functionality to read description from a topic instead of a
  parameter (#234)

* Removed tf2_ros warning (#239)

* fix cmake deprecation (#232)

* Removed tf2_ros warning (#238)

* Removed orocos kdl vendor dependency (#237)

* Removed warnings in geometry2 (#236)

* Replace deprecated tf2_ros headers (#235)

* Removed deprecated command-line argument (#233)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Kenji
  Brameld (TRACLabs), Maurice Alexander Purnawan, mosfet80

ros2action
==========

* Fix "flake8" (#1215)

* Add timeout arguments to "ros2 service call", "ros2 action
  send_goal", "ros2 component", "ros2 lifecycle", and "ros2 param"
  (#1185)

* add osrf_pycommon depend for test_exec. (#1120)

* Fujitatomoya/clearup isolated ros2daemon (#1098)

* Restore environment variables after launch tests (#1086)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* fix ros2action send_goal signal handling. (#1072)

* Fujitatomoya/ros2 action send goal timeout (#1067)

* Make sure to install py.typed files (#1058)

* Relax the check from exact to partial match. (#1055)

* Export Typing information (#1041)

* move QoS methods from ros2topic.api to ros2cli.qos. (#1053)

* remove unnecessary '/' from ros2 action info. (#1049)

* add QoS option to ros2service/ros2action echo commands. (#1036)

* Allow zenoh tests to run with multicast (#992)

* Support 'ros2 action echo' (#978)

* Correct the license content (#979)

* Contributors: Barry Xu, Christophe Bedard, Michael Carlstrom,
  Michael Carroll, Scott K Logan, Tomoya Fujita, mosfet80

ros2bag
=======

* Add "--repeat-all-transient-local" flag for automatic transient-
  local topic detection (#2391)

* Repeat transient-local topics: Recorder, CLI, and Python bindings
  (#2387)

* Suppress multi-threaded process warning from rosbag2 flake8 (#2329)

* Remove deprecated arguments and options from "ros2bag" (#2328)

* Implement circular logging by split count ("--max-bag-files")
  (#2218)

* Improve "ros2 bag convert" performance for fragment cutting and add
  "--input-options" (#2325)

* Add static topics feature for recorder (#2319)

* Add "--max-cache-duration" option for time-bounded snapshots (#2289)

* Add "rosbag2_storage_default_plugins" to "exec_depend" of "ros2bag"
  (#2227)

* Add "input_serialization_format" and "output_serialization_format"
  to "RecordOptions", deprecating "rmw_serialization_format" (#2215)

* Publish messages lost statistics to 'events/messages_lost' topic
  (#2150)

* Expose more of the player and recorder API to Python, and improve
  signal handling (#2062)

* Fix setuptools deprecations (#2087)

* Refactor Python player and recorder APIs into classes (#2047)

* Upstream quality changes from Apex.AI part-2 (#1924)

* Contributors: Christophe Bedard, Luke Sy, Michael Orlov, Tomoya
  Fujita, Tony Najjar, mosfet80

ros2cli
=======

* Add RMW isolation fixture to enable discovery for "rmw_zenoh_cpp"
  tests (#1216)

* Add support for fish (#1211)

* Fix "flake8" (#1215)

* Fix future flake8 regressions (#1196)

* fix deprecated warning for action graph APIs. (#1188)

* Enable always complete (#1190)

* Add fzf-based interactive selection to ros2cli commands (#1151)

* check for invalid ROS discovery configuration and print warning if
  ne… (#1178)

* skip history and depth check for rmw_connextdds. (#1064)

* Remove importlib packages (#1117)

* add verbose in service-info verb (#916)

* Fix handling of empty ROS_DOMAIN_ID in ros2cli (#1112)

* fix: Also catch a TimeoutError (#1092)

* [ros2doctor] Add Action Report (#1076)

* Use rmw_test_fixture to isolate ros2cli tests (#1062)

* fix setuptools deprecations (#1066)

* Add Service report similar to topic report (#1059)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* move QoS methods from ros2topic.api to ros2cli.qos. (#1053)

* Assert HistoryQoS in test_ros2cli_daemon (#1040)

* remove add_subparsers from ros2cli. (#1032)

* Allow zenoh tests to run with multicast (#992)

* Contributors: Christophe Bedard, David V. Lu!!, Kaju-Bubanja, Lee,
  Mario Domínguez López, Michael Carlstrom, Michael Carroll, Minju,
  SPeak, Scott K Logan, Tomoya Fujita, Tony Najjar, Yuyuan Yuan,
  mosfet80

ros2cli_common_extensions
=========================

* Add dependency on ros2plugin in package.xml (#13)

* Update CMakeLists.txt (#11)

* Contributors: Maurice Alexander Purnawan, mosfet80

ros2cli_test_interfaces
=======================

* fix cmake deprecation (#1082)

* Contributors: mosfet80

ros2component
=============

* Fix "flake8" (#1215)

* Add timeout arguments to "ros2 service call", "ros2 action
  send_goal", "ros2 component", "ros2 lifecycle", and "ros2 param"
  (#1185)

* Fix future flake8 regressions (#1196)

* fix setuptools deprecations (#1066)

* Make sure to install py.typed files (#1058)

* Export Typing information (#1041)

* Contributors: Christophe Bedard, Michael Carlstrom, Tomoya Fujita,
  mosfet80

ros2doctor
==========

* Fix future flake8 regressions (#1196)

* Remove importlib packages (#1117)
