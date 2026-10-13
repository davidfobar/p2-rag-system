# Jazzy Jalisco changelog (part 4 of 5)

rosbag2_compression_zstd
========================

* Use std::filesystem instead of rcpputils::fs (#1576)

* Make some changes for newer versions of uncrustify. (#1578)

* Contributors: Chris Lalancette, Roman Sokolkov

rosbag2_cpp
===========

* Support service 2/2 --- rosbag2 service play (#1481)

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Update to use yaml-cpp version 0.8.0. (#1605)

* Use std::filesystem instead of rcpputils::fs (#1576)

* Make some changes for newer versions of uncrustify. (#1578)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* call cv.wait_until only if necessary. (#1521)

* Implement service recording and display info about recorded services
  (#1480)

* Switch to target_link_libraries everywhere. (#1504)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* ros2 bag convert now excludes messages not in [start_time;end_time]
  (#1455)

* Replace TSAUniqueLock implementation with rcpputils::unique_lock
  (#1454)

* Add BagSplitInfo service call on bag close (#1422)

* Rewrite TimeControllerClockTest.unpaused_sleep_returns_true to be
  correct (#1384)

* Implement storing and loading ROS_DISTRO from metadata.yaml and mcap
  files (#1241)

* Don't crash when type definition cannot be found (#1350)

* Add recorder stop() API (#1300)

* Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michael
  Orlov, Patrick Roncagliolo, Peter Favrholdt, Roman Sokolkov, Tomoya
  Fujita, jmachowinski

rosbag2_examples_cpp
====================

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* Contributors: Michael Orlov, Patrick Roncagliolo

rosbag2_examples_py
===================

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Fix a warning from python setuptools. (#1312)

* Contributors: Chris Lalancette, Michael Orlov

rosbag2_interfaces
==================

* Add node name to the Read(Write)SplitEvent message (#1609)

* Contributors: Michael Orlov

rosbag2_performance_benchmarking
================================

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Update to use yaml-cpp version 0.8.0. (#1605)

* Add option to set compression threads priority (#1457)

* Add per group statistics for rosbag2_performance_benchmarking report
  (#1306)

* Set CPU affinity for producers and recorder from benchmark
  parameters (#1305)

* Add CPU usage to rosbag2_performance_benchmarking results report
  (#1304)

* Add config option to use storage_id parameter in benchmark_launch.py
  (#1303)

* Contributors: Chris Lalancette, Michael Orlov, jmachowinski

rosbag2_py
==========

* Add option to disable recorder keyboard controls (#1607)

* Support service 2/2 --- rosbag2 service play (#1481)

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Switch rclpy to be an exec_depend here. (#1606)

* Gracefully handle SIGINT and SIGTERM signals for play and burst CLI
  (#1557)

* Added exclude-topic-types to record (#1582)

* Fix for false negative tests in rosbag2_py (#1592)

* Update rosbag2_py stubs (#1593)

* Add Python stubs for rosbag2_py (#1459) (#1569)

* Filter topic by type (#1577)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Install signal handlers in recorder only inside record method
  (#1464)

* add missing import otherwise it doesnt compile (#1524)

* Implement service recording and display info about recorded services
  (#1480)

* Make "rosbag2_transport::Player::play()" run in a separate thread
  (#1503)

* Switch to target_link_libraries everywhere. (#1504)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* ros2 bag convert now excludes messages not in [start_time;end_time]
  (#1455)

* Add support for compression to python API (#1425)

* Gracefully handle SIGINT and SIGTERM in rosbag2 recorder (#1301)

* Implement storing and loading ROS_DISTRO from metadata.yaml and mcap
  files (#1241)

* Add binding to close the writer (#1339)

* Contributors: Alejandro Hernández Cordero, Andrew Symington, Barry
  Xu, Bernd Pfrommer, Chris Lalancette, Emerson Knapp, Michael Orlov,
  Mikael Arguedas, Patrick Roncagliolo, Peter Favrholdt, Roman
  Sokolkov, Yadu, jmachowinski

rosbag2_storage
===============

* Support service 2/2 --- rosbag2 service play (#1481)

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Update to use yaml-cpp version 0.8.0. (#1605)

* Use std::filesystem instead of rcpputils::fs (#1576)

* Make some changes for newer versions of uncrustify. (#1578)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Remove rcpputils::fs dependencies from rosbag2_storages (#1558)

* Improve performance in SqliteStorage::get_bagfile_size() (#1516)

* Make Player and Recorder Composable (#902) (#1419)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* ros2 bag convert now excludes messages not in [start_time;end_time]
  (#1455)

* Fix missing cstdint include (#1383)

* Implement storing and loading ROS_DISTRO from metadata.yaml and mcap
  files (#1241)

* Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michael
  Orlov, Patrick Roncagliolo, Peter Favrholdt, Roman Sokolkov, Zac
  Stanton, jmachowinski

rosbag2_storage_mcap
====================

* Support service 2/2 --- rosbag2 service play (#1481)

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Update to use yaml-cpp version 0.8.0. (#1605)

* Check existence of a file before passing it to the mcap reader
  (#1594)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Use rw_lock to protect mcap metadata lists. (#1561)

* Remove rcpputils::fs dependencies from rosbag2_storages (#1558)

* remove unused headers (#1544)

* Link and compile against rosbag2_storage_mcap: Fixed issue 1492
  (#1496)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* Store serialized metadata in MCAP file (#1423)

* Implement storing and loading ROS_DISTRO from metadata.yaml and mcap
  files (#1241)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Christopher Wecht, Emerson Knapp, Michael Orlov, Patrick
  Roncagliolo, Roman Sokolkov, Tomoya Fujita, jmachowinski, uupks

rosbag2_storage_sqlite3
=======================

* Support service 2/2 --- rosbag2 service play (#1481)

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Update to use yaml-cpp version 0.8.0. (#1605)

* Make some changes for newer versions of uncrustify. (#1578)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Remove rcpputils::fs dependencies from rosbag2_storages (#1558)

* Change an incorrect TSA annotation. (#1552)

* Improve performance in SqliteStorage::get_bagfile_size() (#1516)

* Update rosbag2_storage_sqlite3 to C++17. (#1501)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* Stop inheriting from std::iterator. (#1424)

* Implement storing and loading ROS_DISTRO from metadata.yaml and mcap
  files (#1241)

* Store metadata in db3 file (#1294)

* Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michael
  Orlov, Patrick Roncagliolo, Roman Sokolkov, jmachowinski

rosbag2_test_common
===================

* Support service 2/2 --- rosbag2 service play (#1481)

* Make some changes for newer versions of uncrustify. (#1578)

* Implement service recording and display info about recorded services
  (#1480)

* Add extra checks in execute_and_wait_until_completion(..) (#1346)

* Address flakiness in rosbag2_play_end_to_end tests (#1297)

* Contributors: Barry Xu, Chris Lalancette, Michael Orlov

rosbag2_test_msgdefs
====================

* Implement service recording and display info about recorded services
  (#1480)

* Don't crash when type definition cannot be found (#1350) * Don't
  fail when type definition cannot be found

* Contributors: Barry Xu, Emerson Knapp

rosbag2_tests
=============

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Added exclude-topic-types to record (#1582)

* Use std::filesystem instead of rcpputils::fs (#1576)

* Filter topic by type (#1577)

* Make some changes for newer versions of uncrustify. (#1578)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Improve performance in SqliteStorage::get_bagfile_size() (#1516)

* Implement service recording and display info about recorded services
  (#1480)

* Mark play_end_to_end test as xfail in Windows (#1452)

* Implement storing and loading ROS_DISTRO from metadata.yaml and mcap
  files (#1241)

* Address flakiness in rosbag2_play_end_to_end tests (#1297)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Cristóbal Arroyo, Emerson Knapp, Michael Orlov, Roman
  Sokolkov, jmachowinski

rosbag2_transport
=================

* Removed warnings - unqualified-std-cast-call (#1618) (#1622)

* Add node name to the Read(Write)SplitEvent message (#1609)

* Add option to disable recorder keyboard controls (#1607)

* Support service 2/2 --- rosbag2 service play (#1481)

* Use middleware send and receive timestamps from message_info during
  recording (#1531)

* Update to use yaml-cpp version 0.8.0. (#1605)

* Gracefully handle SIGINT and SIGTERM signals for play and burst CLI
  (#1557)

* Added exclude-topic-types to record (#1582)

* Use std::filesystem instead of rcpputils::fs (#1576)

* Add transactional state mutex for RecorderImpl class. (#1547)

* Overhaul in the rosbag2_transport::TopicFilter class and relevant
  tests (#1585)

* Filter topic by type (#1577)

* fix: use size_t instead of uint64_t in play_options YAML converter
  (#1575)

* Make some changes for newer versions of uncrustify. (#1578)

* Add topic_id returned by storage to the TopicMetadata (#1538)

* Workaround for flaky test_play_services running with fastrtps
  (#1556)

* Add proper message for --start-paused (#1537)

* "Recording stopped" prints only once. (#1530)

* Cleanup the rosbag2_transport tests (#1518)

* Implement service recording and display info about recorded services
  (#1480)

* Add option to set compression threads priority (#1457)

* Bugfix for incorrect playback rate changes when pressing buttons
  (#1513)

* Make Player and Recorder Composable (#902) (#1419)

* Clang fixes for the latest PlayerImpl code. (#1507)

* Make "rosbag2_transport::Player::play()" run in a separate thread
  (#1503)

* Switch to target_link_libraries everywhere. (#1504)

* Use enum values for offered_qos_profiles in code and string names in
  serialized metadata (#1476)

* Redesign Player class with PIMPL idiom (#1447)

* Don't warn for unknown types if topics are not selected (#1466)

* Remove unused concurrentqueue implementation. (#1465)

* Fix uninitialized value pointed out by clang static analysis.
  (#1440)

* Fix the build with rmw_fastrtps_dynamic. (#1416)

* Fix for rosbag2_transport::Recorder failures due to the unhandled
  exceptions (#1382)

* When using sim time, wait for /clock before beginning recording
  (#1378)

* Fix for possible freeze in Recorder::stop() (#1381)

* Revert "Don't record sim-time messages before first /clock (#1354)"
  (#1377)

* Don't record sim-time messages before first /clock (#1354)

* Fix a clang warning about uninitialized variable. (#1370)

* [bugfix] for parameters not passing to recorder's node from child
  component (#1360)

* Change subscriptions from GenericSubscripton to SubscriptionBase
  (#1337)

* Add recorder stop() API (#1300)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Bernd Pfrommer,
  Chris Lalancette, Christoph Fröhlich, Daisuke Nishimatsu, Emerson
  Knapp, Michael Orlov, Patrick Roncagliolo, Roman Sokolkov, Tomoya
  Fujita, jmachowinski, mergify[bot]

rosidl_cmake
============

* Improve deprecation notice of rosidl_target_interface to give a hint
  on how to update the code (#788)

* Add rosidl_find_package_idl helper function (#754)

* Remove unused splitting of .srv files in CMake (#753)

* Contributors: Alexis Paques, Mike Purvis, Shane Loretz

rosidl_dynamic_typesupport
==========================

* uchar: fix conditional include/typedef (#10)

* uchar: use __has_include(..) on separate line (#8)

* Refactor the handling of nested types. (#7)

* Add C++ version check to char16 definition (#3)

* Contributors: Antonio Cuadros, Chris Lalancette, G.A. vd. Hoorn

rosidl_generator_c
==================

* Fixed warnings - strict-prototypes (#800) (#802)

* Set hints to find the python version we actually want. (#785)

* Add rosidl_find_package_idl helper function (#754)

* Fix IWYU for clangd in C and C++ (#742)

* Contributors: Alexis Paques, Chris Lalancette, Mike Purvis,
  mergify[bot]

rosidl_generator_cpp
====================

* Set hints to find the python version we actually want. (#785)

* Fix constant generation for C++ floats (#772)

* Add rosidl_find_package_idl helper function (#754)

* Fixed visibility control file added to wrong header list variable.
  (#755)

* Fix deprecation warnings for message constants (#750)

* Generate typesupport declarations for actions, messages and services
  (#703)

* Fix IWYU for clangd in C and C++ (#742)

* Contributors: Alexis Paques, Chris Lalancette, Emerson Knapp, Mike
  Purvis, Stefan Fabian

rosidl_generator_dds_idl
========================

* Remove unnecessary parentheses. (#61)

* Contributors: Chris Lalancette

rosidl_generator_py
===================

* Revert install of .so files into python path (#211) There seems that
  some regression might have happened after #195. When removing those
  2 lines, we avoid to install the .so files in lib *and* python path.

* Prototype code for seeing if FindPython3 is usable for rosidl_python
  (#140)

* Add in a missing space. (#203)

* Install compiled libraries only to 'lib' (#195)

* Fix: Missing dependency that causes cmake error in downstream
  (resolves https://github.com/ros2/rosidl_python/issues/198) (#199)

* Contributors: Chris Lalancette, Isaac Saito, Matthias Schoepfer,
  Scott K Logan, Shane Loretz

rosidl_generator_tests
======================

* Fixed warnings - strict-prototypes (#800) (#802)

* Increased the cpplint timeout to 300 seconds (#797)

* Fixes for modern uncrustify. (#793)

* Fix constant generation for C++ floats (#772)

* Fix same named types overriding typesources (#759)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Emerson
  Knapp, mergify[bot]

rosidl_generator_type_description
=================================

* Set hints to find the python version we actually want. (#785)

* Remove unnecessary parentheses. (#783)

* Contributors: Chris Lalancette

rosidl_parser
=============

* Adding interfaces to support "@key" annotation (#796) Co-authored-
  by: Mario Dominguez <mariodominguez@eprosima.com>

* Small fix for newer flake8 compatibility. (#792)

* Remove unnecessary parentheses. (#783)

* Contributors: Chris Lalancette, Miguel Company

rosidl_pycommon
===============

* Remove unnecessary parentheses. (#783)

* Fix same named types overriding typesources (#759)

* Contributors: Chris Lalancette, Emerson Knapp

rosidl_runtime_c
================

* Switch to target_link_libraries. (#776)

* Set the C++ version to 17. (#761)

* Mark _ in benchmark tests as unused. (#741) This helps clang static
  analysis.

* Contributors: Chris Lalancette

rosidl_runtime_cpp
==================

* Suppress a warning around BoundedVector. (#803) (#804) The comment
  has more explanation, but in short GCC 13 has false positives around
  some warnings, so we suppress it for BoundedVector. (cherry picked
  from commit 858e76adb03edba00469b91d50dd5fe0dcb34236) Co-authored-
  by: Chris Lalancette <clalancette@gmail.com>

* Contributors: mergify[bot]

rosidl_runtime_py
=================

* Some fixes for modern flake8. (#25)

* Contributors: Chris Lalancette

rosidl_typesupport_c
====================

* Fixed warnings - strict-prototypes (#155) (#156)

* compare string contents but string pointer addresses. (#153)

* Set hints to find the python version we actually want. (#150)

* Don't override user provided compile definitions (#145)

* Contributors: Chris Lalancette, Emerson Knapp, Tomoya Fujita,
  mergify[bot]

rosidl_typesupport_cpp
======================

* compare string contents but string pointer addresses. (#153)

* Set hints to find the python version we actually want. (#150)

* Don't override user provided compile definitions (#145)

* Added C interfaces to obtain service and action type support. (#143)

* Contributors: Chris Lalancette, Emerson Knapp, Stefan Fabian, Tomoya
  Fujita

rosidl_typesupport_fastrtps_c
=============================

* Adding interfaces to support "@key" annotation (#116) Co-authored-
  by: Mario Dominguez <mariodominguez@eprosima.com>

* Support Fast CDR v2 (#114)

* Improve wide string (de)serialization (#113)

* Set hints to find the python version we actually want. (#112) Co-
  authored-by: Michael Carroll <michael@openrobotics.org>

* Update to C++17 (#111)

* Account for alignment on "is_plain" calculations (#108)

* Contributors: Chris Lalancette, Miguel Company

rosidl_typesupport_fastrtps_cpp
===============================

* Fix how header template works to prevent double-inclusion (#117) Co-
  authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>

* Adding interfaces to support "@key" annotation (#116) Co-authored-
  by: Mario Dominguez <mariodominguez@eprosima.com>

* Support Fast CDR v2 (#114)

* Improve wide string (de)serialization (#113)

* Set hints to find the python version we actually want. (#112) Co-
  authored-by: Michael Carroll <michael@openrobotics.org>

* Update to C++17 (#111)

* Account for alignment on "is_plain" calculations (#108)

* Avoid redundant declarations in generated code for services and
  actions (#102)

* Contributors: Chris Lalancette, Emerson Knapp, Michael Carroll,
  Miguel Company

rosidl_typesupport_introspection_c
==================================

* Fixed warnings - strict-prototypes (#800) (#802)

* Adding interfaces to support "@key" annotation (#796) Co-authored-
  by: Mario Dominguez <mariodominguez@eprosima.com>

* Set hints to find the python version we actually want. (#785)

* Add rosidl_find_package_idl helper function (#754)

* update comment (#757)

* Contributors: Chen Lihui, Chris Lalancette, Miguel Company, Mike
  Purvis, mergify[bot]

rosidl_typesupport_introspection_cpp
====================================

* Adding interfaces to support "@key" annotation (#796) Co-authored-
  by: Mario Dominguez <mariodominguez@eprosima.com>

* Set hints to find the python version we actually want. (#785)

* Switch to target_link_libraries. (#776)

* Add rosidl_find_package_idl helper function (#754)

* update comment (#757)

* Fix deprecation warnings for message constants (#750)

* Contributors: Chen Lihui, Chris Lalancette, Emerson Knapp, Miguel
  Company, Mike Purvis

rosidl_typesupport_introspection_tests
======================================

* One last uncrustify fix for newer uncrustify. (#795)

* Disable zero-variadic-macro-arguments warning when using clang.
  (#768)

* Fixed C++20 warning implicit capture of this in lambda (#766)

* Contributors: AiVerisimilitude, Chris Lalancette

rosidl_typesupport_tests
========================

* Suppress uncrustify on long lines. (#152)

* Contributors: Chris Lalancette

rpyutils
========

* correct the URL and f-strings format (#11)

* Contributors: Chen Lihui

rqt
===

* Add a test dependency on pytest. (#306)

* Contributors: Chris Lalancette

rqt_bag
=======

* Add in copyright tests to rqt_bag. (#154)

* Add a test dependency on pytest. (#153)

* Revert "Add a dependency on pytest to rqt_bag and rqt_bag_plugins.
  (#… (#151)

* Update maintainer to myself. (#150)

* Update maintainer list in package.xml files (#149)

* Add a dependency on pytest to rqt_bag and rqt_bag_plugins. (#148)

* [ros2] Enable Save (#142)

* Call close (#141)

* Use default storage id (#139)

* Contributors: Chris Lalancette, Michael Jeronimo, Yadu, Yadunund

rqt_bag_plugins
===============

* Add a test dependency on pytest. (#153)

* Revert "Add a dependency on pytest to rqt_bag and rqt_bag_plugins.
  (#… (#151)

* Update maintainer to myself. (#150)

* Update maintainer list in package.xml files (#149)

* Add a dependency on pytest to rqt_bag and rqt_bag_plugins. (#148)

* Contributors: Chris Lalancette, Michael Jeronimo

rqt_console
===========

* Add a test dependency on pytest. (#45)

* Contributors: Arne Hitzmann, Chris Lalancette

rqt_graph
=========

* Update maintainer list in package.xml files (#92)

* Add a test dependency on python3-pytest. (#91)

* Refresh rosgraph when params checkbox is clicked (#86)

* Contributors: Chris Lalancette, Michael Jeronimo, Yadunund

rqt_gui_cpp
===========

* Switch to target_link_libraries. (#297)

* Contributors: Chris Lalancette

rqt_gui_py
==========

* fix an exception raised while press ctrl+c to exit (#291)

* Contributors: Chen Lihui

rqt_msg
=======

* Add in python3-pytest test dependency. (#19)

* Small cleanups to rqt_msg (#16)

* Contributors: Chris Lalancette

rqt_plot
========

* Add in copyright tests to rqt_bag. (#95)

* Add a test dependency on pytest. (#94)

* Add in a pytest dependency for running tests. (#92)

* Fix regression from #87 (#90)

* Contributors: Chris Lalancette, Yadunund

rqt_publisher
=============

* Use raw strings for regular expressions. (#44)

* Switch maintainer to me. (#43)

* Update maintainer list in package.xml files (#42)

* Add in a test dependency on pytest. (#41)

* Contributors: Chris Lalancette, Michael Jeronimo

rqt_py_common
=============

* Allow to autocomplete namespaced topics (#299)

* Contributors: Alejandro Hernández Cordero

rqt_py_console
==============

* Add in test dependency on pytest. (#16)

* Fix a crash in the rqt_py_console dialog box. (#15)

* Contributors: Chris Lalancette

rqt_reconfigure
===============

* Explicitly add a pytest test dependency. (#141)

* Remove unnecessary parentheses around if statements. (#140)

* Fixed executor conflict (#126)

* Add param filtering (#128)

* Fix handling of namespaces in the node tree (#132)

* Contributors: Aleksander Szymański, Chris Lalancette, Devarsi Rawal,
  Nick Lamprianidis

rqt_service_caller
==================

* Add in a pytest test dependency. (#28)

* Contributors: Chris Lalancette

rqt_shell
=========

* Change maintainer to clalancette. (#21)

* Add in pytest test dependency. (#19)

* Contributors: Chris Lalancette, Michael Jeronimo

rqt_srv
=======

* Add explicit dependency to python3-pytest. (#12)

* Minor cleanups in rqt_srv for ROS 2 (#9)

* Contributors: Chris Lalancette

rqt_topic
=========

* Small fix for modern flake8. (#50)

* Add explicit python3-pytest dependency. (#48)

* Contributors: Chris Lalancette

rti_connext_dds_cmake_module
============================

* Use unified approach for checking the existence of environment
  variables (#105)

* Contributors: Christopher Wecht

rttest
======

* Update to C++17 (#124)

* Contributors: Chris Lalancette

rviz2
=====

* Add "R" key as shortcut for resetTime (#1088)

* Switch to target_link_libraries. (#1098)

* Contributors: Chris Lalancette, Paul Erik Frivold

rviz_assimp_vendor
==================

* Removed assimp warnings (#1191) (#1192) (cherry picked from commit
  e8dd485d19a35d3abba905020741973e613334e3) Co-authored-by: Alejandro
  Hernández Cordero <alejandro@openrobotics.org>

* Update the vendored package path. (#1184) Since we just updated to
  assimp 5.3, we also need to update the path we look for it. This
  should fix the build with clang which is currently failing.

* Update assimp vendor to 5.3.1 (#1182) This matches what is in Ubuntu
  24.04.

* Update to assimp 5.2.2 (#968)

* Fix the vendoring flags for clang compilation. (#1003)

* Switch to ament_cmake_vendor_package (#995)

* Contributors: Chris Lalancette, Scott K Logan, mergify[bot]

rviz_common
===========

* Update to yaml-cpp 0.8.0 (#1183) yaml-cpp 0.8.0 has a proper CMake
  target, i.e. yaml-cpp::yaml-cpp. Use that here.

* Remove regex_filter_property.hpp from the moc lines. (#1172) Since
  it has no SLOTS or SIGNALS, we don't need to run MOC on it. That
  will both speed up the compilation and remove a warning when
  building.

* Added regex filter field for TF display (#1032)

* Fix camera display overlay (#1151)

* Fixes for uncrustify 0.78. (#1155) Mostly what we do here is to
  disable the indentation on certain constructs that are different
  between 0.72 and 0.78. It isn't my preferred solution, but since it
  only affects a small amount of code (and most of that in macros),
  this seems acceptable to me.

* Append measured subscription frequency to topic status (#1113)

* Implement reset time service (#1109)

* Add "R" key as shortcut for resetTime (#1088)

* Add fullscreen startup option (#1097)

* Switch to target_link_libraries. (#1098)

* Initialize more of the visualization_manager members. (#1090)

* Explicit time conversions and comparisons (#1087)

* Rolling namespace in title (#1074)

* Removed unused code (#1044)

* Remove unused LineEditWithButton::simulateReturnPressed() (#1040)

* Remove warning in depth_cloud_mld.cpp (#1021)

* Added DepthCloud default plugin (#996)

* Stop inheriting from std::iterator. (#1013) In C++17, inheriting
  from std::iterator has been deprecated:
  https://www.fluentcpp.com/2018/05/08/std-iterator-deprecated/ Here,
  switch away from inheriting and just define the interface ourselves
  (which is the current recommended best practice). This removes some
  warnings when building with gcc 13.1.1

* use static QCoreApplication::processEvents() function without a
  QApplication instance (#924)

* Re-implemented setName for tools (#989)

* Add a libqt5-svg dependency to rviz_common. (#992)

* Remove onHelpWiki. (#985)

* Clean Code (#975)

* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Chris
  Lalancette, Felix Exner (fexner), Hyunseok, Markus Bader, Paul Erik
  Frivold, Yadu, Yannis Gerlach, mosfet80

rviz_default_plugins
====================

* Make sure to export all rviz_default_plugins dependencies. (#1181)

* Increase the cpplint timeout to 180 seconds. (#1179)

* Switch to gz_math_vendor. (#1177)

* Fixed camera info warning (#1175)

* Added CameraInfo display (#1166)

* apply origin rotation to inertia box visualization (#1171)

* Added regex filter field for TF display (#1032)

* Added point_cloud_transport (#1008)

* Select QoS reliability policy in DepthCloud Plugin (#1159)

* Fixed crash on DepthCloud plugin (#1161)

* Fixes for uncrustify 0.78. (#1155) Mostly what we do here is to
  disable the indentation on certain constructs that are different
  between 0.72 and 0.78. It isn't my preferred solution, but since it
  only affects a small amount of code (and most of that in macros),
  this seems acceptable to me.

* Fixed crash on DepthCloudPlugin (#1133)

* Wrench accepth nan values fix (#1141)

* DepthCloud plugin: Append measured subscription frequency to topic
  status (#1137)

* Added Cache to camera display for TimeExact (#1138)

* Fixed transport name in DepthCloud plugin (#1134)

* Fix time-syncing message (#1121)

* Switch from ROS_TIME to SYSTEM_TIME on rclcpp::Time construction
  (#1117)

* Append measured subscription frequency to topic status (#1113)

* Fix typo (#1104)

* Fix potencial leak / seg fault (#726)

* Fixed screw display (#1093)

* Explicit time conversions and comparisons (#1087)

* Handle missing effort limit in URDF (#1084)

* (robot) fix styling of log msg (#1080)

* Fix image display wrapping (#1038)

* removed enableInteraction reference (#1075)

* Fix ODR violations in interactive_marker displays. (#1068)

* Improve error handling in LaserScanDisplay (#1035)

* Fix implicit capture of "this" warning in C++20 (#1053)

* Removed unused code (#1044)

* Fixed AccelStamped, TwistStamped and Wrench icons (#1041)

* Fix the flakey rviz_rendering tests (#1026)

* Don't pass screw_display.hpp to the moc generator. (#1018) Since it
  isn't a Qt class, you get a warning from moc: Note: No relevant
  classes found. No output generated. Just skip adding it to the moc
  list here, which gets rid of the warning.

* Added DepthCloud default plugin (#996)

* Added TwistStamped and AccelStamped default plugins (#991)

* Added Effort plugin (#990)

* Improve the compilation time of rviz_default_plugins (#1007)

* Switch to ament_cmake_vendor_package (#995)

* Modify access specifier to protected or public for the scope of
  processMessage() member function (#984)

* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Austin
  Moore, Chris Lalancette, Christoph Fröhlich, Hyunseok, Jonas Otto,
  Lewe Christiansen, Matthijs van der Burgh, Patrick Roncagliolo,
  Scott K Logan, Yadu

rviz_ogre_vendor
================

* Update zlib into CMakeLists.txt (#1128) (#1195) Changes in 1.3 (18
  Aug 2023) - Remove K&R function definitions and zlib2ansi - Fix bug
  in deflateBound() for level 0 and memLevel 9 - Fix bug when
  gzungetc() is used immediately after gzopen() - Fix bug when using
  gzflush() with a very small buffer - Fix crash when gzsetparams()
  attempted for transparent write - Fix test/example.c to work with
  FORCE_STORED - Rewrite of zran in examples (see zran.c version
  history) - Fix minizip to allow it to open an empty zip file - Fix
  reading disk number start on zip64 files in minizip - Fix logic
  error in minizip argument processing - Add minizip testing to
  Makefile - Read multiple bytes instead of byte-by-byte in minizip
  unzip.c - Add memory sanitizer to configure (--memory) - Various
  portability improvements - Various documentation improvements -
  Various spelling and typo corrections Co-authored-by: Chris
  Lalancette <clalancette@gmail.com> (cherry picked from commit
  32eb8b9404927883247e868ab0c7d62b80df2ed1) Co-authored-by: mosfet80
  <realeandrea@yahoo.it>
