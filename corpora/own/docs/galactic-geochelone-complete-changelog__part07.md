# Galactic Geochelone changelog (part 7 of 8)

rosidl_generator_c
==================

* Expose C code generation via rosidl generate CLI (#569)

* Strip action service suffixes from C include prefix (#538)

* Update the maintainers of this repository. (#536)

* Fix the declared language for a few packages (#530)

* Do not depend on rosidl_runtime_c when tests are disabled (#503)

* Contributors: Ben Wolsieffer, Chris Lalancette, Jacob Perron, Michel
  Hidalgo, Scott K Logan

rosidl_generator_cpp
====================

* Expose C++ code generation via rosidl generate CLI (#570)

* Switch to std::allocator_traits. (#564)

* Remove unnecessary assert on pointer created with new (#555)

* Use ASSERT_TRUE to check for nullptr. (#543)

* Update the maintainers of this repository. (#536)

* Add to_yaml() function for C++ messages (#527)

* Add function for getting a types fully qualified name (#514)

* Declaring is_message in namespace rosidl_generator_traits (#512)

* Contributors: Chris Lalancette, Devin Bonnie, Dirk Thomas, Jacob
  Perron, Michel Hidalgo, Sebastian Höffner, Stephen Brawner

rosidl_generator_dds_idl
========================

* Expose .idl to DDS .idl conversion via rosidl translate CLI. (#55)

* Update maintainers. (#54)

* Contributors: Michel Hidalgo, Shane Loretz

rosidl_generator_py
===================

* Remove dependency from rosidl_typesupport_connext_c (#127)

* Expose Python code generation via rosidl generate CLI (#123)

* remove maintainer (#126)

* Update maintainers (#119)

* Fix too early decref of WString when converting from Python to C
  (#117)

* Add pytest.ini so tests succeed locally. (#116)

* Contributors: Andrea Sorbini, Chris Lalancette, Claire Wang, Dirk
  Thomas, Michel Hidalgo

rosidl_parser
=============

* Update and add package.xml descriptions to README (#553)

* Finish support for fixed-point literals.

* Fix parsing of small floats.

* Update the maintainers of this repository. (#536)

* Allow zero length string constants (#507)

* Add pytest.ini so tests succeed locally (#502)

* Contributors: Chris Lalancette, Dirk Thomas, Shane Loretz

rosidl_runtime_c
================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#581)

* Shorten some excessively long lines of CMake (#571)

* Update and add package.xml descriptions to README (#553)

* Fix item number in QD (#546)

* Update the maintainers of this repository. (#536)

* Add rcutils dependency. (#534)

* QD: Add links to hosted API docs (#533)

* Updated Quality Level to 1 (#532)

* Add benchmarks for rosidl_runtime_* packages (#521)

* Fix the declared language for a few packages (#530)

* Add fault injection macros and test (#509)

* Update rosidl_runtime_c QD to QL 2 (#500)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Louise
  Poubel, Scott K Logan, Shane Loretz, Stephen Brawner, brawner,
  shonigmann

rosidl_runtime_cpp
==================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#581)

* Fix typo of package name in README heading (#561)

* Update and add package.xml descriptions to README (#553)

* Fix item number in QD (#546)

* Update the maintainers of this repository. (#536)

* QD: Add links to hosted API docs (#533)

* Updated Quality Level to 1 (#532)

* Add benchmarks for rosidl_runtime_* packages (#521)

* Add to_yaml() function for C++ messages (#527)

* Add function for getting a types fully qualified name (#514)

* Fix misuses of input iterators in BoundedVector (#493)

* Update QD to reflect QL 2 statuses (#499)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Devin
  Bonnie, Dirk Thomas, Jacob Perron, Jonathan Wakely, Louise Poubel,
  Scott K Logan, Shane Loretz, Stephen Brawner, Tully Foote,
  shonigmann

rosidl_runtime_py
=================

* Add pytest.ini so local tests don't display warning (#12)

* Contributors: Chris Lalancette

rosidl_typesupport_c
====================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#108)

* Remove dependencies from Connext type support (#106)

* Expose C typesupport generation via rosidl generate CLI (#105)

* Typo typesupport_identidentifier (#103)

* Remove type_support_dispatch.cpp files. (#101)

* Defer path resolution of rosidl typesupport libraries to dynamic
  linker. (#98)

* Ensure typesupport handle functions do not throw. (#99)

* Explicitly check lib pointer for null (#95)

* Update Quality Declaration to QL 1 (#96)

* Add mock for rcutils_get_symbol failure (#93)

* Update the maintainers (#89)

* Catch exception from has_symbol (#86)

* Added benchmark test to rosidl_typesupport_c/cpp (#84)

* Handle rcpputils::find_library_path() failure (#85)

* Add fault injection macros and unit tests (#80)

* Remove rethrow in extern c code (#82)

* Add Security Vulnerability Policy pointing to REP-2006 (#76)

* Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Chris
  Lalancette, Jose Luis Rivero, Jose Tomas Lorente, Louise Poubel,
  Michel Hidalgo, Shane Loretz, Stephen Brawner, shonigmann

rosidl_typesupport_cpp
======================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#108)

* Remove dependencies from Connext type support (#106)

* Expose C++ typesupport generation via rosidl generate CLI (#104)

* Remove type_support_dispatch.cpp files. (#101)

* Defer path resolution of rosidl typesupport libraries to dynamic
  linker. (#98)

* Ensure typesupport handle functions do not throw. (#99)

* Explicitly check lib pointer for null (#95)

* Update Quality Declaration to QL 1 (#96)

* Update the maintainers (#89)

* Added benchmark test to rosidl_typesupport_c/cpp (#84)

* Handle rcpputils::find_library_path() failure (#85)

* De-duplicate type_support_map.h header (#81)

* Add fault injection macros and unit tests (#80)

* Add Security Vulnerability Policy pointing to REP-2006 (#76)

* Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Chris
  Lalancette, Jose Luis Rivero, Louise Poubel, Michel Hidalgo, Stephen
  Brawner, shonigmann

rosidl_typesupport_fastrtps_c
=============================

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#69)

* Expose FastRTPS C typesupport generation via rosidl generate CLI
  (#65)

* Update QDs with up-to-date content (#64)

* Fix item number in QD (#59)

* Update QL to 2

* Update package maintainers (#55)

* Updat QD (#53)

* Fix invalid return on deserialize function (#51)

* Added benchmark test to rosidl_typesupport_fastrtps_c/cpp (#52)

* Update exec dependencies (#50)

* Add Security Vulnerability Policy pointing to REP-2006 (#44)

* QD Update Version Stability to stable version (#46)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jorge
  Perez, Louise Poubel, Michel Hidalgo, Stephen Brawner, shonigmann,
  sung-goo-kim

rosidl_typesupport_fastrtps_cpp
===============================

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#69)

* Expose FastRTPS C++ typesupport generation via rosidl generate CLI
  (#66)

* Update QDs with up-to-date content (#64)

* Fix item number in QD (#59)

* Update QL to 2

* Update package maintainers (#55)

* Update QD (#53)

* Add benchmark test to rosidl_typesupport_fastrtps_c/cpp (#52)

* Update exec dependencies (#50)

* Add Security Vulnerability Policy pointing to REP-2006 (#44)

* QD Update Version Stability to stable version (#46)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jorge
  Perez, Louise Poubel, Michel Hidalgo, Stephen Brawner, shonigmann

rosidl_typesupport_interface
============================

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#581)

* Fix item number in QD (#546)

* Update the maintainers of this repository. (#536)

* QD: Add links to hosted API docs (#533)

* Update Quality Declaration to QL 1 for rosidl_typesupport_interface
  (#519)

* Update QD to reflect QL 2 statuses (#499)

* Contributors: Chris Lalancette, Louise Poubel, Stephen Brawner,
  brawner, shonigmann

rosidl_typesupport_introspection_c
==================================

* Expose C introspection typesupport generation via rosidl generate
  CLI (#572)

* Update the maintainers of this repository. (#536)

* Fix get_function and get_const_function semantics for arrays (#531)

* Fix the declared language for a few packages (#530)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel
  Hidalgo, Scott K Logan

rosidl_typesupport_introspection_cpp
====================================

* Expose C++ introspection typesupport generation via rosidl generate
  CLI (#573)

* Update the maintainers of this repository. (#536)

* Contributors: Chris Lalancette, Michel Hidalgo

rpyutils
========

* Create a shared function for importing c libraries (#4)

* Add pytest.ini so local tests don't display warning (#3)

* Contributors: Chris Lalancette, Emerson Knapp

rqt
===

* 1.0.7 (#243)

* Remove Dirk from maintainers in package.xml files per request.
  (#236)

* Update maintainers for the crystal-devel branch (#234)

* Contributors: Michael Jeronimo, Scott K Logan

rqt_action
==========

* Updated Open Robotics maintainer

* Fixed package to run with ros2 run (#8)

* Contributors: Alejandro Hernández Cordero, Mabel Zhang

rqt_bag
=======

* Remove an invalid import statement (#101)

* Reset timeline zoom after loading a new bag. (#98)

* Refactor the Rosbag2 class (#91)

* Fix exec_depend (#89)

* Use updated HistoryPolicy values to avoid deprecation warnings (#88)

* Enable recording for ROS2 (#87)

* Enable the playback functionality for ROS2 (#85)

* Port the topic and node selection dialogs to ROS2 (#86)

* Save the serialization format and offered_qos_profiles when
  exporting (#84)

* Enable the export/save bag functionality for ROS2 (#82)

* Update known message types and associated colors (#81)

* Open the bag directory instead of a single file (#80)

* Port the image_view plugin to ROS2 (#78)

* Clean up widgets in plot_view layout correctly (#69) (#77)

* Fix tuples for bisect calls (#67) (#76)

* Fix issue: no vertical scroll bar until window is resized (#63)
  (#75)

* Update the basic plugins for ROS2 (#72)

* Update the rosbag2 python module (#71)

* Dynamically resize the timeline when recording (#66)

* Starting point for resuming the ROS2 port (#70)

* Fix a bug with the status line progress bar (#62)

* Update a few minor status bar-related items (#61)

* Make the tree controls in the Raw View and Plot View consistent
  (#57)

* Update the package.xml files with the latest Open Robotics
  maintainers (#58)

* fix Python 3 issue: long/int (#52)

* save last directory opened to load a bag file (#40)

* fix shebang line for Python 3 (#48)

* bump CMake minimum version to avoid CMP0048 warning

* fix Python 3 exception, wrap filter call in list() (#46)

* add Python 3 conditional dependencies (#44)

* autopep8 (#30)

* add support for opening multiple bag files at once (#25)

* fix debug/warning messages for unicode filenames (#26)

* fix regression from version 0.4.10 (#17)

* fix regression from version 0.4.9 (#16)

* handle errors happening while loading a bag (#14)

* add rqt_bag.launch file (#440)

* fix Python 2 regression from version 0.4.4 (#424)

* use Python 3 compatible syntax (#421)

* fix race condition reading bag files (#412)

* add "From nodes" button to record mode (#348)

* show file size of bag file in the status bar (#347)

* fix mouse wheel delta in Qt 5 (#376)

* Support Qt 5 (in Kinetic and higher) as well as Qt 4 (in Jade and
  earlier) (#359)

* fix publishing wrong topic after scrolling (#362)

* RQT_BAG: Ensure monotonic clock publishing. Due to parallelism
  issues, a message can be published with a simulated timestamp in the
  past. This lead to undesired behaviors when using TF for example.

* Added step-by-step playback capability

* fix viewer plugin relocation issue (#306)

* fix topic type retrieval for multiple bag files (#279)

* fix region_changed signal emission when no start/end stamps are set

* improve right-click menu

* improve popup management (#280)

* implement recording of topic subsets

* sort the list of topics

* update plugin scripts to use full name to avoid future naming
  collisions

* fix visibility with dark Qt theme (#263)

* fix compatibility with Groovy, use queue_size for Python publishers
  only when available (#243)

* use thread for loading bag files, emit region changed signal used by
  plotting plugin (#239)

* export architecture_independent flag in package.xml (#254)

* fix closing and reopening topic views

* use queue_size for Python publishers

* fix raw view not showing fields named 'msg' (#226)

* add option to publish clock tim from bag (#204)

* add groups for rqt plugins, renamed some plugins (#167)

* fix high cpu load when idle (#194)

* update rqt_bag plugin interface to work with qt_gui_core 0.2.18

* fix rendering of icons on OS X (ros-visualization/rqt#83)

* fix shutdown of plugin (#31)

* fix saving parts of a bag (#96)

* fix long topic names (#114)

* fix zoom behavior (#76)

* Fix; skips time when resuming playback (#5)

* Fix; timestamp printing issue (#6)

* expose command line arguments to rqt_bag script

* added fix to set play/pause button correctly when
  fastforwarding/rewinding, adjusted time headers to 0m00s instead of
  0:00m for ease of reading

* support passing bagfiles on the command line (currently behind
  --args)

* first release of this package into Groovy

* Contributors: Aaron Blasdel, Chris Lalancette, Michael Grupp,
  Michael Jeronimo, lsouchet, sambrose

rqt_bag_plugins
===============

* Refactor the Rosbag2 class (#91)

* Port the plot view to ROS2 (#79)

* Port the image_view plugin to ROS2 (#78)

* Starting point for resuming the ROS2 port (#70)

* Make the tree controls in the Raw View and Plot View consistent
  (#57)

* Update the package.xml files with the latest Open Robotics
  maintainers (#58)

* initialize pil_mode when image is compressed (#54)

* support 16-bit bayer images (#45)

* maintain image aspect ratio (#32)

* fix Python 3 issue: long/int (#51)

* fix Python 3 issue: ensure str is encoded before decoding (#50)

* bump CMake minimum version to avoid CMP0048 warning

* add Python 3 conditional dependencies (#44)

* add cairocffi as the fallback module (#43)

* autopep8 (#30)

* fix Python 2 regression from version 0.4.4 (#426)

* use Python 3 compatible syntax (#421)

* fix crash when toggling thumbnail (#380)

* lock bag when reading for plotting (#382)

* Support Qt 5 (in Kinetic and higher) as well as Qt 4 (in Jade and
  earlier) (#359)

* add missing dependency on rqt_plot (#316)

* work around Pillow segfault if PyQt5 is installed (#289, #290)

* add displaying of depth image thumbnails

* add missing dependency on python-cairo (#269)

* fix missing installation of resource subfolder

* add plotting plugin (#239)

* fix rqt_bag to plot array members (#253)

* export architecture_independent flag in package.xml (#254)

* fix PIL/Pillow error (#224)

* first release of this package into Groovy

* Contributors: John Stechschulte, Michael Jeronimo

rqt_console
===========

* Use underscores in setup.cfg instead of dashes (#31)

* Fix regression introduced in #21 (#28)

* Changed the build type to ament_python and added setup.cfg (#21)

* Contributors: Alejandro Hernández Cordero, Michel Hidalgo

rqt_graph
=========

* Make topics that have qos incompatibilities red in the graph, add
  information to the node tooltip (#61)

* Add node name, topic name, and endpoint kind to the qos edge tooltip
  (#60)

* Update maintainers for ROS2 branches (#55)

* add edge tooltip with QoS of publishers and subscribers (#53)

* install executable rqt_graph (#49)

* add setup.cfg with script install directories (#42)

* add pytest.ini so local tests don't display warning (#48)

* Contributors: Ivan Santiago Paunovic, Michael Jeronimo

rqt_gui
=======

* getiterator() renamed to iter() in Python 3.9 (#239)

* Contributors: goekce

rqt_gui_cpp
===========

* use tgt compile features (#247)

* Contributors: Audrow Nash

rqt_gui_py
==========

* Fix a crash at shutdown (#248)

* Contributors: Michael Jeronimo

rqt_msg
=======

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#8)

* Use rosidl_runtype_py instead of message_helpers where possible
  (#11)

* Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic

rqt_plot
========

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#58)

* Fix plots of array items (#71)

* Update maintainers

* Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic,
  Mabel Zhang

rqt_publisher
=============

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#18)

* Drop numpy.float128 references (#26)

* Use rosidl_runtime_py instead of rqt_py_common where possible (#24)

* Add now() to evaluation (#22)

* fix setting expressions on sequence items (#16)

* Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic,
  Michel Hidalgo, Yossi Ovcharik

rqt_py_common
=============

* Avoid installing test interfaces (#228)

* Contributors: Dirk Thomas

rqt_py_console
==============

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#8)

* Contributors: Alejandro Hernández Cordero

rqt_reconfigure
===============

* Cleanups to the install scripts. (#103)

* Fix a flake8 warning. (#99)

* Use timeouts in service calls to avoid hangs (#98)

* Add maintainer to package.xml (#95)

* Save instance state in rqt settings (#90)

* Use safe YAML loader (#89)

* Don't process scroll events unless specifically focused (#88)

* Fix node selection from command line (#87)

* Add pytest.ini so local tests don't display warning (#91)

* Support PEP 338 invocation of rqt_reconfigure (#85)

* Fixed package to run with ros2 run (#81)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael
  Jeronimo, Scott K Logan

rqt_service_caller
==================

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#13)

* ignore services that don't use the SRV_MODE ('srv') (#20)

* Contributors: Alejandro Hernández Cordero, William Woodall

rqt_shell
=========

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#11)

* Contributors: Alejandro Hernández Cordero

rqt_srv
=======

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#4)

* Contributors: Alejandro Hernández Cordero

rqt_top
=======

* Changed the build type to ament_python and fixed package to run with
  ros2 run (#8)

* Contributors: Alejandro Hernández Cordero

rqt_topic
=========

* Add pytest.ini to silence warnings when running locally.

* Fix warnings pointed out by flake8.

* Created an entry-point for rqt_topic in setup.py (#16)

* Fix flake8 errors and add linter tests (#28)

* Update Open Robotics Maintainer (#26)

* Use raw / non-string value for ordering (#23)

* Support order fields as defined in message (#22)

* Fix the type cell value for sequence items (#21)

* Updated version package and license in setup.py (#17)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk
  Thomas, Scott K Logan

rti_connext_dds_cmake_module
============================

* Pass "-Wl,--no-as-needed" for system dependencies of Connext 5.3.1.

* Set "IMPORTED_NO_SONAME true" for Connext 5.3.1 imported library
  target.

* Add "<buildtool_export_depend>" for "ament_cmake".

* Add "<depend>" for "rti-connext-dds-5.3.1"

* Add dependency from rti-connext-dds-5.3.1.

* Initial release.

rttest
======

* Fix up nonsensical handling of NULL in
  rttest_get_{params,statistics} (#107)

* Remove "struct" from rttest_sample_buffer variable declaration.
  (#105)

* Convert the sample buffer to a vector. (#104)

* Use strdup instead of strlen/strcpy dance. (#100)

* Enable basic warnings in rttest (#99)

* Only copy an rttest_sample_buffer if it is not nullptr. (#98)

* Convert timespec to uint64 not long and vice versa (#94) (#96)

* Fix standard deviation overflow(#95) (#97)

* Contributors: Audrow Nash, Chris Lalancette, y-okumura-isp

rviz2
=====

* Use "%s" as format string literal in logging macros (#633)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* Move and update documentation for ROS 2 (#600)

* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

rviz_assimp_vendor
==================

* Always preserve source permissions in vendor packages (#647)

* Add an override flag to force vendored build (#642)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* Updated a hack to avoid CMake warning with assimp 5.0.1 and older,
  applying it cross platforms (#565)

* Contributors: Dirk Thomas, Jacob Perron, Scott K Logan

rviz_common
===========

* Add visualization_frame to the public API (#660)

* Add ViewPicker::get3DPatch to the public API (#657)

* Fix byte indexing for depth patch pixels (#661)

* fix toolbar vanishing when pressing escape (#656)

* Expose VisualizationManager and YamlConfigReader to the public API
  (#649)

* Use the stack for the classes in the property test. (#644)

* Check that the views_man_ and views_man_->getCurrent() are not
  nullptr. (#634)

* Fix for mousewheel to zoom in/out (#623)

* Ensure rviz_common::MessageFilterDisplay processes messages in the
  main thread (#620)

* Fix render window disppearing after saving image (#611)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* TimePanel port (#599)

* Upgrade to tinyxml2 for rviz (#418)

* Fix segfault on changing filter size for non-existent topic (#597)

* improve color support for themes (#590)

* Fix topic IntProperty number ranges (#596)

* Switch to nullptr everywhere. (#592)

* Expose MessageFilterDisplay's queue size (#593)

* Filter topics in drop down menu (#591)

* rviz_common: Remove variadic macro warning check (#421)

* Use retriever.hpp (#589)

* Fix the order of destructors (#572)

* Changed to not install test header files in rviz_rendering. (#564)

* Fixed alphabetical include order (#563)

* Changed to avoid trying to moc generate "env_config.hpp" file.
  (#550)

* Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Jacob
  Perron, Jafar Abdi, Joseph Schornak, Karsten Knese, Martin Idel,
  Michael Ferguson, Michael Jeronimo, Michel Hidalgo, Nico Neumann,
  Rich Mattes, Shane Loretz, ipa-fez, spiralray

rviz_default_plugins
====================

* Add ViewPicker::get3DPatch to the public API (#657)

* Allow to zoom more with orbit controller (#654)

* Fix possible nullptr access in robot_joint.cpp. (#636)

* Fix for mousewheel to zoom in/out (#623)

* Make the types explicit in quaternion_helper.hpp. (#625)

* Update status message by removing colon or adjust colon position
  (#624)

* Do not use assume every RenderPanel has a ViewController. (#613)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* TimePanel port (#599)

* Upgrade to tinyxml2 for rviz (#418)

* Use retriever.hpp (#589)

* Added covariance settings to set pose estimate (#569)

* use reference in range loops to avoid copy (#577)

* Changed to not install test header files in rviz_rendering. (#564)

* Changed to use a dedicated TransformListener thread. (#551)

* Suppressed warnings when building with older Qt versions. (#562)

* Restored compatibility with older Qt versions (#561)

* Contributors: Chen Lihui, Chris Lalancette, Dirk Thomas, Jacob
  Perron, Joseph Schornak, Martin Idel, Matthijs den Toom, Michel
  Hidalgo, Nico Neumann, Shane Loretz, Victor Lamoine, ymd-stella

rviz_ogre_vendor
================

* Always preserve source permissions in vendor packages (#647)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* Pass through CMAKE_{C,CXX}_FLAGS to OGRE build (#587)

* Contributors: Jacob Perron, Scott K Logan

rviz_rendering
==============

* reset current line width when calculating text width (#655)

* Silence a dead store warning. (#643)

* Fix a memory leak when using the ResourceIOSystem. (#641)

* Revert "Support loading meshes other than .mesh and .stl with
  package URIs (#610)" (#638)

* Prevent rviz_rendering::AssimpLoader from loading materials twice.
  (#622)

* Support loading meshes other than .mesh and .stl with package URIs
  (#610)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* Switch to nullptr everywhere. (#592)

* Use retriever.hpp (#589)

* Avoid hidding base class getRenderOperation in PointCloudRenderable
  (#586)

* Changed to not install test header files in rviz_rendering. (#564)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Jacob
  Perron, Michel Hidalgo, Shane Loretz, ipa-fez

rviz_rendering_tests
====================

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* Use retriever.hpp (#589)

* Changed to not install test header files in rviz_rendering. (#564)

* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

rviz_visual_testing_framework
=============================

* Quiet a clang warning about a Qt memory leak. (#651)

* use rcutils_get_env. (#609)

* Add linters and use ament_lint_auto (#608)

* Update maintainers (#607)

* Contributors: Chris Lalancette, Jacob Perron, tomoya

sensor_msgs
===========

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Fix PointCloud2Iterator namespacing in docs (#139)

* Add coverage/performance to qd for sensor_msgs (#137)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Missing cstring header for memcpy in fill_image.hpp (#126)

* Update Quality levels to level 3 (#124)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Andre Nguyen, Chris
  Lalancette, Jose Luis Rivero, Michel Hidalgo, Stephen Brawner,
  brawner, shonigmann

sensor_msgs_py
==============

* Use underscores instead of dashes in setup.cfg (#150)

* Port of point_cloud2.py from ROS1 to ROS2. As seperate pkg. (#128)

* Contributors: Ivan Santiago Paunovic, Sebastian Grans

shape_msgs
==========

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

shared_queues_vendor
====================

* Explicitly add emersonknapp as maintainer (#692)

* Update the package.xml files with the latest Open Robotics
  maintainers (#535)

* Contributors: Emerson Knapp, Michael Jeronimo

spdlog_vendor
=============

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#24)

* Update to spdlog 1.8.2 (#23)

* Remove a stale TODO (#22)

* Always preserve source permissions in vendor packages (#20)

* Remove unnecessary call to find_package(PATCH) (#18)

* Updated QD to 1 (#16)

* bump spdlog version to 1.6.1 (#15)

* Bump QD to level 3 and updated QD (#14)

* Add Security Vulnerability Policy pointing to REP-2006. (#13)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk
  Thomas, Scott K Logan, shonigmann
