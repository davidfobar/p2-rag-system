# Iron Irwini Changelog (part 3 of 5)

* Service introspection (#988)

* to create a sublogger while getting child of Logger (#1084)

* Fix #983 by saving future and checking for + raising any exceptions
  (#1073)

* Force C++17 support on. (#1076)

* Use RCPPUTILS_SCOPE_EXIT to cleanup unparsed_indices_c. (#1075)

* Explicitly link atomic when building with Clang (#1065)

* Fix test_publisher linter for pydocstyle 6.2.2 (#1063)

* Add default preset qos profile (#1062)

* Add on_parameter_event method to the AsyncParameterClient. (#1061)

* Add documentation page for rclpy.clock (#1055)

* Rewrite test code without depending on parameter client (#1045)

* Add parallel callback test (#1044)

* decorator should not be callable. (#1050)

* typo fix. (#1049)

* Add in a warning for a depth of 0 with KEEP_LAST. (#1048)

* Add feature of wait for message (#953). (#960)

* Document rclpy.time.Time class (#1040)

* Deal with ParameterUninitializedException for parameter service
  (#1033)

* Improve documentation in rclpy.utilities (#1038)

* Document rclpy.utilities.remove_ros_args (#1036)

* Fix incorrect comparsion on whether parameter type is NOT_SET
  (#1032)

* [rolling] Update maintainers (#1035)

* Set the default number of threads of the MultiThreadedExecutor to 2
  (#1031)

* Update the rclpy method documentation. (#1026)

* Revert "Raise user handler exception in MultiThreadedExecutor.
  (#984)" (#1017)

* Waitable should check callback_group if it can be executed. (#1001)

* support wildcard matching for params file (#987)

* Raise user handler exception in MultiThreadedExecutor. (#984)

* Add wait_for_node method (#930)

* Create sublogger for action server and action client (#982)

* Support for pre-set and post-set parameter callback. (#966)

* fix gcc 7.5 build errors (#977)

* make _on_parameter_event return result correctly (#817)

* Fix a small typo in documentation. (#967)

* Add Parameter Client (#959)

* Change sphinx theme to readthedocs (#950)

* Name and type in descriptor(s) is ignored via declare_parameter(s).
  (#957)

* Typo fix (#951)

* Add py.typed to package (#946)

* Fix rclpy.shutdown() from hanging when triggered from callback
  (#947)

* Check if the context is already shutdown. (#939)

* Avoid causing infinite loop when message is empty (#935)

* Expose 'best available' QoS policies (#928)

* remove feedback callback when the goal has been completed. (#927)

* Allow to create a subscription with a callback that also receives
  the message info (#922)

* Contributors: Achille Verheye, Audrow Nash, Barry Xu, Brian, Brian
  Chen, Chen Lihui, Chris Lalancette, Cristóbal Arroyo, Deepanshu
  Bansal, Emerson Knapp, Erki Suurjaak, Felix Divo, Florian Vahl,
  Gonzo, GuiHome, Ivan Santiago Paunovic, Jacob Perron, Lei Liu, Lucas
  Wendland, Michael Carroll, Sebastian Freitag, Seulbae Kim, Shane
  Loretz, Steve Nogar, Takeshi Ishita, Tomoya Fujita, Tony Najjar,
  Yadu, Yuki Igarashi, mergify[bot]

rcpputils
=========

* Add missing header for strlen (#169)

* issue-167 (#172)

* [rolling] Update maintainers - 2022-11-07 (#166)

* require C++17 and deprecate the rcppmath namespace (#165)

* Mirror rolling to master

* Fix possible race condition in create_directories() (#162)

* Contributors: Artem Shumov, Audrow Nash, Sebastian Freitag, William
  Woodall, bijoua29

rcutils
=======

* fix memory leak (#423)

* Add convenience error handling macros (#421)

* Calculate the next power-of-two for the user in hash_map_init.
  (#420)

* update cast to modern style (#418)

* Remove deprecated header get_env.h (#417)

* Updates to rcutils to make rosdoc2 generation happier. (#416)

* add RCUTILS_LOGGING_AUTOINIT_WITH_ALLOCATOR. (#415)

* Fix memory leak in string_map.c in rcutils (#411)

* avoid unnecessary copy for rcutils_char_array_vsprintf. (#412)

* Add missing stddef include for size_t (#410)

* Add SHA256 utility implementation (#408)

* Upgrade rcutils to C++17. (#392)

* [rolling] Update maintainers - 2022-11-07 (#404)

* Fix build on OpenHarmony (#395)

* regression of thread-safety for logging macros (#393)

* add portable nonnull macros (#382)

* Fix memory leak when adding the same key to the logger hash map
  multiple times (#391)

* time_unix: uses ZEPHYR_VERSION_CODE instead (#390)

* Cleanup time_unix.c (#389)

* time_unix: namespace zephyr headers (#383)

* Restrict overmatching MACH ifdef to only trigger on OSX and Mach
  (#386)

* Optimize rcutils_logging_get_logger_effective_level() (#381)

* Change syntax __VAR_ARGS__ to __VA_ARGS__ (#376)

* Fix a bug in hash_map_get_next_key_and_data. (#375)

* More fixes from review.

* Fixes from review.

* Make g_rcutils_logging_output_handler static.

* Make g_rcutils_logging_default_logger_level static.

* Optimize rcutils_find_lastn where possible.

* Don't bother computing the hash_map key if the hash map is empty.

* Make sure to expand char_array by at least 1.5x.

* Optimize index computation in hash_map_find.

* Improve the performance of rcutils_logging_format_message. (#372)

* Get rid of unnecessary ret variable.

* Get rid of unnecessary ifdef cplusplus checks in the C file.

* Get rid of unnecessary rcutils_custom_add_{gtest,gmock}

* Get rid of unnecessary and unused RMW switching for logging tests.

* Remove unnecessary IS_OUTPUT_COLORIZED macro.

* Rename logging internal structures to use our new convention.

* Make all of the logging 'expand' methods static.

* Fix up error checking for RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED.

* Cleanup error handling for the RCUTILS_CONSOLE_OUTPUT_FORMAT checks.

* Revamp error handling in rcutils_logging_initialize_with_allocator.

* Revamp rcutils_logging_initialize_with_allocator.

* Make a few logging global variables static.

* Optimize calls via the RCUTILS_LOG macros. (#369)

* time_unix: add zephyr posix time (#368)

* Optimize the implementation of rcutils_char_array_strncpy. (#367)

* strdup.c: fix arbitrary length overread (#366)

* Mirror rolling to master

* strdup.c: fix 1 byte buffer overread (#363)

* Clarify duration arg description in logging macros (#359)

* Update rcutils_steady_time_now to return the same data as
  std::chrono (#357)

* Contributors: AIxWall, Abrar Rahman Protyasha, Audrow Nash, Chen
  Lihui, Chris Lalancette, Emerson Knapp, Felipe Neves, Jacob Perron,
  Mario Prats, Maximilian Downey Twiss, Nikolai Morin, Tomoya Fujita,
  William Woodall, Yakumoo, guijan, methylDragon

rmw
===

* Dynamic Subscription (BONUS: Allocators): rmw (#353)

* Runtime Interface Reflection: rmw (#340)

* [rmw] Improve handling of dynamic discovery (#338)

* rmw_send_reqponse returns RMW_RET_TIMEOUT. (#350)

* Add a note about asynchronicity of discovery. (#352)

* Add matched event support (#331)

* Add type hash to rmw_topic_endpoint_info_t (rep2011) (#348)

* Add in inconsistent topic defines and data structures. (#339)

* Update documented expectations for GIDs (#335)

* Fix rmw->rwm typo (#347)

* Add rmw count clients, services (#334)

* make writer_guid uint8_t[] instead of int8_t for consistency with
  rmw_gid_t (#329)

* Update rmw to C++17. (#346)

* Reduce GID storage to 16 bytes. (#345)

* Move the RMW_CHECK_TYPE_IDENTIFIERS_MATCH macro to a C header.
  (#343)

* [rolling] Update maintainers - 2022-11-07 (#337)

* Remove unused test_loaned_message_sequence.cpp (#336)

* callback can be NULL to clear in Listener APIs. (#332)

* Add rmw_get_gid_for_client method (#327)

* Add 'best available' QoS policies (#320) The best available policy
  should select the highest level of service for the QoS setting while
  matching with the majority of endpoints. For example, in the case of
  a DDS middleware subscription, this means: * Prefer reliable
  reliability if all existing publishers on the same topic are
  reliable, otherwise use best effort. * Prefer transient local
  durability if all existing publishers on the same topic are
  transient local, otherwise use volatile. * Prefer manual by topic
  liveliness if all existing publishers on the same topic are manual
  by topic, otherwise use automatic. * Use a deadline that is equal to
  the largest deadline of existing publishers on the same topic. * Use
  a liveliness lease duration that is equal to the largest lease
  duration of existing publishers on the same topic.

* Move statuses definitions to rmw/events_statuses/ (#232)

* Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette,
  Emerson Knapp, Geoffrey Biggs, Jacob Perron, Lee, Minju, Nikolai
  Morin, Tomoya Fujita, William Woodall, methylDragon

rmw_connextdds
==============

* Dynamic Subscription (BONUS: Allocators): rmw_connextdds (#115)

* Revert "Refactor serialization support to use allocators and refs"

* Refactor serialization support to use allocators and refs

* Add stubs for new rmw interfaces (#111)

* Add rmw_get_gid_for_client impl (#92)

* Switch ROS2 -> ROS 2 everywhere (#83)

* Contributors: Brian, Chris Lalancette, methylDragon

rmw_connextdds_common
=====================

* [rmw_connextdds] New RMW discovery options (#108)

* Call get_type_hash_func (#113)

* Type hash distribution during discovery (rep2011) (#104)

* Implement matched event (#101)

* Add in implementation of inconsistent topic. (#103)

* Add rmw_get_gid_for_client impl (#92)

* Fix assert statement to allow the seconds field of a DDS_Duration_t
  to be zero (#88)

* Handle 'best_available' QoS policies in common (#85)

* Resolve build error with RTI Connext DDS 5.3.1 (#82)

* Contributors: Andrea Sorbini, Barry Xu, Brian, Chris Lalancette,
  Emerson Knapp, Grey, Jose Luis Rivero, Michael Carroll, Michael
  Jeronimo

rmw_connextddsmicro
===================

* Dynamic Subscription (BONUS: Allocators): rmw_connextdds (#115)

* Add stubs for new rmw interfaces (#111)

* Add rmw_get_gid_for_client impl (#92)

* Switch ROS2 -> ROS 2 everywhere (#83)

* Contributors: Brian, Chris Lalancette, methylDragon

rmw_cyclonedds_cpp
==================

* Dynamic Subscription (BONUS: Allocators): rmw_cyclonedds (#451)

* Add stubs for new rmw interfaces (#447)

* [rmw_cyclonedds] Improve handling of dynamic discovery (#429)

* Call get_type_hash_func (#448)

* Type hash distribution in discovery (rep2011) (#437)

* Disable inconsistent topic events. (#444)

* Implement matched event (#435)

* Implement inconsistent topic. (#431)

* Make sure to add semicolons to the CHECK_TYPE_IDENTIFIER_MATCH.
  (#432)

* [rolling] Update maintainers - 2022-11-07 (#428)

* Export CycloneDDS dependency (#424)

* add NULL check before accessing object. (#423)

* Add rmw_get_gid_for_client impl (#402)

* Makes topic_name a const ref

* Adds topic name to error msg when create_topic fails

* Improve error message when create_topic fails (#405)

* Change wrong use of %d to print uint32_t to PRIu32 (#253)

* Add cstring include. (#393)

* Handle 'best_available' QoS policies (#389)

* Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette,
  Emerson Knapp, Geoffrey Biggs, Jose Luis Rivero, Shane Loretz,
  Tomoya Fujita, Tully Foote, Voldivh, eboasson, methylDragon

rmw_dds_common
==============

* Type hash in GraphCache, user_data encoding tools (#70)

* Mark benchmark _ as unused. (#71)

* Update rmw_dds_common to C++17. (#69)

* Change Gid.msg to be 16 bytes. (#68)

* Minor cleanups of test_qos. (#67)

* [rolling] Update maintainers - 2022-11-07 (#65)

* build shared lib only if BUILD_SHARED_LIBS is set (#62)

* Update maintainers (#61)

* Add functions for resolving 'best available' QoS policies (#60)
  Given a QoS profile and set of endpoints for the same topic,
  overwrite any policies set to BEST_AVAILABLE with a policy such that
  it matches all endpoints while maintaining a high level of service.
  Add testable functions for updating BEST_AVAILABLE policies, *
  qos_profile_get_best_available_for_subscription *
  qos_profile_get_best_available_for_publisher and add convenience
  functions that actual query the graph for RMW implementations to
  use, * qos_profile_get_best_available_for_topic_subscription *
  qos_profile_get_best_available_for_topic_publisher

* Contributors: Audrow Nash, Chris Lalancette, Emerson Knapp, Jacob
  Perron, hannes09, methylDragon

rmw_fastrtps_cpp
================

* Dynamic Subscription (BONUS: Allocators): rmw_fastrtps (#687)

* Runtime Interface Reflection: rmw_fastrtps (#655)

* [rmw_fastrtps] Improve handling of dynamic discovery (#653)

* Call get_type_hash_func (#680)

* Type hash distribution in discovery (rep2011) (#671)

* Implement inconsistent topic event (#654)

* Update all rmw_fastrtps packages to C++17. (#674)

* Rewrite how Topics are tracked in rmw_fastrtps_cpp. (#669)

* Allow loaned messages without data-sharing (#568)

* Fix incoherent dissociate_writer to dissociate_reader (#647) (#649)

* [rolling] Update maintainers - 2022-11-07 (#643)

* Add rmw_get_gid_for_client impl (#631)

* Use Fast-DDS Waitsets instead of listeners (#619)

* Remove rosidl_cmake dependency (#629)

* Revert "add line feed for RCUTILS_SAFE_FWRITE_TO_STDERR (#608)"
  (#612)

* add line feed for RCUTILS_SAFE_FWRITE_TO_STDERR (#608)

* Allow null arguments in the EventsExecutor parameters (#602)

* Add RMW_CHECKS to rmw_fastrtps_cpp EventsExecutor implementation

* Handle 'best_available' QoS policies (#598)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Geoffrey Biggs, Jacob Perron, Jose Luis Rivero, Miguel Company,
  Oscarchoi, Ricardo González, Tomoya Fujita, methylDragon

rmw_fastrtps_dynamic_cpp
========================

* Dynamic Subscription (BONUS: Allocators): rmw_fastrtps (#687)

* Runtime Interface Reflection: rmw_fastrtps (#655)

* [rmw_fastrtps] Improve handling of dynamic discovery (#653)

* Call get_type_hash_func (#680)

* Type hash distribution in discovery (rep2011) (#671)

* Implement inconsistent topic event (#654)

* Update all rmw_fastrtps packages to C++17. (#674)

* Rewrite how Topics are tracked in rmw_fastrtps_cpp. (#669)

* Allow loaned messages without data-sharing (#568)

* Fix incoherent dissociate_writer to dissociate_reader (#647) (#649)

* [rolling] Update maintainers - 2022-11-07 (#643)

* Add rmw_get_gid_for_client impl (#631)

* Use Fast-DDS Waitsets instead of listeners (#619)

* Revert "add line feed for RCUTILS_SAFE_FWRITE_TO_STDERR (#608)"
  (#612)

* add line feed for RCUTILS_SAFE_FWRITE_TO_STDERR (#608)

* Allow null arguments in the EventsExecutor parameters (#602)

* Add EventExecutor to rmw_fastrtps_dynamic_cpp

* Fix cpplint error (#601)

* Handle 'best_available' QoS policies (#598)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Geoffrey Biggs, Jacob Perron, Jose Luis Rivero, Miguel Company,
  Oscarchoi, Ricardo González, Tomoya Fujita, methylDragon

rmw_fastrtps_shared_cpp
=======================

* Fix matched event issues (#683)

* Dynamic Subscription (BONUS: Allocators): rmw_fastrtps (#687)

* Check for triggered guard conditions before waiting (#685)

* Runtime Interface Reflection: rmw_fastrtps (#655)

* [rmw_fastrtps] Improve handling of dynamic discovery (#653)

* Type hash distribution in discovery (rep2011) (#671)

* Implement matched event (#645)

* Implement inconsistent topic event (#654)

* Update all rmw_fastrtps packages to C++17. (#674)

* Rewrite how Topics are tracked in rmw_fastrtps_cpp. (#669)

* Delay lock on message callback setters (#657)

* Make sure to add semicolons to the CHECK_TYPE_IDENTIFIER_MATCH.
  (#658)

* Allow loaned messages without data-sharing (#568)

* Fix incoherent dissociate_writer to dissociate_reader (#647) (#649)

* [rolling] Update maintainers - 2022-11-07 (#643)

* Remove duplicated code (#637)

* Call callbacks only if unread count > 0 (#634)

* Add rmw_get_gid_for_client impl (#631)

* Use Fast-DDS Waitsets instead of listeners (#619)

* Take all available samples on service/client on_data_available.
  (#616)

* Revert "add line feed for RCUTILS_SAFE_FWRITE_TO_STDERR (#608)"
  (#612)

* add line feed for RCUTILS_SAFE_FWRITE_TO_STDERR (#608)

* Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette,
  Emerson Knapp, Geoffrey Biggs, Michael Carroll, Miguel Company,
  Oscarchoi, Ricardo González, Tomoya Fujita, mauropasse, methylDragon

rmw_implementation
==================

* Dynamic Subscription (BONUS: Allocators): rmw_implementation (#219)

* Runtime Interface Reflection: rmw_implementation (#215)

* Mark the benchmark _ variables as unused. (#218)

* Update rmw_implementation to C++17. (#214)

* [rolling] Update maintainers - 2022-11-07 (#212)

* Build-time RMW selection does not need ament_index_cpp (#210)

* Add rmw_get_gid_for_client & tests (#206)

* Contributors: Audrow Nash, Brian, Chris Lalancette, G.A. vd. Hoorn,
  methylDragon

rmw_implementation_cmake
========================

* [rolling] Update maintainers - 2022-11-07 (#337)

* Contributors: Audrow Nash

robot_state_publisher
=====================

* Update robot_state_publisher to C++17. (#204)

* [rolling] Update maintainers - 2022-11-07 (#203)

* Mirror rolling to ros2

* Contributors: Audrow Nash, Chris Lalancette

ros2action
==========

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette

ros2bag
=======

* Cleanup the help text for ros2 bag record. (#1329) (#1333)

* Enable document generation using rosdoc2 for ament_python pkgs
  (#1260)

* CLI: Get storage-specific values from plugin (#1209)

* Fix up some of the wording in the record help text. (#1228)

* Add topic_name option to info verb (#1217)

* rosbag2_storage: set MCAP as default plugin (#1160)

* rosbag2_py: parametrize tests across storage plugins (#1203)

* Added option to change node name for the recorder from the Python
  API (#1180)

* rosbag2_cpp: test more than one storage plugin (#1196)

* rosbag2_storage: expose default storage ID as method (#1146)

* Fix for ros2 bag play exit with non-zero code on SIGINT (#1126)

* ros2bag: move storage preset validation to sqlite3 plugin (#1135)

* Add option to prevent message loss while converting (#1058)

* Added support for excluding topics via regular expressions (#1046)

* Readers/info can accept a single bag storage file, and detect its
  storage id automatically (#1072)

* Add short -v option to ros2 bag list for verbose (#1065)

* Use a single variable for evaluating the filter regex (#1053)

* Add additional mode of publishing sim time updates triggered by
  replayed messages (#1050)

* Renamed --topics-regex to --regex and -e in Player class to be
  consistent with Recorder (#1045)

* Use first available writer in recording if default "sqlite3" not
  available. (#1044)

* Add the ability to record any key/value pair in 'custom' field in
  metadata.yaml (#1038)

* Added support for filtering topics via regular expressions on
  Playback (#1034)

* Fix incorrect boundary check for "playback_duration" and
  "play_until_timestamp" (#1032)

* Adds play until timestamp functionality (#1005)

* Add CLI verb for burst mode of playback (#980)

* Add play-for specified number of seconds functionality (#960)

* Make unpublished topics unrecorded by default (#968)

* Contributors: Agustin Alba Chicar, Chris Lalancette, DensoADAS,
  Emerson Knapp, EsipovPA, Esteve Fernandez, Geoffrey Biggs, Hunter
  L.Allen, Keisuke Shima, Michael Orlov, Sean Kelly, Tony Peng, Yadu,
  james-rms, kylemarcey, mergify[bot], ricardo-manriquez

ros2cli
=======

* Set automatically_declare_parameters_from_overrides in DirectNode.
  (#813)

* Enable document generation using rosdoc2 (#811)

* Fix linters (#808)

* add timeout option for ros2param to find node. (#802)

* Save method list via connection check to XMLRPC server. (#796)

* ZSH argcomplete: call compinit only if needed (#750)

* Fix network aware node issue (#785)

* [rolling] Update maintainers - 2022-11-07 (#776)

* XMLRPC server accepts request from all local IP addresses. (#729)

* Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo, Ivan
  Santiago Paunovic, Tomoya Fujita, Yadu, mjbogusz

ros2cli_common_extensions
=========================

* [rolling] Update maintainers - 2022-11-07 (#7)

* Update maintainers (#6)

* Contributors: Audrow Nash, methylDragon

ros2cli_test_interfaces
=======================

* [rolling] Update maintainers - 2022-11-07 (#776)

* Remove action_msgs dependency (#743)

* Contributors: Audrow Nash, Jacob Perron

ros2component
=============

* Enable document generation using rosdoc2 (#811)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Fix the component load help to mention load, not unload. (#756)

* Remove unused arguments from ros2 component types. (#711)

* Contributors: Audrow Nash, Chris Lalancette, Yadu

ros2doctor
==========

* Shutdown ros2doctor hello when ctrl-c is received (#829)

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* Enable document generation using rosdoc2 (#811) * Fix warnings for
  ros2component, ros2doctor, ros2interface, and ros2node

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette, Michael Carroll, Yadu

ros2interface
=============

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* Enable document generation using rosdoc2 (#811)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette, Yadu

ros2launch
==========

* [rolling] Update maintainers - 2022-11-07 (#331)

* Contributors: Audrow Nash

ros2lifecycle
=============

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette

ros2lifecycle_test_fixtures
===========================

* Update the ros2cli test fixture to C++17. (#789)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette

ros2multicast
=============

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Add --group and --port options to ros2 multicast (#770)

* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

ros2node
========

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* Enable document generation using rosdoc2 (#811) * Fix warnings for
  ros2component, ros2doctor, ros2interface, and ros2node

* Fix linters (#808)

* add timeout option for ros2param to find node. (#802)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Updated wording in list.py (#775)

* Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo,
  Michael Wrock, Tomoya Fujita, Yadu

ros2param
=========

* remove deprecated options (#824)

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* add timeout option for ros2param to find node. (#802)

* Fix printing of integer and double arrays. (#804)

* [rolling] Update maintainers - 2022-11-07 (#776)

* refactor: make ros2param use rclpy.parameter_client (#716)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Tomoya Fujita

ros2pkg
=======

* Fix typo in ros2pkg warning message. (#828)

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* resolve #790 (#801)

* Add alias library targets for CMake (#718)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette, Kenji Brameld, RFRIEDM-
  Trimble, Tomoya Fujita

ros2run
=======

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette

ros2service
===========

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* [rolling] Update maintainers - 2022-11-07 (#776)

* Contributors: Audrow Nash, Chris Lalancette

ros2test
========

* [rolling] Update maintainers - 2022-11-07 (#12)

* update maintainer

* Contributors: Audrow Nash, Dharini Dutia, quarkytale

ros2topic
=========

* remove deprecated options (#824)

* Make all of the dependencies in pure Python packages exec_depend.
  (#823)

* Expect type hash cli output in test (#822)

* Fix the type annotation in pub.py. (#814)

* Switch to using new event_handler instead of qos_event. (#787)

* avoid flaky test that subscriber might not receive the message
  (#810)

* Adds a "--max-wait-time" option to "ros2 topic pub" (#800)

* Fix some flake8 warnings related to style. (#805)

* Adds a timeout feature to rostopic echo (#792)

* Refactor common types (#791)

* Allow configuring liveliness in ros2 topic echo and pub (#788)

* Extend timeout to shutdown the command line process. (#783)

* [rolling] Update maintainers - 2022-11-07 (#776)

* a couple of typo fixes. (#774)

* Add support use_sim_time for ros2 topic hz/bw/pub. (#754)

* Use set_message_fields from rosidl_runtime_py (#761)

* Expand auto to the current time when passed to a Header field (#749)

* Add verbose option to echo that also prints the associated message
  info (#707)

* update docs for bandwidth functions. (#709)

* Split the bandwidth functions into a get and print. (#708)

* Contributors: Arjo Chakravarty, Audrow Nash, Chen Lihui, Chris
  Lalancette, Emerson Knapp, Esteve Fernandez, Ivan Santiago Paunovic,
  Lei Liu, Tomoya Fujita

ros2trace
=========

* Move ros2trace tests to new test_ros2trace package (#63)

* Error out if trace already exists unless 'append' option is used
  (#58)

* Improve 'ros2 trace' command error handling & add end-to-end tests
  (#54)

* Contributors: Christophe Bedard

ros_testing
===========

* [rolling] Update maintainers - 2022-11-07 (#12)

* update maintainer

* Contributors: Audrow Nash, Dharini Dutia, quarkytale

rosbag2
=======

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Move sqlite3 storage implementation to rosbag2_storage_sqlite3
  package (#1113)

* Contributors: Emerson Knapp, Michael Orlov

rosbag2_compression
===================

* Add in a missing cstdint include. (#1321) (#1322)

* Fix warning from ClassLoader in sequential compression reader and
  writer (#1299) (#1316)

* Add message definition read API (#1292)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* set_read_order: return success (#1177)

* Add "update_metadata(BagMetadata)" API for storage plugin interface
  (#1149)

* Reverse read order API and sqlite storage implementation (#1083)

* Add option to prevent message loss while converting (#1058)

* set default metadata of compressed message (in case compressor does
  not set it) (#1060)

* Speed optimization: Preparing copyless publish/subscribing by using
  const message for writing (#1010)

* Add the ability to record any key/value pair in 'custom' field in
  metadata.yaml (#1038)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, DensoADAS,
  Emerson Knapp, Hunter L. Allen, Joshua Hampp, Michael Orlov, Tony
  Peng, james-rms, mergify[bot]

rosbag2_compression_zstd
========================

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Speed optimization: Preparing copyless publish/subscribing by using
  const message for writing (#1010)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, DensoADAS,
  Joshua Hampp, Michael Orlov

rosbag2_cpp
===========

* Add recorder stop() API (#1300) (#1334)

* Add type_hash in MessageDefinition struct (#1296)

* Add message definition read API (#1292)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* Fix for flaky "TimeControllerClockTest::unpaused_sleep_returns_true"
  test (#1290)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Fix rwm->rmw spelling (#1249)

* Expose more Writer methods in python interface (#1220)

* rosbag2_storage: set MCAP as default plugin (#1160)

* Parametrize all rosbag2_tests for both supported storage plugins
  (#1221)

* rosbag2_cpp: test more than one storage plugin (#1196)

* Replace language for "db3"/"db"/"database" (#1194)

* set_read_order: return success (#1177)

* Remove explicit sqlite3 from code (#1166)

* Add "update_metadata(BagMetadata)" API for storage plugin interface
  (#1149)

* Reader and writer can use default storage by not specifying (#1167)

* rosbag2_storage: expose default storage ID as method (#1146)

* Don't reopen file for every seek if we don't have to. Search
  directionally for the correct file (#1117)

* Add SplitBagfile recording service. (#1115)

* Reverse read order API and sqlite storage implementation (#1083)

* Replace "std::filesystem::path(..)" with "rcpputils::fs::path(..)"
  (#1104)

* Fix issue where sequentialwriter only sets metadata duration to the
  duration of the final file (#1098)
