# Humble Hawksbill changelog (part 3 of 5)

* Fix include order for cpplint (#84) Relates to
  https://github.com/ament/ament_lint/pull/324

* Update maintainers to Chris Lalancette (#83)

* Fix renamed "rcpputils" header (#81)

* Update includes after rcutils/get_env.h deprecation (#75)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe
  Bedard, Jacob Perron

rcl_yaml_param_parser
=====================

* Install includes it include/${PROJECT_NAME} (#959)

* Update maintainers to Ivan Paunovic and William Woodall (#952)

* Tweak rcl_yaml_param_parser documentation (#939)

* Contributors: Audrow Nash, Michel Hidalgo, Shane Loretz

rclcpp
======

* remove DEFINE_CONTENT_FILTER cmake option (#1914)

* remove things that were deprecated during galactic (#1913)

* add take_data_by_entity_id API to waitable (#1892)

* add content-filtered-topic interfaces (#1561)

* [NodeParameters] Set name in param info pre-check (#1908)

* Add test-dep ament_cmake_google_benchmark (#1904)

* Add publish by loaned message in GenericPublisher (#1856)

* Add missing ament dependency on rcl_interfaces (#1903)

* Update data callback tests to account for all published samples
  (#1900)

* Increase timeout for acknowledgments to account for slower Connext
  settings (#1901)

* clang-tidy: explicit constructors (#1782)

* Add client/service QoS getters (#1784)

* Fix a bunch more rosdoc2 issues in rclcpp. (#1897)

* time_until_trigger returns max time if timer is cancelled (#1893)

* Micro-optimizations in rclcpp (#1896)

* spin_all with a zero timeout. (#1878)

* Add RMW listener APIs (#1579)

* Remove fastrtps customization on tests (#1887)

* Install headers to include/${PROJECT_NAME} (#1888)

* Use ament_generate_version_header (#1886)

* use universal reference to support rvalue. (#1883)

* fix one subscription can wait_for_message twice (#1870)

* Add return value version of get_parameter_or (#1813)

* Cleanup time source object lifetimes (#1867)

* add is_spinning() method to executor base class

* Cleanup the TypeAdapt tests (#1858)

* Cleanup includes (#1857)

* Fix include order and relative paths for cpplint (#1859)

* Rename stringstream in macros to a more unique name (#1862)

* Add non transform capabilities for intra-process (#1849)

* Fix rclcpp documentation build (#1779)

* Use UninitializedStaticallyTypedParameterException (#1689)

* Add wait_for_all_acked support (#1662)

* Add tests for function templates of declare_parameter (#1747)

* Fixes for uncrustify 0.72 (#1844)

* use private member to keep the all reference underneath. (#1845)

* Make node base sharable (#1832)

* Add Clock::sleep_for() (#1828)

* Synchronize rcl and std::chrono steady clocks in Clock::sleep_until
  (#1830)

* Use rclcpp::guard_condition (#1612)

* Call CMake function to generate version header (#1805)

* Use parantheses around logging macro parameter (#1820)

* Remove author by request (#1818)

* Update maintainers (#1817)

* min_forward & min_backward thresholds must not be disabled (#1815)

* Re-add Clock::sleep_until (#1814)

* Fix lifetime of context so it remains alive while its dependent node
  handles are still in use (#1754)

* Add the interface for pre-shutdown callback (#1714)

* Take message ownership from moved LoanedMessage (#1808)

* Suppress clang dead-store warnings in the benchmarks. (#1802)

* Wait for publisher and subscription to match (#1777)

* Fix unused QoS profile for clock subscription and make ClockQoS the
  default (#1801)

* Fix dangerous std::bind capture in TimeSource implementation.
  (#1768)

* Fix dangerous std::bind capture in ParameterEventHandler
  implementation. (#1770)

* Handle sigterm, in the same way sigint is being handled. (#1771)

* rclcpp::Node copy constructor: make copy of node_waitables_ member.
  (#1799)

* Extend NodeGraph to match what rcl provides. (#1484)

* Context::sleep_for(): replace recursion with do-while to avoid
  potential stack-overflow. (#1765)

* extend_sub_namespace(): Verify string::empty() before calling
  string::front(). (#1764)

* Deprecate the "void shared_ptr<MessageT>" subscription callback
  signatures. (#1713)

* Remove can_be_nullptr assignment check for QNX case. (#1752)

* Update client API to be able to remove pending requests. (#1734)

* Fix: Allow to add a node while spinning in the
  StaticSingleThreadedExecutor. (#1690)

* Add tracing instrumentation for executor and message taking. (#1738)

* Fix: Reset timer trigger time before execute in
  StaticSingleThreadedExecutor. (#1739)

* Use FindPython3 and make python3 dependency explicit. (#1745)

* Use rosidl_get_typesupport_target(). (#1729)

* Fix returning invalid namespace if sub_namespace is empty. (#1658)

* Add free function to wait for a subscription message. (#1705)

* Use rcpputils/scope_exit.hpp and remove rclcpp/scope_exit.hpp.
  (#1727)

* Remove unsafe get_callback_groups API. Callers should change to
  using for_each_callback_group(), or store the callback groups they
  need internally.

* Add in callback_groups_for_each. The main reason to add this method
  in is to make accesses to the callback_groups_ vector thread-safe.
  By having a callback_groups_for_each that accepts a std::function,
  we can just have the callers give us the callback they are
  interested in, and we can take care of the locking. The rest of this
  fairly large PR is cleaning up all of the places that use
  get_callback_groups() to instead use callback_groups_for_each().

* Use a different mechanism to avoid timers being scheduled multiple
  times by the MultiThreadedExecutor (#1692)

* Fix windows CI (#1726) Fix bug in AnyServiceCallback introduced in
  #1709.

* Support to defer to send a response in services. (#1709) Signed-off-
  by: Ivan Santiago Paunovic <ivanpauno@ekumenlabs.com>

* Fix documentation bug. (#1719) Signed-off-by: William Woodall
  <william@osrfoundation.org>

* Removed left over "is_initialized()" implementation (#1711) Leftover
  from https://github.com/ros2/rclcpp/pull/1622

* Fixed declare parameter methods for int and float vectors (#1696)

* Cleaned up implementation of the intra-process manager (#1695)

* Added the node name to an executor "runtime_error" (#1686)

* Fixed a typo "Attack" -> "Attach" (#1687)

* Removed use of std::allocator<>::rebind (#1678) rebind is deprecated
  in c++17 and removed in c++20

* Allow declare uninitialized parameters (#1673)

* Fix syntax issue with gcc (#1674)

* [service] Don't use a weak_ptr to avoid leaking (#1668)

* Fix doc typo (#1663)

* [rclcpp] Type Adaptation feature (#1557)

* Do not attempt to use void allocators for memory allocation. (#1657)

* Keep custom allocator in publisher and subscription options alive.
  (#1647)

* Fix get_publishers_subscriptions_info_by_topic test in test_node.cpp
  (#1648)

* Use OnShutdown callback handle instead of OnShutdown callback
  (#1639)

* use dynamic_pointer_cast to detect allocator mismatch in intra
  process manager (#1643)

* Contributors: Abrar Rahman Protyasha, Ahmed Sobhy, Alberto Soragna,
  Andrea Sorbini, Audrow Nash, Barry Xu, Bi0T1N, Chen Lihui, Chris
  Lalancette, Christophe Bedard, Doug Smith, Emerson Knapp, Gaël
  Écorchard, Geoffrey Biggs, Gonzo, Grey, Ivan Santiago Paunovic,
  Jacob Perron, Jorge Perez, Karsten Knese, Kenji Miyake, M.
  Hofstätter, M. Mostafa Farzan, Mauro Passerino, Michel Hidalgo,
  Miguel Company, Nikolai Morin, Petter Nilsson, Scott K Logan, Shane
  Loretz, Steve Macenski, Tomoya Fujita, William Woodall, Yong-Hao
  Zou, iRobot ROS, livanov93, mauropasse

rclcpp_action
=============

* remove things that were deprecated during galactic (#1913)

* add take_data_by_entity_id API to waitable (#1892)

* Fix rosdoc2 issues (#1897)

* Add RMW listener APIs (#1579)

* Install headers to include/${PROJECT_NAME} (#1888)

* Fix include order and relative paths for cpplint (#1859)

* Fixes for uncrustify 0.72 (#1844)

* Use rclcpp::guard_condition (#1612)

* Remove author by request (#1818)

* Update maintainers (#1817)

* Suppress clang dead-store warnings in the benchmarks. (#1802)

* Deprecate the "void shared_ptr<MessageT>" subscription callback
  signatures (#1713)

* Use rcpputils/scope_exit.hpp and remove rclcpp/scope_exit.hpp.
  (#1727)

* Fixed occasionally missing goal result caused by race condition
  (#1677)

* Bump the benchmark timeout for benchmark_action_client (#1671)

* Returns CancelResponse::REJECT while goal handle failed to transit
  to CANCELING state (#1641)

* Fix action server deadlock issue that caused by other mutexes locked
  in CancelCallback (#1635)

* Contributors: Abrar Rahman Protyasha, Alberto Soragna, Chris
  Lalancette, Christophe Bedard, Jacob Perron, Kaven Yau, Shane
  Loretz, Tomoya Fujita, William Woodall, iRobot ROS, mauropasse

rclcpp_components
=================

* Select executor in node registration (#1898)

* Fix rosdoc2 issues in rclcpp (#1897)

* Fix bugprone-exception-escape in node_main.cpp.in (#1895)

* small improvements to node_main.cpp.in

* Install headers to include/${PROJECT_NAME} (#1888)

* Use spin() in component_manager_isolated.hpp (#1881)

* add use_global_arguments for node options of component nodes (#1776)

* Add rclcpp_components::component (#1855)

* Add parameter to configure number of thread (#1708)

* remove RCLCPP_COMPONENTS_PUBLIC in class ComponentManagerIsolated
  (#1843)

* create component_container_isolated (#1781)

* Remove author by request (#1818)

* Update maintainers (#1817)

* Suppress clang dead-store warnings in the benchmarks. (#1802)

* Update client API to be able to remove pending requests. (#1734)

* Deprecate method names that use CamelCase in rclcpp_components.
  (#1716)

* Added a hook to generate node options in ComponentManager (#1702)

* Contributors: Alberto Soragna, Chris Lalancette, Daisuke Nishimatsu,
  Hirokazu Ishida, Ivan Santiago Paunovic, Jacob Perron, Rebecca
  Butler, Shane Loretz, gezp

rclcpp_lifecycle
================

* remove things that were deprecated during galactic (#1913)

* Fix rosdoc2 issues (#1897)

* Install headers to include/${PROJECT_NAME} (#1888)

* LifecycleNode::on_deactivate deactivate all managed entities.
  (#1885)

* Automatically transition lifecycle entities when node transitions
  (#1863)

* Remove author by request (#1818)

* Update maintainers (#1817)

* Suppress clang dead-store warnings in the benchmarks. (#1802)

* Update forward declarations of "rcl_lifecycle" types (#1788)

* Deprecate the "void shared_ptr<MessageT>" subscription callback
  signatures (#1713)

* Update client API to be able to remove pending requests. (#1734)

* Change log level for lifecycle_publisher. (#1715)

* Fix: RCLCPP_PUBLIC -> RCLCPP_LIFECYCLE_PUBLIC (#1732)

* Use rcpputils/scope_exit.hpp and remove rclcpp/scope_exit.hpp
  (#1727)

* Remove unsafe get_callback_groups API. Callers should change to
  using for_each_callback_group(), or store the callback groups they
  need internally.

* Add in callback_groups_for_each. The main reason to add this method
  in is to make accesses to the callback_groups_ vector thread-safe.
  By having a callback_groups_for_each that accepts a std::function,
  we can just have the callers give us the callback they are
  interested in, and we can take care of the locking. The rest of this
  fairly large PR is cleaning up all of the places that use
  get_callback_groups() to instead use callback_groups_for_each().

* Fix destruction order in lifecycle benchmark (#1675)

* [rclcpp] Type Adaptation feature (#1557)

* Contributors: Abrar Rahman Protyasha, Alberto Soragna, Audrow Nash,
  Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob
  Perron, Michel Hidalgo, Shane Loretz, Tomoya Fujita, William Woodall

rclpy
=====

* Make rclpy dependencies explicit (#906)

* Avoid exception in Node constructor when use override for
  'use_sim_time' (#896)

* time_until_next_call returns max if timer is canceled. (#910)

* Properly implement action server/client handle cleanup. (#905)

* Make sure to take out contexts on Action{Client,Server}. (#904)

* Make sure to free the goal_status_array when done using it. (#902)

* Bugfix to Node.destroy_rate() result (#901)

* Remove fastrtps customization on tests (#895)

* fix typo (#890)

* Document that Future.result() may return None (#884)

* update doc release number (#885)

* Fix multi-threaded race condition in client.call_async (#871)

* Fix include order for cpplint (#877)

* Bugfix/duration to msg precision (#876)

* Update to pybind11 2.7.1 (#874)

* QoS history depth is only available with KEEP_LAST (#869)

* Implement managed nodes. (#865)

* Make rclpy.try_shutdown() behavior to follow rclpy.shutdown() more
  closely. (#868)

* Update TopicEndpointTypeEnum.__str__() method to include history
  kind and history depth. (#849)

* Add Clock.sleep_for() using Clock.sleep_until(). (#864)

* Add Clock.sleep_until() (#858)

* Add __enter__ and __exit__ to JumpHandle. (#862)

* Don't override rclpy._rclpy_pybind11 docs. (#863)

* Improve JumpThreshold documentation and forbid zero durations.
  (#861)

* Fix time.py and clock.py circular import. (#860)

* Make context.on_shutdown() allow free functions. (#859)

* Fix automatically declared parameters descriptor type. (#853)

* Shutdown asynchronously when sigint is received. (#844)

* Update maintainers. (#845)

* Add entities to callback group before making them available to the
  executor to avoid a race condition. (#839)

* Avoid race condition in client.call(). (#838)

* Handle sigterm. (#830)

* Use pybind11 for signal handling, and delete now unused
  rclpy_common, pycapsule, and handle code. (#814)

* Fix memory leak in Service::take_request() and
  Client::take_response(). (#828)

* Add Publisher.wait_for_all_acked(). (#793)

* Only add one done callback to a future in Executor. (#816)

* Add convert function from ParameterValue to Python builtin. (#819)

* Call Context._logging_fini() in Context.try_shutdown(). (#800)

* Lift LoggingSeverity enum as common dependency to logging and
  rcutils_logger modules (#785)

* Set Context.__context to None in __init__(). (#812)

* Remove unused function make_mock_subscription. (#809)

* Removed common.c/h (#789)

* Allow declaring uninitialized parameters (#798)

* Reject cancel request if failed to transit to CANCEL_GOAL state
  (#791)

* Deleted handle as it should no longer be used (#786)

* Removed some functions in common.c and replaced them in utils.cpp
  (#787)

* Moved exception.cpp/hpp to the _rclpy_pybind11 module (#788)

* Print 'Infinite' for infinite durations in topic endpoint info
  (#722)

* Break log function execution ASAP if configured severity is too high
  (#776)

* Convert Node and Context to use C++ Classes (#771)

* Misc action server improvements (#774)

* Misc action goal handle improvements (#767)

* Convert Guardcondition to use C++ classes (#772)

* Removed unused structs "rclpy_client_t" and "rclpy_service_t" (#770)

* Convert WaitSet to use C++ Classes (#769)

* Convert ActionServer to use C++ Classes (#766)

* Convert ActionClient to use C++ classes (#759)

* Use py::class_ for rcl_action_goal_handle_t (#751)

* Convert Publisher and Subscription to use C++ Classes (#756)

* Rename QoS*Policy enum's to *Policy (#379)

* Use params from node '/**' from parameter YAML file (#370)

* Updated to use params from node '/**' from parameter YAML file.
  (#399)

* Contributors: Alejandro Hernández Cordero, Anthony, Artem Shumov,
  Auguste Lalande, Barry Xu, Chris Lalancette, Emerson Knapp, Erki
  Suurjaak, Greg Balke, Ivan Santiago Paunovic, Jacob Perron, Lei Liu,
  Louise Poubel, Miguel Company, Shane Loretz, Tomoya Fujita, ksuszka

rcpputils
=========

* Install includes to include/${PROJECT_NAME} (#160)

* Fix include order for cpplint (#158)

* [path] Declare the default assignment operator (#156)

* Fixes for uncrustify 0.72 (#154)

* Fix the BSD license headers to use the standard one. (#153)

* Update maintainers to Chris Lalancette (#152)

* Add checked convert_to_nanoseconds() function (#145)

* Add missing sections in docs/FEATURES.md TOC (#151)

* [env] Add "set_env_var" function (#150)

* Add missing cstddef include (#147)

* Add accumulator test to CMakeLists.txt (#144)

* "rcpputils::fs": Fix doxygen parameter identifier (#142)

* Make thread safety macro C++ standards compliant (#141)

* Fix API documentation for clean "rosdoc2" build (#139)

* Improve "rcppmath" Doxygen documentation (#138)

* Improve documentation of utilities in docs/FEATURES.md (#137)

* Include "rcppmath" utilities in docs/FEATURES.md (#136)

* Fix "IllegalStateException" reference in FEATURES (#135)

* migrate rolling mean from ros2_controllers to rcppmath (#133)

* Update includes after rcutils/get_env.h deprecation (#132)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Chris
  Lalancette, Christophe Bedard, Jacob Perron, Karsten Knese,
  Octogonapus, Shane Loretz

rcutils
=======

* Update launch test for change related to enviroment variables in
  launch (#354)

* Remove dst_size from strlen usage (#353)

* Install headers to include${PROJECT_NAME} (#351)

* Use static_cast instead of C-style cast (#349)

* Fixing up documentation build when using rosdoc2 (#344)

* Stop double-defining structs. (#333)

* Use FindPython3 explicitly instead of FindPythonInterp implicitly
  (#345)

* Fix build on Android (#342)

* Deprecate get_env.h and move content to env.{h,c} (#340)

* Contributors: Chris Lalancette, Christophe Bedard, Ivan Santiago
  Paunovic, Jacob Perron, Jorge Perez, Shane Loretz, William Woodall

resource_retriever
==================

* Install headers to include/${PROJECT_NAME} (#72)

* Fix include order for cpplint (#69)

* Update maintainers (#66)

* Remove the deprecated retriever.h header (#63)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, Shane
  Loretz

rmw
===

* Add content filtered topics support. (#302)

* Add sequence numbers to rmw_message_info_t. (#318)

* Add rmw_feature_supported(). (#318)

* Add EventsExecutor (#286)

* Document that rmw_wait() SHOULD use a monotonic clock (#316)

* Install headers to include/${PROJECT_NAME} (#317)

* Update rmw_server_is_available() API documentation. (#277)

* Add client/service QoS getters. (#314)

* Fix up documentation build for rmw when using rosdoc2 (#313)

* Fix up errors in doxygen documentation (#311)

* Fix copy-paste error in API doc for rmw_get_gid_for_publisher (#310)

* Add rmw_publisher_wait_for_all_acked support. (#296)

* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe
  Bedard, Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz, iRobot
  ROS, mauropasse

rmw_connextdds
==============

* Exclude missing sample info fields when building rmw_connextddsmicro
  (#79)

* Update launch_testing_ros output filter prefixes for Connext6 (#80)

* Add support for user-specified content filters (#68)

* add stub for content filtered topic (#77)

* Add rmw listener apis (#44)

* Add client/service QoS getters. (#67)

* Add rmw_publisher_wait_for_all_acked support. (#20)

* Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Ivan Santiago
  Paunovic, iRobot ROS, mauropasse

rmw_connextdds_common
=====================

* Exclude missing sample info fields when building rmw_connextddsmicro
  (#79)

* Properly initialize CDR stream before using it for filtering (#81)

* Add support for user-specified content filters (#68)

* add stub for content filtered topic (#77)

* Add sequence numbers to message info structure (#74)

* Add rmw listener apis (#44)

* Fix cpplint errors (#69)

* Add client/service QoS getters. (#67)

* Update rmw_context_impl_t definition (#65)

* Use the new rmw_dds_common::get_security_files API (#61)

* Add rmw_publisher_wait_for_all_acked support. (#20)

* Support extended signature for
  "message_type_support_callbacks_t::max_serialized_size()" from
  "rosidl_typesupport_fastrtps_cpp". (#14)

* Update includes after rcutils/get_env.h deprecation. (#55)

* Always modify UserObjectQosPolicy regardless of override policy.
  (#53)

* Improved conversion of time values between ROS and DDS formats.
  (#43)

* Allow sharing DomainParticipant with C++ applications. (#25)

* Add environment variable to control override of
  DomainParticipantQos. (#41)

* Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Chris
  Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron,
  Michel Hidalgo, Miguel Company, iRobot ROS, mauropasse

rmw_connextddsmicro
===================

* Exclude missing sample info fields when building rmw_connextddsmicro
  (#79)

* Add support for user-specified content filters (#68)

* add stub for content filtered topic (#77)

* Add sequence numbers to message info structure (#74)

* Add rmw listener apis (#44)

* Add client/service QoS getters. (#67)

* Add rmw_publisher_wait_for_all_acked support. (#20)

* Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Ivan Santiago
  Paunovic, iRobot ROS, mauropasse

rmw_cyclonedds_cpp
==================

* Fix get_topic_name and handling long service names

* Add serialization for SDK_DATA

* Additional checks for loan API

* Depend on just rmw_dds_common::rmw_dds_common_library (#385)

* Fix error message in rmw_init_options_copy(). (#380)

* Add content filter topic feature empty stub. (#289)

* Update to work with Cyclone 0.9.0 and Iceoryx 2.0 (#379)

* Fill message info sequence numbers as unsupported, add
  rmw_feature_supported() implementation. (#381)

* Fix a warning by making a pointer nullptr. (#375)

* Bump QDs to QL2 (#371)

* Add EventsExecutor (#256)

* Call dissociate_reader in rmw_destroy_subscription

* Wrap creation of new serdata_rmw within a try-catch block

* Fix memory leak in error scenario on the publish side with SHM

* Fix memory leaks on the take side with SHM

* rename _cyclonedds_has_shm to follow the convention

* Add iceoryx_binding_c as dependency to rmw_cyclonedds_cpp

* Release iox_chunk to iceoryx in serdata_free if the iox_chunk is
  still available

* Update iceoryx_subscriber also when constructing the serdata from
  the iox chunk

* Fix cpplint errors (#363)

* Updates for uncrustify 0.72 (#358)

* Export only rmw::rmw to downstream targets (#360)

* Export modern CMake targets (#357)

* Free with the same allocator in rmw_destroy_node (#355)

* Add client/service QoS getters. (#343)

* Updated version number and quality level. (#349)

* Update package maintainers. (#351)

* Fix undesired memory initialization in zero-copy data path. (#348)

* Fix QoS depth settings for clients/service being ignored. (#340)

* Link to Cyclone DDS in Quality Declaration. (#342)

* Update rmw_context_impl_t definition (#337)

* Add quality declaration for rmw_cyclonedds_cpp (#335)

* Fix use of deprecated is_loan_available (#336)

* Add -latomic for RISC-V (#332)

* Add pub/sub init, publish and take instrumentation using tracetools
  (#329)

* Pass the CRL down to CycloneDDS if it exists (#325)

* Use the new rmw_dds_common::get_security_files API (#323)

* Add rmw_publisher_wait_for_all_acked support. (#294)

* Fix zero copy issues. (#309)

* Handle allocation errors during message deserialization. (#313)

* Update includes after rcutils/get_env.h deprecation. (#312)

* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe
  Bedard, Dietrich Krönke, Erik Boasson, Haowei Wen, Ivan Santiago
  Paunovic, Jacob Perron, Joe Speed, Michel Hidalgo, Shane Loretz,
  Sumanth Nirmal, eboasson, guillaume-pais-siemens, iRobot ROS,
  mauropasse

rmw_dds_common
==============

* Depend on target generated by rosidl_typesupport_cpp (#58)

* Use rosidl_get_typesupport_target() and target_link_libraries().
  (#57)

* Install headers to include/${PROJECT_NAME} (#56)

* Fix include order for cpplint (#55)

* Fix up rmw_dds_common documentation when using rosdoc2 (#54)

* Add support for Certificate Revocation List files (#52)

* Silence clang warning ("range-loop-construct") (#53)

* Add a common function for security files. (#51)

* Normalize rmw_time_t according to DDS spec (#48)

* Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron,
  Karsten Knese, Michel Hidalgo, Shane Loretz

rmw_fastrtps_cpp
================

* Add pub/sub init, publish and take instrumentation using tracetools
  (#591)

* Add content filter topic feature (#513)

* Add sequence numbers to message info structure (#587)

* Removed some heap interactions in rmw_serialize.cpp (#590)

* Add EventsExecutor (#468)

* Install headers to include/${PROJECT_NAME} (#578)

* Add client/service QoS getters. (#560)

* Correctly recalculate serialized size on bounded sequences. (#540)

* Fix type size alignment. (#550)

* Change links from index.ros.org -> docs.ros.org (#539)

* Add rmw_publisher_wait_for_all_acked support. (#519)

* Loan messages implementation (#523) * Added is_plain_ attribute to
  base TypeSupport. * Added new methods to base TypeSupport. *
  Implementation of rmw_borrow_loaned_message. * Implementation of
  rmw_return_loaned_message_from_publisher. * Enable loan messages on
  publishers of plain types. * Implementation for taking loaned
  messages. * Enable loan messages on subscriptions of plain types.

* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe
  Bedard, Ivan Santiago Paunovic, Miguel Company, Shane Loretz,
  WideAwakeTN, iRobot ROS, mauropasse

rmw_fastrtps_dynamic_cpp
========================

* Add content filter topic feature (#513)

* Add sequence numbers to message info structure (#587)

* Add EventsExecutor (#468)

* Install headers to include/${PROJECT_NAME} (#578)

* Add client/service QoS getters. (#560)

* Correctly recalculate serialized size on bounded sequences. (#540)

* Fix type size alignment. (#550)

* Add rmw_publisher_wait_for_all_acked support. (#519)

* Loan messages implementation (#523) * Added is_plain_ attribute to
  base TypeSupport. * Added new methods to base TypeSupport. *
  Implementation of rmw_borrow_loaned_message. * Implementation of
  rmw_return_loaned_message_from_publisher. * Enable loan messages on
  publishers of plain types. * Implementation for taking loaned
  messages. * Enable loan messages on subscriptions of plain types.

* Contributors: Barry Xu, Chen Lihui, Ivan Santiago Paunovic, Miguel
  Company, Shane Loretz, iRobot ROS, mauropasse

rmw_fastrtps_shared_cpp
=======================

* Address linter waning for windows. (#592)

* Add pub/sub init, publish and take instrumentation using tracetools
  (#591)

* Add content filter topic feature (#513)

* Add sequence numbers to message info structure (#587)

* Add EventsExecutor (#468)

* Complete events support (#583)

* Install headers to include/${PROJECT_NAME} (#578)

* Change default to synchronous (#571)

* Fix cpplint error (#574)

* Fixes for uncrustify 0.72 (#572)

* Add client/service QoS getters. (#560)

* Fix QoS depth settings for clients/service being ignored. (#564)

* Update rmw_context_impl_t definition. (#558)

* Update the LoanManager to do internal locking. (#552)

* Pass the CRL down to Fast-DDS if available. (#546)

* Use the new rmw_dds_common::get_security_files (#544)

* Support for SubscriptionOptions::ignore_local_publications (#536)

* Change links from index.ros.org -> docs.ros.org (#539)

* Add rmw_publisher_wait_for_all_acked support. (#519)

* Loan messages implementation (#523) * Added is_plain_ attribute to
  base TypeSupport. * Added new methods to base TypeSupport. *
  Implementation of rmw_borrow_loaned_message. * Implementation of
  rmw_return_loaned_message_from_publisher. * Enable loan messages on
  publishers of plain types. * Implementation for taking loaned
  messages. * Enable loan messages on subscriptions of plain types.

* Export rmw_dds_common as an rmw_fastrtps_shared_cpp dependency
  (#530)

* Update includes after rcutils/get_env.h deprecation (#529)

* Contributors: Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette,
  Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Jose
  Antonio Moral, Michel Hidalgo, Miguel Company, Shane Loretz, Tomoya
  Fujita, iRobot ROS, mauropasse

rmw_implementation
==================

* add content-filtered-topic interfaces (#181)

* Add rmw_feature_supported() (#204)

* Add EventsExecutor (#161)

* Fix relative path include syntax for cpplint (#203)

* Support and prefer exported targets from rmw implementations (#201)

* Add client/service QoS getters. (#196)

* Update maintainers to Audrow Nash and Michael Carroll. (#199)

* Fix renamed "rcpputils" header (#198)

* Fix rmw_implementation generated documentation (#197)

* Add rmw_publisher_wait_for_all_acked. (#188)

* Attempt to load any available RMW implementation. (#189)

* Update includes after rcutils/get_env.h deprecation (#190)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Chen
  Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic,
  Jacob Perron, Michel Hidalgo, Shane Loretz, iRobot ROS, mauropasse

rmw_implementation_cmake
========================

* Use FastDDS as default DDS (#315)

* Contributors: Audrow Nash

robot_state_publisher
=====================

* Depend on orocos_kdl_vendor (#191)

* export dependencies, to use robot_state_publisher as a component
  (#193)

* Fix include order for cpplint (#186)

* Change how parameter updates are handled (#180)

* Install includes to instal/${PROJECT_NAME} (#184)

* Make the change_fixed_joint test more robust (#183)

* Add in a test to make sure fixed transforms change on update

* Small C++ nice-isms in the tests

* Switch to using target_include_directories for tests

* Publish new fixed transforms when URDF is updated

* Make joint_states subscription QoS configurable; default to
  SensorDataQoS (#179)

* Remove dependency on urdfdom_headers (#168)

* Fix deprecated subscriber callbacks (#173)

* Cleanup the documentation in the RobotStatePublisher class. (#172)

* Always publish fixed frames to /tf_static (#158)
