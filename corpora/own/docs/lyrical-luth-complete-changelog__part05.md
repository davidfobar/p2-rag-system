# ROS 2 Lyrical Luth Complete Changelog (part 5 of 6)

rosidl_default_generators
=========================

* fix cmake deprecation (#31)

* Contributors: mosfet80

rosidl_default_runtime
======================

* fix cmake deprecation (#31)

* Contributors: mosfet80

rosidl_dynamic_typesupport
==========================

* Don't automatically enable verbose makefiles (#17)

* Contributors: Chris Lalancette

rosidl_dynamic_typesupport_fastrtps
===================================

* Merge pull request #11 from mosfet80/patch-1

* Don't automatically enable verbose makefiles. (#9)

* Contributors: Chris Lalancette, mosfet80

rosidl_generator_c
==================

* Export typing Information (#903)

* Uniform cmake minVersion (#849)

* rosidl_cli: Add type description support (#857)

* Contributors: Francisco Rossi, Michael Carlstrom, mosfet80

rosidl_generator_cpp
====================

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* Use IWYU pragma export to avoid clangd warnings for generated
  headers (#902)

* rosidl_generator_cpp: constexpr message traits and to_tuple_ref for
  generated structs (#928)

* Make "data_type" and "name" traits constexpr (#929)

* Export typing Information (#903)

* Add static_cast (#884)

* Uniform cmake minVersion (#849)

* rosidl_cli: Add type description support (#857)

* Add missing cstdint include (#864)

* Removed deprecated methods (#863)

* Contributors: Adam Leeper, Alejandro Hernández Cordero, CY Chen,
  Francisco Rossi, Michael Carlstrom, mosfet80, Øystein Sture

rosidl_generator_dds_idl
========================

* Update cmake version requirements (#64)

* Contributors: mosfet80

rosidl_generator_py
===================

* Use absolute names for type hints (#258)

* Feature: add depends flag for ament_python_install_package (#254)

* Add support for rosidl::Buffer in rosidl Python path for rclpy
  (#250)

* Cast Sequence to list on assignment (with templates) (#249)

* Fix linter violations with flake8-import-order 0.19.0 (#248)

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#238)

* Deprecate using set for container based input (#243)

* Update to use new BaseImpl (#241)

* remove second call (#232)

* Derive Messages from Base Classes (#230)

* Remove NoReturn for now (#229)

* Static typing for Message, Services, and Actions (#206)

* Contributors: Anthony Welte, CY Chen, Michael Carlstrom, Nadav
  Elkabets

rosidl_generator_rs
===================

* fix(rosidl_generator_rs_generate_interfaces): Remove poisoning of
  global CMAKE_SHARED_LINKER_FLAGS variable (#22)

* Change the package metadata to point to the new ros-env crate (#21)

* Fix TransientParseError on Ubuntu Resolute (#20)

* fix: do not monkey-patch _removesuffix into str (#18)

* fix: add str.removesuffix() backport for Python < 3.9 (RHEL 8) (#17)

* feat: relative Module Path Resolution (#12) * Changed all generated
  code to use relative symbols instead of "crate::" ones. Reworked the
  rosidl_generator_rs slightly to be a bit simpler. Separate actual
  templates from the files that reuse them. * WIP For adding
  documentation to all structs, members, and constants generated from
  idl's. * Clean up all the surfaced warnings from generated code.

* build: update rosidl_runtime_rs dependency version to 0.6 (#14)

* fix: update rosidl_runtime_rs dependency version to 0.5 (#11)

* Fix use of serde (#9) * Fix use of serde * Include serde for
  services ---------

* Update to the latest version of Action trait (#7) * Update to the
  latest version of Action trait * Fix use of serde ---------

* fix cmake deprecation (#6) * fix cmake deprecation cmake version <
  then 3.10 is deprecated * Update CMakeLists.txt

* fix: clean up dependencies (#5)

* fix: added missing dependency

* clean up changelog. Removed rosidl_runtime_rs as a dependency

* set python executable var to custom cmake commands (#3)

* Contributors: Esteve Fernandez, Grey, Kimberly N. McGuire, Sam
  Privett, Shane Loretz, Silvio Traversaro, mosfet80

rosidl_generator_tests
======================

* Use new aggregate rosidl target instead of _TARGETS (#952)

* rosidl_generator_cpp: constexpr message traits and to_tuple_ref for
  generated structs (#928)

* Make "data_type" and "name" traits constexpr (#929)

* fix cmake <3.10 deprecation (#875)

* Contributors: Alexis Tsogias, Michael Carlstrom, mosfet80, Øystein
  Sture

rosidl_generator_type_description
=================================

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#910)

* Add missing dependency on ament_cmake_pytest (#914)

* Export typing Information (#903)

* Uniform cmake minVersion (#849)

* rosidl_cli: Add type description support (#857)

* Contributors: Anthony Welte, Francisco Rossi, Michael Carlstrom,
  Scott K Logan, mosfet80

rosidl_parser
=============

* Fix future regressions on flake8 (#936)

* Add Optional Parsing (#883)

* fix cmake <3.10 deprecation (#875)

* Contributors: Michael Carlstrom, mosfet80

rosidl_pycommon
===============

* fix regressions (#951)

* Fix future regressions on flake8 (#936)

* Add BaseImpl (#912)

* Export typing Information (#903)

* Provide base classes in "rosidl_pycommon" (#887)

* fix setuptools deprecation (#880)

* Contributors: Michael Carlstrom, mosfet80

rosidl_runtime_c
================

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* Fix copy/paste errors in type support docs (#906)

* fix cmake <3.10 deprecation (#875)

* Add an ament_cmake_gtest dependency to rosidl_runtime_c. (#865)

* Contributors: CY Chen, Chris Lalancette, Christophe Bedard, mosfet80

rosidl_runtime_cpp
==================

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* rosidl_generator_cpp: constexpr message traits and to_tuple_ref for
  generated structs (#928)

* Make "data_type" and "name" traits constexpr (#929)

* fix cmake <3.10 deprecation (#875)

* Add missing cstdint include (#864)

* Contributors: CY Chen, Michael Carlstrom, mosfet80, Øystein Sture

rosidl_runtime_py
=================

* Add support for rosidl::Buffer in rosidl Python path for rclpy (#39)

* Fix flake8 (#40)

* Add py.typed to the package (#37)

* fix setuptools deprecations (#35)

* Contributors: CY Chen, Michael Carlstrom, Vladimir Gerts, mosfet80

rosidl_typesupport_c
====================

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#168)

* Contributors: Anthony Welte

rosidl_typesupport_cpp
======================

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#168)

* Remove deprecated rosidl_typesupport_cpp/type_support_map.h (#167)

* De-duplicate type_support_map.h header (#81)

* Contributors: Anthony Welte, Christophe Bedard

rosidl_typesupport_fastrtps_c
=============================

* Update rosidl typesupport to support rosidl::Buffer in nested
  uint8[] (#151) (#152)

* Add support for rosidl::Buffer type serialization (#144)

* use variable to control shared/static build type (#138)

* Switch ament_index_python and rosidl_cli to exec_depend. (#137)

* Removed deprecated code (#135)

* fix cmake deprecation (#134)

* Check remaining size before resizing sequences (#130)

* Contributors: Alejandro Hernández Cordero, Anthony Welte, CY Chen,
  Chris Lalancette, Jay Sridharan, Miguel Company, mergify[bot],
  mosfet80

rosidl_typesupport_fastrtps_cpp
===============================

* Clean up logs in buffer serialization functions (#153) (#154)

* Update rosidl typesupport to support rosidl::Buffer in nested
  uint8[] (#151) (#152)

* Add missing build dependencies for exported dependencies (#149)

* Add support for rosidl::Buffer type serialization (#144)

* use variable to control shared/static build type (#138)

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#136)

* Switch ament_index_python and rosidl_cli to exec_depend. (#137)

* Removed deprecated code (#135)

* fix cmake deprecation (#134)

* Check remaining size before resizing sequences (#130)

* Contributors: Alejandro Hernández Cordero, Anthony Welte, CY Chen,
  Chris Lalancette, Jay Sridharan, Miguel Company, Scott K Logan,
  mergify[bot], mosfet80

rosidl_typesupport_interface
============================

* fix cmake <3.10 deprecation (#875)

* Contributors: mosfet80

rosidl_typesupport_introspection_c
==================================

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#910)

* Export typing Information (#903)

* Uniform cmake minVersion (#849)

* rosidl_cli: Add type description support (#857)

* Contributors: Anthony Welte, CY Chen, Francisco Rossi, Michael
  Carlstrom, mosfet80

rosidl_typesupport_introspection_cpp
====================================

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies (#910)

* Export typing Information (#903)

* Uniform cmake minVersion (#849)

* rosidl_cli: Add type description support (#857)

* Contributors: Anthony Welte, CY Chen, Francisco Rossi, Michael
  Carlstrom, mosfet80

rosidl_typesupport_introspection_tests
======================================

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type
  (#942)

* fix cmake <3.10 deprecation (#875)

* Disable test failing in coverage jobs, see #812 (#853)

* Contributors: CY Chen, Jorge J. Perez, mosfet80

rosidl_typesupport_tests
========================

* pass all tests for rmw_cyclonedds_cpp. (#171)

* Contributors: Tomoya Fujita

rpyutils
========

* Enforce ament_mypy --ament-strict (#22)

* fix setuptools deprecations (#17)

* Contributors: Michael Carlstrom, mosfet80

rqt
===

* fix setuptools deprecations (#334)

* fix setuptools deprecations (#329)

* Contributors: mosfet80

rqt_action
==========

* fix setuptools deprecations (#19)

* Remove CODEOWNERS and mirror-rolling-to-main workflow (#16)

* Contributors: Alejandro Hernández Cordero, mosfet80

rqt_bag
=======

* Fix Qt6 issues (backport #207) (#208)

* Support Qt6 (#206)

* Cleanup mislabeled BSD license (#205)

* Better handling of large bag files (#178)

* Display roll, pitch, yaw values for quaternions (#179)

* Fix flake8 error in setup.py (#192)

* Improved raw view to better handle arrays and time objects (#173)

* plot_view: Fixed display of initial message (#180)

* fix setuptools deprecations (#185)

* Fixed timeline resolution (#175)

* Contributors: Alejandro Hernández Cordero, Martin Pecka, Michael
  Carlstrom, mergify[bot], mosfet80

rqt_bag_plugins
===============

* Support Qt6 (#206)

* Display roll, pitch, yaw values for quaternions (#179)

* Fix flake8 error in setup.py (#192)

* Fixed image helper and added support for PNG-coded compressedDepth
  (#176)

* Improve plot view (#174)

* plot_view: Fixed display of initial message (#180)

* fix setuptools deprecations (#185)

* Contributors: Alejandro Hernández Cordero, Martin Pecka, Michael
  Carlstrom, mosfet80

rqt_console
===========

* Support Qt6 (#58)

* fixed copyright test (#57)

* added copyright header

* fixed flake8 (#56)

* fixed flake8

* remove residual imports in colored output test-file (#55)

* remove residual imports

* basic support for colors and bold/bright using ANSI escape codes
  (#54)

* replace colorama dependency with manual ansi codes

* add checkbox in the settings

* support more color codes

* basic support for colors and bold/bright

* fix setuptools deprecations (#50)

* Contributors: Alejandro Hernández Cordero, Arne Hitzmann, Peter,
  mosfet80, peter

rqt_graph
=========

* Support Wheel event in qt6 (backport #116) (#117)

* Fix: broken dependency (#115)

* Support Qt6 (#114)

* add warning for type incompatibilities (#105)

* Remove rqt_graph script. (#66)

* fix setuptools deprecations (#107)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jonas
  Otto, Matthew Foran, mergify[bot], mosfet80

rqt_gui
=======

* Fix setupTools deprecations (#322)

* Contributors: mosfet80

rqt_gui_cpp
===========

* Cleanup headers (#347) (#350)

* Use qt-base-dev / libqtwidgets (#345)

* fix: include unistd.h for getpid (#341)

* Support Qt6 (#339)

* Removed deprecated header (#340)

* Use qt6 as the default dependency from rosdep (#337)

* fix compile with qt6 (#321)

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Shane
  Loretz, mergify[bot], mosfet80

rqt_gui_py
==========

* Support Qt6 (#339)

* Fix setupTools deprecations (#322)

* Contributors: Alejandro Hernández Cordero, mosfet80

rqt_msg
=======

* Support Qt6 (#27)

* fix setuptools deprecations (#23)

* Remove CODEOWNERS (#20)

* Contributors: Alejandro Hernández Cordero, mosfet80

rqt_plot
========

* Use qt-base-dev / libqtwidgets (#128)

* Support Qt6 (#127)

* fix setuptools deprecations (#123)

* Added missing test dependency (#118)

* Fix for displaying constant curves (#114)

* Contributors: Alejandro Hernández Cordero, Martin Pecka, Shane
  Loretz, mosfet80

rqt_publisher
=============

* fix flake8 (backport #57) (#58)

* Support Qt6 (#56)

* fix setuptools deprecations (#52)

* Contributors: Alejandro Hernández Cordero, mergify[bot], mosfet80

rqt_py_common
=============

* Cleanup headers (#347) (#350)

* Use qt-base-dev / libqtwidgets (#345)

* Support Qt6 (#339)

* fix compile with qt6 (#321)

* Contributors: Alejandro Hernández Cordero, Shane Loretz,
  mergify[bot], mosfet80

rqt_py_console
==============

* Add Qt6 compatibility (#25) Co-authored-by: Alejandro Hernandez
  Cordero <ahcorde@gmail.com>

* fix setuptools deprecations (#21)

* Contributors: Shane Loretz, mosfet80

rqt_reconfigure
===============

* Support Qt6 (#158)

* Harden behavior if double value or limit is Infinity (#161)

* Scale IntegerEditor if range exceeds int32 (#160)

* Ignore A005 for future flake8 (#159)

* Cleanup mislabeled BSD license (#157)

* fix setuptools deprecation (#153)

* If updating remote fails, reflect the failure locally (#144)

* Remove CODEOWNERS (#147)

* Contributors: Alejandro Hernández Cordero, Christoph Fröhlich,
  Jonathan Selling, Michael Carlstrom, mosfet80

rqt_service_caller
==================

* Support Qt6 (#38)

* fix setuptools deprecations (#33)

* Contributors: Alejandro Hernández Cordero, mosfet80

rqt_shell
=========

* make linters happy

* Fix setuptools deprecation (#26)

* Contributors: Alejandro Hernandez Cordero, mosfet80

rqt_srv
=======

* fix setuptools deprecations (#16)

* Remove CODEOWNERS (#13)

* Contributors: Alejandro Hernández Cordero, mosfet80

rqt_topic
=========

* Support Qt6 (#67)

* Add Qt6 compatibility (#66)

* Tweak expected error in test for Pydantic v2 compat (#65)

* Use choose_qos() from ros2 topic echo (#55)

* Enable flake8 (#58)

* Open source rewrite of rqt_topic (#47) Co-authored-by: Evan Flynn
  <evan.flynn@apex.ai> Co-authored-by: Alejandro Hernandez Cordero
  <ahcorde@gmail.com>

* fix setuptools deprecations (#57)

* Contributors: Alejandro Hernández Cordero, Evan Flynn, Romain
  Reignier, Scott K Logan, Shane Loretz, mosfet80

rti_connext_dds_cmake_module
============================

* Update Connext from 7.3.0 to 7.7.0, disable monitoring library by
  default, and use synchronous publishing mode (#219)

* Fix cmake deprecation (#198)

* Contributors: Francisco Gallego Salido, mosfet80

rttest
======

* cleanups and removed dead code (#141) (#144)

* Fix cmake deprecation (#134)

* Contributors: mergify[bot], mosfet80

rviz2
=====

* Use rosdep keys that select Qt5 or Qt6 by platform (#1720)

* Use new ROSIDL aggregate CMake target (#1688)

* Fix Qt version resolution when both Qt5 and Qt6 are installed -
  CMake defaults to ascending resolution and Qt5 will be found when
  Qt6 is desired (Rolling, L-Turtle, and beyond). (#1689)

* Use qt6 as the default dependency from rosdep (#1635)

* get rid of deprecated rclcpp::spin_some() (#1567)

* feat: support both qt5 and qt6 (#1187)

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu,
  Emerson Knapp, Nathan Brooks, Shane Loretz

rviz_common
===========

* Use rosdep keys that select Qt5 or Qt6 by platform (#1720)

* Compressed Image Display (#1288)

* fix: Fixed compilation on MSVC 2022 (#1706)

* Removed Qt6 warnings (#1704)

* Fixed regresion is RHEL (#1703)

* Remove warnings (#1693)

* Link against "GTest::gmock" target (#1699)

* Reduce "QFile" dependency (#1652)

* Use new ROSIDL aggregate CMake target (#1688)

* Fix Qt version resolution when both Qt5 and Qt6 are installed -
  CMake defaults to ascending resolution and Qt5 will be found when
  Qt6 is desired (Rolling, L-Turtle, and beyond). (#1689)

* Cleanups in rviz_common (#1686)

* Add tests for shallow and deep copy in Config (#1682)

* Build performance optimizations for rviz_common (#1677)

* Use get_package_share_path (#1671)

* Fix setHidden regression in PropertyTreeWidget (#1667)

* Add topic name filtering when adding new visualizations (#1662)

* use QPointer in QTimer::singleShot to prevent use-after-free (#1657)

* Fix Not loading plugins due to incorrect package path (#1651)

* Updated deprecated ament_index_cpp API (#1647)

* Fix crash with no tools (#1639)

* Use qt6 as the default dependency from rosdep (#1635)

* Pointcloud2 display set QoS to best effort (#1621)

* Cleanup deprecated code (#1619)

* Removed support for yaml-cpp lower than 0.5 (#1605)

* Removed duplicated forward class declaration (#1602)

* resolved TODO in visualization manager (#1603)

* Fix incorrect Qt signal connection in combo box (#1596)

* Removed tinyxml2_vendor dependency (#1591)

* Replace QRegExp with QRegularExpression to support Qt6 (#1592)

* fix crash (#1587)

* added option to change filemode (#1537)

* Removed deprecation warning in tf2 (#1585)

* Std chrono update in default plugins (#1579)

* Removed deprecations (#1556)

* rviz common ros service property (#1548)

* add ros action property (#1549)

* Deprecates update(float, float) methods and provides
  update(std::chrono::duration, std::chrono::duration) replacements.
  (#1533)

* Replace deprecated tf2_ros headers (#1529)

* Postpone hiding of properties until insertion into model is finished
  (#1508)

* Don't hide rows of properties not within the model (#1507)

* Remove redundant check (#1506)

* Fix panel deletion (#1037)

* Config::mapGetBool causes segmentation fault when value_out is
  nullptr (#1471)

* feat: support both qt5 and qt6 (#1187)

* Fixed crash when a resource is not available (#1455)

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

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, David
  V. Lu!!, Emerson Knapp, Janosch Machowinski, Joshua Supratman, Mark
  Johnson, Mateusz Żak, Matteo Princisgh, Matthew Foran, Michael
  Carroll, Nathan Brooks, Oscmoar07, Patrick Roncagliolo, Shane
  Loretz, mini-1235, nelson, t0k0shi

rviz_default_plugins
====================

* Use rosdep keys that select Qt5 or Qt6 by platform (#1720)

* Compressed Image Display (#1288)

* Removed Qt6 warnings (#1704)

* Switch rviz service resource retriever to use new repo's code
  (#1698)

* Link against "GTest::gmock" target (#1699)

* Improve marker common (#1687)

* Reduce "QFile" dependency (#1652)

* Use new ROSIDL aggregate CMake target (#1688)

* Fix Qt version resolution when both Qt5 and Qt6 are installed -
  CMake defaults to ascending resolution and Qt5 will be found when
  Qt6 is desired (Rolling, L-Turtle, and beyond). (#1689)

* Remove redundant compilation of test fixtures (#1673)

* Updated deprecated ament_index_cpp API (#1647)

* Add CameraInfo topic property to DepthCloudDisplay (#1643)

* Use qt6 as the default dependency from rosdep (#1635)

* Pointcloud2 display set QoS to best effort (#1621)

* Fix Translation Issue in XYOrbitViewController (#1630)

* Overcome 16384 size limit (#1622)

* Removed already done TODO (#1604)

* Fixed issue 1593 (#1598)

* Removed tf2 warning (#1586)

* Removed deprecation warning in tf2 (#1585)

* Std chrono update in default plugins (#1579)

* Fix pointcloud2 display divide by 0 (#1581)

* add support for ffmpeg_image_transport and point_cloud_transport
  (#1568)

* Extend the message filter display for point cloud 2 display (#1566)

* Support image transport lifecycle (#1472)

* Fix QoS profile loading for InitialPoseTool from rviz config files
  (#1544)

* Replace rmw_qos_profile_t with rclcpp::QoS (#1525)

* Replace deprecated tf2_ros headers (#1529)

* fix deprecated include (#1530)

* point_cloud_transport update API call (#1526)

* Better handling of missing transport plugins (#1488)

* Fixed deprecation warning on point_cloud_transport:
  rmw_qos_profile_t (#1491)

* Add symbol visibility macros to make*Palette public functions
  (#1492)

* Fix /rviz/get_resource (#1487)

* Removed point_cloud_transport deprecation (#1474)

* Frame view controller: Removed warnings (#1470)

* Fix compile with qt6 (#1475)

* Fix Issue with Quaternion Angular Distance (#1473)

* PointStampedDisplay: Ignore incoming messages if disabled (#1036)

* Removed unused headers from resouce retriever (#1463)

* feat: support both qt5 and qt6 (#1187)

* [rviz_default_plugins] Add missing export dependencies (#1461)

* Backported FrameAligned camera (#1453)

* Changed Marker Displays to allow toggling visibility of namespaces
  (#1402)

* Do not use ${Qt5Widgets_INCLUDE_DIRS} to avoid creating non-
  relocatable CMake config files (#1450)

* PointCloudDisplay: Fix decay time 0 keeping more than the last
  message (#1400)

* Work in progress using the new resource retriever apis (#1262)

* Include chrono (#1353)

* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Antonio
  Brandi, Daisuke Nishimatsu, Eesha Kumar, Emerson Knapp, Felix Exner
  (fexner), Georg Flick, Guillaume Doisy, Harrison Chen, Kenji Brameld
  (TRACLabs), Kosuke Takeuchi, Lennart Reiher, Mark Johnson, Matthew
  Foran, Michael Carroll, Nathan Brooks, Shane Loretz, Silvio
  Traversaro, Stefan Fabian, Stoyan Gaydarov, mosfet80

rviz_ogre_vendor
================

* Add patch to remove "binary_function" (#1691)

* Bump cmake version and suppress warning for rviz_ogre_vendor (#1684)

* Remove vendoring freetype and zlib on Windows (#1636)

* Add RVIZ_OGRE_VENDOR_MANGLE_NAME_OF_LIBRARIES_USED_BY_RVIZ option to
  further mangle ogre libraries used by rviz (#1493)

* Add missing glew dependency for ogre vendor package (#1350)

* Contributors: Dhruv Patel, Michael Carroll, Shane Loretz, Silvio
  Traversaro, Stefan Fabian

rviz_rendering
==============

* Use rosdep keys that select Qt5 or Qt6 by platform (#1720)

* Fix build for Ubuntu 26 (#1694)

* Fix Qt version resolution when both Qt5 and Qt6 are installed -
  CMake defaults to ascending resolution and Qt5 will be found when
  Qt6 is desired (Rolling, L-Turtle, and beyond). (#1689)

* Updated deprecated ament_index_cpp API (#1647)

* Use qt6 as the default dependency from rosdep (#1635)

* Removed unused files (#1600)

* Removed assimp vendor package (#1574)

* Update OGRE mesh files from ROS1 RViz (#1536) (#1559)

* add resourceExists check to loadEmbeddedTexture before loading
  texture (#1542)

* Assign the geometry to the resource group "rviz_rendering" (#1502)

* Removed windows warning (#1486)

* Handle glTF Y-Up frame convention on mesh load (#1482)

* Removed unused headers from resouce retriever (#1463)

* feat: support both qt5 and qt6 (#1187)

* WrenchVisual::setForceColor and setTorqueColor clamp values (#1437)

* Missing Null Pointer Check in TrianglePolygon Constructor Leads to
  Crash (#1434)

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

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, John
  TGZ, Michael Carlstrom, Michael Carroll, Michel Hidalgo, Nathan
  Brooks, Shane Loretz, matthias88, mergify[bot], mosfet80

rviz_rendering_tests
====================

* Use rosdep keys that select Qt5 or Qt6 by platform (#1720)

* Fix Qt version resolution when both Qt5 and Qt6 are installed -
  CMake defaults to ascending resolution and Qt5 will be found when
  Qt6 is desired (Rolling, L-Turtle, and beyond). (#1689)

* Updated deprecated ament_index_cpp API (#1647)

* Use qt6 as the default dependency from rosdep (#1635)

* feat: support both qt5 and qt6 (#1187)

* Work in progress using the new resource retriever apis (#1262)

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu,
  Michael Carroll, Nathan Brooks, Shane Loretz

rviz_visual_testing_framework
=============================

* Use rosdep keys that select Qt5 or Qt6 by platform (#1720)

* Use new ROSIDL aggregate CMake target (#1688)

* Fix Qt version resolution when both Qt5 and Qt6 are installed -
  CMake defaults to ascending resolution and Qt5 will be found when
  Qt6 is desired (Rolling, L-Turtle, and beyond). (#1689)

* Use get_package_share_path (#1671)

* Update ament_index_cpp API (#1649)

* Use qt6 as the default dependency from rosdep (#1635)

* Removed deprecation warning in tf2 (#1585)

* Replace deprecated tf2_ros headers (#1529)

* feat: support both qt5 and qt6 (#1187)

* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu,
  Emerson Knapp, Nathan Brooks, Shane Loretz

sensor_msgs
===========

* [ADD] missing PointField type entries (#301)

* Update point_cloud2_iterator.hpp (#298)

* Fix CMAKE deprecation (#288)

* Enhance NV12 and NV21 Support in sensor_msgs::image_encodings (#264)

* Contributors: Adam Leeper, Zhaoyuan Cheng, mosfet80, wodtko

sensor_msgs_py
==============

* Use structured NumPy points.dtype.itemsize as default point_step in
  create_cloud (#295)

* fix setuptools deprecation (#293)

* Contributors: mosfet80, xndcn

service_msgs
============

* Fix cmake deprecation (#180)

* Contributors: mosfet80

shape_msgs
==========

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

spdlog_vendor
=============

* Remove CODEOWNERS and mirror-rolling-to-master. (#38)

* Contributors: Chris Lalancette

sros2
=====

* Fix "load_file_into_BIO: File could not be found, opened or is
  empty" error on Windows (#386) (#387)

* python3-pytest-timeout is missing for test dependency. (#377)

* Clean up isolated ros2 daemon process for tests. (#375)

* Remove importlib (#368)

* Timezone aware datetimes + remove hack from #209 (#300)

* fix setuptools deprecations (#357)

* Use rmw_test_fixture to isolate ros2cli tests (#356)

* update utilities to pass instance not class of ec.SECP256R1 (#352)

* suppress multi-threaded warnings. (#346)

* Switch to get_rmw_additional_env (#339)

* Fix github-workflow mypy error (#336)

* Contributors: Michael Carlstrom, Mikael Arguedas, Scott K Logan,
  Tomoya Fujita, cdisco, mergify[bot], mosfet80, yadunund

sros2_cmake
===========

* Update CMakeLists.txt (#344)

* Contributors: mosfet80

statistics_msgs
===============

* Fix cmake deprecation (#180)

* Contributors: mosfet80

std_msgs
========

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

std_srvs
========

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

stereo_msgs
===========

* Fix CMAKE deprecation (#288)

* Contributors: mosfet80

tango_icons_vendor
==================

* fix cmake deprecation (#15)

* Remove the mirror-rolling-to-master workflow (#12)

* Remove CODEOWNERS (#11)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette,
  mosfet80

test_cli
========

* fix CMAKE deprecation (#572)

* Contributors: mosfet80

test_cli_remapping
==================

* Use new ROSIDL aggregate CMake target (#587)

* fix CMAKE deprecation (#572)

* Contributors: Emerson Knapp, mosfet80

test_communication
==================

* Use new ROSIDL aggregate CMake target (#587)

* disable interoperability check for CycloneDDS and FastRTPS for
  WString (#586)

* Fix index (#585)

* Update subscription callback signatures (#575)

* get rid of deprecated rclcpp::spin_some(). (#574)

* fix CMAKE deprecation (#572)

* Use EnableRmwIsolation in launch tests (#571)

* Switch to isolated test fixture macros (#571)

* Add tests for Keyed types (#568)

* Remove use of ament_target_dependencies (#566)

* Skip all multi-vendor pub/sub tests with zenoh (#560)

* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Francisco
  Gallego Salido, Janosch Machowinski, Michael Carlstrom, Scott K
  Logan, Shane Loretz, Tomoya Fujita, mini-1235, mosfet80, yadunund

test_interface_files
====================

* Update CMakeLists.txt (#26)

* Remove CODEOWNERS and mirror-rolling-to-master workflow. (#23)

* Contributors: Chris Lalancette, mosfet80
