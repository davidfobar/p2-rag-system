# ROS 2 Lyrical Luth Complete Changelog (part 6 of 6)

test_launch_ros
===============

* Add tests for new component container refactor (#536)

* Surpressing multi-threaded process warning from flake8. (#520)

* correct typos (#524)

* set PYTHONUNBUFFERED to 1 to avoid hangs due to lost buffers (#519)

* Make FindPackage substitutions a Path to get operator / (#494)

* Expose lifecycle_node (#327) (with test) (#482)

* Switch osrf_pycommon dependency to system package (#431)

* Fix SetUseSimTime for launch frontends (#488)

* fix setuptools deprecations (#475)

* Fix: LoadComposableNodes fails to parse wildcard param files
  correctly (#460) (#465)

* Contributors: Auguste Lalande, Christophe Bedard, Clara Berendsen,
  Emerson Knapp, Emre Kuru, Jasper van Brakel, Scott K Logan, Skyler
  Medeiros, Tomoya Fujita, mosfet80

test_launch_testing
===================

* Fix CMake deprecation (#899)

* Allow Path in substitutions, instead of requiring cast to str (#873)

* Contributors: Emerson Knapp, mosfet80

test_msgs
=========

* Add "ament_cmake_mypy" to "test_msgs" (#187)

* Fix cmake deprecation (#180)

* Contributors: Michael Carlstrom, mosfet80

test_osrf_testing_tools_cpp
===========================

* fix cmake deprecation (#94)

* Contributors: mosfet80

test_quality_of_service
=======================

* Use new ROSIDL aggregate CMake target (#587)

* fix CMAKE deprecation (#572)

* Switch to isolated test fixture macros (#571)

* Use rmw_event_type_is_supported to skip tests (#563)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K
  Logan, mosfet80

test_rclcpp
===========

* Add tests isolation in test_rclcpp (#583)

* info message comes from deferred signal handler with another thread.
  (#576)

* get rid of deprecated rclcpp::spin_some(). (#574)

* fix CMAKE deprecation (#572)

* Use EnableRmwIsolation in launch tests (#571)

* Ensure test verifies the existence of all spawning nodes (#558)

* Contributors: Alejandro Hernández Cordero, Julien Enoch, Scott K
  Logan, Tomoya Fujita, Yuyuan Yuan, mosfet80

test_rmw_implementation
=======================

* Use new aggregate rosidl target instead of _TARGETS (#276)

* test_rmw_implementation: add test isolation (#275)

* Add rmw_get_clients_info_by_service ,
  rmw_servers_clients_info_by_service (#238)

* fix cmake deprecation (#267)

* Test failing deserialization of invalid sequence length (#261)

* add ignore_local_publications_serialized test. (#255)

* Contributors: Alexis Tsogias, Julien Enoch, Lee, Miguel Company,
  Minju, Tomoya Fujita, mosfet80

test_ros2trace
==============

* Skip test_ros2trace's tracing tests for now (#218)

* Allow creating snapshot sessions (#195)

* Only check test process events in test_runtime_disable (#193)

* Add runtime tracing opt-out mechanism (#185)

* fix setuptools deprecation (#189)

* Use timeout for everything in test_ros2trace tests (#174)

* Contributors: Christophe Bedard, Michel Hidalgo, Shravan Deva,
  mosfet80

test_security
=============

* Use new ROSIDL aggregate CMake target (#587)

* fix CMAKE deprecation (#572)

* Contributors: Emerson Knapp, mosfet80

test_tf2
========

* fix typos (#921)

* Use new ROSIDL aggregate CMake target (#907)

* added toMsg for eigen-accel as well as its tests (#887)

* Move author tags to file brief (#870)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Adding NodeInterfaces API Design (#714)

* Change tf2_ros C to C++ headers (#805)

* Uniform cmake min version (#764)

* Add "rclcpp::shutdown" (#762)

* Contributors: Alireza Moayyedi, Auguste Lalande, Emerson Knapp, Gary
  Servin, Lucas Wendland, R Kent James, Yuyuan Yuan, mosfet80

test_tracetools
===============

* fix: Fixed compiation on MSVC 2022 (#243)

* Use new ROSIDL aggregate CMake target (#238)

* Support tracepoints for complex message flow annotation used by ROS
  2 plugin of Eclipse Trace Compass (#233)

* Update subscription callback signatures (#217)

* Add runtime tracing opt-out mechanism (#185)

* Update CMakeLists.txt (#176)

* Contributors: Emerson Knapp, Janosch Machowinski, Michel Hidalgo,
  Raphael van Kempen, mini-1235, mosfet80

test_tracetools_launch
======================

* Allow creating snapshot sessions (#195)

* fix setuptools deprecation (#189)

* Make trace action parameters substitutable for xml and yaml launch
  files (#188)

* Make trace action parameters substitutable (#187)

* Address typing issues reported by mypy in tracetools_launch (#184)

* Contributors: Christophe Bedard, Shravan Deva, mosfet80

tf2
===

* Added tests for static cache (#920)

* Replacing with clean index-based iteration and avoid division by
  zero (#901)

* fix typos (#921)

* Fix StaticCache::getData() returning true on empty cache (#908)

* Use new ROSIDL aggregate CMake target (#907)

* Fix CPP style in tf2 (#902)

* local variable tf2 no longer shadows the tf2:: (#903)

* Replaced char* with std::string (#904)

* Fix misleading extrapolation time in buffer_core (#832) (#896)

* static function to crate quaternions directly from rotation added
  (#881)

* Expose Doxygen output in tf2, showing former Doxygen front page also
  as README.md (#871)

* Move author tags to file brief (#870)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Fix various documentation errors in tf2 (#857)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Fix REP url locations (#847)

* Adding explicit handling for normalization of zero-quaternions
  (#839)

* Cleanup TF2 dependencies (#843)

* Added tf2 documentation to docs.ros.org (#671)

* Add RPY quaternion constructor (#806)

* Default initialize TransformStorage's frame_id_ and child_frame_id_
  with UINT32_MAX (#783)

* Removed deprecated headers tf2 (#789)

* Add isnan support (#780)

* Overflow Issue in durationFromSec() Function when Handling Extremely
  Large or Small Values (#785)

* Do not clobber callback handles when cancelling pending
  transformable requests (#779)

* Uniform cmake min version (#764)

* Contributors: Alejandro Hernández Cordero, Alireza Moayyedi,
  Andreas, Auguste Lalande, Chris Lalancette, Emerson Knapp, Markus
  Bader, Michael Carlstrom, Pavel Guzenfeld, R Kent James, Selim
  Ağırman, Simon Jusner, Tim Clephas, Timo Röhling, cramke, mosfet80

tf2_bullet
==========

* Use new ROSIDL aggregate CMake target (#907)

* Move author tags to file brief (#870)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Set Cmake Policy CMP0144 (#819)

* Change tf2_ros C to C++ headers (#805)

* Uniform cmake min version (#764)

* Contributors: Cristóbal Arroyo, Emerson Knapp, Gary Servin, R Kent
  James, mosfet80

tf2_eigen
=========

* fix typos (#921)

* Use new ROSIDL aggregate CMake target (#907)

* added toMsg for eigen-accel as well as its tests (#887)

* Move author tags to file brief (#870)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Add fromMsg for converting from Accel to Eigen (#844)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Change tf2_ros C to C++ headers (#805)

* Uniform cmake min version (#764)

* Contributors: Alireza Moayyedi, Auguste Lalande, Emerson Knapp, Gary
  Servin, R Kent James, mosfet80

tf2_eigen_kdl
=============

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Cleanup mislabeled BSD license (#855)

* Removed orocos kdl vendor dependency (#826)

* Uniform cmake min version (#764)

* Contributors: Alejandro Hernández Cordero, R Kent James, mosfet80

tf2_geometry_msgs
=================

* fix typos (#921)

* fix: doTransform of VelocityStamped added input vector after
  transform (#909)

* Use new ROSIDL aggregate CMake target (#907)

* Copy child_frame_id from input (#889)

* Move author tags to file brief (#870)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Removed orocos kdl vendor dependency (#826)

* Change tf2_ros C to C++ headers (#805)

* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson
  Knapp, Gary Servin, R Kent James, Yannik Meinken, cramke

tf2_kdl
=======

* Use new ROSIDL aggregate CMake target (#907)

* Move author tags to file brief (#870)

* Documentation fixes for tf2_kdl (#869)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Removed orocos kdl vendor dependency (#826)

* Change tf2_ros C to C++ headers (#805)

* Uniform cmake min version (#764)

* Fix external docs mappings (#757)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Emmanuel,
  Gary Servin, R Kent James, mosfet80

tf2_msgs
========

* fix typos (#921)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Uniform cmake min version (#764)

* Contributors: Auguste Lalande, R Kent James, mosfet80

tf2_py
======

* fix typos (#921)

* Use new ROSIDL aggregate CMake target (#907)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Cleanup TF2 dependencies (#843)

* Contributors: Auguste Lalande, Chris Lalancette, Emerson Knapp, R
  Kent James

tf2_ros
=======

* fix typos (#921)

* Use new ROSIDL aggregate CMake target (#907)

* Move author tags to file brief (#870)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Prevent log spam from tf2_ros message_filter (#851)

* Updated tf2_echo with some other features (#802) (#840)

* Replace std::sleep_for with rclcpp::clock::sleep_for (#835)

* Removed deprecation rclcpp::spin_some(node) (#824)

* Adding NodeInterfaces API Design (#714)

* ger rid of deprecated rclcpp::spin_some(). (#821)

* Ensure variable is considered volatile in message_filter_test (#812)

* Change tf2_ros C to C++ headers (#805)

* Fix message filter target frames string (#803)

* Remove deprecation warnings (#790)

* Uniform cmake min version (#764)

* Add "rclcpp::shutdown" (#762)

* Fix external docs mappings (#757)

* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson
  Knapp, Emmanuel, Gary Servin, Lucas Wendland, Mirko Ferrati, R Kent
  James, Sergei Zobov, Tomoya Fujita, Yuyuan Yuan, mergify[bot],
  mini-1235, mosfet80

tf2_ros_py
==========

* fix typos (#921)

* flake8 fixes (#919)

* prevent AttributeError when static_only=true (#906)

* fixed typoe in buffer.py (#905)

* Increase robustness of listener and broadcaster test (#894)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation
  into packages (#856)

* Cleanup TF2 dependencies (#843)

* Fixed inconsistency of C++ and Python implementations of
  StaticTransformPublisher (#820)

* Fix deprecation warning (#804)

* Remove deprecation warnings (#790)

* Fix external docs mappings (#757)

* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Chris
  Lalancette, Dominik, Emmanuel, Michael Carlstrom, Michael Carroll, R
  Kent James, mosfet80

tf2_sensor_msgs
===============

* fix typos (#921)

* Use new ROSIDL aggregate CMake target (#907)

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Solved TODO with copyright in tf2_sensor_msgs (#836)

* Removed orocos kdl vendor dependency (#826)

* Add imu & mag support in "tf2_sensor_msgs" (#800) (#813)

* Change tf2_ros C to C++ headers (#805)

* Add normals rotation in "PointCloud2" "doTransform" (#792)

* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson
  Knapp, Gary Servin, Patrick Roncagliolo, R Kent James

tf2_tools
=========

* Modernize conf.py files to only include modified Copyright,
  eliminati… (#865)

* Fix Setuptools deprecations (#809)

* Contributors: R Kent James, mosfet80

tlsf
====

* update cmake requirements (#18)

* Contributors: mosfet80

tlsf_cpp
========

* cleanups and removed dead code (#141) (#144)

* fix: Removed AllocatorMemoryStrategy (backport #140) (#142)

* Remove deprecation warnings (#139)

* Use new ROSIDL aggregate CMake target (#137)

* tlsf_cpp: add test isolation (#136)

* Update subscription callback signatures (#135)

* Fix cmake deprecation (#134)

* Explicitly shutdown context before test exits (#129)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Julien
  Enoch, mergify[bot], mini-1235, mosfet80, yadunund

topic_monitor
=============

* Add mypy config (#776)

* Switching to example_interfaces (#674)

* fix setuptools deprecations (#733)

* Update README.md (#718) (#719)

* Contributors: Dan Mascarenhas, Lucas Wendland, mergify[bot],
  mosfet80

topic_statistics_demo
=====================

* Use new ROSIDL aggregate CMake target (#781)

* Switching to example_interfaces (#674)

* Uniform CMAKE min VERSION (#714)

* Contributors: Emerson Knapp, Lucas Wendland, mosfet80

tracetools
==========

* Support tracepoints for complex message flow annotation used by ROS
  2 plugin of Eclipse Trace Compass (#233)

* Removed warning (#225)

* Add runtime tracing opt-out mechanism (#185)

* Fix Clang warnings by using proper function prototypes in macros
  (#179)

* Update CMakeLists.txt (#176)

* Removed clang warning (#168)

* Contributors: Alejandro Hernández Cordero, Michel Hidalgo, Raphael
  van Kempen, Shravan Deva, mosfet80

tracetools_launch
=================

* tracetools_launch: use parse_if_substitutions for non-string action
  params (#234)

* Add example launch files for snapshot mode (#206)

* Allow creating snapshot sessions (#195)

* Add launch files with preconfigured dual session (#196)

* Add support for starting tracing at runtime (#191)

* fix setuptools deprecation (#189)

* Make trace action parameters substitutable for xml and yaml launch
  files (#188)

* Make trace action parameters substitutable (#187)

* Address typing issues reported by mypy in tracetools_launch (#184)

* Contributors: Christophe Bedard, Sarthak Bagga, Shravan Deva,
  mosfet80

tracetools_read
===============

* Work around segfault when reading trace with babeltrace1 Python API
  (#246)

* Ignore A0005 (#237)

* fix setuptools deprecation (#189)

* Address typing issues reported by mypy in tracetools_launch (#184)

* Contributors: Christophe Bedard, Michael Carlstrom, mosfet80

tracetools_test
===============

* Set default values on TraceTestCase to avoid errors on >=8.2.0
  pytest (#236)

* Only check test process events in test_runtime_disable (#193)

* fix setuptools deprecation (#189)

* Address typing issues reported by mypy in tracetools_launch (#184)

* Contributors: Christophe Bedard, Clara Berendsen, mosfet80

tracetools_trace
================

* Support tracepoints for complex message flow annotation used by ROS
  2 plugin of Eclipse Trace Compass (#233)

* Ignore A0005 (#237)

* Add exec_depend on procps to tracetools_trace for ps command (#227)

* Handle SIGTERM and gracefully stop tracing in interactive tracing
  mode (#219)

* Use overwrite mode for snapshot sessions (#210)

* Allow creating snapshot sessions (#195)

* Add support for starting tracing at runtime (#191)

* fix setuptools deprecation (#189)

* Address typing issues reported by mypy in tracetools_launch (#184)

* Warn if kernel might be paranoid about 'perf:thread:' context fields
  (#173)

* Fix pluralization in ros2 trace output (#169)

* Contributors: Christophe Bedard, Michael Carlstrom, Raphael van
  Kempen, Shravan Deva, mosfet80

trajectory_msgs
===============

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

turtlesim
=========

* Add icon for Lyrical Luth (#196) (#197)

* Use rosdep keys that select Qt5 or Qt6 by platform (#195)

* Use new ROSIDL aggregate CMake target (#194)

* Use get_package_share_path (#193)

* fix bug loading turtle images (#192)

* Updated deprecated ament_index_cpp API (#190)

* Use qt6 as the default dependency from rosdep (#189)

* get rid of deprecated rclcpp::spin_some() (#183)

* Support Qt6 (#170)

* Add icon for Kilted Kaiju (#180)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K
  Logan, Shane Loretz, dcconner, mergify[bot]

turtlesim_msgs
==============

* fix: swap action and message file group names in CMakeLists.txt
  (#186) (#187)

* fix cmake deprecation (#182)

* Contributors: mergify[bot], mosfet80

type_description_interfaces
===========================

* Fix cmake deprecation (#180)

* Contributors: mosfet80

uncrustify_vendor
=================

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#38)

* Contributors: Chris Lalancette

unique_identifier_msgs
======================

* fix cmake deprecation (#33)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#31)

* Contributors: Chris Lalancette, mosfet80

urdf
====

* Remove "urdf_world/types.h" deprecation (#54)

* Fix CMAKE deprecation (#48)

* Removed tinyxml2_vendor dependency (#47)

* Contributors: Alejandro Hernández Cordero, mosfet80

urdf_parser_plugin
==================

* Remove "urdf_world/types.h" deprecation (#54)

* Fix CMAKE deprecation (#48) cmake version < then 3.10 is deprecated

* Contributors: Alejandro Hernández Cordero, mosfet80

urdfdom
=======

* Support for URDF Specification 1.2 * Extend parsing of acceleration,
  deceleration and jerk limits from "limit" tag (#212) * Update
  default limits for the joint limits and safety limits (#249) * Add
  invalid data checks to the Geometry data (#242) * Require
  urdfdom_headers 3.0.0 (#257)

* Use URDF_MAJOR_VERSION for SOVERSION (#248)

* Revert "Extend parsing of acceleration, deceleration and jerk limits
  from "limit" tag (#212)" This was a breaking change that will be
  released in 6.0.0

* Prevent CI from failing fast to allow all builds to complete (#254)

* Remove "urdf_world/types.h" deprecation (#251)

* Extend parsing of acceleration, deceleration and jerk limits from
  "limit" tag (#212)

* ROS 2 CI: build urdfdom_headers from source (#246)

* Disable system workflow because "urdfdom_headers" isn't available on
  Ubuntu 24.04 (#240)

* Fix ROS 2 CI workflow by updating Ubuntu version and checkout action
  (#239)

* Support for URDF Specification 1.1 * Add support for capsule
  geometry type (#238) * Add documentation about versioning * Require
  version 2.1.0 of urdfdom_headers Co-authored-by: Steve Peters
  <scpeters@openrobotics.org> * Support quaternions in URDF 1.1 (#235)
  Co-authored-by: Guillaume Doisy <doisyg@users.noreply.github.com>

* Fix multiple format-string vulnerabilities in URDF parser logging
  (#243) User-controlled URDF content was passed directly to
  CONSOLE_BRIDGE_logError() at multiple call sites, allowing printf-
  style format string interpretation. All affected logging paths now
  use explicit "%s" format specifiers to ensure input is treated as
  data and to prevent information disclosure or undefined behavior.

* More logging format string fixes (#244) * Add explicit "%s" format
  strings when logging * Use %s format string instead of string
  addition

* Read cmake version from package.xml (#236) * Use regex to match
  version string. Based on suggestion from Chris Lalancette. * Require
  cmake minimum version 3.10 Co-authored-by: Chris Lalancette
  <clalancette@gmail.com>

* Revert "Quaternion in urdf (PR123 new attempt) (#231)" (#231)

* Quaternion in urdf (PR123 new attempt) (#194)

* Removed tinyxml2_vendor dependency (#225)

* Relax the version compatibility for urdfdom_headers. (#222)

* Removed deprecated code (#217)

* Remove ROS 1 workflows and update ROS 2 (#218)

* Improvements for the URDF xsd specification (#200)

* Update ros2.yaml (#214)

* fix: missing header (#216)

* Contributors: Alejandro Hernández Cordero, Amin Ya, Chris
  Lalancette, Florencia, Guillaume Doisy, Jose Luis Rivero, Pierre
  Ballif, Sai Kishor Kothakota, Steve Peters, mosfet80

urdfdom_headers
===============

* Update lower, upper, effort, and velocity default joint limits (#95)

* Clean up declaration of ModelInterface's SharedPtrs (#99)

* Extend "JointLimits" class to include acceleration, deceleration and
  jerk limits (#83)

* Revert "Extend JointLimits class to include acceleration,
  deceleration and jerk limits (#83)" This was a breaking change that
  will be released in 3.0.0

* Clean up declaration of ModelInterface's SharedPtrs (#99)

* Revert cleanup of ModelInterface's SharedPtrs (#33)

* Revert fix for assumption that CMAKE_INSTALL_*DIR paths are relative
  (#90) (#97)

* Clean up declaration of ModelInterface's SharedPtrs (#33)

* Fix assumption that CMAKE_INSTALL_*DIR paths are relative (#90)

* Extend "JointLimits" class to include acceleration, deceleration and
  jerk limits (#83)

* Add support for capsule geometry type (#94)

* 2.0.2

* Read cmake version from package.xml (#92) Use regex to match version
  string. Copied from ros/urdfdom#236.

* quaternions in urdf (PR 51 new attempt) + bump version (#77)

* fix cmake deprecation (#89) cmake version < then 3.10 is deprecated

* 2.0.0

* Remove all dependencies from the package.xml. (#88) This package
  does not have any header dependencies, so we don't need any of them
  here.

* Fix package.xml deps to use vendored packages (#87)

* add package.xml file from release repository (#85)

* Removed headers, implementation was deprecated and removed (#86)

* Remove CODEOWNERS. (#81) It is outdated and no longer serving its
  intended purpose.

* Contributors: Aarav Gupta, Alejandro Hernández Cordero, Chris
  Lalancette, Guillaume Doisy, Jorge J. Perez, Lucien Morey, Michal
  Sojka, Robert Haschke, Sai Kishor Kothakota, Steve Peters, mosfet80

visualization_msgs
==================

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

yaml_cpp_vendor
===============

* Replace ament_vendor with cmake modules (#56)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#52)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

zenoh_cpp_vendor
================

* Use zenoh-cpp 481b71b fixing build with MSVC 2022 in C++20 mode
  (#969)

* Bump Zenoh to 1.8.0, fix Windows shutdown hang, and resolve
  synchronization with "undeclare" (#964)

* Revert changes to build against rust >= 1.75 and bump zenoh to 1.8.0
  (#960)

* Revert patch of Cargo.lock with new Zenoh commit due to Windows test
  failures (#959)

* Update Cargo.lock with new Zenoh commit (#957)

* Build against "rust >= 1.75" for ROS Lyrical (#945)

* Bump zenoh to 1.8.0 (#935)

* Allow use of non-vendored Zenoh if present (#908)

* Bump "zenoh" to 1.7.1 (#870)

* Fix REP url locations (#858)

* Bump zenoh to 1.6.2 (#842)

* Bump Zenoh to 1.5.1 (#774)

* Bump Zenoh to v1.5.0 (#728)

* Change zenoh-c features to use its default + shared-memory +
  transport_serial (#692)

* Bump Zenoh to 1.4.0 (#652)

* fix: pin rust toolchain to v1.75.0 (#602)

* fix: use the right commit to bump zenoh to v1.3.2 (#607)

* Contributors: ChenYing Kuo (CY), Julien Enoch, Shane Loretz, Tim
  Clephas, Yadunund, Yuyuan Yuan, Øystein Sture

zenoh_security_tools
====================

* Address outstanding TODO items (#896)

* Removed tinyxml2_vendor dependency (#829)

* Fix commands in zenoh_security_tools README (#814)

* Revert "fix: handle missing enclaves_dir argument for
  zenoh_security_tools (#…" (#802)

* Correct a description error in the zenoh_security_tools README
  (#789)

* fix: handle missing enclaves_dir argument for zenoh_security_tools
  (#788)

* SROS: add ACL rules for TRANSIENT_LOCAL pub/sub (fix #753) (#779)

* Fix handling of enclave path in zenoh_security_tools (#770)

* Update CMakeLists.txt (#617)

* Fix warning on Windows (#615)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe
  Bedard, Julien Enoch, Tomoya Fujita, Yadunund, mosfet80
