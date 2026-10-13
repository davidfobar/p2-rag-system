# Galactic Geochelone changelog (part 3 of 8)

* add plugin examples for the tutorial

* update instructions for catkin

* remove uselessly linked library fixes #28

* add a tutorial for image_transport

* add Jack as maintainer

* update my email address

* fix the urls

* use the pluginlib script to remove some warnings

* added license headers to various cpp and h files

* get rid of the deprecated class_loader interface

* CMakeLists.txt clean up

* Updated package.xml file(s) to handle new catkin buildtool_depend
  requirement

* add the right link libraries

* Isolated plugins into their own library to follow new
  class_loader/pluginlib guidelines.

* remove the brief attribute

* add xml file

* fix bad folder/libraries

* fix dependencies

* add catkin as a dependency

* comply to the catkin API

* install the include directories

* make the libraries public

* catkinize for Groovy

* Initial image_common stack check-in, containing image_transport.

* Contributors: Aaditya Saraiya, Aaron Blasdel, Carl Delsey, Gary
  Servin, Jacob Perron, Jochen Sprickerhof, Karsten Knese, Lucas
  Walter, Martin Guenther, Martin Idel, Max Schwarz, Michael Carroll,
  Mikael Arguedas, Mirza Shah, Thibaud Chupin, Vincent Rabaud, William
  Woodall, gerkey, kwc, mihelich, mirzashah, pmihelich, straszheim,
  vrabaud

interactive_markers
===================

* Cleanup bsd 3 clause license usage (#61)

* Add missing includes (#81)

* Update maintainers (#79)

* Increase test timeout necessary for Connext (#77)

* Fix clang warnings (#75)

* Remove explicit template parameter in "spin_until_future_complete"
  (#72)

* Contributors: Bjar Ne, Dirk Thomas, Jacob Perron, Sarthak Mittal,
  Tully Foote

intra_process_demo
==================

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo

kdl_parser
==========

* Remove tinyxml dependency from kdl_parser. (#43)

* Remove unused find_library call (#40)

* Contributors: Chris Lalancette, Michael Carroll

laser_geometry
==============

* Use rclcpp::Duration::from_seconds (#72)

* update maintainers

* increase test timeout

* Contributors: Dirk Thomas, Ivan Santiago Paunovic, Jonathan Binney,
  Mabel Zhang

launch
======

* Only try to wrap the fd in a socket on Windows (#498)

* Close the socket pair used for signal management (#497)

* Remove is_winsock_handle() and instead test if wrapping the handle
  in a socket.socket() works (#494)

* Add frontend substitution for logging directory (#490)

* Add arg_choice arg to DeclareLaunchArguments (#483)

* Support Python 3.8-provided importlib.metadata (#482)

* Workaround asyncio signal handling on Unix (#479)

* Handle signals within the asyncio loop. (#476)

* Support non-interactive launch.LaunchService runs (#475)

* print stderr message when command failed (#474)

* Add frontend support for LogInfo action (#467)

* Validate unparsed attributes and subentities in launch_xml and
  launch_yaml (#468)

* Fix bug in launch.actions.TimerAction.parse() (#470)

* Allow configuring logging directory through environment variables
  (#460)

* Update package maintainers (#465)

* Expose Timer action in launch xml (#462)

* Fix dollar symbols in substitution grammar (#461)

* Add new conditions for checking launch configuration values (#453)

* Refactor launch service run_async loop to wait on futures and queued
  events (#449)

* Fix documentation typo (#446)

* Fix type_utils.extract_type() function. (#445)

* Handle empty strings in type coercion. (#443)

* Consolidate type_utils in a way that can be reused in substitution
  results that need to be coerced to a specific type (#438)

* Delete unnecessary loading of
  'launch.frontend.interpolate_substitution_method' entry point that
  was never used (#434)

* Avoid side effect, defer until needed (#432)

* Remove pkg_resources, replace it with the use of the more modern
  importlib* libraries. (#430)

* Remove the asyncio.wait loop parameter. (#429)

* Add pytest.ini so local tests don't display warning (#428)

* Defer shutdown if already running (#427)

* Add respawn and respawn_delay support (#426)

* Fix up parser.py (#414)

* Contributors: CHEN, Chris Lalancette, Christophe Bedard, Dan Rose,
  Dirk Thomas, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez,
  Michel Hidalgo, Scott K Logan, Takamasa Horibe, Victor Lopez

launch_ros
==========

* Support Python 3.8 importlib.metadata, declare dependency (#229)

* Add options extensions to ros2launch and extensibility to the node
  action (#216)

* Make sure ParameterFile __del__ works without exception. (#212)

* Fix docblock in LoadComposableNodes (#207)

* Validate complex attributes of 'node' action (#198)

* Node.__init__() executable and ComposableNode.__init__() plugin
  arguments aren't optional (#197)

* Remove constructors arguments deprecated since Foxy (#190)

* Make name and namespace mandatory in ComposableNodeContainer, remove
  deprecated alternatives (#189)

* Merge pull request #183 from ros2/update-maintainers Update the
  package.xml files with the latest Open Robotics maintainers

* Move previous maintainer to <author>

* Update the package.xml files with the latest Open Robotics
  maintainers

* Fix AttributeError when accessing component container name (#177)

* Handle any substitution types for SetParameter name argument (#182)

* Asynchronously wait for load node service response (#174)

* Fix case where list of composable nodes is zero (#173)

* Do not use event handler for loading composable nodes (#170)

* Fix race with launch context changes when loading composable nodes
  (#166)

* Substitutions in parameter files (#168)

* Fix documentation typo (#167)

* Fix problems when parsing a "Command" "Substitution" as a parameter
  value (#137)

* Add a way to set remapping rules for all nodes in the same scope
  (#163)

* Resolve libyaml warning when loading parameters from file (#161)

* Fix ComposableNode ignoring PushRosNamespace actions (#162)

* Add a SetParameter action that sets a parameter to all nodes in the
  same scope (#158)

* Make namespace parameter mandatory in LifecycleNode constructor
  (#157)

* Avoid using a wildcard to specify parameters if possible (#154)

* Fix no specified namespace (#153)

* Add pytest.ini so local tests don't display warning (#152)

* Contributors: Chris Lalancette, Dereck Wonnacott, Geoffrey Biggs,
  Ivan Santiago Paunovic, Jacob Perron, Michael Jeronimo, Scott K
  Logan

launch_testing
==============

* Use unittest.mock instead of mock (#487)

* Update package maintainers (#465)

* Disable cleanup of test cases once they have been run (#406)

* Fix max() with empty sequence (#440)

* Use unittest.TestCase.id() for pytest failure reprs. (#436)

* Use unittest.TestCase.id() to put together jUnit XML output. (#435)

* Claim ownership (#433)

* Contributors: Dirk Thomas, Michel Hidalgo, Scott K Logan, William
  Woodall

launch_testing_ament_cmake
==========================

* Update package maintainers (#465)

* Add bsd license to launch due to files from roslaunch (#456)

* Use launch_test CMake target as output file basename (#448)

* Find Python debug interpreter on Windows (#437)

* Contributors: Dirk Thomas, Michel Hidalgo, William Woodall

launch_testing_ros
==================

* Use underscores in setup.cfg instead of dashes. (#227)

* Merge pull request #183 from ros2/update-maintainers

* Move Pete to author, per clalancette

* Update the package.xml files with the latest Open Robotics
  maintainers

* Add pytest.ini so local tests don't display warning (#152)

* Contributors: Chris Lalancette, Michael Jeronimo, Mike Purvis

launch_xml
==========

* Add frontend support for LogInfo action (#467)

* Validate unparsed attributes and subentities in launch_xml and
  launch_yaml (#468)

* Add test for launch.actions.TimerAction (#470)

* Update package maintainers (#465)

* Use new type_utils functions (#438)

* Add pytest.ini so local tests don't display warning (#428)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Jacob
  Perron, Michel Hidalgo

launch_yaml
===========

* Add frontend support for LogInfo action (#467)

* Validate unparsed attributes and subentities in launch_xml and
  launch_yaml (#468)

* Update package maintainers (#465)

* Use new type_utils functions (#438)

* Close YAML file when we're done. (#415)

* Add pytest.ini so local tests don't display warning (#428)

* Contributors: Chris Lalancette, Dan Rose, Ivan Santiago Paunovic,
  Jacob Perron, Michel Hidalgo

libcurl_vendor
==============

* Update libcurl_vendor to the latest version (7.75.0). (#60)

* Add an override flag to force vendored build (#58)

* Update maintainers (#53)

* bump curl version to 7.68 (#47)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk
  Thomas, Scott K Logan

libstatistics_collector
=======================

* fix: measured values after the decimal point are truncated #79 (#80)

* Update linter to run on rolling+focal (#81)

* Add automerge.yml config file (#70)

* Update QD to QL 1 (#68)

* Updated QD (#64)

* Updated QD Performance tests (#58)

* Added benchmark test to libstatistics_collector (#57) * Added
  benchmark test to libstatistics_collector * cppcheck supressed
  unknown macro warning - macos * Reset heap counters * Added feedback
  * Remove unknownMacro suppression from CMakeLists.txt * Added
  feedback * moved benchmark test to test/benchmark * Added feedback
  Co-authored-by: Devin Bonnie
  <47613035+dabonnie@users.noreply.github.com>

* Report failed workflows (#56) Allow codecov failures to be silent

* Add default CODEOWNERS file (#55)

* Remove repo activity from individual repositories in favor of
  centralized reporting (#52)

* Don't attempt to report if originating from a fork (#43)

* Removed doxygen warnings (#41) Co-authored-by: Anas Abou Allaban
  <allabana@amazon.com>

* Add autoapprove action for dependabot (#40)

* Create Dependabot config file (#31) * Create Dependabot config file
  * Randomize time of run Co-authored-by: dependabot-preview[bot]
  <27856297+dependabot-preview[bot]@users.noreply.github.com> Co-
  authored-by: Prajakta Gokhale <prajaktg@amazon.com>

* Updated QD to 3 (#30)

* Add Security Vulnerability Policy pointing to REP-2006. (#24) Co-
  authored-by: Emerson Knapp
  <537409+emersonknapp@users.noreply.github.com>

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Devin
  Bonnie, Emerson Knapp, Lucas Han, Prajakta Gokhale, Stephen Brawner,
  hsgwa

libyaml_vendor
==============

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#38)

* Update libyaml_vendor to 0.2.5. (#37)

* Fix linker flags for tests when CMake < 3.13 (#35)

* Always preserve source permissions in vendor packages (#31)

* Fix target_link_directories/link_directories in cmake (#29)

* Included benchmark tests (#20)

* Update Quality Declaration (#23)

* Update package maintainers. (#22)

* Bump QD to 3 and some minor style fixes (#19)

* Add Security Vulnerability Policy pointing to REP-2006. (#18)

* Add quality declaration libyaml_vendor (#12)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jorge
  Perez, Michel Hidalgo, Scott K Logan, shonigmann

lifecycle
=========

* Cleanup the README.rst for the lifecycle demo. (#508)

* change ParameterEventHandler to take events as const ref instead of
  shared pointer (#494)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Add missing required parameter in LifecycleNode launch action (#456)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michael
  Jeronimo, William Woodall

lifecycle_msgs
==============

* Change index.ros.org -> docs.ros.org. (#122)

* Updating Quality Declaration (#120)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner,
  brawner, shonigmann

logging_demo
============

* Update logging macros (#476)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Audrow Nash, Michael Jeronimo

map_msgs
========

* update maintainers

* Contributors: Mabel Zhang, Steve Macenski

message_filters
===============

* Find and export dependencies properly (#54)

* Add pytest.ini so local tests don't display warning (#47)

* Contributors: Chris Lalancette, Michel Hidalgo

mimick_vendor
=============

* Always preserve source permissions in vendor packages (#19)

* Suppress update of pinned git repository (#17)

* Don't overwrite -Wno-dev CMake argument (#18)

* Add missing build tool dependency on 'git' (#16)

* Update tag for armv7l support. (#15)

* Update tag for new cmake version requirement (#14)

* Export include directories (#13)

* Update package maintainers (#10)

* Suppress cppcheck for MMK_MANGLE_ (#8)

* Change Mimick tagged version. (#7)

* Change tag to pull latest Mimick version (#6)

* Pin Mimick version. (#5)

* Change imported dep to match ROS 2 fork (#4)

* Avoid CMAKE_BUILD_TYPE warnings on Windows. (#3)

* Remove dep tag + add maintainer(#2)

* Configure MSVC x64 builds when appropriate. (#1)

* First iteration vendor for Mimick library

* Contributors: Jorge Perez, Michel Hidalgo, Scott K Logan, Stephen
  Brawner, brawner

nav_msgs
========

* Change index.ros.org -> docs.ros.org. (#149)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#145)

* Update QDs to QL 1 (#135)

* Update package maintainers. (#132)

* Updated Quality Level to 2 (#131)

* Add LoadMap service (#129)

* Update Quality levels to level 3 (#124)

* Finish up API documentation (#123)

* Add Security Vulnerability Policy pointing to REP-2006. (#120)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel
  Hidalgo, Stephen Brawner, Steve Macenski, brawner, shonigmann

osrf_pycommon
=============

* Fix osrf.py_common.process_utils.get_loop() implementation (#70)

* Python 2/3 version conflict (#69)

* remove jessie because we no longer support 3.4 (#67)

* Remove deprecated use of asyncio.coroutine decorator. (#64)

* Fix the __str__ method for windows terminal_color. (#65)

* Contributors: Chris Lalancette, Jochen Sprickerhof, Michel Hidalgo,
  William Woodall

osrf_testing_tools_cpp
======================

* [osrf_testing_tools_cpp] Add warnings (#54)

* Update cmake minimum version to 2.8.12 (#61)

* Add googletest v1.10.0 (#55)

* Workarounds for Android (#52) (#60)

* Change "WIN32" to "__WIN32" (#53)

* fix execinfo.h not found for QNX (#50)

* Contributors: Ahmed Sobhy, Audrow Nash, Dan Rose, Jacob Perron,
  Stephen Brawner

pendulum_control
================

* Replace rmw_connext_cpp with rmw_connextdds (#489)

* Remove ineffective log output (#450) (#477)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Remove deprecated warning (#459)

* Follow API/file name changes (ros2/realtime_support#94) (#451)

* Contributors: Anas Abou Allaban, Andrea Sorbini, Michael Jeronimo, y
  -okumura-isp

pendulum_msgs
=============

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Contributors: Michael Jeronimo

performance_test_fixture
========================

* Record calls to calloc, update tests (#15)

* Make allocation counter atomic (#13) Even if the benchmark itself
  isn't threaded, the process we're testing could be. In any case,
  this should prevent those shenanigans from messing up the
  measurement.

* Add methods for pausing/resuming performance metrics (#10) * Add
  methods for pausing/resuming performance metrics

* Add benchmarks to evaluate overhead (#11) * Add benchmarks to
  evaluate overhead in performance tests

* Add namespace performance_test_fixture to .cpp (#9)

* Export dependency on benchmark and osrf_testing_tools_cpp (#8)

* Update maintainers (#7)

* Expose a function for resetting the heap counters (#6)

* Stop recording memory operations sooner (#5)

* Suppress memory tools warning if tests will be skipped (#4)

* Export dependency on ament_cmake_google_benchmark (#3)

* Add missing dependency on ament_cmake_google_benchmark (#2)

* Initial 'performance_test_fixture' package (#1)

* Initial commit

* Contributors: Alejandro Hernández Cordero, Scott K Logan, brawner

pluginlib
=========

* Use rcpputils for the filesystem implementation. (#212)

* Check for NULL in XMLElement::Attribute

* Check for NULL in XMLElement::GetText

* Check for NULL in XMLNode::Value

* Remove unused variable output_library (#211)

* Make Chris a maintainer of pluginlib. (#210)

* Add QNX C++ fs library compiler option (#205)

* Fix cmake 3.5 compatibility (#203)

* Add function for same-package pluginlib tests (#201)

* Remove deprecated boost functions (#199)

* Contributors: Ahmed Sobhy, Chris Lalancette, Jeremie Deray, Karsten
  Knese, Shane Loretz

pybind11_vendor
===============

* Update maintainers (#7)

* Merge pull request #3 from ros2/fix_windows_warning

* remove passing in CMAKE_BUILD_TYPE Signed-off-by: Mabel Zhang
  <mabel@openrobotics.org>

* cleanup Signed-off-by: Mabel Zhang <mabel@openrobotics.org>

* do not define CMAKE_BUILD_TYPE on windows Signed-off-by: Mabel Zhang
  <mabel@openrobotics.org>

* suppress all developer warnings Signed-off-by: Mabel Zhang
  <mabel@openrobotics.org>

* suppress warning on windows Signed-off-by: Mabel Zhang
  <mabel@openrobotics.org>

* attempt to fix windows warning Signed-off-by: Mabel Zhang
  <mabel@openrobotics.org>

* Disable building pybind11 tests (#1) Signed-off-by: Karsten Knese
  <karsten@openrobotics.org>

* Update to pybind 2.5.0 (#2) Signed-off-by: Mabel Zhang
  <mabel@openrobotics.org>

* Create pybind11 vendor package. Signed-off-by: Michael Carroll
  <michael@openrobotics.org>

* Contributors: Karsten Knese, Mabel Zhang, Michael Carroll, Shane
  Loretz

python_cmake_module
===================

* Update maintainers (#2)

* Contributors: Shane Loretz

python_qt_binding
=================

* Add repo README

* Shorten some long lines of CMake (#99)

* Update maintainers (#96) (#98)

* Add pytest.ini so local tests don't display warning (#93)

* Contributors: Chris Lalancette, Scott K Logan, Shane Loretz

qt_dotgraph
===========

* add API to set edge tooltip (#237)

qt_gui
======

* Always prefer 'Tango' icon theme (#250)

* Fix 'dict_keys' object not subscriptable (#243)

* allow hide title in standalone (#235)

* add logic to load qt_gui_icons on windows and macOS (#222)

* fix exporting perspective for Python 3.6 (#228)

* remove tango-icon-theme dependency (#224)

* Contributors: Michael Jeronimo, Scott K Logan

qt_gui_cpp
==========

* Fix duplicated QMap to QMultiMap (#244)

* Switch to using the filesystem implementation in rcpputils. (#239)

* avoid a warning about C++ plugins on Windows (#232)

* qt_gui_cpp_sip: declare private assignment operator for SIP (#226)

* Contributors: Chris Lalancette, Homalozoa X

quality_of_service_demo_cpp
===========================

* Add demo of how to use qos overrides (#474)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Update comments in quality_of_service_demo_cpp message_lost_talker
  and message_lost_listener (#458)

* Add message lost status event demo using rclcpp (#453)

* Contributors: Ivan Santiago Paunovic, Michael Jeronimo

quality_of_service_demo_py
==========================

* Use underscores instead of dashes in setup.cfg (#502)

* QoS overrides demo in python (#479)

* Update deprecated qos policy value names (#468)

* Update the package.xml files with the latest Open Robotics
  maintainers (#466)

* Add rclpy message lost status event demo (#457)

* Contributors: Ivan Santiago Paunovic, Michael Jeronimo

rcl
===

* Fix up test_network_flow_endpoints. (#912)

* Make test_two_timers_ready_before_timeout less flaky (#911)

* Add publishing instrumentation (#905)

* Unique network flows (#880)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#909)

* Add functions for waiting for publishers and subscribers (#907)

* Revert "Mark cyclonedds test_service test as flakey (#648)" (#904)

* Guard against returning NULL or empty node names (#570)

* Remove exceptions for rmw_connext_cpp tests. (#903)

* Add support for rmw_connextdds (#895)

* Put an argument list of 'void' where no arguments are expected.
  (#899)

* Cleanup documentation for doxygen. (#896)

* Reference test resources directly from source tree (#554)

* Re-add "Improve trigger test for graph guard condition (#811)"
  (#884)

* Revert "Improve trigger test for graph guard condition (#811)"
  (#883)

* Move the guard condition cleanup after removing callback. (#877)

* Make test_subscription_nominal_string_sequence more reliable (#881)

* Improve trigger test for graph guard condition (#811)

* Add NULL check in remap.c (#879)

* Add const to constant rcl_context functions (#872)

* Fix another failing test on CentOS 7 (#863)

* Update QDs to QL 1 (#866)

* Address clang static analysis issues (#865)

* Fix flaky test_info_by_topic (#859)

* Update QL (#858)

* Refactor for removing unnecessary source code (#857)

* Clarify storing of current_time (#850)

* Make tests in test_graph.cpp more reliable (#854)

* Fix for external log segfault after SIGINT (#844)

* Update tracetools QL and add to rcl_lifecycle's QD (#845)

* Make test logging rosout more reliable (#846)

* Return OK when finalizing zero-initialized contexts (#842)

* Zero initialize events an size_of_events members of rcl_wait_set_t
  (#841)

* Update deprecated gtest macros (#818)

* Make sure to check the return value of rcl APIs. (#838)

* Add convenient node method to get a final topic/service name (#835)

* Remove redundant error formatting (#834)

* Fix memory leak in rcl_subscription_init()/rcl_publisher_init()
  (#794)

* Update maintainers (#825)

* Add a semicolon to RCUTILS_LOGGING_AUTOINIT. (#816)

* Improve error messages in rcl_lifecycle (#742)

* Fix memory leak on serialized message in
  test_publisher/subscription.cpp (#801)

* Fix memory leak because of mock test (#800)

* Spelling correction (#798)

* Fix that not to deallocate event impl in some failure case (#790)

* calling fini functions to avoid memory leak (#791)

* Bump rcl arguments' API test coverage (#777)

* Fix rcl arguments' API memory leaks and bugs (#778)

* Add coverage tests wait module (#769)

* Fix wait set allocation cleanup (#770)

* Improve test coverage in rcl (#764)

* Check if rcutils_strdup() outcome immediately (#768)

* Cleanup rcl_get_secure_root() implementation (#762)

* Add fault injection macros to rcl functions (#727)

* Yield rcl_context_fini() error codes (#763)

* Do not invalidate context before successful shutdown (#761)

* Zero initialize guard condition on failed init (#760)

* Adding tests to arguments API (#752)

* Extend rcl_expand_topic_name() API test coverage (#758)

* Add coverage tests 94% to service API (#756)

* Clean up rcl_expand_topic_name() implementation (#757)

* Complete rcl enclave validation API coverage (#751)

* Cope with base function restrictions in mocks (#753)

* Fix allocation when copying arguments (#748)

* Complete rcl package's logging API test coverage (#747)

* Improve coverage to 95% in domain id, init option, rmw
  implementation id and log level modules (#744)

* Fix rcl package's logging API error code documentation and handling
  (#746)

* Fix bug error handling in get_param_files (#743)

* Complete subscription API test coverage (#734)

* increase timeouts in test_services fixtures for Connext (#745)

* Tweaks to client.c and subscription.c for cleaner init/fini (#728)

* Improve error checking and handling in subscription APIs (#739)

* Add deallocate calls to free strdup allocated memory (#737)

* Add missing calls to rcl_convert_rmw_ret_to_rcl_ret (#738)

* Add mock tests, publisher 95% coverage (#732)

* Restore env variables set in the test_failing_configuration. (#733)

* Expose qos setting for /rosout (#722)

* Reformat rmw_impl_id_check to call a testable function (#725)

* Add extra check for invalid event implementation (#726)

* Consolidate macro duplication (#653)

* Add test for subscription message lost event (#705)

* Add function rcl_event_is_valid (#720)

* Move actual domain id from node to context (#718)

* Removed doxygen warnings (#712)

* Remove some dead code.

* Make sure to call rcl_arguments_fini at the end of the test.

* Add remap needed null check (#711)

* Make public init/fini rosout publisher (#704)

* Move rcl_remap_copy to public header (#709)

* Implement a generic way to change logging levels (#664)

* Remove domain_id and localhost_only from node_options (#708)

* Add coverage tests (#703)

* Add bad arguments tests for coverage (#698)

* Remove unused internal prototypes (#699)

* Update quality declaration and coverage (#674)

* Add setter and getter for domain_id in rcl_init_options_t (#678)

* Remove unused pytest dependency from rcl. (#695)

* Fix link to latest API docs (#692)

* Keep domain id if ROS_DOMAIN_ID is invalid. (#689)

* Remove unused check context.c (#691)

* Add check rcl_node_options_copy invalid out (#671)

* Update tracetools' QL to 2 in rcl's QD (#690)

* Improve subscription coverage (#681)

* Improve rcl timer test coverage (#680)

* Improve wait sets test coverage (#683)

* Improve rcl init test coverage. (#684)

* Improve clock test coverage. (#685)

* Add message lost event (#673)

* Minor fixes to rcl clock implementation. (#688)

* Improve enclave validation test coverage. (#682)

* Use RCL_RET_* codes only. (#686)

* Fixed doxygen warnings (#677)

* Add tests for rcl package (#668)

* Remove logging_external_interface.h, provided by
  rcl_logging_interface package now (#676)

* Print RCL_LOCALHOST_ENV_VAR if error happens via rcutils_get_env.
  (#672)

* Contributors: Ada-King, Alejandro Hernández Cordero, Ananya
  Muddukrishna, Andrea Sorbini, Audrow Nash, Barry Xu, Chen Lihui,
  Chris Lalancette, Christophe Bedard, Dan Rose, Dirk Thomas, Geoffrey
  Biggs, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Lei Liu,
  Michel Hidalgo, Nikolai Morin, Scott K Logan, Stephen Brawner, Thijs
  Raymakers, brawner, shonigmann, tomoya

rcl_action
==========

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#909)

* Don't expect RCL_RET_TIMEOUT to set an error string (#900)

* Add support for rmw_connextdds (#895)

* Avoid setting error message twice. (#887)

* Address various clang static analysis fixes (#864)

* Update QDs to QL 1 (#866)

* Update QL (#858)

* Make sure to always check return values (#840)

* Update deprecated gtest macros (#818)

* Make sure to check the return value of rcl APIs. (#838)

* Update maintainers (#825)

* Store reference to rcl_clock_t instead of copy (#797)

* Use valid clock in case of issue in rcl_timer_init (#795)

* Add fault injection macros and unit tests to rcl_action (#730)

* Change some EXPECT_EQ to ASSERT_EQ in test_action_server. (#759)

* Removed doxygen warnings (#712)

* Address issue 716 by zero initializing pointers and freeing memory
  (#717)

* Update quality declaration and coverage (#674)

* Fixed doxygen warnings (#677)

* Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Audrow
  Nash, Chen Lihui, Chris Lalancette, Ivan Santiago Paunovic, Shane
  Loretz, Stephen Brawner, brawner, shonigmann

rcl_interfaces
==============

* Change index.ros.org -> docs.ros.org. (#122)

* Updating Quality Declaration (#120)

* Add field to the parameter description to specify dynamic/static
  typing. (#118)

* Update quality declaration to QL 1. (#116)

* Update package maintainers. (#112)

* Increase Quality level of packages to 3 (#108)

* Add Security Vulnerability Policy pointing to REP-2006. (#106)

* Updating QD to reflect package versions (#107)

* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel
  Hidalgo, Stephen Brawner, brawner, shonigmann

rcl_lifecycle
=============

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#909)

* make rcl_lifecycle_com_interface optional in lifecycle nodes (#882)

* Update QDs to QL 1 (#866)

* Update QL (#858)

* Make sure to always check return values (#840)

* Update tracetools QL and add to rcl_lifecycle's QD (#845)

* Add compiler warnings (#830)

* Make sure to check the return value of rcl APIs. (#838)
