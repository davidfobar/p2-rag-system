# Iron Irwini Changelog (part 4 of 5)

* Delete obsolete compression_options.cpp from rosbag2_cpp (#1078)

* Readers/info can accept a single bag storage file, and detect its
  storage id automatically (#1072)

* Remove deprecated rosbag2_cpp/storage_options.hpp, for post-Humble
  releases (#1064)

* Speed optimization: Preparing copyless publish/subscribing by using
  const message for writing (#1010)

* Add the ability to record any key/value pair in 'custom' field in
  metadata.yaml (#1038)

* Notification of significant events during bag recording and playback
  (#908)

* Bugfix for "Playing the bags recorded with split by duration/size is
  playing only the last recorded .db3." (#1022)

* Improve test_time_controller test (#1012)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, DensoADAS,
  Emerson Knapp, Geoffrey Biggs, Hunter L. Allen, Jorge Perez, Joshua
  Hampp, Kaju-Bubanja, Michael Orlov, Tony Peng, james-rms,
  mergify[bot], rshanor

rosbag2_examples_cpp
====================

* rosbag2_storage: add type description hash to topic metadata (#1272)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Add API samples on main branch - Rolling C++ API examples (#1068)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp,
  Michael Orlov, james-rms

rosbag2_examples_py
===================

* Fix a warning from python setuptools. (#1312) (#1314)

* Add API samples for Python [rebased] (#1253) * Add API samples for
  Python * Package Renaming and Move * linting + copyright * more
  linting --------- Co-authored-by: Geoffrey Biggs
  <gbiggs@killbots.net>

* Contributors: David V. Lu!!, mergify[bot]

rosbag2_interfaces
==================

* Update rosbag2 to C++17. (#1238)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Add SplitBagfile recording service. (#1115)

* Adds stop operation for rosbag2::Player (#1007)

* Notification of significant events during bag recording and playback
  (#908)

* Adds play until timestamp functionality (#1005)

* Add CLI verb for burst mode of playback (#980)

* Add play-for specified number of seconds functionality (#960)

* Contributors: Agustin Alba Chicar, Chris Lalancette, Geoffrey Biggs,
  Michael Orlov, Misha Shalem, rshanor

rosbag2_performance_benchmarking
================================

* Add tests for rosbag2_performance_benchmarking pkg (#1268)

* Fix expectations for rosbag2 return code in
  rosbag2_performance_benchmarking (#1267)

* Update rosbag2 to C++17. (#1238)

* Use thread pool to run benchmark publishers in
  rosbag2_performance_benchmarking (#1250)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Skip ament_package() call when not building
  rosbag2_performance_benchmarking (#1242)

* Add option to specify a message type (#1153)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Replace language for "db3"/"db"/"database" (#1194)

* Remove explicit sqlite3 from code (#1166)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp,
  Michael Orlov, Shane Loretz, carlossvg

rosbag2_performance_benchmarking_msgs
=====================================

* Add tests for rosbag2_performance_benchmarking pkg (#1268)

* Skip ament_package() call when not building
  rosbag2_performance_benchmarking (#1242)

* [rolling] Bump to 0.19.0 (#1232)

* Add option to specify a message type (#1153)

* Contributors: Audrow Nash, Michael Orlov, Shane Loretz, carlossvg

rosbag2_py
==========

* Add binding to close the writer (#1339) (#1340)

* Add type_hash in MessageDefinition struct (#1296)

* Store message definitions in SQLite3 storage plugin (#1293)

* Add message definition read API (#1292)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Expose more Writer methods in python interface (#1220)

* rosbag2_storage: set MCAP as default plugin (#1160)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* rosbag2_py: parametrize tests across storage plugins (#1203)

* Added option to change node name for the recorder from the Python
  API (#1180)

* Replace language for "db3"/"db"/"database" (#1194)

* Remove explicit sqlite3 from code (#1166)

* Move python get_default_storage_id to storage module instead of
  writer (#1165)

* rosbag2_storage: expose default storage ID as method (#1146)

* rosbag2_py: set defaults for config when bag rewriting (#1121)

* Reverse read order API and sqlite storage implementation (#1083)

* expose py Reader metadata, improve "rosbag2_py.BagMetadata"
  usability (#1082)

* Added support for excluding topics via regular expressions (#1046)

* Use a single variable for evaluating the filter regex (#1053)

* Add additional mode of publishing sim time updates triggered by
  replayed messages (#1050)

* Renamed --topics-regex to --regex and -e in Player class to be
  consistent with Recorder (#1045)

* Add the ability to record any key/value pair in 'custom' field in
  metadata.yaml (#1038)

* Added support for filtering topics via regular expressions on
  Playback (#1034)

* Adds play until timestamp functionality (#1005)

* Add CLI verb for burst mode of playback (#980)

* Add play-for specified number of seconds functionality (#960)

* Make unpublished topics unrecorded by default (#968)

* Fix test rosbag2_py test compatibility with Python < 3.8 (#987)

* Contributors: Agustin Alba Chicar, Chris Lalancette, Daisuke
  Nishimatsu, Emerson Knapp, Esteve Fernandez, Geoffrey Biggs, Hunter
  L. Allen, Michael Orlov, Scott K Logan, Sean Kelly, Tony Peng,
  james-rms, kylemarcey, mergify[bot], ricardo-manriquez

rosbag2_storage
===============

* Add type_hash in MessageDefinition struct (#1296)

* Add message definition read API (#1292)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* rosbag2_storage: set MCAP as default plugin (#1160)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* set_read_order: return success (#1177)

* Remove explicit sqlite3 from code (#1166)

* Add "update_metadata(BagMetadata)" API for storage plugin interface
  (#1149)

* rosbag2_storage: expose default storage ID as method (#1146)

* Don't reopen file for every seek if we don't have to. Search
  directionally for the correct file (#1117)

* Reverse read order API and sqlite storage implementation (#1083)

* Remove YAML_CPP_DLL define (#964)

* Added support for excluding topics via regular expressions (#1046)

* Readers/info can accept a single bag storage file, and detect its
  storage id automatically (#1072)

* Use a single variable for evaluating the filter regex (#1053)

* Speed optimization: Preparing copyless publish/subscribing by using
  const message for writing (#1010)

* Renamed --topics-regex to --regex and -e in Player class to be
  consistent with Recorder (#1045)

* Add the ability to record any key/value pair in 'custom' field in
  metadata.yaml (#1038)

* Added support for filtering topics via regular expressions on
  Playback (#1034)

* Contributors: Akash, Chris Lalancette, Daisuke Nishimatsu,
  DensoADAS, Emerson Knapp, Esteve Fernandez, Hunter L. Allen, Joshua
  Hampp, Michael Orlov, Tony Peng, james-rms

rosbag2_storage_default_plugins
===============================

* rosbag2_storage: set MCAP as default plugin (#1160)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Move sqlite3 storage implementation to rosbag2_storage_sqlite3
  package (#1113)

* Reverse read order API and sqlite storage implementation (#1083)

* Add support for old db3 schema used on distros prior to Foxy (#1090)

* Added support for excluding topics via regular expressions (#1046)

* Contributors: Emerson Knapp, Esteve Fernandez, Michael Orlov, james-
  rms

rosbag2_storage_mcap
====================

* Add type_hash in MessageDefinition struct (#1296)

* Add message definition read API (#1292)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* CLI: Get storage-specific values from plugin (#1209)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* rosbag2_cpp: test more than one storage plugin (#1196)

* set_read_order: return success (#1177)

* rosbag2_storage_mcap: merge into rosbag2 repo (#1163)

* mcap_storage: 'none' is a valid storage preset profile (#86)

* mcap_storage: handle update_metadata call (#83)

* Update clang-format rules to fit ROS 2 style guide (#80)

* Revert "read_order: throw exception from set_read_order for
  unsupported orders"

* read_order: throw exception from set_read_order for unsupported
  orders

* Fix compile flags to work on rosbag_storage:0.17.x (#78)

* Fix Windows build (#73)

* set defaults for SQLite plugin parity (#68)

* rosbag2_storage_mcap: add storage preset profiles (#57)

* rename test_fixture_interfaces package to testdata (#64)

* Switch to using the vendored zstd library. (#59)

* Add set_read_order reader API (#54)

* Some minor improvements in rosbag2_storage_mcap after review (#58)

* Revert "rosbag2_storage_mcap: add storage preset profiles"

* rosbag2_storage_mcap: add storage preset profiles

* Store IDL message definitions in Schema records when no MSG
  definition is available (#43)

* Support timestamp-ordered playback (#50)

* Support regex topic filtering

* Add all lz4 sources to fix undefined symbols at runtime (#46)

* Upgrade mcap to fix LZ4 error and segfault (#42)

* Fix build for Foxy (#34)

* fix: minor issues (#31) * remove unnecessary block * use
  target_link_libraries instead of ament_target_dependencies * remove
  ros environment * add prefix to compile definition

* Update email address for Foxglove maintainers (#32)

* Added mcap_vendor package. Updated CMakeLists.txt to fetch
  dependencies with FetchContent rather than Conan.

* CMake build script will now execute pip install conan automatically.

* [1.0.0] Use Summary section for get_metadata() and seek(), implement
  remaining methods (#17)

* feat: add play impl (#16)

* chore: refine package.xml (#15)

* Don't throw when READ_WRITE mode is used; add .mcap file extension
  to recorded files (#14)

* Add dynamic message definition lookup (#13)

* Switch C++ formatter to clang-format (#12)

* Merge pull request #7 from ros-tooling/jhurliman/reader-writer

* uninitialized struct

* lint

* lint

* lint

* Reader and writer implementation

* Merge pull request #6 from wep21/add-metadata-impl

* feat: add metadata impl

* Merge pull request #5 from wep21/mcap-storage-impl

* chore: update cmake minimum version

* chore: install mcap header

* chore: include mcap header

* fix: move fetch content into rosbag2 storage mcap

* Merge pull request #3 from ros-
  tooling/emersonknapp/mcap_plugin_skeleton

* Add rosbag2_storage_mcap skeleton

* Contributors: Andrew Symington, Chris Lalancette, Daisuke
  Nishimatsu, Emerson Knapp, Jacob Bandes-Storch, James Smith, John
  Hurliman, Michael Orlov, james-rms, wep21

rosbag2_storage_sqlite3
=======================

* Add type_hash in MessageDefinition struct (#1296)

* Store message definitions in SQLite3 storage plugin (#1293)

* Add message definition read API (#1292)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* CLI: Get storage-specific values from plugin (#1209)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Remove sqlite3-specific info from main README, make it more storage
  agnostic and point to plugin-specific README (#1193)

* set_read_order: return success (#1177)

* Add "update_metadata(BagMetadata)" API for storage plugin interface
  (#1149)

* Store db schema version and ROS_DISTRO name in db3 files (#1156)

* ros2bag: move storage preset validation to sqlite3 plugin (#1135)

* Move sqlite3 storage implementation to rosbag2_storage_sqlite3
  package (#1113)

* Use a single variable for evaluating the filter regex (#1053)

* Renamed --topics-regex to --regex and -e in Player class to be
  consistent with Recorder (#1045)

* Added support for filtering topics via regular expressions on
  Playback (#1034)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp,
  Esteve Fernandez, Michael Orlov, james-rms

rosbag2_test_common
===================

* Address flakiness in rosbag2_play_end_to_end tests (#1297) (#1330)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* rosbag2_py: parametrize tests across storage plugins (#1203)

* Fix for ros2 bag play exit with non-zero code on SIGINT (#1126)

* Split up the include of rclcpp.hpp (#1027)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, Michael Orlov,
  james-rms, mergify[bot]

rosbag2_test_msgdefs
====================

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265) The intention of this PR is to move the message-definition-
  finding capability outside of rosbag2_storage_mcap, and allow any
  rosbag2 storage plugin to store message definitions.

* Contributors: james-rms

rosbag2_tests
=============

* Address flakiness in rosbag2_play_end_to_end tests (#1297) (#1330)

* Add type_hash in MessageDefinition struct (#1296)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* rosbag2_storage: set MCAP as default plugin (#1160)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* Parametrize all rosbag2_tests for both supported storage plugins
  (#1221)

* Make rosbag2_tests agnostic to storage implementation (#1192)

* Get rid from attempt to open DB file in "wait_for_db()" test fixture
  (#1141)

* Fix for ros2 bag play exit with non-zero code on SIGINT (#1126)

* Move sqlite3 storage implementation to rosbag2_storage_sqlite3
  package (#1113)

* Readers/info can accept a single bag storage file, and detect its
  storage id automatically (#1072)

* Add the ability to record any key/value pair in 'custom' field in
  metadata.yaml (#1038)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp,
  Hunter L. Allen, Michael Orlov, Tony Peng, james-rms, mergify[bot]

rosbag2_transport
=================

* Change subscriptions from GenericSubscripton to SubscriptionBase
  (#1338)

* Add recorder stop() API (#1300) (#1334)

* Read message definitions from input files in bag_rewrite (#1295)

* Add message definition read API (#1292)

* Move rosbag2_transport::Recorder implementation to pimpl (#1291)

* rosbag2_storage: add type description hash to topic metadata (#1272)

* rosbag2_cpp: move local message definition source out of MCAP plugin
  (#1265)

* Use RMW methods to initialize endpoint info instead of brace
  initializer to guard against upcoming struct change (#1257)

* Update rosbag2 to C++17. (#1238)

* Use target_link_libraries instead of ament_target_dependencies
  (#1202)

* Print "Hidden topics are not recorded" only once. (#1225)

* rosbag2_storage: set MCAP as default plugin (#1160)

* Add Michael Orlov as maintainer in rosbag2 packages (#1215)

* rosbag2_transport: parametrize test_rewrite (#1206)

* rosbag2_cpp: test more than one storage plugin (#1196)

* Replace language for "db3"/"db"/"database" (#1194)

* set_read_order: return success (#1177)

* Remove explicit sqlite3 from code (#1166)

* Add pause and resume service calls for rosbag2 recorder (#1131)

* Redesign record_services tests to make them more deterministic
  (#1122)

* Add SplitBagfile recording service. (#1115)

* Reverse read order API and sqlite storage implementation (#1083)

* make recorder node composable by inheritance (#1093)

* Mark "test_play_services" as xfail for FastRTPS and CycloneDDS
  (#1091)

* fixed typo (#1057)

* Fix hangout in rosbag2 player and recorder when pressing "CTRL+C"
  (#1081)

* Added support for excluding topics via regular expressions (#1046)

* Use a single variable for evaluating the filter regex (#1053)

* Add additional mode of publishing sim time updates triggered by
  replayed messages (#1050)

* Speed optimization: Preparing copyless publish/subscribing by using
  const message for writing (#1010)

* Renamed --topics-regex to --regex and -e in Player class to be
  consistent with Recorder (#1045)

* Refactor play until and duration tests (#1024)

* Added support for filtering topics via regular expressions on
  Playback (#1034)

* Adds stop operation for rosbag2::Player (#1007)

* Fix incorrect boundary check for "playback_duration" and
  "play_until_timestamp" (#1032)

* Split up the include of rclcpp.hpp (#1027)

* Notification of significant events during bag recording and playback
  (#908)

* Adds play until timestamp functionality (#1005)

* Add CLI verb for burst mode of playback (#980)

* Add on play message callbacks to the "rosbag2::Player" class (#1004)

* Add play-for specified number of seconds functionality (#960)

* Reduce message spam when topics to be recorded do not exist (#1018)

* Address flakiness in record_all_with_sim_time test (#1014)

* Add debug instrumentation for "test_play_services" (#1013)

* Fix for rosbag2::Player freeze when pressing ctrl+c in pause mode
  (#1002)

* Add the /bigobj flag to Windows Debug builds. (#1009)

* Make unpublished topics unrecorded by default (#968)

* Make peek_next_message_from_queue return a SharedPtr. (#993)

* Change the topic names in test_record.cpp (#988)

* Contributors: Agustin Alba Chicar, Bernardo Taveira, Brian, Chris
  Lalancette, Cristóbal Arroyo, Daisuke Nishimatsu, DensoADAS, Emerson
  Knapp, Esteve Fernandez, Geoffrey Biggs, Jorge Perez, Joshua Hampp,
  Michael Orlov, Misha Shalem, Sean Kelly, Tony Peng, james-rms,
  kylemarcey, mergify[bot], rshanor

rosgraph_msgs
=============

* Update common_interfaces to C++17. (#215) (#151)

* [rolling] Update maintainers - 2022-11-07 (#150)

* Contributors: Audrow Nash, Chris Lalancette

rosidl_adapter
==============

* rosidl_adapter/cmake/rosidl_adapt_interfaces.cmake: Make ament free
  (#709)

* [service introspection] generate service_event messages (#700)

* Adding tests for unicode support in message comments. (#720)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Add action2idl script (#654)

* Contributors: Audrow Nash, Brian, Guilherme Henrique Galelli
  Christmann, John Daktylidis, Yasushi SHOJI

rosidl_cli
==========

* Fix warnings (#726)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Contributors: Audrow Nash, Yadu

rosidl_cmake
============

* Type Description Codegen and Typesupport (rep2011) (#727)

* Type hash in interface codegen (rep2011) (#722)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Skip rosidl_generate_interfaces dependency export on SKIP_INSTALL.
  (#708)

* Move rosidl_cmake Python module to a new package rosidl_pycommon
  (#696) Deprecate the Python module in rosidl_cmake and move the
  implementation to the new package rosidl_pycommon.

* Fix comment in camel case conversion function (#683)

* Protect rosidl_target_interfaces from using NOTFOUND in
  include_directories (#679)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Jacob Perron, Jose Luis Rivero, Shane Loretz

rosidl_core_generators
======================

* [rolling] Update maintainers - 2022-11-07 (#2)

* Add generators and runtime configuration packages (#1) Moved (and
  renamed) from rosidl_defaults. Related PR:
  https://github.com/ros2/rosidl_defaults/pull/22

* Contributors: Audrow Nash, Jacob Perron

rosidl_core_runtime
===================

* [rolling] Update maintainers - 2022-11-07 (#2)

* Add generators and runtime configuration packages (#1) Moved (and
  renamed) from rosidl_defaults. Related PR:
  https://github.com/ros2/rosidl_defaults/pull/22

* Contributors: Audrow Nash, Jacob Perron

rosidl_default_generators
=========================

* add service_msgs depend (#24)

* [rolling] Update maintainers - 2022-11-07 (#25)

* Move dependencies to rosidl_core and depend on action_msgs (#22)
  Move implementation to new packages rosidl_core_generators and
  rosidl_runtime_generators The new packages are located in a separate
  repository: https://github.com/ros2/rosidl_core.git rosidl_defaults
  now depends on the new packages, plus message definitions required
  for Actions (namely action_msgs). This allows users to avoid having
  to explictly depend on action_msgs.

* Contributors: Audrow Nash, Brian, Jacob Perron

rosidl_default_runtime
======================

* add service_msgs depend (#24)

* [rolling] Update maintainers - 2022-11-07 (#25)

* Move dependencies to rosidl_core and depend on action_msgs (#22)
  Move implementation to new packages rosidl_core_generators and
  rosidl_runtime_generators The new packages are located in a separate
  repository: https://github.com/ros2/rosidl_core.git rosidl_defaults
  now depends on the new packages, plus message definitions required
  for Actions (namely action_msgs). This allows users to avoid having
  to explictly depend on action_msgs.

* Contributors: Audrow Nash, Brian, Jacob Perron

rosidl_dynamic_typesupport
==========================

* Fix up the exports for rosidl_dynamic_typesupport. (#5)

* Refactor dynamic message type support impl to use allocators (#2)

* Runtime Interface Reflection: rosidl_dynamic_typesupport (#1)

* Contributors: Chris Lalancette, William Woodall, methylDragon

rosidl_dynamic_typesupport_fastrtps
===================================

* Remove more unnecessary semicolons (#4)

* Dynamic Subscription (BONUS: Allocators):
  rosidl_dynamic_typesupport_fastrtps (#3)

* Remove unnecessary semicolons. (#2)

* Runtime Interface Reflection: rosidl_dynamic_typesupport_fastrtps
  (#1)

* Contributors: Chris Lalancette, methylDragon

rosidl_generator_c
==================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Expose type hash on typesupports (rep2011) (#729)

* Type hash in interface codegen (rep2011) (#722)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Move rosidl_generator_c/cpp tests to a separate package (#701)

* Move rosidl_cmake Python module to a new package rosidl_pycommon
  (#696) Deprecate the Python module in rosidl_cmake and move the
  implementation to the new package rosidl_pycommon.

* Add namespaced ALIAS target to easily consume generated libraries
  via add_subdirectory (#605)

* Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron,
  Silvio Traversaro

rosidl_generator_cpp
====================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Expose type hash on typesupports (rep2011) (#729)

* Type hash in interface codegen (rep2011) (#722)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Move rosidl_generator_c/cpp tests to a separate package (#701)

* Move rosidl_cmake Python module to a new package rosidl_pycommon
  (#696) Deprecate the Python module in rosidl_cmake and move the
  implementation to the new package rosidl_pycommon.

* Add namespaced ALIAS target to easily consume generated libraries
  via add_subdirectory (#605)

* Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron,
  Silvio Traversaro

rosidl_generator_dds_idl
========================

* [rolling] Update maintainers - 2022-11-07 (#60)

* Replace rosidl_cmake imports with rosidl_pycommon (#59)

* Contributors: Audrow Nash, Jacob Perron

rosidl_generator_py
===================

* Hides the assertions that checks the data types of the message
  fields. (#194)

* Service introspection (#178)

* [rolling] Update maintainers - 2022-11-07 (#189)

* Remove stray numpy import (#185)

* man_farmer:
     Fix NaN values bound numpy windows version (#182)

* Allow NaN values to pass floating point bounds check. (#167)

* Replace rosidl_cmake imports with rosidl_pycommon (#177)

* Change decode error mode to replace (#176)

* Merge pull request #173 from ros2/quarkytale/fix_import_order

* fix flake

* sorting after conversion

* Revert "Use modern cmake targets to avoid absolute paths to appear
  in binary archives (#160)" (#166)

* Use modern cmake targets to avoid absolute paths to appear in binary
  archives (#160)

* michel as author

* adding maintainer

* Contributors: Audrow Nash, Ben Wolsieffer, Brian, Cristóbal Arroyo,
  Dharini Dutia, Eloy Briceno, Ivan Santiago Paunovic, Jacob Perron,
  Tomoya Fujita, quarkytale, Øystein Sture

rosidl_generator_tests
======================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Type hash in interface codegen (rep2011) (#722)

* [service introspection] generate service_event messages (#700) * add
  service event message

* [rolling] Update maintainers - 2022-11-07 (#717)

* Move rosidl_generator_c/cpp tests to a separate package (#701)

* Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron

rosidl_generator_type_description
=================================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Expose type hash on typesupports (rep2011) (#729)

* Type hash in interface codegen (rep2011) (#722)

* Contributors: Emerson Knapp

rosidl_parser
=============

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Always include whitespace in string literals (#688)

* Contributors: Audrow Nash, Brian, Shane Loretz

rosidl_pycommon
===============

* Type Description Codegen and Typesupport (rep2011) (#727)

* Type hash in interface codegen (rep2011) (#722)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Move rosidl_cmake Python module to a new package rosidl_pycommon
  (#696) Deprecate the Python module in rosidl_cmake and move the
  implementation to the new package rosidl_pycommon.

* Contributors: Audrow Nash, Emerson Knapp, Jacob Perron

rosidl_runtime_c
================

* Dynamic Subscription (BONUS: Allocators): rosidl (#737)

* Runtime Interface Reflection: rosidl (#728)

* Type Description Codegen and Typesupport (rep2011) (#727)

* Copied type_description_interfaces structs (rep2011) (#732)

* Expose type hash on typesupports (rep2011) (#729)

* Type hash in interface codegen (rep2011) (#722)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* Contributors: Audrow Nash, Brian, Emerson Knapp, methylDragon

rosidl_runtime_cpp
==================

* Type Description Codegen and Typesupport (rep2011) (#727)

* Copied type_description_interfaces structs (rep2011) (#732)

* Fix a few more clang analysis problems. (#731)

* Return reference from BoundedVector::emplace_back (#730)

* [service introspection] generate service_event messages (#700)

* [rolling] Update maintainers - 2022-11-07 (#717)

* fix conversion to ‘std::streamsize’ {aka ‘long int’} from ‘size_t’
  {aka ‘long unsigned int’} may change the sign of the result (#715)

* Contributors: Alexander Hans, Audrow Nash, Brian, Chris Lalancette,
  Emerson Knapp, ralwing

rosidl_runtime_py
=================

* Replace the use __slots__ for the appropiate API (#23)

* fix(typing): "get_interface_packages" returns a dict (#22)

* [rolling] Update maintainers - 2022-11-07 (#21)

* Expand timestamps for std_msgs.msg.Header and
  builtin_interfaces.msg.Time if 'auto' and 'now' are passed as values
  (#19)

* Document a missing parameter in message_to_yaml. (#18)

* Mirror rolling to master

* Contributors: Audrow Nash, Chris Lalancette, Eloy Briceno, Esteve
  Fernandez, 兰陈昕

rosidl_typesupport_c
====================

* Type Description Nested Support (#141)

* Fix rosidl_typesupport_c/cpp exec dependencies. (#140)

* Type hashes in typesupport (rep2011) (#135)

* Mark benchmark _ as UNUSED. (#134)

* Service introspection (#127)

* Update rosidl_typesupport to C++17. (#131)

* [rolling] Update maintainers - 2022-11-07 (#130)

* Replace rosidl_cmake imports with rosidl_pycommon (#126)

* [service introspection] Use stddef.h instead of cstddef (#125)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Jacob Perron

rosidl_typesupport_cpp
======================

* Type Description Nested Support (#141)

* Fix rosidl_typesupport_c/cpp exec dependencies. (#140)

* Type hashes in typesupport (rep2011) (#135)

* Mark benchmark _ as UNUSED. (#134)

* Service introspection (#127)

* Update rosidl_typesupport to C++17. (#131)

* [rolling] Update maintainers - 2022-11-07 (#130)

* Replace rosidl_cmake imports with rosidl_pycommon (#126)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Jacob Perron

rosidl_typesupport_fastrtps_c
=============================

* Type Description Nested Support (#101)

* Type hashes on typesupport (rep2011) (#98)

* Expose type hash to typesupport structs (rep2011) (#95)

* Mark benchmark _ as UNUSED. (#96)

* Service introspection (#92)

* Update rosidl_typesupport_fastrtps to C++17. (#94)

* [rolling] Update maintainers - 2022-11-07 (#93)

* Replace rosidl_cmake imports with rosidl_pycommon (#91)

* Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp,
  Jacob Perron

rosidl_typesupport_fastrtps_cpp
===============================

* Type Description Nested Support (#101)

* Type hashes on typesupport (rep2011) (#98)

* Depend on ament_cmake_ros to default SHARED to ON (#99)

* Expose type hash to typesupport structs (rep2011) (#95)

* Mark benchmark _ as UNUSED. (#96)

* Service introspection (#92)
