# Humble Hawksbill changelog (part 4 of 5)

* corrected publish_frequency default in README (#166)

* Add tf frame_prefix parameter (#159)

* Contributors: Abrar Rahman Protyasha, Anthony Deschamps, Chris
  Lalancette, Jacob Perron, Kenji Brameld, Nils Schulte, Russell
  Joyce, Shane Loretz, Steve Nogar

ros2action
==========

* Add timeout to kill hanging tests (#701)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Shane Loretz

ros2bag
=======

* support to publish as loaned message (#981)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* support to publish as loaned message (#981)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Bump version number to avoid conflict

* Make sure published messages are acknowledged for play mode (#951)

* TopicFilter use regex_search instead of regex_match (#932)

* Add start-offset play option (#931)

* Expose bag_rewrite as "ros2 bag convert" (#921)

* Add "ignore leaf topics" option to recorder (#925)

* Auto-detect storage_id for Reader (if possible) (#918)

* Add pause/resume options to the bag recorder (#905)

* Add --start-paused option to "ros2 bag play" (#904)

* Update package maintainers (#899)

* Fix converter plugin choices for record (#897)

* Add missing spaces to error message (#875)

* keyboard controls for pause/resume toggle and play-next: (#847)

* Add --snapshot-mode argument to the "record" verb (#851)

* Refactor plugin query mechanism and standardize trait management
  (#833)

* Update "PlayOptions::delay" to "rclcpp::Duration" to get nanosecond
  resolution (#843)

* Load compression and serialization choices via plugin query (#827)

* Add delay option (#789)

* Avoid passing exception KeyboardInterrupt to the upper layer (#788)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Cameron
  Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic,
  Jacob Perron, Jorge Perez, Kosuke Takeuchi, Michel Hidalgo, Sonia
  Jin, Tony Peng

ros2cli
=======

* Fix importlib_metadata warning on Python 3.10. (#706)

* Add timeout to kill hanging tests (#701)

* Use try_shutdown() instead of shutdown() in DirectNode.__exit__()
  (#683)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Reapply #659 (#661)

* Revert "Make the ros2cli output always line buffered (#659)" (#660)

* Make the ros2cli output always line buffered (#659)

* add uuid to ros2 daemon node name. (#658)

* Transfer daemon socket ownership on spawn. (#652)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Ivan
  Santiago Paunovic, Michel Hidalgo, Tomoya Fujita

ros2cli_test_interfaces
=======================

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

ros2component
=============

* Add timeout to kill hanging tests (#701)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Drop deprecated get_container_components_info() API. (#647)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Michel Hidalgo

ros2doctor
==========

* Fix importlib_metadata warning on Python 3.10. (#706)

* Add timeout to kill hanging tests (#701)

* Switch ros2 doctor to using psutil for network checks. (#687)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Improve ros2 doctor on Windows. (#631)

* Add QoS compatibility check and report. (#621)

* Contributors: Aditya Pande, Alberto Soragna, Audrow Nash, Chris
  Lalancette, Ivan Santiago Paunovic, Shane Loretz

ros2interface
=============

* Add timeout to kill hanging tests (#701)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Shane Loretz

ros2launch
==========

* Update maintainers in setup.py (#287)

* Use frontend group dependency & explicit dependencies in ros2launch
  (#256)

* Update package maintainers (#284)

* Add regex filter for selective launch-prefix application (#261)

* Resolves #37 - Added --launch-prefix argument for 'ros2 launch'
  command (#254)

* Use sets of file extensions provided by parser extensions (#252)

* Simplify logic to fix absolute paths (#230)

* add way to include other Python launch files (launch #122)

* Contributors: Audrow Nash, Cameron Miller, Christophe Bedard, Michel
  Hidalgo, rob-clarke

ros2lifecycle
=============

* Add timeout to kill hanging tests (#701)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Shane Loretz

ros2lifecycle_test_fixtures
===========================

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

ros2multicast
=============

* Add timeout to kill hanging tests (#701)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

ros2node
========

* Add timeout to kill hanging tests (#701)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Shane Loretz

ros2param
=========

* Add timeout to kill hanging tests (#701)

* Fix how ros2 param interprets command-line arguments. (#684)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Removed redundant code (#666)

* Reapply #659 (#661)

* Fix flaky ros2 param list (#656)

* Skip None Result (#646)

* add '--write' option to avoid an unintentional data loss. (#638)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Ivan
  Santiago Paunovic, Jacob Perron, Jay Wang, Tomoya Fujita

ros2pkg
=======

* Add timeout to kill hanging tests (#701)

* Use local git config instead of global (#693)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* [ros2pkg] Skip copyright tests in template packages (#676)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Generate LICENSE files on ros2 pkg create. (#650)

* Handle ValueError (#643)

* Pass package exports to template in pkg create api (#619) (#628)

* Add changelogs (#635)

* Contributors: Abrar Rahman Protyasha, Aditya Pande, Amro Al-Baali,
  Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Shane Loretz,
  rob-clarke, tim-fan

ros2run
=======

* Add timeout to kill hanging tests (#701)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* check subprocess.returncode to print error message. (#639)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Tomoya Fujita

ros2service
===========

* Add timeout to kill hanging tests (#701)

* Also provide --include-hidden-services for "ros2 service list" verb
  (#551)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Add changelogs (#635)

* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic,
  Karsten Knese, Shane Loretz

ros2test
========

* Use new domain_coordinator API (#10)

* Contributors: Timo Röhling

ros2topic
=========

* Add timeout to kill hanging tests (#701)

* Add yaml dump flow style. (#698)

* support ros2topic echo once option. (#695)

* Fix special case for fastrtps incompatible QoS. (#694)

* Depend on launch packages instead of ros_testing to avoid circular
  dependency (#685)

* Add QoS history and depth information if available. (#678)

* Cleanup mislabeled BSD license (#447)

* Update maintainers to Aditya Pande, Audrow Nash, and Michael
  Jeronimo (#673)

* Updated maintainers (#670)

* Update lost messages test case (#669)

* Implementation of message filtering for ros2 (#654)

* Change default QoSProfile for pub (#653)

* Add option in ros2 topic pub to wait for N matching subscriptions,
  use N=1 by default when combined with --times (#642)

* "ros2 topic pub" starts publishing right away. (#626)

* Fix Topic Info Test with "Infinite" printing (#616)

* Add changelogs (#635)

* QoS autodetection (#613)

* Make Lost Messages option ON by default (#633)

* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Emerson
  Knapp, Gonzo, Ivan Santiago Paunovic, Jorge Perez, Shane Loretz,
  Tomoya Fujita, Tully Foote, matthews-jca

ros2trace
=========

* Fix 'ros2 trace' fini() error

* Don't require kernel tracer and detect when it's not installed

* Deprecate 'context_names' param and replace with 'context_fields'

* Contributors: Christophe Bedard

rosbag2
=======

* Bump version number to avoid conflict

* Update package maintainers (#899)

* Contributors: Chris Lalancette, Michel Hidalgo

rosbag2_compression
===================

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Remove unnecessary public definition. (#950)

* Changes for uncrustify 0.72 (#937)

* Bugfix for broken bag split when using cache (#936)

* Update package maintainers (#899)

* Don't preprocess a storage file more than once (#895)

* added seek interface (#836)

* Refactor plugin query mechanism and standardize trait management
  (#833)

* fix sequential reader rollover-to-next-file strategy: (#839)

* Load compression and serialization choices via plugin query (#827)

* Contributors: Cameron Miller, Chris Lalancette, Michael Orlov,
  Michel Hidalgo, Shane Loretz, sonia

rosbag2_compression_zstd
========================

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Update package maintainers (#899)

* Contributors: Chris Lalancette, Michel Hidalgo, Shane Loretz

rosbag2_cpp
===========

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Remove unnecessary public definition. (#950)

* Fix relative path syntax for cpplint (#947)

* Mark up the message_cache with TSA annotations (#946)

* Changes for uncrustify 0.72 (#937)

* Redesign in cache consumer and circular message cache to get rid
  from busy loop (#941)

* Bugfix for broken bag split when using cache (#936)

* Remove JumpHandler copy-implementation from
  PlayerClock/TimeControllerClock (#935)

* Auto-detect storage_id for Reader (if possible) (#918)

* Add --start-paused option to "ros2 bag play" (#904)

* Use the message_introspection header to get MessageMember. (#903)

* Update package maintainers (#899)

* Fix converter plugin choices for record (#897)

* Enable sanitizers only if code actually can run (#572)

* Need to pass introspection TS to converter plugin for it to be
  useful (#896)

* Don't preprocess a storage file more than once (#895)

* Fix a bug on invalid pointer address when using "MESSAGE"
  compressio… (#866)

* Metadata per file info (#870)

* Fix TSA warnings when building with clang thread analysis. (#877)

* Implement snapshot mechanism and corresponding ROS Service (#850)

* Circular Message Cache implementation for snapshot feature (#844)

* Fix discovery silently stops after unknown msg type is found. (#848)

* added seek interface (#836)

* Refactor plugin query mechanism and standardize trait management
  (#833)

* fix sequential reader rollover-to-next-file strategy: (#839)

* Load compression and serialization choices via plugin query (#827)

* Workaround for false positive findings by clang thread safety
  analysis in time controller jump callbacks API. (#799)

* Add callbacks for PlayerClock::jump(time_point) API with CI fix
  (#779)

* Revert "Add callbacks for PlayerClock::jump(time_point) API (#775)"
  (#778)

* Add callbacks for PlayerClock::jump(time_point) API (#775)

* Contributors: Audrow Nash, Barry Xu, Cameron Miller, Chris
  Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron,
  Jorge Perez, Lei Liu, Michael Orlov, Michel Hidalgo, Shane Loretz,
  Tony Peng, Wojciech Jaworski, sonia

rosbag2_interfaces
==================

* Bump version number to avoid conflict

* Add burst-mode to Player (#977)

* Update package maintainers (#899)

* Implement snapshot mechanism and corresponding ROS Service (#850) *
  Add snapshot service to recorder node * Simplify and clarify double
  buffering patterns

* Contributors: Cameron Miller, Chris Lalancette, Geoffrey Biggs,
  Michel Hidalgo

rosbag2_performance_benchmarking
================================

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Enable YAML encoding/decoding for RecordOptions and StorageOptions
  (#916) * Enable YAML encoding/decoding for RecordOptions and
  StorageOptions

* Update package maintainers (#899)

* Updated node declare_parameter to new syntax (#882)

* Updated benchmark package to use writer close() instead of old
  reset() (#881)

* Contributors: Adam Dąbrowski, Chris Lalancette, Emerson Knapp,
  Michel Hidalgo, Shane Loretz

rosbag2_py
==========

* support to publish as loaned message (#981)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* support to publish as loaned message (#981)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Bump version number to avoid conflict

* Make sure published messages are acknowledged for play mode (#951)

* Fix relative path syntax for cpplint (#947)

* Update to pybind11 2.7.1 (#945)

* Add start-offset play option (#931)

* Expose bag_rewrite as "ros2 bag convert" (#921)

* Add "ignore leaf topics" option to recorder (#925)

* Add a ReaderWriterFactory utility to share logic for reuse (#923)

* Add pause/resume options to the bag recorder (#905)

* Add --start-paused option to "ros2 bag play" (#904)

* Update package maintainers (#899)

* Fix converter plugin choices for record (#897)

* Metadata per file info (#870)

* keyboard controls for pause/resume toggle and play-next: (#847)

* Add --snapshot-mode argument to the "record" verb (#851)

* Add stopRecording into rosbag2_py (#854)

* added seek interface (#836)

* Refactor plugin query mechanism and standardize trait management
  (#833)

* Update "PlayOptions::delay" to "rclcpp::Duration" to get nanosecond
  resolution (#843)

* Load compression and serialization choices via plugin query (#827)

* Add delay option (#789)

* Handle SIGTERM gracefully in recording (#792)

* Contributors: Abrar Rahman Protyasha, Afonso da Fonseca Braga,
  Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson
  Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Kosuke
  Takeuchi, Michel Hidalgo, Tony Peng, Wojciech Jaworski, sonia

rosbag2_storage
===============

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Remove unnecessary public definition. (#950)

* Enable YAML encoding/decoding for RecordOptions and StorageOptions
  (#916)

* Update package maintainers (#899)

* Provide MetadataIO interface to convert metadata to a string in
  memory, alongside file IO versions (#894)

* Metadata per file info (#870)

* Implement snapshot mechanism and corresponding ROS Service (#850)

* added seek interface (#836)

* Refactor plugin query mechanism and standardize trait management
  (#833)

* Contributors: Audrow Nash, Cameron Miller, Chris Lalancette, Emerson
  Knapp, Jorge Perez, Michel Hidalgo, Shane Loretz, Tony Peng,
  Wojciech Jaworski, sonia

rosbag2_storage_default_plugins
===============================

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Emit a warning rather than crash when a message is too big for
  sqlite (#919)

* Enable YAML encoding/decoding for RecordOptions and StorageOptions
  (#916)

* Update package maintainers (#899)

* added seek interface (#836)

* Contributors: Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane
  Loretz, William Woodall, sonia

rosbag2_test_common
===================

* Bump version number to avoid conflict

* Install headers to include/${PROJECT_NAME} (#958)

* Update package maintainers (#899)

* Make sure the subscription exists before publishing messages (#804)

* Handle SIGTERM gracefully in recording (#792)

* Add spin_and_wait_for_matched to PublicationManager and update test
  c… (#797)

* Avoid passing exception KeyboardInterrupt to the upper layer (#788)

* Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michel
  Hidalgo, Shane Loretz

rosbag2_tests
=============

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Revert "Add the ability to record any key/value pair in the 'custom'
  field in metadata.yaml (#976)" (#984)

* Add the ability to record any key/value pair in the 'custom' field
  in metadata.yaml (#976)

* Bump version number to avoid conflict

* Add pause/resume options to the bag recorder (#905)

* Update package maintainers (#899)

* Fix a bug on invalid pointer address when using "MESSAGE"
  compressio… (#866)

* Metadata per file info (#870)

* Fix record test to reflect plugin query changes (#838)

* Make sure the subscription exists before publishing messages (#804)

* Handle SIGTERM gracefully in recording (#792)

* Add spin_and_wait_for_matched to PublicationManager and update test
  c… (#797)

* Remove rmw_fastrtps_cpp find_package in rosbag2_tests (#774)

* Contributors: Audrow Nash, Barry Xu, Cameron Miller, Chris
  Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jorge Perez,
  Michel Hidalgo, Tony Peng, Wojciech Jaworski

rosbag2_transport
=================

* support to publish as loaned message (#981)

* support to publish as loaned message (#981)

* Bump version number to avoid conflict

* Add burst-mode to Player (#977)

* Install headers to include/${PROJECT_NAME} (#958)

* Make sure published messages are acknowledged for play mode (#951)

* Changes for uncrustify 0.72 (#937)

* TopicFilter use regex_search instead of regex_match (#932)

* Add start-offset play option (#931)

* Add parentheses suggested by Clang on OSX to fix build warning
  (#930)

* Bag rewriter (C++) (#920)

* Add "ignore leaf topics" option to recorder (#925)

* Rewrite TopicFilter for single-call reusability (#924)

* Add a ReaderWriterFactory utility to share logic for reuse (#923)

* Add pause/resume options to the bag recorder (#905)

* Add logging macros for rosbag2_transport (#917)

* Enable YAML encoding/decoding for RecordOptions and StorageOptions
  (#916)

* Expose the QoS object wrapper (#910)

* Add --start-paused option to "ros2 bag play" (#904)

* Update package maintainers (#899)

* Add a Seek service (#874)

* Add simple keyboard control for playback rate (#893)

* Fix a bug on invalid pointer address when using "MESSAGE"
  compressio… (#866)

* Fix typo (#880)

* Use Reader's seek() method for seeking/jumping in Player (#873)

* keyboard controls for pause/resume toggle and play-next: (#847)

* Implement snapshot mechanism and corresponding ROS Service (#850)

* Circular Message Cache implementation for snapshot feature (#844)

* Add jump/seek API for Player class (#826)

* Restructure test_play_timing to one test per case, to see which
  times out (#863)

* Fix discovery silently stops after unknown msg type is found. (#848)

* Fixing deprecated subscriber callback warnings (#852)

* Bugfix for race condition in Player::peek_next_message_from_queue()
  (#849)

* added seek interface (#836)

* Update "PlayOptions::delay" to "rclcpp::Duration" to get nanosecond
  resolution (#843)

* Move notification about ready for playback inside
  play_messages_from_queue() (#832)

* Add wait for player to be ready for playback in Player::play_next()
  method (#814)

* Make sure the subscription exists before publishing messages (#804)

* Add delay option (#789)

* Copy recorder QoS profile to local variable so that temporary value
  isn't cleared (#803)

* test_play_services: fail gracefully on future error (#798)

* Recording with --all and --exclude fix (#765)

* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Bastian
  Jäger, Cameron Miller, Chris Lalancette, Emerson Knapp, Geoffrey
  Biggs, Ivan Santiago Paunovic, Kosuke Takeuchi, Lei Liu, Louise
  Poubel, Michael Orlov, Michel Hidalgo, Piotr Jaroszek, Shane Loretz,
  sonia

rosgraph_msgs
=============

* Update maintainers to Chris Lalancette (#130)

* Contributors: Audrow Nash

rosidl_adapter
==============

* rename nested loop index (#643)

* Fix how comments in action interfaces are processed (#632)

* Pass comments in ros interface constants to the .idl generated files
  (#630)

* Update package maintainers (#624)

* Make rosidl packages use FindPython3 instead of FindPythonInterp
  (#612)

* Fix escaping in string literals (#595)

* Ignore multiple "#" characters and dedent comments (#594)

* Contributors: Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz,
  ibnHatab

rosidl_cli
==========

* Fix importlib_metdata warning with Python 3.10. (#674)

* Update maintainers to Michel Hidalgo and Shane Loretz (#633)

* Update package maintainers (#624)

* Support passing keyword arguments to rosidl CLI extensions (#597)

* Add missing f for format string (#600)

* Contributors: Audrow Nash, Chris Lalancette, Michel Hidalgo, Shane
  Loretz

rosidl_cmake
============

* Make rosidl_get_typesupport_target return -NOTFOUND instead of
  FATAL_ERROR (#672)

* Add introspection typesupport tests for C/C++ messages (#651)

* Use target output name for exporting typesupport library (#625)

* Update package maintainers (#624)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#611)

* Add rosidl_get_typesupport_target and deprecate
  rosidl_target_interfaces (#606)

* Bundle and ensure the exportation of rosidl generated targets (#601)

* Contributors: Jonathan Selling, Michel Hidalgo, Shane Loretz

rosidl_default_generators
=========================

* Unroll group dependencies (#20)

* Contributors: Shane Loretz

rosidl_default_runtime
======================

* Unroll group dependencies (#20)

* Contributors: Shane Loretz

rosidl_generator_c
==================

* Fix error handling when copying C sequence messages (#671)

* Install generated headers to include/${PROJECT_NAME} (#670)

* Misc cleanup in the rosidl generator extensions (#662)

* Set the output size unconditionally when copying sequences (#669)

* Implement copy function for C messages (#650)

* Implement equality operator function for C messages. (#648)

* Generate documentation in generated C header files based on ROS
  interfaces comments (#593)

* Update package maintainers (#624)

* Make rosidl packages use FindPython3 instead of FindPythonInterp
  (#612)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#611)

* Bundle and ensure the exportation of rosidl generated targets (#601)

* Fix a cpplint allocator regression. (#590)

* Use RCUtils allocators in rosidl_generator_c (#584)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel
  Hidalgo, Nikolai Morin, Pablo Garrido, Shane Loretz

rosidl_generator_cpp
====================

* Install generated headers to include/${PROJECT_NAME} (#670)

* Misc cleanup in the rosidl generator extensions (#662)

* Add missing build_export_depend dependency (#665)

* Fix bug where rosidl_runtime_cpp wasn't depended upon (#660)

* Fix include order for cpplint (#644)

* Set CXX standard to 17 (#635)

* Update package maintainers (#624)

* Make rosidl packages use FindPython3 instead of FindPythonInterp
  (#612)

* Support flow style YAML printing (#613)

* Revert "Bundle and ensure the exportation of rosidl generated
  targets" (#611)

* Relocate to_yaml() under message namespace (#609)

* Bundle and ensure the exportation of rosidl generated targets (#601)

* Contributors: Jacob Perron, Jorge Perez, Michel Hidalgo, Shane
  Loretz, Øystein Sture

rosidl_generator_dds_idl
========================

* Add changelog (#56)

* Contributors: Ivan Santiago Paunovic

rosidl_generator_py
===================

* Removes erroneous unmatched closing parenthesis (#125)

* require Python 3.6 as we use format strings in various places (#152)

* Fix rosidl_generator_py assuming incorect library names (#149)

* Fix for msg file containing a property field that is not at the end
  (#151)

* Update package maintainers (#147)

* Use rosidl_get_typesupport_target() (#139)

* Support available typesupport specification in CLI extension (#133)

* Use python_d for test_cli_extension in Debug mode (#136)

* Add missing float/double bounds check (#128)

* Added optimization for copying arrays using buffer protocol (#129)

* Add smoke test for CLI extension (#132)

* Install generated Python interfaces in a Python package (#131)

* Contributors: Charles Cross, Chen Lihui, Michel Hidalgo, Seulbae
  Kim, Shane Loretz, William Woodall, ksuszka

rosidl_parser
=============

* Set maybe_placeholders to False for lark 1.+ compatibility (#664)

* Generate documentation in generated C header files based on ROS
  interfaces comments (#593)

* Pass comments in ros interface constants to the .idl generated files
  (#630)

* Update package maintainers (#624)

* Fix escaping in string literals (#595)

* Contributors: Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz

rosidl_runtime_c
================

* Fix error handling when copying C sequence messages (#671)
