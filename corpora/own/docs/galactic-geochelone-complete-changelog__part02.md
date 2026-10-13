# Galactic Geochelone changelog (part 2 of 8)

ament_lint
==========

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_lint_auto
===============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Use correct lint package dependencies (#278)

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Esteve
  Fernandez, Scott K Logan

ament_lint_cmake
================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* ament_lint_cmake: default linelength in argumentparser for
  consistency (#306)

* 0.10.3

* Fix ament_lint_cmake line length expression (#236) This regular
  expression is using the re.VERBOSE flag, meaning that characters
  after an un-escaped '#' character are interpreted as a comment and
  are not part of the expression. Also set the default maximum line
  length to 140 columns.

* Add Audrow as a maintainer (#294)

* Make CMake linter line length configurable (#235) Co-authored-by:
  Miaofei <miaofei@amazon.com>

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Emerson
  Knapp, Scott K Logan

ament_lint_common
=================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_mypy
==========

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang

ament_package
=============

* Revert "Generate Setuptools Dict Helper Method (#126)" (#131)

* Generate Setuptools Dict Helper Method (#126)

* Add Audrow as a maintainer (#127)

* Support Python 3.8-provided importlib.metadata (#124)

* Declare missing dependency on python3-importlib-resources (#123)

* make AMENT_TRACE_SETUP_FILES output sourceable (#120)

* update maintainers

* Switch ament_package to using importlib. (#118)

* Add pytest.ini so local tests don't display warning (#117)

* add configure-time flag to skip parent_prefix_path (#115)

* Contributors: Audrow Nash, Chris Lalancette, David V. Lu!!, Dirk
  Thomas, Mabel Zhang, Scott K Logan

ament_pclint
============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Add pytest marks to ament_pclint tests. (#202) * Add pytest marks to
  ament_pclint tests. * fix failed tests Co-authored-by: Miaofei
  <miaofei@amazon.com>

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan, Steven! Ragnarök

ament_pep257
============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* remove use of "extend" action in argparse (#262)

* Expand ignores to pep257 definition. (#241) * Expand ignores to
  pep257 definition. (ament #240) * add '--allow-undocumented' flag to
  enforce pep257 * restore existing default error codes to check * fix
  no-ignores logic * expose options from pydocstyle * allow user to
  explicitly set convention to "ament" * fix typo in populating argv
  for pydocstyle * reformat ament convention list * Add help info for
  ament convention

* Add pytest.ini so local tests don't display warning. (#259)

* remove match args to allow pydocstyle defaults (#243)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan, Ted Kern

ament_pycodestyle
=================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_pyflakes
==============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

ament_uncrustify
================

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Allow 'C++' as language, but convert it to 'CPP' (#302)

* Allow correct languages on uncrustify (#272) * Allow correct
  languages on uncrustify. * Update dictionary.

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Miguel
  Company, Scott K Logan

ament_xmllint
=============

* Remove Claire as a maintainer. (#312) * Remove Claire as a
  maintainer. * Remove dead email addresses. * Remove more dead email
  addresses. * Switch setup.py maintainer to Audrow.

* 0.10.3

* Add Audrow as a maintainer (#294)

* Drop trailing tab from package manifests (#291) Follow-up to
  8bf194aa1ac282db5483dd0d3fefff8f325b0db8

* Update maintainer (#274) * update maintainer * add authors

* Add pytest.ini so local tests don't display warning. (#259)

* Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K
  Logan

builtin_interfaces
==================

* Change index.ros.org -> docs.ros.org. (#122)

* Updating Quality Declaration (#120)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Document that Time and Duration are explictly ROS Time (#103)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  Tully Foote, brawner, shonigmann

camera_calibration_parsers
==========================

* Fix formatting and include paths for linters (#157)

* ROS2 Using the filesystem helper in rcpputils (#133)

* [Windows][ros2] Avoid build break for Visual Studio 2019 v16.3
  (#135)

* Camera Calibration Parsers ROS2 Port (#105)

* Image Transport ROS2 port (#84)

* Use Boost_LIBRARIES instead of Boost_PYTHON_LIBRARY This was causing
  issues when building with python3 since then "Boost_PYTHON_LIBRARY"
  is not set, instead cmake sets "Boost_PYTHON3_LIBRARY". So instead
  of adding each library separately, using "Boost_LIBRARIES" seems to
  be better. For reference, from the cmake docs: "` Boost_LIBRARIES
  - Boost component libraries to be linked Boost\_<C>_LIBRARY -
  Libraries to link for component <C> `"

* Properly detect Boost Python 2 or 3 This fixes #59

* 1.11.11

* update changelogs

* Add install target for python wrapper library

* Only link against needed Boost libraries 9829b02 introduced a python
  dependency into find_package(Boost..) which results in
  ${Boost_LIBRARIES} containing boost_python and such a dependency to
  libpython at link time. With this patch we only link against the
  needed libraries.

* Add python wrapper for readCalibration. Reads .ini or .yaml
  calibration file and returns camera name and sensor_msgs/cameraInfo.

* Use $catkin_EXPORTED_TARGETS

* Remove no-longer-neccessary flags to allow OS X to use 0.3 and 0.5
  of yaml-cpp.

* remove buggy CMake message

* fix #39

* make sure test does not fail

* [camera_calibration_parsers] Better error message when calib file
  can't be written

* add rosbash as a test dependency

* add a test dependency now that we have tests

* parse distortion of arbitraty length in INI This fixes #33

* add a test to parse INI calibration files with 5 or 8 D param

* Add yaml-cpp case for building on Android

* Fix catkin_make failure (due to yaml-cpp deps) for mac os

* fix bad yaml-cpp usage in certain conditions fixes #24

* add a dependency on pkg-config to have it work on Indigo

* fix YAML CPP 0.5.x compatibility

* Contributors: Andreas Klintberg, Gary Servin, Helen Oleynikova,
  Isaac IY Saito, Jochen Sprickerhof, Kartik Mohta, Markus Roth,
  Martin Idel, Michael Carroll, Sean Yen, Vincent Rabaud, Yifei Zhang

camera_info_manager
===================

* Fix formatting and include paths for linters (#157)

* Enable Windows build. (#159)

* Fix abort criteria for setCameraInfoService callback (#132)

* camera_info_manager ROS2 port (#94)

* Image Transport ROS2 port (#84)

* Fix the find_package(catkin) redundancy

* Add a dependency between the test and the test executable

* Add camera_calibration_parsers dependency to camera_info_manager

* 1.11.11

* update changelogs

* Return empty CameraInfo when !ros::ok()

* Return empty CameraInfo when !ros::ok()

* fix compilation on Fedora, fixes #42

* simplify target_link_libraries That should fix #35

* Add public member function to manually set camera info (#19)

* make rostest in CMakeLists optional (ros/rosdistro#3010)

* check for CATKIN_ENABLE_TESTING

* add Jack as maintainer

* add gtest libraries linkage

* fix the rostest dependency

* fix catkin gtest and rostest problem

* fix unit test dependencies

* Removed duplicated test dependancy Test dependencies should never
  duplicate build or run dependencies.

* fix the urls

* Updated package.xml file(s) to handle new catkin buildtool_depend
  requirement

* remove the brief attribute

* fix bad folder/libraries

* add missing rostest dependency

* fix bad dependency

* fix dependencies

* add catkin as a dependency

* comply to the catkin API

* add missing linkage

* install the include directories

* fix build issues

* make the libraries public

* API documentation review update

* suppress misleading camera_info_manager error messages [#5273]

* remove deprecated global CameraInfoManager symbol for Fuerte (#4971)

* Revert to using boost::mutex, not boost::recursive_mutex.

* Hack saveCalibrationFile() to stat() the containing directory and
  attempt to create it if necessary. Test for this case.

* Reload camera info when camera name changes.

* Implement most new Electric API changes, with test cases.

* Add ${ROS_HOME} expansion, with unit test cases. Do not use "$$" for
  a single '$', look for "${" instead.

* Use case-insensitive comparisons for parsing URL tags (#4761). Add
  unit test cases to cover this. Add unit test case for camera name
  containing video mode.

* add test for resolving an empty URL

* Deprecate use of global CameraInfoManager symbol in E-turtle
  (#4786). Modify unit tests accordingly.

* provide camera_info_manager namespace, fixes #4760

* Add support for "package://" URLs.

* Fixed tests to work with new CameraInfo.

* Moved image_common from camera_drivers.

* Contributors: Aaron Blasdel, Enrique Fernandez, Jack O'Quin,
  Jonathan Bohren, Joseph Schornak, Lukas Bulwahn, Martin Idel, Max
  Schettler, Michael Carroll, Sean Yen, Vincent Rabaud, blaise,
  mihelich, mirzashah

class_loader
============

* Remove travis. (#182)

* Change index.ros.org -> docs.ros.org. (#181)

* Fix ternary null check found by clang static analysis (#176)

* Update QD to QL 1 (#177)

* Updated console_bridge QL in QD

* Update package maintainers. (#169)

* enable building a static library (#163)

* Update Quality Declaration to reflect QL 2 (#160).

* Increase coverage with a graveyard behavior test and unmanaged
  instance test (#159)

* Add Security Vulnerability Policy pointing to REP-2006. (#157)

* Clean up and improve documentation (#156)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk
  Thomas, Michel Hidalgo, Stephen Brawner, ahcorde, brawner

common_interfaces
=================

* Update package maintainers. (#132)

* Contributors: Michel Hidalgo

composition
===========

* Fix leak(#480) (#481)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo, y-okumura-isp

composition_interfaces
======================

* Change index.ros.org -> docs.ros.org. (#122)

* Updating Quality Declaration (#120)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  brawner, shonigmann

cyclonedds
==========

* DATA_AVAILABLE was not always triggered when by a dispose and
  sometimes triggered in the absence of an observable state change
  (arrival of a dispose for an already-disposed instance where the
  dispose had not yet been read);

* Restores functionality of the "raw ethernet" mode as well as IPv6
  with link-local addresses, both accidentally broken in 0.6.0;

* Fixes a crash in processing endpoint discovery data containing
  unrecognised locator kinds;

* Fixes type conversion for local historical data (e.g., mixed use of
  ROS 2 C/C++ type supports in combination with transient-local
  endpoints within a single process);

* Fixes a use-after-free of "lease" objects with manual-by-topic
  writers;

* Mark instance as "alive" in the reader history and generate an
  invalid sample to notify the application even if the sample itself
  is dropped because the same or a later one is present already (e.g.,
  on reconnecting to a transient-local writer);

* Fix a crash when doing an instance lookup on a built-in topic using
  the key value;

* No longer auto-dispose instances as soon as some registered writer
  disappears, instead do it only when all of them have unregistered
  it;

* Fix performance of read_instance and take_instance by performing a
  proper instance lookup.

demo_nodes_cpp
==============

* Fix small print issue in allocator tutorial. (#509) (#512)

* Small fixes for even_parameters_node. (#500)

* change ParameterEventHandler to take events as const ref instead of
  shared pointer (#494)

* Fix integer type in RCLCPP_* macro printf. (#492)

* Add a demo for the new ParameterEventHandler class (#486)

* Filter qos overrides in paramter events demos (#491)

* Update code now that parameter types are static by default (#487)

* Update logging macros (#476)

* Make sure to wait for the service before declaring events. (#473)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic,
  Michael Jeronimo, William Woodall

demo_nodes_cpp_native
=====================

* Update demo_nodes_cpp_native to new Fast DDS API (#493)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo, Miguel Company

demo_nodes_py
=============

* Use underscores instead of dashes in setup.cfg (#502)

* Update deprecated qos policy value names (#468)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Ivan Santiago Paunovic, Michael Jeronimo

diagnostic_msgs
===============

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

domain_coordinator
==================

* Update package maintainers. (#11)

* Add pytest.ini to suppress warning output locally. (#8)

* Contributors: Chris Lalancette, Michel Hidalgo

dummy_map_server
================

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo

dummy_robot_bringup
===================

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo

dummy_sensors
=============

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo

example_interfaces
==================

* Change links from index.ros.org -> docs.ros.org. (#13)

* Update maintainer. (#12)

* Contributors: Chris Lalancette, Jacob Perron

examples_rclcpp_cbg_executor
============================

* Fix clang warnings about type mismatches. (#309)

* Support for cbg_executor package on QNX (#305)

* Demo for callback-group-level executor concept. (#302)

* Contributors: Chris Lalancette, Ralph Lange, joshua-qnx

examples_rclcpp_minimal_action_client
=====================================

* Update maintainers (#292)

* Update goal response callback signature (#291)

* Make sure to include what you use in all examples. (#284)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob
  Perron, Shane Loretz

examples_rclcpp_minimal_action_server
=====================================

* Update maintainers (#292)

* Make sure to include what you use in all examples. (#284)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane
  Loretz

examples_rclcpp_minimal_client
==============================

* Update maintainers (#292)

* Make sure to include what you use in all examples. (#284)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane
  Loretz

examples_rclcpp_minimal_composition
===================================

* Update maintainers (#292)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

examples_rclcpp_minimal_publisher
=================================

* Unique network flows (#296)

* Update maintainers (#292)

* Make sure to include what you use in all examples. (#284)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna,
  Chris Lalancette, Shane Loretz

examples_rclcpp_minimal_service
===============================

* Update maintainers (#292)

* Make sure to include what you use in all examples. (#284)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane
  Loretz

examples_rclcpp_minimal_subscriber
==================================

* Unique network flows (#296)

* Update maintainers (#292)

* Make sure to include what you use in all examples. (#284)

* Remove a TODO in the not_composable demo. (#285)

* Add Topic Statistics Example (#281)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna,
  Chris Lalancette, Devin Bonnie, Shane Loretz

examples_rclcpp_minimal_timer
=============================

* Update maintainers (#292)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Shane Loretz

examples_rclcpp_multithreaded_executor
======================================

* Use "char *" in logging macros (#295)

* Update maintainers (#292)

* Added common linters (#265)

* Contributors: Alejandro Hernández Cordero, Audrow Nash, Shane Loretz

examples_rclpy_executors
========================

* Use underscores instead of dashes in setup.cfg (#310)

* Update maintainers (#292)

* Contributors: Ivan Santiago Paunovic, Shane Loretz

examples_rclpy_guard_conditions
===============================

* Use underscores instead of dashes in setup.cfg (#310)

* Update maintainers (#292)

* [rclpy] Create a package with an example showing how guard
  conditions work (#283)

* Contributors: Audrow Nash, Ivan Santiago Paunovic, Shane Loretz

examples_rclpy_minimal_action_client
====================================

* Use underscores instead of dashes in setup.cfg (#310)

* Using asyncio with ros2 action client (#301)

* Update maintainers (#292)

* Added missing linting tests (#287)

* Contributors: Allison Thackston, Ivan Santiago Paunovic, Shane
  Loretz, alemme

examples_rclpy_minimal_action_server
====================================

* Use underscores instead of dashes in setup.cfg (#310)

* Update maintainers (#292)

* Added missing linting tests (#287)

* Contributors: Allison Thackston, Ivan Santiago Paunovic, Shane
  Loretz

examples_rclpy_minimal_client
=============================

* Use underscores instead of dashes in setup.cfg (#310)

* Remove bare exception catching (#299)

* Update maintainers (#292)

* Contributors: Ivan Santiago Paunovic, Shane Loretz

examples_rclpy_minimal_publisher
================================

* Use underscores instead of dashes in setup.cfg (#310)

* Update maintainers (#292)

* Contributors: Ivan Santiago Paunovic, Shane Loretz

examples_rclpy_minimal_service
==============================

* Use underscores instead of dashes in setup.cfg (#310)

* Update maintainers (#292)

* Contributors: Ivan Santiago Paunovic, Shane Loretz

examples_rclpy_minimal_subscriber
=================================

* Use underscores instead of dashes in setup.cfg (#310)

* Update maintainers (#292)

* Contributors: Ivan Santiago Paunovic, Shane Loretz

examples_rclpy_pointcloud_publisher
===================================

* Use underscores instead of dashes in setup.cfg (#310)

* add pointcloud publisher example (#276)

* Contributors: Evan Flynn, Ivan Santiago Paunovic

examples_tf2_py
===============

* Use underscores instead of dashes in setup.cfg. (#403) (#404)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Add pytest.ini so local tests don't display warning (#276)

* Split tf2_ros in tf2_ros and tf2_ros_py (#210)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

fastrtps_cmake_module
=====================

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#69)

* Use CMake config dirs as hint for header/library search (#56)

* Update package maintainers (#55)

* QD Update Version Stability to stable version (#46)

* Contributors: Alejandro Hernández Cordero, Dirk Thomas, Michel
  Hidalgo, shonigmann

geometry2
=========

* Port eigen_kdl.h/cpp to ROS2 (#311)

* Update maintainers of the ros2/geometry2 fork. (#328)

* Contributors: Chris Lalancette, Jafar Abdi

geometry_msgs
=============

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Update Quality levels to level 3 (#124)

* Finish up API documentation (#123)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

google_benchmark_vendor
=======================

* Shrink the size of the tz_offset variable. (#13)

* Update the patching to work on Windows without admin. (#11)

* Always preserve source permissions in vendor packages. (#12)

* Update package maintainers. (#10)

* Upgrade google benchmark from v1.5.1 to v1.5.2 to include QNX patch.
  (#9)

* Set the SOVERSION on benchmark libraries. (#8)

* Set minimum criteria for system package. (#3)

* Work around warnings building Google Benchmark w/Clang. (#2)

* Initial google_benchmark_vendor package. (#1)

* Initial commit.

* Contributors: Ahmed Sobhy, Chris Lalancette, Michel Hidalgo, Scott K
  Logan

image_common
============

* [ros2] image_common metapackage (#129)

* 1.11.11

* update changelogs

* add Jack as maintainer

* comply to REP 0127

* add missing description

* define metapackage

* Contributors: Vincent Rabaud, chapulina

image_tools
===========

* Initialize time stamp for published image messages (#475)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Added more parameters for camera topic examples (#465)

* Contributors: Jacob Perron, Michael Jeronimo

image_transport
===============

* Fix formatting and include paths for linters (#157)

* Fix QoS initialization from RMW QoS profile (#158)

* add missing set header (#140)

* Update to use new count APIs (#128)

* use latest ros2 API (#127)

* Update ROS2 branch to account for new NodeOptions interface (#120)

* camera_info_manager ROS2 port (#94)

* Pointer api updates (#104)

* Fix rcutils API change by just removing it. (#103)

* [ROS2] corrections to remapping for raw images (#97)

* Make ROS2 ImageTransport conform to old api (#88)

* Image Transport ROS2 Port (#84)

* Disable image publisher plugins by name (#60) * Disable publisher
  plugins by name * Now have per publisher blacklist instead of
  image_transport wide.

* update to use non deprecated pluginlib macro

* Extend documentation of "getCameraInfoTopic" Document the fact that
  the "base_topic" argument must be resolved in order to build the
  correct camera info topic.

* Added cv::waitkey(10) for blank popup Without the cv::waitkey(10),
  it results in a blank popup which crashes/ leads to a black popup.
  This change corrects that problem. ROS Kinetic, Ubuntu 16.04.3

* Fix CMake of image_transport/tutorial and polled_camera Fix loads of
  problems with the CMakeLists.

* image_transport/tutorial: Add dependency on generated msg Without
  this, build fails on Kinetic because ResizedImage.h has not been
  generated yet.

* image_transport/tutorial: Add missing catkin_INCLUDE_DIRS Without
  this, compilation files on Kinetic because ros.h cannot be found.

* 1.11.11

* update changelogs

* fix linkage in tutorials

* Use $catkin_EXPORTED_TARGETS

* image_transport: fix CameraSubscriber shutdown (circular shared_ptr
  ref) CameraSubscriber uses a private boost::shared_ptr to share an
  impl object between copied instances. In
  CameraSubscriber::CameraSubscriber(), it handed this shared_ptr to
  boost::bind() and saved the created wall timer in the impl object,
  thus creating a circular reference. The impl object was therefore
  never freed. Fix that by passing a plain pointer to boost::bind().

* avoid a memory copy for the raw publisher

* add a way to publish an image with only the data pointer

* Make function inline to avoid duplicated names when linking
  statically
