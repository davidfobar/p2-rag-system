# Jazzy Jalisco changelog (part 5 of 5)

* Change an rviz_ogre_vendor dependency to libfreetype-dev. (#1167)
  The situation is complicated, but in versions of Ubuntu prior to
  Focal and versions of Debian prior to Bookworm, the name of the
  library was 'libfreetype6-dev'. Since Focal and Bookworm, the name
  of the library is 'libfreetype-dev'. While 'libfreetype-dev'
  provides a "virtual package" for 'libfreetype6-dev', we should
  really use the new canonical name. Further, there is currently a bug
  on ros_buildfarm where it doesn't properly deal with "virtual
  packages" like this. This is currently preventing this package from
  building on Ubuntu Noble. That bug is being worked on separately.
  Finally, I'll note that we already have a libfreetype-dev key in
  rosdep, so we just switch to using that here which should work
  around the bug on the buildfarm, and also use the correct canonical
  name going forward.

* fix: modify typo in cmake args for mac (#1160)

* feat: support macos (#1156)

* Suppress a couple more of clang warnings in rviz_ogre_vendor.
  (#1102)

* Fix the vendoring flags for clang compilation. (#1003) Several of
  the flags are not available on clang, so don't add them there. This
  fixes the clang build for me locally.

* Switch to ament_cmake_vendor_package (#995)

* CMake: rename FeatureSummary.cmake to avoid name clashes (#953)

* FIX CVE in external libraries (#961)

* Contributors: Chris Lalancette, Daisuke Nishimatsu, Gökçe Aydos,
  Scott K Logan, mergify[bot], mosfet80

rviz_rendering
==============

* Added CameraInfo display (#1166)

* Fix camera display overlay (#1151)

* Fixes for uncrustify 0.78. (#1155) Mostly what we do here is to
  disable the indentation on certain constructs that are different
  between 0.72 and 0.78. It isn't my preferred solution, but since it
  only affects a small amount of code (and most of that in macros),
  this seems acceptable to me.

* fixed MovableText::getWorldTransforms transform (#1118)

* Switch to target_link_libraries. (#1098)

* Update rviz_rendering and rviz_rendering_tests to C++17. (#1096)

* Include MeshShape class (#1064)

* Use assimp to load stl (#1063)

* RVIZ_RENDERING_PUBLIC to export class RenderSystem (#1072)

* Restore the maybe-uninitialized flag in covariance_visual.hpp
  (#1071)

* Fix up warnings when building with clang. (#1070)

* Use buildsystem info to get the ros_package_name (#1062)

* make box-mode point cloud shader lighter on top than bottom (#1058)

* Removed warning when building in release mode (#1057)

* Fixed low FPS when sending point markers (#1049)

* Removed unused code (#1044)

* Fix the flakey rviz_rendering tests (#1026)

* Added TwistStamped and AccelStamped default plugins (#991)

* Added Effort plugin (#990)

* load GLB meshes (#1001)

* Fixed camera default plusin crash (#999)

* Clean Code (#975) * Clean Code

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Felix F
  Xu, Morgan Quigley, Yaswanth, mosfet80

rviz_rendering_tests
====================

* Remove the loading_ascii_stl_files_fail (#1125)

* Update rviz_rendering and rviz_rendering_tests to C++17. (#1096)

* Use assimp to load stl (#1063)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

rviz_visual_testing_framework
=============================

* Improve the compilation time of rviz_default_plugins (#1007)

* Contributors: Chris Lalancette

sensor_msgs
===========

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* [J-Turtle] Fix uninitialized values in NavSatFix and add missing
  NavSatStatus UNKNOWN (#220) * Fix unitialized values in NavSatFix
  and add missing UNKNOWN * Fixes #196 * Fix default initialization
  instead of constants * Define SERVICE_UNKNOWN Co-authored-by: Tully
  Foote <tully.foote@gmail.com> Co-authored-by: Martin Pecka
  <peci1@seznam.cz>

* Use target qualifier for checking the cpp typesupport exists (#238)

* sensor_msgs/CompressedImage: updated description of format field
  (#231)

* Return true for isColor if format is YUYV or UYUV (#229)

* Contributors: Chris Lalancette, Kenji Brameld, Ryan

sensor_msgs_py
==============

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Allow pointcloud create_cloud function to set specific point_step
  (#223)

* Fix read_points_numpy field_names parameter

* Contributors: Chris Lalancette, George Broughton

shape_msgs
==========

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

shared_queues_vendor
====================

* Remove unused concurrentqueue implementation. (#1465) rosbag2 only
  depends on the readerwriter queue.

* Contributors: Chris Lalancette

spdlog_vendor
=============

* Removed spdlog_vendor warnings (#36) (#37) (cherry picked from
  commit 4510d9ab4389f84daac77210f3fdf8aab372b938) Co-authored-by:
  Alejandro Hernández Cordero <ahcorde@gmail.com>

* Upgrade to v1.12.0. (#35)

* Switch to ament_cmake_vendor_package (#34)

* Contributors: Marco A. Gutierrez, Scott K Logan, mergify[bot]

sqlite3_vendor
==============

* Switch to ament_cmake_vendor_package (#1400)

* Contributors: Scott K Logan

sros2
=====

* Fix linux tutorial: cloning example policies and set of default
  policies for a node (#295) (#296) * clone policies to temporary dir
  as subversion hack doesnt work anymore * add get_type_description
  service to policies * update MacOS similarly * update all
  permissions with new topics * dont rule out cycloneDDS * example of
  enclave override Co-authored-by: Chris Lalancette
  <clalancette@gmail.com> (cherry picked from commit
  ca6bb12cc650b73e7ccfc0fa789d8b49358d44ad) Co-authored-by: Mikael
  Arguedas <mikael.arguedas@gmail.com>

* Use modern PKCS7 to sign the certificate bytes. (#290)

* Fix a number of warnings on Ubuntu 24.04. (#289)

* Fix SSH commands in SROS2_Linux.md (#286)

* Contributors: Boris Boutillier, Chris Lalancette, mergify[bot]

std_msgs
========

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

std_srvs
========

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

stereo_msgs
===========

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

test_cli
========

* Switch to target_link_libraries everywhere. (#532)

* Contributors: Chris Lalancette

test_cli_remapping
==================

* Switch to target_link_libraries everywhere. (#532)

* Contributors: Chris Lalancette

test_communication
==================

* Small fix for modern flake8. (#539)

* Switch to target_link_libraries everywhere. (#532)

* Add integration test for nested messages. (#530)

* Adjust for new rclcpp::Rate API (#516)

* Contributors: Alexey Merzlyakov, Chris Lalancette

test_launch_ros
===============

* Small fixes for modern flake8. (#395)

* add "--log-file-name" command line argument for test. (#387)

* Fix an assert in the test_launch_ros tests. (#367)

* Fix misspelled "receive". (#362)

* Contributors: Chris Lalancette, Tomoya Fujita

test_launch_testing
===================

* Update to C++17 (#742)

* Contributors: Chris Lalancette

test_msgs
=========

* Increase the timeout for the test_msgs rosidl_generated_cpp cpplint.
  (#163) This should make it much more likely to succeed on Windows.

* Fix for invalid conversion from const char8_t* to char for C++20
  (#160)

* Contributors: AiVerisimilitude, Chris Lalancette

test_quality_of_service
=======================

* Cleanup header includes in test_quality_of_service. (#533)

* Switch to target_link_libraries everywhere. (#532)

* Fix test QoS on macOS by moving qos_utilities.cpp to the four tests;
  fixes #517 (#518)

* Contributors: Chris Lalancette, PhDittmann

test_rclcpp
===========

* Addressed TODO in test_local_parameters (#545)

* Actually skip the gtest_subscription test on Connext. (#544)

* Increased time in test_multithreaded (#543)

* Improve the node_name test. (#538)

* Change up the formatting in the test_rclcpp tests. (#537)

* Revamp test_rclcpp to compile far few files. (#535)

* Mark gtest_subscription__rmw_connextdds xfail. (#531)

* refactor corrected depth check for prefix in parameter_fixtures.hpp
  (#529)

* Remove an unnecessary capture in test_rclcpp. (#527)

* Cleanup of the CMakeLists.txt for test_rclcpp. (#526)

* Add a fix for the tests given the new type description parameter
  (#520)

* Changes ros_timer_init for ros_timer_init2 (#508)

* refactor the multi_access_publisher test to avoid dead locks (#515)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Eloy
  Briceno, Emerson Knapp, Lee, Minju, William Woodall

test_rmw_implementation
=======================

* Compile the test_rmw_implementation tests fewer times. (#224)

* Switch to using target_link_libraries everywhere. (#222)

* Add rmw_count_clients,services & test (#208)

* Contributors: Chris Lalancette, Lee, Minju

test_ros2trace
==============

* Add explicit context fields test to test_ros2trace (#107)

* Allow tracing tests to be run in parallel with other tests (#95)

* Make test_ros2trace depend on test_tracetools_launch.

* Switch to custom lttng-ctl Python bindings (#81)

* Contributors: Chris Lalancette, Christophe Bedard

test_security
=============

* Update to C++17 (#528)

* Switch to target_link_libraries everywhere. (#532)

* Adjust for new rclcpp::Rate API (#516)

* Extract sros_artifacts fixture into a CMake script (#525)

* Use test fixtures to create SROS artifacts (#522)

* Contributors: Alexey Merzlyakov, Chris Lalancette, Scott K Logan

test_tf2
========

* Compile fix for upcomming changes to rclcpp::Executor (#668)

* Adding addition BUILD_TESTING requirement (#660)

* normalize quaternions on tf2_eigen (#644)

* Contributors: Lucas Wendland, Paul Gesel, jmachowinski

test_tracetools
===============

* Improve tracetools_test and simplify test_tracetools code (#109)

* Install test_tracetools_mark_process (#113)

* Remove unnecessary <string> include (#111)

* Include <string> in mark_process.cpp (#110)

* Remove unnecessary print in test (#108)

* Add test for GenericPublisher/Subscriber (#97)

* Use lttng_ust_tracef instead of lttng_ust__tracef (#103)

* Use a memcmp for the expected symbol name. (#100)

* Fix the build on RHEL-9. (#98)

* Allow tracing tests to be run in parallel with other tests (#95)

* Fix interference between test_tracetools and ros2lifecycle tests
  (#96)

* Make tracing test assert messages more descriptive (#93)

* Update tests and docs after new rmw_publish timestamp field (#90)

* Switch to target_link_libraries in test_tracetools. (#83)

* Improve test coverage of rclcpp_callback_register in test_tracetools
  (#69)

* Disable tracing on Android (#71)

* Contributors: Chris Lalancette, Christophe Bedard, Przemysław
  Dąbrowski, h-suzuki-isp

test_tracetools_launch
======================

* Improve tracing configuration error reporting (#85)

* Contributors: Christophe Bedard

tf2
===

* Enable Twist interpolator (#646) Co-authored-by: Tully Foote
  <tullyfoote@intrinsic.ai>

* Warning Message Intervals for canTransform (#663)

* Nacho/minor fixes tf2 cache (#658)

* Removing console_bridge (#655)

* Fix constantly increasing memory in std::list (#636)

* Update the tf2 documentation (#638)

* Fix error code returned in BufferCore::walkToTopParent (#601)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ignacio
  Vizzo, Lucas Wendland, Patrick Roncagliolo

tf2_bullet
==========

* Removed obsolete headers (#645)

* Contributors: Alejandro Hernández Cordero

tf2_eigen
=========

* Removed obsolete headers (#645)

* normalize quaternions on tf2_eigen (#644)

* Fix clang build warnings. (#628)

* Add another reference for twist transformation. Comment correction.
  (#620)

* Contributors: Alejandro Hernández Cordero, AndyZe, Chris Lalancette,
  Paul Gesel

tf2_eigen_kdl
=============

* Fix installation directory of .dll files in tf2_eigen_kdl (#657)

* Remove unnecessary use of ament_target_dependencies. (#637) We can
  just use target_link_libraries instead.

* Fix clang build warnings. (#628)

* Contributors: Chris Lalancette, Silvio Traversaro

tf2_geometry_msgs
=================

* Enable Twist interpolator (#646) Co-authored-by: Tully Foote
  <tullyfoote@intrinsic.ai>

* Removed obsolete headers (#645)

* Add doTransform support for Point32, Polygon and PolygonStamped
  (backport #616) (#619)

* Contributors: Alejandro Hernández Cordero, mergify[bot]

tf2_kdl
=======

* Removed obsolete headers (#645)

* Contributors: Alejandro Hernández Cordero

tf2_py
======

* Enable Twist interpolator (#646) Co-authored-by: Tully Foote
  <tullyfoote@intrinsic.ai>

* Contributors: Alejandro Hernández Cordero

tf2_ros
=======

* Compile fix for upcomming changes to rclcpp::Executor (#668)

* Enable Twist interpolator (#646) Co-authored-by: Tully Foote
  <tullyfoote@intrinsic.ai>

* Adding NodeInterfaces to Buffer (#656)

* Reformat some code to make uncrustify happier. (#654)

* Enable intra-process (#649) (#642)

* Avoid unecessary time conversions. (#635)

* Expose TF2 listener CB (#632)

* Fix invalid timer handle exception (#474)

* Fix for #589 - Should be able to transform with default timeout
  (#593)

* Enable StaticTransformBroadcaster in Intra-process enabled
  components (#607)

* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Chris
  Lalancette, Cliff Wu, Lucas Wendland, Patrick Roncagliolo, Steve
  Macenski, jmachowinski, vineet131

tf2_ros_py
==========

* Transform Data Callback Python (#664)

* Make sure to cache transforms in tf2_ros_py. (#634)

* Remove 'efficient copy' prints (#625)

* Add time jump callback (#608)

* Contributors: Chris Lalancette, Erich L Foster, Lucas Wendland,
  Matthijs van der Burgh

tf2_sensor_msgs
===============

* Removed obsolete headers (#645)

* Fix clang build warnings. (#628)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

tf2_tools
=========

* [view_frames] log filenames after it's been determined (#674) (#675)
  (cherry picked from commit 24643fce510d8cc836fe6e5277a1d3f86a21af04)
  Co-authored-by: Mikael Arguedas <mikael.arguedas@gmail.com>

* Add in tests for tf2_tools. (#647)

* Contributors: Chris Lalancette, mergify[bot]

topic_monitor
=============

* Update maintainer list in package.xml files (#665)

* fix readme for topic_monitor. (#630)

* Contributors: Michael Jeronimo, Tomoya Fujita

topic_statistics_demo
=====================

* Update maintainer list in package.xml files (#665)

* Contributors: Michael Jeronimo

tracetools
==========

* Replace all occurences of index.ros.org (#114)

* Switch to ament_generate_version_header for tracetools (#112)

* Fixes for newer uncrustify (#101)

* Update tests and docs after new rmw_publish timestamp field (#90)

* Add timestamp to rmw_publish tracepoint (#74)

* Add TRACETOOLS_ prefix to tracepoint-related public macros (#56)

* Disable tracing on Android (#71)

* Add new rclcpp_subscription_init tracepoint to support new intra-
  process comms

* Contributors: Chris Lalancette, Christophe Bedard, Christopher
  Wecht, Przemysław Dąbrowski

tracetools_launch
=================

* Replace all occurences of index.ros.org (#114)

* Use single underscore for private vars in Python (#92)

* Improve tracing configuration error reporting (#85)

* Fix warnings when using mypy 1.8.0. (#89)

* Remove extra single quote in LdPreload debug log (#79)

* Contributors: Chris Lalancette, Christophe Bedard

tracetools_read
===============

* Replace all occurences of index.ros.org (#114)

* Improve tracetools_test and simplify test_tracetools code (#109)

* Allow tracing tests to be run in parallel with other tests (#95)

* Contributors: Chris Lalancette, Christophe Bedard

tracetools_test
===============

* Replace all occurences of index.ros.org (#114)

* Improve tracetools_test and simplify test_tracetools code (#109)

* Improve assertEventOrder failure output (#106)

* Allow tracing tests to be run in parallel with other tests (#95)

* Fix interference between test_tracetools and ros2lifecycle tests
  (#96)

* Make tracing test assert messages more descriptive (#93)

* Fix use of mutable default arg in tracetools_test (#84)

* Switch <depend> to <exec_depend> in pure Python packages (#67)

* Contributors: Chris Lalancette, Christophe Bedard

tracetools_trace
================

* Replace all occurences of index.ros.org (#114)

* Improve tracing configuration error reporting (#85)

* Add a space in between not and parentheses. (#88)

* Switch to custom lttng-ctl Python bindings (#81)

* Create start/pause/resume/stop sub-commands for 'ros2 trace' (#70)

* Detect issue with LTTng and Docker and report error when tracing
  (#66)

* Contributors: Chris Lalancette, Christophe Bedard

trajectory_msgs
===============

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette

turtlesim
=========

* Add icon for Jazzy. (#167) (#168) (cherry picked from commit
  014955e15a6ac3b1649cbf21e11c8547ebd47af7) Co-authored-by: Marco A.
  Gutierrez <marcogg@marcogg.com>

* [teleop_turtle_key] update usage string to match keys captured by
  keyboard (#165) (#166) On windows it will stay uppercase but
  shouldn't impact users compared to current situation (cherry picked
  from commit e2853cac87f0c62db6294e5bc351e5b52fcd1ae1) Co-authored-
  by: Mikael Arguedas <mikael.arguedas@gmail.com>

* Shorten the callback definition for uncrustify. (#163)

* Use same QoS for all topic pub/subs (#161)

* Remove all uses of ament_target_dependencies. (#159)

* Crop galactic.png and rolling.png to 45x45. (#158)

* Remove the unused member variable last_state_ (#156)

* Added common tests (#154)

* Heavy cleanup of the draw_square tutorial. (#152) * Heavy cleanup of
  the draw_square tutorial. In particular: 1. Make it conform to the
  current ROS 2 style. 2. Add in copyright information. 3. Refactor
  the entire code into a class, which tidies it up quite a bit and
  removes a bunch of globals. 4. Make sure to wait for the reset to
  complete before trying to move the turtle.

* Remove the range constraints from the holonomic parameter. (#150)

* Add icon (#148)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jason
  O'Kane, Yadu, mergify[bot]

uncrustify_vendor
=================

* Update to uncrustify 0.78.1 (#37) * Update to uncrustify 0.78.1 *
  Fix the uncrustify version detection logic. And make sure we are at
  least 0.78.

* Switch to ament_cmake_vendor_package (#34)

* Contributors: Chris Lalancette, Scott K Logan

unique_identifier_msgs
======================

* Update to C++17 (#27)

* Contributors: Chris Lalancette

urdf
====

* Switch to target_link_libraries (#36)

* Contributors: Chris Lalancette

urdf_parser_plugin
==================

* Switch to target_link_libraries (#36)

* Contributors: Chris Lalancette

visualization_msgs
==================

* Remove references to index.ros.org. (#244)

* Adds ARROW_STRIP to Marker.msg (#242)

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Chris Lalancette, Tom Noble

yaml_cpp_vendor
===============

* Removed warnigns (#49) (#50) (cherry picked from commit
  4b6808fd0f9b0b5e05928c0c8e44fd976a043d33) Co-authored-by: Alejandro
  Hernández Cordero <ahcorde@gmail.com>

* Upgrade to yaml-cpp 0.8.0 (#48) Co-authored-by: Chris Lalancette
  <clalancette@gmail.com>

* Support yaml-cpp >= 0.8.0 (#46)

* Disable the -Wshadow warning when building under clang. (#45)

* Switch to ament_cmake_vendor_package (#43)

* Revamp the extras file to find the correct version. (#42)

* Contributors: Chris Lalancette, Marco A. Gutierrez, Scott K Logan,
  Silvio Traversaro, mergify[bot]

zstd_vendor
===========

* Updated zstd to 1.5.5 (#1617) (#1624)

* Switch to ament_cmake_vendor_package (#1400)

* Contributors: Scott K Logan, mergify[bot]
