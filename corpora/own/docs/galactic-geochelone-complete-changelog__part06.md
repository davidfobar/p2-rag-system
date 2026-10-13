# Galactic Geochelone changelog (part 6 of 8)

* Fix up C functions to never throw. (#149)

* Restored Dirk as author (#155)

* Update maintainers (#154)

* Updated performance QD section (#153)

* Update Quality Declaration to QL2. (#151)

* Add nominal test for symbol prefetch() and unload. (#145)

* Added benchmark test to rmw_implementation (#127)

* Test load and lookup functionality. (#135)

* Remove domain_id and localhost_only from node API (#114)

* Move the quality declaration into the rmw_implementation
  subdirectory. (#111)

* Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna,
  Andrea Sorbini, Chris Lalancette, Ivan Santiago Paunovic, Jacob
  Perron, Michel Hidalgo, Scott K Logan, Stephen Brawner, shonigmann

rmw_implementation_cmake
========================

* Shorten some excessively long lines of CMake (#300)

* Change default RMW vendor to CycloneDDS. (#293)

* Update rmw QD to QL 1 (#289)

* Update maintainers (#282)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Scott K
  Logan, Stephen Brawner

robot_state_publisher
=====================

* Stop rejecting unknown parameters. (#161)

* clean up license to be standard bsd 3 clause (#130)

* Update the maintainers. (#151)

* fix types in range loops to avoid copy due to different type (#143)

* Make sure not to crash on an invalid URDF. (#141)

* Don't export exe as library (#25) (ros2 #28)

* Contributors: Chris Lalancette, Dirk Thomas, Tully Foote

ros1_bridge
===========

* Fix logging for updated rclcpp interface (#303)

* Fix typo in comments (#297)

* Update to use rosidl_parser and .idl files rather than
  rosidl_adapter and .msg files (#296)

* Update maintainers (#286)

* use hardcoded QoS (keep all, transient local) for /tf_static topic
  in dynamic_bridge (#282)

* document explicitly passing the topic type to 'ros2 topic echo'
  (#279)

* Fix multiple definition if message with same name as service exists
  (#272)

* Contributors: Dirk Thomas, Jacob Perron, Michael Carroll, Vicidel,
  William Woodall

ros2action
==========

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

ros2bag
=======

* /clock publisher in Player (#695)

* Introducing Reindexer CLI (#699)

* rosbag2_py pybind wrapper for "record" - remove rosbag2_transport_py
  (#702)

* Add rosbag2_py::Player::play to replace rosbag2_transport_python
  version (#693)

* Explicitly add emersonknapp as maintainer (#692)

* use rosbag2_py for ros2 bag info (#673)

* CLI query rosbag2_py for available storage implementations (#659)

* Recorder --regex and --exclude options (#604)

* Fix the tests on cyclonedds by translating qos duration values
  (#606)

* SQLite storage optimized by default (#568)

* Fix a bug on parsing wrong description in plugin xml file (#578)

* Compress bag files in separate threads (#506)

* Sqlite storage double buffering (#546) * Double buffers * Circular
  queue and FLUSH option as define * Minor naming and lexical fixes. *
  Removed FLUSH_BUFFERS define check. * Sqlite3 storage logging fixes.
  * Sqlite3 storage circular buffer with pre allocated memory. *
  Sqlite3 storage buffers moved to shared_ptrs. * Uncrustify * Moved
  double buffers to writer * Buffer layer reset in seq compression
  writer in rosbag2 cpp * Buffer layer for rosbag2 writer refactor *
  Changed buffers in BufferLayer to std vectors. * BufferLayer
  uncrustify * Removed non-applicable test for writer cache. *
  BufferLayer review fixes * Rosbag metadata msgs count fixed for
  BufferLayer * Condition variable for buffer layer sync. * Fixed
  buffer locks * Buffers in BufferLayer refactored, moved into new
  class * Buffer layer split bags fixed. * Storage options include fix
  in buffer layer header. * Mutex around swapping buffers in buffer
  layer. * Fixed cache 0 bug in buffer layer. * Minor buffer layer
  refactor. * Counting messages in writer refactored. * Changed
  default cache size to 100Mb and updated parameter description *
  Applied review remarks: - significant refactoring: separation of
  cache classes - applied suggested improvements - some renaming -
  reduce code duplication that would otherwise increase with cache
  refactor, between compression and plain writers * Applied review
  comments - cache consumer now takes a callback and is independent of
  storage - namespace changes, renaming, cleaning - counting and
  logging messages by topic * linter * Changes after review: fixing
  flushing, topic counts, and more * Fix for splitting - flushing
  state now correctly turns off * cache classes documentation *
  simplified signature * a couple of tests for cache * address review:
  explicit constructor and doxygen styling * Windows warnings fix *
  fixed type mismatch warning on Windows * added minor comment Co-
  authored-by: Piotr Jaroszek <piotr.jaroszek@robotec.ai>

* read yaml config file (#497)

* List all storage plugins in plugin xml file (#554)

* add storage_config_uri (#493)

* Update deprecated qos policy value names (#548)

* Add record test for ros2bag (#523)

* Removed duplicated code in record (#534)

* Change default cache size for sequential_writer to a non zero value
  (#533)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* [ros2bag test_record] Gets rid of time.sleep and move to using
  command.wait_for_output (#525)

* Add pytest.ini back to ros2bag. (#492)

* performance testing packages (#442)

* Validate QoS profile values are not negative. (#483)

* catch parent exception (#472)

* add wait for closed file handles on Windows (#470)

* introduce ros2 bag list <plugins> (#468)

* move wait_for_shutdown() call out of the context manager (#466)

* Adding db directory creation to rosbag2_cpp (#450)

* use a single temp dir for the test class (#462)

* Add per-message ZSTD compression (#418)

* Add split by time to recording (#409)

* Add pytest.ini so local tests don't display warning (#446)

* Contributors: Adam Dąbrowski, Barry Xu, Chris Lalancette, Dirk
  Thomas, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jaison
  Titus, Jesse Ikawa, Karsten Knese, Marwan Taher, Michael Jeronimo,
  P. J. Reed, jhdcs

ros2cli
=======

* Add changelog. (#636)

* Ensure only one daemon can run at a time. (#622)

* Remove maintainer. (#597)

* Add option to support use_sim_time. (#581)

* Bugfix for #563. (#570)

* Add Audrow as a maintainer. (#591)

* Support Python 3.8-provided importlib.metadata. (#585)

* Update maintainers. (#568)

* Added dependency to python3-argcomplete to ros2cli. (#564)

* Remove use of pkg_resources from ros2cli. (#537)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Daisuke
  Sato, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan, Tomoya
  Fujita, Yoan Mollard

ros2cli_common_extensions
=========================

* remove maintainer (#5)

* update maintainer (#4)

* First implementation (#2)

* Contributors: Bo Sun, Claire Wang

ros2cli_test_interfaces
=======================

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Make ros2cli_test_interfaces version equal to other packages.

* Remove ros2interface test dependencies on builtin interface. (#579)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Ivan
  Santiago Paunovic

ros2component
=============

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Ensure consistent timeout in ros2component list. (#526)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic,
  Michel Hidalgo

ros2doctor
==========

* Improve ros2 doctor on Windows. (#631) (#634)

* Add changelog. (#636)

* Continue to next iteration after exceptions in generate_reports.
  (#623)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Support Python 3.8-provided importlib.metadata. (#585)

* Update maintainers. (#568)

* Remove pkg_resources from ros2doctor. (#537)

* Make ros2doctor depend on ros_environment and fix platform.py bug on
  error. (#538)

* Refactor ros2doctor hello verb. (#521)

* Contributors: Alberto Soragna, Audrow Nash, Chris Lalancette, Claire
  Wang, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan,
  mergify[bot]

ros2interface
=============

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Remove ros2interface test dependencies on builtin interface. (#579)

* Update maintainers. (#568)

* Handle inline comments on constants correctly. (#548)

* Update quoted comments in the test (#540)

* Add option to include/remove whitespace and comments. (#527)

* Show "expanded" message definition. (#524)

* Contributors: Audrow, Audrow Nash, Claire Wang, Ivan Santiago
  Paunovic, Tully Foote

ros2launch
==========

* Add options extensions to ros2launch and extensibility to the node
  action (#216)

* Support non-interactive ros2 launch executions (#210)

* Merge pull request #183 from ros2/update-maintainers

* Move previous maintainer to <author>

* Update the package.xml files with the latest Open Robotics
  maintainers

* Add pytest.ini so local tests don't display warning (#152)

* Contributors: Chris Lalancette, Geoffrey Biggs, Michael Jeronimo,
  Michel Hidalgo

ros2lifecycle
=============

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

ros2lifecycle_test_fixtures
===========================

* Add changelog. (#636)

* Depend on rclcpp::rclcpp target. (#618) Contributors: Audrow Nash

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

ros2multicast
=============

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

ros2node
========

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

ros2param
=========

* Add changelog. (#636)

* Make the ros2param --filter test more reliable. (#606)

* Add wildcard loading to ros2 param load. (#602)

* Ros2 param dump/load should use fully qualified node names. (#600)

* Add --filter options for 'ros2 param list'. (#592)

* Remove maintainer. (#597)

* Add rosparam verb load. (#590)

* Add Audrow as a maintainer. (#591)

* Add "--param-type" option to ros2param list. (#572)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic,
  Victor Lopez, tomoya

ros2pkg
=======

* Add changelog. (#636)

* Use underscores in setup.cfg.em instead of dashes. (#627)

* Add space for "ROS 2". (#617)

* Use target_compile_features for c/c++ standards. (#615)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Declare missing dependency on python3-importlib-resources. (#584)

* Update maintainers. (#568)

* Fix incorrect EXPORT for executables. (#545)

* Switch ros2pkg to using importlib.

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Dirk
  Thomas, Ivan Santiago Paunovic, Scott K Logan, Shane Loretz

ros2run
=======

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

ros2service
===========

* Add changelog. (#636)

* Remove maintainer. (#597)

* Add Audrow as a maintainer. (#591)

* Update maintainers. (#568)

* Check that passed type is actually a service. (#559)

* Contributors: Audrow Nash, Claire Wang, Dirk Thomas, Ivan Santiago
  Paunovic

ros2test
========

* Add pytest.ini so local tests don't display warning (#8)

* Contributors: Chris Lalancette

ros2topic
=========

* Add changelog. (#636)

* Add verbose info for topic list. (#351)

* Remove maintainer. (#597)

* Add option to support use_sim_time. (#581)

* Add Audrow as a maintainer. (#591)

* Add filter option to ros2topic . (#575)

* Update deprecated qos policy value names. (#571)

* Update maintainers. (#568)

* Fix the test to use the topic name. (#566)

* Improve the error message for invalid message types. (#558)

* Use reliable QoS for ros2topic tests. (#555)

* Add option to echo serialized messages. (#470)

* Enable --no-daemon flag for some cli tools. (#514)

* Use transient_local and longer keep-alive for pub tests. (#546)

* Add --keep-alive option to 'topic pub'. (#544)

* Add option to ros2 topic echo to report lost messages. (#542)

* Support QoS Depth and History via ros2 topic pub/echo. (#528)

* Contributors: Audrow Nash, ChenYing Kuo, Chris Lalancette, Claire
  Wang, Dereck Wonnacott, Dirk Thomas, Ivan Santiago Paunovic, Jacob
  Perron, Scott K Logan, Tomoya Fujita, tomoya

ros_testing
===========

* Use rostest CMake target as output file basename. (#9)

* Contributors: Michel Hidalgo

rosbag2
=======

* Explicitly add emersonknapp as maintainer (#692)

* RMW-implementation-searcher converter in rosbag2_cpp (#670)

* Move zstd compressor to its own package (#636)

* add storage_config_uri (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* AMENT_IGNORE rosbag2_py for now (#509)

* rosbag2_py reader and writer (#308)

* Contributors: Emerson Knapp, Karsten Knese, Mabel Zhang, Michael
  Jeronimo

rosbag2_compression
===================

* Explicitly add emersonknapp as maintainer (#692)

* Reindexer core (#641) Add a new C++ Reindexer class for
  reconstructing metadata from bags that are missing it.

* CLI query rosbag2_py for available storage implementations (#659)

* Move zstd compressor to its own package (#636)

* Remove rosbag2_compression test dependencies on zstd implementation
  in prep for moving it into a separate package (#637)

* Make compressor implementations into a plugin via pluginlib (#624)

* Use ZSTD's streaming interface for [de]compressing files (#543)

* Fix build issues when rosbag2_storage is binary installed (#585)

* Fix relative metadata paths in SequentialCompressionWriter (#613)

* Fix deadlock race condition on compression shutdown (#616)

* Deduplicate SequentialCompressionReader business logic, add fallback
  to find bagfiles in incorrectly-written metadata (#612)

* Compress bag files in separate threads (#506)

* Sqlite storage double buffering (#546)

* add storage_config_uri (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Do not expect empty StorageOptions URI to work in
  CompressionWriterTest (#526)

* Remove some code duplication between SequentialWriter and
  SequentialCompressionWriter (#527)

* Fix exception thrown given invalid arguments with compression
  enabled (#488)

* Adding db directory creation to rosbag2_cpp (#450)

* Consolidate ZSTD utility functions (#459)

* Add per-message ZSTD compression (#418)

* Contributors: Adam Dąbrowski, Christophe Bedard, Devin Bonnie,
  Emerson Knapp, Jaison Titus, Karsten Knese, Marwan Taher, Michael
  Jeronimo, P. J. Reed, jhdcs

rosbag2_compression_zstd
========================

* Add test_depend ament_cmake_gmock (#639)

* Move zstd compressor to its own package (#636)

* Contributors: Emerson Knapp, Shane Loretz

rosbag2_cpp
===========

* Add set_rate to PlayerClock (#727)

* Enforce non-null now_fn in TimeControllerClock (#731)

* Fix pause snapshot behavior and add regression test (#730)

* Pause/resume PlayerClock (#704)

* Remove -Werror from builds, enable it in Action CI (#722)

* Enable thread safety analysis for rosbag2_cpp and add annotations in
  TimeControllerClock (#710)

* PlayerClock initial implementation - Player functionally unchanged
  (#689)

* Explicitly add emersonknapp as maintainer (#692)

* Reindexer core (#641) Add a new C++ Reindexer class for
  reconstructing metadata from bags that are missing it.

* use rclcpp serialized messages to write data (#457)

* alternative write api (#676)

* RMW-implementation-searcher converter in rosbag2_cpp (#670)

* CLI query rosbag2_py for available storage implementations (#659)

* Fix --topics flag for ros2 bag play being ignored for all bags after
  the first one. (#619)

* Fix a crash in test_message_cache. (#635)

* Fix build issues when rosbag2_storage is binary installed (#585)

* Deduplicate SequentialCompressionReader business logic, add fallback
  to find bagfiles in incorrectly-written metadata (#612)

* include what you use (#600)

* Only dereference the data pointer if it is valid. (#581)

* Add back rosbag2_cpp::StorageOptions as deprecated (#563)

* Sqlite storage double buffering (#546)

* correct master build (#552)

* add storage_config_uri (#493)

* Mutex around writer access in recorder (#491)

* if cache data exists, it needs to flush the data into the storage
  before shutdown (#541)

* Change default cache size for sequential_writer to a non zero value
  (#533)

* SequentialWriter to cache by message size instead of message count
  (#530)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Remove some code duplication between SequentialWriter and
  SequentialCompressionWriter (#527)

* disable sanitizer by default (#517)

* Fix typo in error message (#475)

* introduce defaults for the C++ API (#452)

* Adding db directory creation to rosbag2_cpp (#450)

* comment out unused variable (#460)

* minimal c++ API test (#451)

* Add split by time to recording (#409)

* Contributors: Adam Dąbrowski, Alexander, Chris Lalancette, Dirk
  Thomas, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jaison
  Titus, Karsten Knese, Marwan Taher, Michael Jeronimo, P. J. Reed,
  Patrick Spieler, Tomoya Fujita, jhdcs

rosbag2_interfaces
==================

* Add rosbag2_interfaces package with playback service definitions
  (#728)

* Contributors: Emerson Knapp

rosbag2_performance_benchmarking
================================

* fixed a memory leak in no-transport benchmark (#674)

* report of performance improvements in rosbag2 (roughly since Foxy)
  (#651)

* Performance benchmarking improvements (#634)

* Performance benchmarking refactor (#594)

* Sqlite storage double buffering (#546)

* read yaml config file (#497)

* add storage_config_uri (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* performance testing packages (#442)

* Contributors: Adam Dąbrowski, Karsten Knese, Michael Jeronimo, Piotr
  Jaroszek

rosbag2_py
==========

* Remove -Werror from builds, enable it in Action CI (#722)

* Split Rosbag2Transport into Player and Recorder classes - first pass
  to enable further progress (#721)

* /clock publisher in Player (#695)

* Introducing Reindexer CLI (#699)

* Fix rosbag2_py transport test for py capsule (#707)

* rosbag2_py pybind wrapper for "record" - remove rosbag2_transport_py
  (#702)

* Add rosbag2_py::Player::play to replace rosbag2_transport_python
  version (#693)

* Explicitly add emersonknapp as maintainer (#692)

* RMW-implementation-searcher converter in rosbag2_cpp (#670)

* use rosbag2_py for ros2 bag info (#673)

* CLI query rosbag2_py for available storage implementations (#659)

* Fix build issues when rosbag2_storage is binary installed (#585)

* Fix the tests on cyclonedds by translating qos duration values
  (#606)

* add storage_config_uri (#493)

* Workaround pybind11 bug on Windows when
  CMAKE_BUILD_TYPE=RelWithDebInfo (#538)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Fix rosbag2_py on Windows debug and stop ignoring the package (#531)

* Fix rosbag2_py bug when using libc++ (#529)

* AMENT_IGNORE rosbag2_py for now (#509)

* rosbag2_py reader and writer (#308)

* Contributors: Emerson Knapp, Ivan Santiago Paunovic, Karsten Knese,
  Mabel Zhang, Michael Jeronimo, P. J. Reed, jhdcs

rosbag2_storage
===============

* Remove -Werror from builds, enable it in Action CI (#722)

* PlayerClock initial implementation - Player functionally unchanged
  (#689)

* Explicitly add emersonknapp as maintainer (#692)

* Reindexer core (#641) Add a new C++ Reindexer class for
  reconstructing metadata from bags that are missing it.

* Remove outdated pluginlib cmake script from rosbag2_storage (#661)

* CLI query rosbag2_py for available storage implementations (#659)

* Shorten some excessively long lines of CMake (#648)

* SQLite storage optimized by default (#568) * Use optimized pragmas
  by default in sqlite storage. Added option to use former behavior

* Use std::filesystem compliant non-member "exists" function for path
  object (#593)

* Update codes since rcutils_calculate_directory_size() is changed
  (#567)

* add storage_config_uri (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Add split by time to recording (#409)

* Contributors: Adam Dąbrowski, Barry Xu, Emerson Knapp, Josh
  Langsfeld, Karsten Knese, Michael Jeronimo, Scott K Logan, jhdcs

rosbag2_storage_default_plugins
===============================

* Remove -Werror from builds, enable it in Action CI (#722)

* Explicitly add emersonknapp as maintainer (#692)

* Reindexer core (#641) Add a new C++ Reindexer class for
  reconstructing metadata from bags that are missing it.

* Fix build issues when rosbag2_storage is binary installed (#585)

* Mutex protection for db writing and stl collections in writer &
  storage (#603)

* SQLite storage optimized by default (#568)

* read yaml config file (#497)

* add storage_config_uri (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Contributors: Adam Dąbrowski, Emerson Knapp, Karsten Knese, Michael
  Jeronimo, P. J. Reed, jhdcs

rosbag2_test_common
===================

* Remove -Werror from builds, enable it in Action CI (#722)

* Fix bad_function_call by replacing rclcpp::spin_some with
  SingleThreadedExecutor (#705)

* Explicitly add emersonknapp as maintainer (#692)

* Remove temporary directory platform-specific logic from test fixture
  (#660)

* Stabilize test_record by reducing copies of executors and messages
  (#576)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Contributors: Emerson Knapp, Michael Jeronimo

rosbag2_tests
=============

* Remove -Werror from builds, enable it in Action CI (#722)

* Explicitly add emersonknapp as maintainer (#692)

* Reindexer core (#641) Add a new C++ Reindexer class for
  reconstructing metadata from bags that are missing it.

* use rclcpp serialized messages to write data (#457)

* Alternative write api (#676)

* RMW-implementation-searcher converter in rosbag2_cpp (#670)

* Use rosbag2_py for ros2 bag info (#673)

* Remove temporary directory platform-specific logic from test fixture
  (#660)

* Fix --topics flag for ros2 bag play being ignored for all bags after
  the first one. (#619)

* Move zstd compressor to its own package (#636)

* Fix relative metadata paths in SequentialCompressionWriter (#613)

* Recorder --regex and --exclude options (#604)

* Fix the tests on cyclonedds by translating qos duration values
  (#606)

* add storage_config_uri (#493)

* Removed duplicated code in record (#534)

* Change default cache size for sequential_writer to a non zero value
  (#533)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Mark flaky tests as xfail for now (#520)

* introduce defaults for the C++ API (#452)

* Adding db directory creation to rosbag2_cpp (#450)

* minimal c++ API test (#451)

* Add split by time to recording (#409)

* Contributors: Adam Dąbrowski, Alexander, Emerson Knapp, Jaison
  Titus, Karsten Knese, Marwan Taher, Michael Jeronimo, jhdcs

rosbag2_transport
=================

* cleanup cmakelists (#726)

* turn recorder into a node (#724)

* turn player into a node (#723)

* Remove -Werror from builds, enable it in Action CI (#722)

* Split Rosbag2Transport into Player and Recorder classes - first pass
  to enable further progress (#721)

* /clock publisher in Player (#695)

* use rclcpp logging macros (#715)

* use rclcpp::Node for generic pub/sub (#714)

* PlayerClock initial implementation - Player functionally unchanged
  (#689)

* Fix bad_function_call by replacing rclcpp::spin_some with
  SingleThreadedExecutor (#705)

* rosbag2_py pybind wrapper for "record" - remove rosbag2_transport_py
  (#702)

* Add rosbag2_py::Player::play to replace rosbag2_transport_python
  version (#693)

* Fix and clarify logic in test_play filter test (#690)

* Explicitly add emersonknapp as maintainer (#692)

* Add QoS decoding translation for infinite durations to
  RMW_DURATION_INFINITE (#684)

* Add support for rmw_connextdds (#671)

* Use rosbag2_py for ros2 bag info (#673)

* Fix build issues when rosbag2_storage is binary installed (#585)

* Regex and exclude fix for rosbag recorder (#620)

* Recorder --regex and --exclude options (#604)

* SQLite storage optimized by default (#568)

* Fixed playing if unknown message types exist (#592)

* Compress bag files in separate threads (#506)

* Stabilize test_record by reducing copies of executors and messages
  (#576)

* add storage_config_uri (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* resolve memory leak for serialized message (#502)

* Use shared logic for importing the rosbag2_transport_py library in
  Python (#482)

* fix missing target dependencies (#479)

* reenable cppcheck for rosbag2_transport (#461)

* More reliable topic remapping test (#456)

* Add split by time to recording (#409)

* export shared_queues_vendor (#434)

* Contributors: Adam Dąbrowski, Andrea Sorbini, Chen Lihui, Dirk
  Thomas, Emerson Knapp, Karsten Knese, Michael Jeronimo, P. J. Reed,
  Piotr Jaroszek, jhdcs

rosgraph_msgs
=============

* Change index.ros.org -> docs.ros.org. (#122)

* Updating Quality Declaration (#120)

* Update README.md (#119)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  brawner, shonigmann

rosidl_adapter
==============

* Expose .msg/.srv/.action to .idl conversion via rosidl translate CLI
  (#576)

* Support hex constants in msg files (#559)

* Treat t as whitespace (#557)

* Update the maintainers of this repository. (#536)

* Refactor regex for valid package/field names (#508)

* Add pytest.ini so tests succeed locally (#502)

* Contributors: Chris Lalancette, Dereck Wonnacott, Dirk Thomas,
  Michel Hidalgo

rosidl_cli
==========

* Align rosidl_cli package version with the rest of the repo. (#579)

* Expose an API for each rosidl CLI command. (#577)

* Add rosidl translate CLI. (#575)

* Add rosidl generate CLI. (#567)

* Contributors: Michel Hidalgo, Shane Loretz

rosidl_cmake
============

* Shorten some excessively long lines of CMake (#571)

* Update the maintainers of this repository. (#536)

* Modifications to python generator lib to return generated files
  (#511)

* Contributors: Alex Tyshka, Chris Lalancette, Scott K Logan

rosidl_default_generators
=========================

* Update maintainers (#13)

* Contributors: Shane Loretz

rosidl_default_runtime
======================

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#18)

* Update QD to QL 1 (#15)

* Update maintainers (#13)

* Updated QD to 2 in README.md (#12)

* Update rosidl_default_runtime QD to QL2. (#11)

* Bump the QUALITY_DECLARATION to level 3. (#10)

* Add Security Vulnerability Policy pointing to REP-2006. (#9)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Shane Loretz, Stephen Brawner, shonigmann
