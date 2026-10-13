# ROS 2 Kilted Kaiju Complete Changelog (part 4 of 5)

* Update minimum CMake version CMakeLists.txt.em (#969)

* Add ament_xmllint test by default to ament_python packages. (#957)

* Drop dependency on python3-pkg-resources (#946)

* Support empy4 and empy3 (#921)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Larry
  Gezelius, Scott K Logan, Sebastian Castro, Shane Loretz, Shynur

ros2run
=======

* Add signal handler SIGIN/SIGTERM to ros2run (#899)

* Contributors: Tomoya Fujita

ros2service
===========

* Use "get_service" in "ros2service call" (#994)

* Allow zenoh tests to run with multicast (#992)

* Support QoS options for "ros2 service call" (#966)

* Maintaining consistency of automatically putting time stamps in the
  service and action calls similiar to publishing in rostopics. (#961)

* Switch to using the rclpy.init context manager. (#920)

* Switch to using rclpy.init context manager. (#918)

* Contributors: Chris Lalancette, Michael Carlstrom, Michael Carroll,
  Sukhvansh Jain, Tomoya Fujita

ros2test
========

* Add in test_xmllint to ros2test. (#13)

* Contributors: Chris Lalancette

ros2topic
=========

* Custom Completion Finder for fetching topic prototype (#995)

* Documented now and auto keywords (#1008)

* Conditional deserialization of message for "ros2 topic hz" (#1005)

* Enable "ros2 topic echo" with entries of array fields (#996)

* Allow zenoh tests to run with multicast (#992)

* Adapt tests to Zenoh (#988)

* Adjust topic hz and bw command description (#987)

* Add support for topic QOS for ros2topic bw, delay and hz (#935)

* Start the simulation from 1 second for the test (#975)

* Support QoS options for "ros2 service call" (#966)

* Support ros2 topic pub yaml file input (#925)

* support multiple fields in ros2topic echo (#964)

* NodeStrategy supports node name argument. (#941)

* feat(echo --clear): add --clear option to echo (#819)

* Support multiple topics via ros2 topic hz. (#929)

* Remove TODO for OpenSplice DDS issue. (#928)

* Switch to using rclpy.init context manager. (#918)

* Contributors: Alejandro Hernández Cordero, Anthony Welte, Chris
  Lalancette, Fabian Thomsen, Florencia, Guillaume Beuzeboc, Kostubh
  Khandelwal, Leander Stephen D'Souza, Martin Pecka, Michael Carroll,
  SangtaekLee, Tomoya Fujita

ros2trace
=========

* Expose types for tracing tools (#153)

* Contributors: Michael Carlstrom

ros_environment
===============

* Update ROS_DISTRO for Kilted Kaiju (#41)

* Remove CODEOWNERS. (#40)

* Contributors: Chris Lalancette, Scott K Logan

rosbag2
=======

* Support replaying multiple bags (#1848)

* Contributors: Christophe Bedard

rosbag2_compression
===================

* Bugfix: Update metadata with new file_info before saving it first
  time (#1843)

* Make snapshot writing into a new file each time it is triggered
  (#1842)

* Add cli option compression-threads-priority (#1768)

* Bugfix for bag_split event callbacks called to early with file
  compression (#1643)

* Fix for regression in "open_succeeds_twice" and
  "minimal_writer_example" tests (#1667)

* Bugfix for writer not being able to open again after closing (#1599)

* Contributors: Alejandro Hernández Cordero, Michael Orlov, Roman,
  yschulz

rosbag2_cpp
===========

* Add support for finding action types message definitions in the
  "LocalMessageDefinitionSource" class to be able to store actions
  message definitions during recording. (#1965)

* Add message sequence number to the messages write API (#1961)

* Implement actions recording and displaying information about
  recorded actions features (#1939)

* Set environment variables to run tests with "rmw_zenoh_cpp" with
  multicast discovery (#1946)

* Add more logging info to storage and reader/writer open operations
  (#1881)

* Add PlayerClock::wakeup() to interrupt sleeping (#1869)

* Support replaying multiple bags (#1848)

* Bugfix: Update metadata with new file_info before saving it first
  time (#1843)

* Make snapshot writing into a new file each time it is triggered
  (#1842)

* Bugfix for rosbag2_cpp serialization converter (#1814)

* Allow unknown types in bag rewrite (#1812)

* Add computation of size contribution to info verb (#1726)

* [WIP] Remove rcpputils::fs dependencies in rosbag2 packages (#1740)

* Removed deprecated write method (#1738)

* Bugfix for bag_split event callbacks called to early with file
  compression (#1643)

* Add topics with zero message counts to the
  SQLiteStorage::get_metadata(). (#1725)

* Propagate "custom_data" and "ros_distro" in to the metadata.yaml
  file during re-indexing (#1700)

* Bugfix for writer not being able to open again after closing (#1599)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe
  Bedard, Cole Tucker, Michael Orlov, Nicola Loi, Tomoya Fujita,
  Yadunund, yschulz

rosbag2_examples_cpp
====================

* Add rosbag2_examples_cpp/simple_bag_reader.cpp. (#1683)

* Contributors: Tomoya Fujita

rosbag2_examples_py
===================

* avoid using internal modules for examples. (#1905)

* Add test_xmllint.py to python packages. (#1879)

* simple_bag_reader.py should publish the data for each timer
  callback. (#1767)

* Change the python examples to use the rclpy context manager. (#1758)

* Add rosbag2_examples_cpp/simple_bag_reader.cpp. (#1683)

* Contributors: Chris Lalancette, Tomoya Fujita

rosbag2_py
==========

* Add message sequence number to the messages write API (#1961)

* Add actions replay feature (#1955)

* Implement actions recording and displaying information about
  recorded actions features (#1939)

* Add bindings to close method in PyReader and PyCompressionReader
  (#1935)

* Remove SHARED from pybind11_add_module (#1929)

* Progress bar for ros2 bag play (#1836)

* Upstream quality changes from Apex.AI part 1 (#1903)

* Add support for replaying based on publication timestamp (#1876)

* Support replaying multiple bags (#1848)

* Add in python3-dev build dependency. (#1863)

* Add "--sort" CLI option to the "ros2 bag info" command (#1804)

* Remove use of python_cmake_module (#1570)

* Added method to introspect QoS in Python (#1648)

* Update CI scripts to use Ubuntu Noble distros and bump action
  scripts to latest versions (#1709)

* Add cli option compression-threads-priority (#1768)

* Add computation of size contribution to info verb (#1726)

* Bugfix for wrong timestamps in ros2 bag info (#1745)

* Add bindings for LocalMessageDefinitionSource (#1697)

* Add --log-level to ros2 bag play and record (#1625)

* Included to_rclcpp_qos_vector to Python wrappers (#1642)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Christophe Bedard, Michael Orlov, Nicola Loi, Roman,
  Sanoronas, Silvio Traversaro, methylDragon, Øystein Sture

rosbag2_storage
===============

* Add message sequence number to the messages write API (#1961)

* Add actions replay feature (#1955)

* Add more logging info to storage and reader/writer open operations
  (#1881)

* Contributors: Barry Xu, Michael Orlov

rosbag2_storage_mcap
====================

* Add message sequence number to the messages write API (#1961)

* Add actions replay feature (#1955)

* Upstream quality changes from Apex.AI part 1 (#1903)

* Add vscode gitignore rule and remove vscode folder (#1698)

* Contributors: Barry Xu, Michael Orlov, methylDragon

rosbag2_storage_sqlite3
=======================

* Add actions replay feature (#1955)

* Fix incorrect zero size for sqlite storage (#1759)

* Fix for failing throws_on_invalid_pragma_in_config_file on Windows
  (#1742)

* Add topics with zero message counts to the
  SQLiteStorage::get_metadata(). (#1725)

* Contributors: Barry Xu, Michael Orlov, Roman, Tomoya Fujita

rosbag2_test_common
===================

* Add actions replay feature (#1955)

* Implement actions recording and displaying information about
  recorded actions features (#1939)

* Upstream quality changes from Apex.AI part 1 (#1903)

* Use tmpfs in rosbag2 temporary_directory_fixture (#1901)

* Add debug information for flaky can_record_again_after_stop test
  (#1871)

* Remove use of python_cmake_module (#1570)

* Improve the reliability of rosbag2 tests (#1796)

* Small cleanups to the rosbag2 tests. (#1792)

* [WIP] Remove rcpputils::fs dependencies in rosbag2 packages (#1740)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Michael Orlov

rosbag2_test_msgdefs
====================

* Add support for finding action types message definitions in the
  "LocalMessageDefinitionSource" class to be able to store actions
  message definitions during recording. (#1965)

* Contributors: Tomoya Fujita

rosbag2_tests
=============

* Implement actions recording and displaying information about
  recorded actions features (#1939)

* Upstream quality changes from Apex.AI part 1 (#1903)

* Increase timeout to 180s for test_rosbag2_record_end_to_end (#1889)

* Add "--sort" CLI option to the "ros2 bag info" command (#1804)

* Improve the reliability of rosbag2 tests (#1796)

* Small cleanups to the rosbag2 tests. (#1792)

* Add computation of size contribution to info verb (#1726)

* Bugfix for wrong timestamps in ros2 bag info (#1745)

* Fix for a false negative integration test with bag split in recorder
  (#1743)

* Propagate "custom_data" and "ros_distro" in to the metadata.yaml
  file during re-indexing (#1700)

* Sweep cleanup in rosbag2 recorder CLI args verification code (#1633)

* Fix for regression in "open_succeeds_twice" and
  "minimal_writer_example" tests (#1667)

* Add optional '--topics' CLI argument for 'ros2 bag record' (#1632)

* Bugfix for writer not being able to open again after closing (#1599)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Cole Tucker, Michael Orlov, Nicola Loi, Sanoronas,
  yadunund, yschulz

rosbag2_transport
=================

* Add actions replay feature (#1955)

* Implement actions recording and displaying information about
  recorded actions features (#1939)

* Set environment variables to run tests with "rmw_zenoh_cpp" with
  multicast discovery (#1946)

* Initialize filter with namespaced updated topics and services.
  (rolling) (#1944)

* Fix: QoS incompatibilities are not expected with rmw_zenoh_cpp
  (#1936)

* Address windows warnings in the progress bar class (#1927)

* Don't delete existing subscription if failed to create a new one
  (#1923)

* Progress bar for ros2 bag play (#1836)

* Upstream quality changes from Apex.AI part 1 (#1903)

* Use tmpfs in rosbag2 temporary_directory_fixture (#1901)

* Bugfix: Recorder discovery does not restart after being stopped
  (#1894)

* Bugfix. Event publisher not starting for second run after stop
  (#1888)

* Add support for replaying based on publication timestamp (#1876)

* Publish clock after delay is over and disable delay on next loops
  (#1861)

* Add PlayerClock::wakeup() to interrupt sleeping (#1869)

* Add debug information for flaky can_record_again_after_stop test
  (#1871)

* Support replaying multiple bags (#1848)

* Reintroduce "Don't warn for unknown types if topics are not
  selected" (#1825)

* Allow unknown types in bag rewrite (#1812)

* Improve the reliability of rosbag2 tests (#1796)

* Removed warnings (#1794)

* Small cleanups to the rosbag2 tests. (#1792)

* Add cli option compression-threads-priority (#1768)

* [WIP] Remove rcpputils::fs dependencies in rosbag2 packages (#1740)

* Bugfix for bag_split event callbacks called to early with file
  compression (#1643)

* Bugfix for issue where unable to create composable nodes with
  compression (#1679)

* Add support for "all" and "exclude" in RecordOptions YAML decoder
  (#1664)

* Add unit tests to cover message's send and received timestamps
  during recording (#1641)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris
  Lalancette, Christophe Bedard, Michael Orlov, Nicola Loi, Ramon
  Wijnands, Roderick Taylor, Roman, Yuyuan Yuan, Øystein Sture

rosidl_adapter
==============

* Types for rosidl_adapter (#828)

* Support empy3 and empy4 (#821)

* Contributors: Alejandro Hernández Cordero, Michael Carlstrom

rosidl_cli
==========

* Rosidl cli types with "specs_set" fix (#831)

* Contributors: Chris Lalancette, Michael Carlstrom

rosidl_core_generators
======================

* Add mechanism to disable workaround for dependency groups (#3)

* Contributors: Scott K Logan

rosidl_core_runtime
===================

* Add mechanism to disable workaround for dependency groups (#3)

* Contributors: Scott K Logan

rosidl_default_runtime
======================

* Minor update to quality declaration (#27)

* Contributors: Christophe Bedard

rosidl_dynamic_typesupport
==========================

* Switch to ament_cmake_ros_core package (#15)

* Bump minimum CMake version to 3.20 (#14)

* Drop support for long double/float128. (#12)

* Contributors: Chris Lalancette, Michael Carroll, mosfet80

rosidl_dynamic_typesupport_fastrtps
===================================

* Switch to ament_cmake_ros_core package (#8)

* Changes to build against Fast DDS 3.0 (#5)

* Drop support for long double/float128. (#6)

* Contributors: Chris Lalancette, Miguel Company, Scott K Logan

rosidl_generator_c
==================

* Switch to ament_cmake_ros_core package (#856)

* Deterministic iteration order for reproducible codegen (#846)

* Add types "rosidl_pycommon" (#824)

* Contributors: Harry Sarson, Michael Carlstrom, Michael Carroll

rosidl_generator_cpp
====================

* Add name and data_type traits for actions (#848)

* Add types "rosidl_pycommon" (#824)

* Contributors: Michael Carlstrom, Nathan Wiebe Neufeldt

rosidl_generator_dds_idl
========================

* Update cmake version requirements (#64)

* Contributors: mosfet80

rosidl_generator_py
===================

* Fix "__eq__" for Array fields (#224)

* Remove use of ament_target_dependencies (#222)

* Revamp how we check for the correct class. (#218)

* Remove python_cmake_module and set hints (#204)

* Add rosidl_generator_py to the rosidl_runtime_packages group (#212)

* Contributors: Chris Lalancette, Michael Carlstrom, Scott K Logan,
  Shane Loretz

rosidl_generator_tests
======================

* Add name and data_type traits for actions (#848)

* Silence one more gcc false-positive. (#814)

* Switch to using fastjsonschema for schema validation. (#809)

* Contributors: Chris Lalancette, Nathan Wiebe Neufeldt

rosidl_generator_type_description
=================================

* Switch to ament_cmake_ros_core package (#856)

* Contributors: Michael Carroll

rosidl_parser
=============

* Finish adding types to "rosidl_parser" (#832)

* Add types to definition.py in "rosidl_parser" (#791)

* Contributors: Michael Carlstrom

rosidl_pycommon
===============

* Add test_xmllint to rosidl_pycommon. (#833)

* Add types "rosidl_pycommon" (#824)

* Support empy3 and empy4 (#821)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael
  Carlstrom

rosidl_runtime_c
================

* Switch to ament_cmake_ros_core package (#856)

* Implement "resize" function for String (#806)

* Fix u16 docs and improve docs formatting (#805)

* Contributors: Christophe Bedard, Michael Carroll, WATANABE Aoi

rosidl_runtime_cpp
==================

* Suppress warnings in the benchmarks for upstream GCC false
  positives. (#810)

* Contributors: Chris Lalancette

rosidl_runtime_py
=================

* Use deepcopy in set_message_fields for safety. (#34)

* Remove CODEOWNERS and mirror-rolling-to-master. (#31)

* Contributors: Chris Lalancette, Tomoya Fujita

rosidl_typesupport_c
====================

* Switch to ament_cmake_ros_core package (#166)

* Uniform cmake requirement (#163)

* Cleanup warning message in rosidl_typesupport_c tests. (#161)

* Add mechanism to disable workaround for dependency groups (#157)

* Add 'mimick' label to tests which use Mimick (#158)

* Contributors: Chris Lalancette, Scott K Logan, mosfet80

rosidl_typesupport_cpp
======================

* Switch to ament_cmake_ros_core package (#166)

* Uniform cmake requirement (#163)

* Add mechanism to disable workaround for dependency groups (#157)

* Contributors: Scott K Logan, mosfet80

rosidl_typesupport_fastrtps_c
=============================

* Switch to ament_cmake_ros_core package (#127)

* Remove dependency on fastrtps_cmake_module (#120)

* Remove CODEOWNERS and mirror-rolling-to-master workflow (#124)

* Remove deprecated functions benchmark tests (#122)

* Contributors: Chris Lalancette, Miguel Company, Scott K Logan

rosidl_typesupport_fastrtps_cpp
===============================

* Switch to ament_cmake_ros_core package (#127)

* Remove dependency on fastrtps_cmake_module (#120)

* Remove CODEOWNERS and mirror-rolling-to-master workflow (#124)

* Remove deprecated functions benchmark tests (#122)

* Contributors: Chris Lalancette, Miguel Company, Scott K Logan

rosidl_typesupport_introspection_c
==================================

* Switch to ament_cmake_ros_core package (#860)

* Add types "rosidl_pycommon" (#824)

* Contributors: Michael Carlstrom, Scott K Logan

rosidl_typesupport_introspection_cpp
====================================

* Switch to ament_cmake_ros_core package (#860)

* Add types "rosidl_pycommon" (#824)

* Contributors: Michael Carlstrom, Scott K Logan

rosidl_typesupport_introspection_tests
======================================

* Suppress false positive warnings from gcc. (#811)

* Contributors: Chris Lalancette

rosidl_typesupport_tests
========================

* Uniform cmake requirement (#163)

* Contributors: mosfet80

rpyutils
========

* Add py.typed to Package Data (#16)

* Add Create py.typed (#15)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#13)

* Add types and ament_mypy to rpyutils. (#12)

* Contributors: Chris Lalancette, Michael Carlstrom

rqt_bag
=======

* Add standard tests for rqt_bag and rqt_bag_plugins (#171)

* Updated player QoS (#164)

* Adapted to rosbag2_py (#156)

* Fixed button icons (#159)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_bag_plugins
===============

* Add standard tests for rqt_bag and rqt_bag_plugins (#171)

* Adapted to rosbag2_py (#156)

* Fixed image timeline renderer (#158)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_console
===========

* Add in standard tests. (#48)

* Remove CODEOWNERS and mirror-rolling-to-main workflow (#46)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_graph
=========

* Add in standard tests. (#104)

* Remove CODEOWNERS (#102)

* Fixed fit_in_view icon button (#95)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_gui
=======

* Add in standard tests for rqt_gui and rqt_gui_py (#318)

* Contributors: Chris Lalancette

rqt_gui_cpp
===========

* Added common test to rqt_gui_cpp and deprecate h headers (#311)

* Updated deprecated qt_gui_cpp headers (#309)

* Contributors: Alejandro Hernández Cordero

rqt_gui_py
==========

* Add in standard tests for rqt_gui and rqt_gui_py (#318)

* Contributors: Chris Lalancette

rqt_plot
========

* Add unit tests for topic name validation & field expansion (#108)

* Fix double slash when plotting all sub-fields with trailing slash
  (#107)

* Fix listing of nested basic type fields (#101)

* Fix f-string and add single quote around field name (#100)

* Add single quotes around topic in validation msg for consistency
  (#99) This is more consistent with the other messages below.

* Add in the rest of the standard ament_python tests. (#98)

* Remove CODEOWNERS (#96)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  Christophe Bedard

rqt_publisher
=============

* Add in the remaining standard ament_python tests. (#49)

* Add in LICENSE. (#46)

* Remove CODEOWNERS (#47)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_py_common
=============

* Stop using python_cmake_module. (#304)

* Use an rclpy context manager. (#312)

* Added common test to rqt_py_common (#310)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_py_console
==============

* Add the standard tests to rqt_py_console. (#19)

* Remove CODEOWNERS (#17)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_service_caller
==================

* Update rqt_service_caller to our standard policies. (#31)

* Remove CODEOWNERS (#29)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_shell
=========

* Add in standard tests to rqt_shell. (#24) That way we know it
  conforms to our standards.

* Remove CODEOWNERS (#22)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rqt_topic
=========

* Override subscriber qos (#51)

* Remove CODEOWNERS (#52)

* Contributors: Alejandro Hernández Cordero

rti_connext_dds_cmake_module
============================

* Update Connext to 7.3.0 (#181)

* Quiet a warning when CONNEXTDDS_DIR or NDDSHOME is not found. (#158)

* Contributors: Chris Lalancette, lobolanja

rttest
======

* Don't try to build on BSD (#126)

* Contributors: Scott K Logan

rviz2
=====

* Expose the possibility to create ROS node with custom "NodeOptions"
  (#1347)

* uniform CMAKE requirement (#1335)

* Detect wayland and make sure X rendering is used. (#1253)

* Fixed RViz2 linters (#1231)

* Contributors: Alejandro Hernández Cordero, Matthew Elwin, Patrick
  Roncagliolo, mosfet80

rviz_assimp_vendor
==================

* Revert "Update ASSIMP_VENDOR CMakeLists.txt (#1226)" (#1249)

* Update ASSIMP_VENDOR CMakeLists.txt (#1226) CLEAN UNUSED CHECK SE
  MIN ASSIMP VERSION TO 5.3.1 SET C++ VERSION TO 17

* Contributors: Chris Lalancette, mosfet80

rviz_common
===========

* Work in progress using the new resource retriever apis (#1262)

* addTrackedObject Function Fails to Handle Null Pointer, Causing
  Crash When nullptr is Passed (#1375)

* Add test to check mapGetString when key is missing (#1361)

* UniformStringStream::parseFloat Fails to Handle Invalid Float
  Formats Correctly (#1360)

* Fix Potential Null Pointer Dereference in
  VisualizerApp::getRenderWindow() to Prevent Crashes (#1359)

* Extend support for type adaptation (REP 2007) in rviz_common for TF-
  filtered displays (#1346)

* Expose the possibility to create ROS node with custom "NodeOptions"
  (#1347)

* uniform CMAKE requirement (#1335)

* Add basic support for type adaptation (REP 2007) in "rviz_common"
  for displays (#1331)

* Fix preferred tools loading names (#1321)

* Add RVIZ_COMMON_PUBLIC macro to ToolManager (#1323)

* Clean visualization_manager.cpp (#1317)

* Fix Deprecated tf2 headers (#1289)

* include QString (#1298)

* Handle time source exception (#1285)

* Fully handle "Tool::processKeyEvent" return value (#1270)

* Handle "Tool::Finished" returned by "processKeyEvent" (#1257)

* Added more time to copyright on Windwos (#1252)

* Added common test for rviz_common (#1232)

* Set ContentsMargins for RenderPanel to 0 to avoid borders in
  fullscreen mode. Fixes #1024 (#1228)

* Updated deprecated message filter headers (#1239)

* Correclty load icons of panels with whitespaces in their name
  (#1241)

* Prepping for qos deprecation (#1214)

* Replace ESC shortcut for exiting full screen with solution from
  https://github.com/ros-visualization/rviz/pull/1416 (#1205)

* Contributors: Alejandro Hernández Cordero, Bo Chen, Lucas Wendland,
  Matthew Foran, Michael Carroll, Michael Ripperger, Patrick
  Roncagliolo, RaduPopescu, Silvio Traversaro, mosfet80

rviz_default_plugins
====================

* PointCloudDisplay: Fix decay time 0 keeping more than the last
  message (#1400)

* Work in progress using the new resource retriever apis (#1262)

* Include chrono (#1353)

* fix: add rclcpp::shutdown (#1343)

* Nv12 color format (#1318) Co-authored-by: zycczy
  <zycczyby@gmail.com>

* uniform CMAKE requirement (#1335)

* Initialize lookup table only once at compile time (#1330) Co-
  authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>

* Fixed the XY Orbit controller move (#1327) Co-authored-by: Terry
  Scott <tscott@seegrid.com>

* Fix Deprecated tf2 headers (#1289)

* Change EffortDisplay superclass from MessageFilterDisplay to
  RosTopicDisplay to avoid dropping messages with empty frame_id.
  (#1312)

* Fix access control for Accel, Effort and Twist displays (#1311)

* remove unused variable (#1301)

* include QString (#1298)

* Clean code for Image display (#1271)

* Handle time source exception (#1285)

* replace deprecated encodings 'yuv422' and 'yuv422_yuy2' (#1276)

* Update urdf model.h deprecation (#1266)

* Enabling manual space width for TextViewFacingMarker (#1261)

* Added more time to copyright on Windwos (#1252)

* Updated deprecated message filter headers (#1239)

* Fixed RViz default plugin license linter (#1230)

* Contributors: Alejandro Hernández Cordero, Christian Rauch, Lucas
  Wendland, Matthew Foran, Michael Carroll, Patrick Roncagliolo, Peng
  Wang, Stefan Fabian, Terry Scott, Tom Moore, Yuyuan Yuan, disRecord,
  mosfet80, quic-zhaoyuan, suchetanrs

rviz_ogre_vendor
================

* Add missing glew dependency for ogre vendor package (#1350)

* Use official freetype github mirror instead of savannah (#1348)

* Fix flags for both clang and gcc. (#1219)

* Update freetype lib (#1216)

* Update zlib into CMakeLists.txt (#1128) Changes in 1.3 (18 Aug 2023)
  - Remove K&R function definitions and zlib2ansi - Fix bug in
  deflateBound() for level 0 and memLevel 9 - Fix bug when gzungetc()
  is used immediately after gzopen() - Fix bug when using gzflush()
  with a very small buffer - Fix crash when gzsetparams() attempted
  for transparent write - Fix test/example.c to work with FORCE_STORED
  - Rewrite of zran in examples (see zran.c version history) - Fix
  minizip to allow it to open an empty zip file - Fix reading disk
  number start on zip64 files in minizip - Fix logic error in minizip
  argument processing - Add minizip testing to Makefile - Read
  multiple bytes instead of byte-by-byte in minizip unzip.c - Add
  memory sanitizer to configure (--memory) - Various portability
  improvements - Various documentation improvements - Various spelling
  and typo corrections Co-authored-by: Chris Lalancette
  <clalancette@gmail.com>

* Contributors: Chris Lalancette, Silvio Traversaro, Stefan Fabian,
  mosfet80

rviz_rendering
==============

* BillboardLine::addPoint() does not throw an exception when exceeding
  max_points_per_line limit (#1436)

* Constructor ScrewVisual::ScrewVisual does not handle null pointers,
  leading to crashes (#1435)

* Removed Windows warnings (#1413)

* Memory Access Error When Handling Empty Strings in
  splitStringIntoTrimmedItems Function (#1412)

* Crash due to Unhandled Null Pointer in ParameterEventsFilter
  Constructor (#1411)

* MovableText constructor does not validate invalid character height,
  default fallback missing (#1398)

* Invalid Parameter Handling in CovarianceVisual::CovarianceVisual
  Constructor (#1396)

* Lack of Validity Check for Invalid Parameters in
  EffortVisual::EffortVisual Constructor (#1395)

* Grid Class Constructor Does Not Handle Null Pointer, Leading to
  Program Crash (#1394)

* Crash in MovableText::update() when caption is an empty string due
  to uninitialized resource usage (#1393)

* Work in progress using the new resource retriever apis (#1262)

* uniform CMAKE requirement (#1335)

* Clean ogre_render_window_impl.cpp (#1334)

* include QString (#1298)

* Use consistent conditionals in render_system.hpp (#1294)

* Avoid redefinition of default color materials (#1281)

* Added more time to copyright on Windwos (#1252)

* Fix: issue #1220. (#1237) Co-authored-by: Alejandro Hernández
  Cordero <ahcorde@gmail.com>

* Added common test: rviz_rendering (#1233)

* Contributors: Alejandro Hernández Cordero, Masayoshi Dohi, Matthew
  Foran, Michael Carroll, Scott K Logan, chama1176, mosfet80

rviz_rendering_tests
====================

* Work in progress using the new resource retriever apis (#1262)

* uniform CMAKE requirement (#1335)

* Added common test to rviz_rendering_tests (#1234)

* Contributors: Alejandro Hernández Cordero, Michael Carroll, mosfet80

rviz_resource_interfaces
========================

* Work in progress using the new resource retriever apis (#1262)

* Contributors: Michael Carroll

rviz_visual_testing_framework
=============================

* uniform CMAKE requirement (#1335)

* Fix Deprecated tf2 headers (#1289)

* include QString (#1298)

* Added common test to rviz_visual_testing_framework (#1235)

* Contributors: Alejandro Hernández Cordero, Lucas Wendland, Matthew
  Foran, mosfet80

sensor_msgs
===========

* Add NV12 to color formats (#253)

* Contributors: Lukas Schäper

sensor_msgs_py
==============

* Add ament_xmllint to sensor_msgs_py. (#259)

* Fix formatting in sensor_msgs_py (#248)

* Contributors: Chris Lalancette, Christophe Bedard

service_msgs
============

* Add missing build_export_depend on rosidl_core_runtime (#165)

* Contributors: Scott K Logan

sqlite3_vendor
==============

* Bump sqlite3 to 3.45.1 (#1737)

* Contributors: Christophe Bedard

sros2
=====

* Switch to get_rmw_additional_env (#339)

* Fix github-workflow mypy error (#336)

* Give more time to generate policies in tests (#323)

* Switch to context manager for rclpy tests. (#322)

* [FIX] remove dangerous mutable default arguments in
  generate_artifacts (#318)

* Fix sros2 tests on Windows Debug. (#317)

* [TESTS] Update tests and add test for generate_artifacts (#311)

* remove deprecated create_key and list_keys verbs (#302)

* Fix linux tutorial: cloning example policies and set of default
  policies for a node (#295)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Mikael
  Arguedas, Tomoya Fujita, yadunund

test_cli
========

* Stop using python_cmake_module. (#536)

* Use rclpy.init context manager where we can. (#547) This allows us
  to cleanup, while using a lot less code to try and track it.

* Contributors: Chris Lalancette

test_cli_remapping
==================

* Stop using python_cmake_module. (#536)

* Use rclpy.init context manager where we can. (#547) This allows us
  to cleanup, while using a lot less code to try and track it.
