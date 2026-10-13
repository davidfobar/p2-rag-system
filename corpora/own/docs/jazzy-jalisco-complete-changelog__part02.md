# Jazzy Jalisco changelog (part 2 of 5)

* Improve launch file parsing error messages (#626)

* Contributors: Chris Lalancette, Matthew Elwin, Timon Engelke

libcurl_vendor
==============

* Add "lib" to the Windows curl search path. (#96) (#97) In CMake 3.3,
  a commit made it so that the find_package module in CMake had a
  compatibility mode where it would automatically search for packages
  in a <prefix>/lib subdirectory. In CMake 3.6, this compatibility
  mode was reverted for all platforms *except* Windows. That means
  that since CMake 3.3, we haven't actually been using the path as
  specified in "curl_DIR", but we have instead been inadvertently
  relying on that fallback behavior. In CMake 3.28, that compatibilty
  mode was also removed for Windows, meaning that we are now failing
  to find_package(curl) in downstream packages (like
  resource_retriever). Fix this by adding in the "lib" directory that
  always should have been there. I'll note that this *only* affects
  our Windows builds, because this code is in a if(WIN32) block.
  (cherry picked from commit 1839d583190eb9dcf339eaaf6bebe632d94664a6)
  Co-authored-by: Chris Lalancette <clalancette@gmail.com>

* Switch to ament_cmake_vendor_package (#86)

* Contributors: Scott K Logan, mergify[bot]

liblz4_vendor
=============

* Make sure to build_export_depend liblz4-dev. (#1614)

* Switch to using ament_vendor_package for lz4. (#1583)

* Contributors: Chris Lalancette

libstatistics_collector
=======================

* Bump pascalgn/automerge-action from 0.16.2 to 0.16.3

* Bump codecov/codecov-action from 4.1.1 to 4.2.0

* Fixes for newer uncrustify. (#186)

* Bump actions/upload-artifact from 3 to 4

* Switch to using target_link_libraries everywhere. (#174)

* Bump rolling to 1.6.3 (#173)

* Bump actions/checkout from 3 to 4 (#169)

* Add API to use message_info instead unserialized message (#170)

* Bump codecov/codecov-action from 3.1.3 to 3.1.4

* Bump actions/checkout from 3 to 4 (#169)

* Add API to use message_info instead unserialized message (#170)

* Bump codecov/codecov-action from 3.1.3 to 3.1.4

* Add in missing cstdint include. (#165)

* Bump codecov/codecov-action from 3.1.2 to 3.1.3

* Contributors: Chris Lalancette, Lucas Wendland, Michael Orlov,
  dependabot[bot]

libyaml_vendor
==============

* Update quality declaration documents (#62)

* remove rcpputils and rcutils dependency (#61)

* Set to C++17. (#59)

* Switch to ament_cmake_vendor_package (#58)

* Contributors: Chris Lalancette, Christophe Bedard, Kenta Yonekura,
  Scott K Logan

lifecycle
=========

* A few uncrustify fixes for 0.78. (#667)

* Update maintainer list in package.xml files (#665)

* Migrate std::bind calls to lambda expressions (#659)

* Switch to using RCLCPP logging macros in the lifecycle package.
  (#644)

* Contributors: Chris Lalancette, Felipe Gomes de Melo, Michael
  Jeronimo

lifecycle_py
============

* Update maintainer list in package.xml files (#665)

* Contributors: Michael Jeronimo

logging_demo
============

* Update maintainer list in package.xml files (#665)

* Migrate std::bind calls to lambda expressions (#659)

* Contributors: Felipe Gomes de Melo, Michael Jeronimo

lttngpy
=======

* Replace all occurences of index.ros.org (#114)

* Fixes for newer uncrustify (#101)

* Fix Python not being found for lttngpy in Windows debug mode (#87)

* Switch to custom lttng-ctl Python bindings (#81)

* Contributors: Chris Lalancette, Christophe Bedard

map_msgs
========

* Update maintainer list in package.xml files

* Update to C++17

* Contributors: Chris Lalancette, Michael Jeronimo, Steve Macenski

mcap_vendor
===========

* Switch to using ament_vendor_package for lz4. (#1583)

* Switch to target_link_libraries everywhere. (#1504)

* Update mcap to v1.1.0 (#1361)

* Contributors: Chris Lalancette, Emerson Knapp

message_filters
===============

* Update TimeSynchronizer usage example. (#115)

* Remove 'using' keyword in message_filters (#106)

* Remove the use of ament_target_dependencies. (#105)

* Fixes pointed out by clang (#104)

* Mark subscription cb parameter const (#103)

* Update the HasHeader check to be more specific. (#101)

* TypeAdapters support (#95) (#96)

* Cleanup a few minor things in the filters. (#100)

* Fix python examples (#99)

* feat: add signal time functions to ExactTime policy (#94)

* Contributors: Chris Lalancette, Patrick Roncagliolo, Ricardo de
  Azambuja, Russ, rkeating-planted

mimick_vendor
=============

* Bump vendored mimick version for ros2/Mimick#32 (#35)

* Update to the commit that fixes mmk_noreturn. (#34)

* Update to the commit the fixes exe stack on macOS. (#33)

* Update to the comment that fixes the executable stack. (#32)

* Update to take advantage of TARGET_ARCH (#28)

* Switch to ament_cmake_vendor_package (#31)

* Contributors: Chris Lalancette, Michael Carroll, Scott K Logan

nav_msgs
========

* Removed TODO (#243)

* Clarify the license. (#241) In particular, every package in this
  repository is Apache 2.0 licensed except for sensor_msgs_py. So
  move the CONTRIBUTING.md and LICENSE files down into the individual
  packages, and make sure that sensor_msgs_py has the correct
  CONTRIBUTING.md file (it already had the correct LICENSE file).

* Contributors: Alejandro Hernández Cordero, Chris Lalancette

orocos_kdl_vendor
=================

* Ensure that orocos_kdl_vendor doesn't accidentally find itself.
  (#27) (#28) When initially building the orocos_kdl_vendor package
  (on platforms where it actually builds), it turns out that it places
  a valid cmake configuration in the build directory. In turn, that
  means that a subsequent rebuild will find this configuration in the
  build directory, and throw the rest of the logic off. This only
  seems to be a problem with CMake 3.29 and later, though I can't say
  exactly why at the moment. Workaround this problem by writing the
  configuration out to a temporary file, and then moving it into the
  final place with the final name. (cherry picked from commit
  7aad6d1ad9fa54f3a48f1f194a85127e362c8ade) Co-authored-by: Chris
  Lalancette <clalancette@gmail.com>

* Update to the latest orocos_kdl_kinematics commit. (#25)

* Switch to ament_cmake_vendor_package (#20)

* Contributors: Chris Lalancette, Scott K Logan, mergify[bot]

osrf_pycommon
=============

* Catch all of the spurious warnings from get_event_loop. (#94)

* Add bookworm as a python3 target (#91)

* Suppress warning for specifically handled behavior (#87)

* Update supported platforms (#93)

* Add GitHub Actions CI workflow (#88)

* Contributors: Chris Lalancette, Scott K Logan, Tully Foote

osrf_testing_tools_cpp
======================

* Upgrade to Google test 1.14.0 (#84)

* Contributors: Chris Lalancette

pendulum_control
================

* Update maintainer list in package.xml files (#665)

* [pendulum_control Install targets to project lib (#624)

* Contributors: Michael Jeronimo, Yadu

pendulum_msgs
=============

* Update maintainer list in package.xml files (#665)

* Contributors: Michael Jeronimo

pluginlib
=========

* Switch from rcpputils::fs to std::filesystem (#254)

* Remove redundant throw of a std::runtime_error (#232)

* Update to C++17 (#251)

* Fix wShadow compile warning (#250)

* Contributors: Chris Lalancette, Christophe Bedard, Hunter L. Allen,
  Steve Macenski

pybind11_vendor
===============

* Update to pybind11 2.11.1 (#28)

* Add Apache 2.0 LICENSE file (#27)

* Switch to ament_cmake_vendor_package (#24)

* Contributors: Chris Lalancette, Michael Carroll, Scott K Logan

python_cmake_module
===================

* Use FindPython3 instead of FindPythonInterp (#7)

* Contributors: Shane Loretz

python_orocos_kdl_vendor
========================

* Update to the latest orocos_kdl_kinematics commit. (#25)

* Contributors: Chris Lalancette

python_qt_binding
=================

* Suppress warning from Shiboken2. (backport #137) (#138) Co-authored-
  by: Chris Lalancette <clalancette@gmail.com> Co-authored-by:
  Alejandro Hernández Cordero <ahcorde@gmail.com>

* Switch to C++17 for SIP and Shiboken (#135)

* Set hints to find the python version we actually want. (#134)

* Remove unnecessary parentheses around assert. (#133)

* Switch to FindPython3 in the shiboken_helper.cmake. (#132)

* Cleanup of the sip_configure.py file. (#131)

* Update the SIP support so we can deal with a broken RHEL-9. (#129)

* Contributors: Chris Lalancette, Christophe Bedard, mergify[bot]

qt_dotgraph
===========

* Handle empty dotcode nodes. (#290)

* Small fix for modern flake8. (#289)

* Contributors: Chris Lalancette

qt_gui
======

* Remove unnecessary parentheses for assert. (#286)

* (qt_gui) extended theme logic to get icons (#279)

* Contributors: Chris Lalancette, Matthijs van der Burgh

qt_gui_cpp
==========

* Switch from rcpputils::fs to std::filesystem (#288)

* Set hints to find the python version we actually want. (#287)

* Update to C++17 (#278)

* fix unload warning (#274)

* Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard

quality_of_service_demo_cpp
===========================

* Update maintainer list in package.xml files (#665)

* Explicit time conversion (#657)

* Cleanup the interactive quality of service demos. (#637)

* More quality of service demo cleanup (#632)

* Fix small typos in the incompatible_qos demos. (#629)

* Contributors: AiVerisimilitude, Chris Lalancette, Michael Jeronimo

quality_of_service_demo_py
==========================

* Update maintainer list in package.xml files (#665)

* More quality of service demo cleanup (#632)

* Fix small typos in the incompatible_qos demos. (#629)

* Fix the quality_of_service_demo_py output to look like the C++ one.
  (#626)

* Use non-deprecated rclpy import. (#615)

* Contributors: Chris Lalancette, Michael Jeronimo

rcl
===

* Fix up rmw_cyclonedds timestamp testing. (#1156) (#1157) We are
  about to fix it so that rmw_cyclonedds has receive_timestamp
  support, so we also need to enable that support here in rcl. We
  actually rewrite the logic a bit because now the only combination
  that doesn't work is rmw_connextdds on Windows. (cherry picked from
  commit 6d53d24a863c3e9e4a41e9fe5f550271210d9d9d) Co-authored-by:
  Chris Lalancette <clalancette@gmail.com>

* Fixed warnings - strict-prototypes (#1148) (#1150)

* chore: Minor style improvements (#1147) Co-authored-by: Janosch
  Machowinski <J.Machowinski@cellumation.com>

* improved rcl_wait in the area of timeout computation and spurious
  wakeups (#1146) Added special handling for timers with a clock that
  has time override enabled. For these timer we should not compute a
  timeout, as the waitset is waken up by the associated guard
  condition. Before this change, the waitset could wait up, because of
  an expected ready timer, that was acutally not ready, as the time
  update to the ROS_TIME had not yet arrived.

* Add tracepoint for publish_serialized_publish (#1136) * Add
  tracepoint for publish_serialized_publish * Add: tracepoint for
  rcl_take_serialized_message ---------

* Revert "improved rcl_wait in the area of timeout computation and
  spurious wakeups (#1135)" (#1142) This reverts commit
  3c6c5dc47dac23d70722a60b2c0a387d2e71b71d.

* improved rcl_wait in the area of timeout computation and spurious
  wakeups (#1135) * feat: Allow usage of rcl_timer_clock with const
  rcl_timer_t* * fix: Fixed purious wake-ups on ROS_TIME timers with
  ROS_TIME enabled Added special handling for timers with a clock that
  has time override enabled. For theses timer we should not compute a
  timeout, as the waitset is waken up by the associated guard
  condition. Before this change, the waitset could wait up, because of
  an expected ready timer, that was acutally not ready, as the time
  update to the ROS_TIME had not yet arrived. * feat: Added
  rcl_timer_get_next_call_time * fix(rcl_wait): Improved timeout
  computation in case of many timers This commit changes the
  computation of the timer timeout, to be more precise, in the case,
  of many registered timers. --------- Co-authored-by: Janosch
  Machowinski <j.machowinski@nospam.org>

* Generate version header using ament_generate_version_header(..)
  (#1141)

* Add rcl_timer_call_with_info function that retrieves the expected
  and the actual timer trigger times (#1113) Co-authored-by: Alexis
  Tsogias <a.tsogias@cellumation.com> Co-authored-by: Michael Carroll
  <carroll.michael@gmail.com> Co-authored-by: Tomoya Fujita
  <Tomoya.Fujita@sony.com>

* document out parameters for rcl_get_node_names and
  rcl_get_node_names_with_enclaves (#1137) * document out params for
  rcl_get_node_names Co-authored-by: Chris Lalancette
  <clalancette@gmail.com>

* Cleanups for uncrustify 0.78. (#1134) Mostly this is expanding
  macros, as this is just easier to read anyway. But we also mark one
  section as INDENT-OFF.

* Re-order rcl_logging_interface include (#1133)

* Remove unnecessary macros. (#1132) These really don't add anything,
  and allows us to avoid some changes in macro formatting between
  Ubuntu 22.04 and Ubuntu 24.04.

* Update quality declaration documents (#1131)

* add unit tests for --log-file-name argument. (#1130)

* support "--log-file-name" to ros args. (#1127)

* Make sure to disable a test_node test on RHEL. (#1124)

* remove static function rcl_ret_from_rcutils_ret(). (#1122)

* Remove AMENT_DEPENDENCIES from rcl_add_custom_gtest. (#1119)

* Remove unncecessary dependencies in tests (#1114)

* a rosout publisher of a node might not exist (#1115)

* Set disable loan to on by default. (#1110)

* Return service from node_type_description_service_init (#1112)

* next_call_time will always be greater than now after calling
  rcl_timer_call. (#1089)

* Add rcl count clients, servicec & tests (#1011)

* Improve the reliability of test_get_type_description_service.
  (#1107)

* Remove most remaining uses of ament_target_dependencies. (#1102)

* Just remove rcpputils::fs dependency (#1105)

* Decouple rosout publisher init from node init. (#1065)

* Cleanup the error handling in rcl_node_init. (#1099)

* Fix a clang warning for suspicious string concatentation. (#1101)

* add the link to the topic name rules. (#1100)

* Cut down the amount of time for test_logging_rosout. (#1098)

* Simplify local_namespace handling in rcl_node_init. (#1097)

* Reduce the number of tests we run (#1096)

* Adding duplicate node information (#1088)

* Revamp the test_get_type_description_service. (#1095)

* Cleanup network flow endpoints test. (#1094)

* Reduce the failure timeout time for namespaces. (#1093)

* Shorten wait time for a subscription not being ready. (#1092)

* rcl_send_response returns RCL_RET_TIMEOUT. (#1048)

* Move test_namespace into the correct directory. (#1087)

* Reset errors in tests to reduce warnings (#1085)

* Cleanup error reporting in the type hash code. (#1084)

* Instrument loaned message publication code path (#1083)

* Add "~/get_type_description" service (rep2011) (#1052)

* Modifies timers API to select autostart state (#1004)

* test publisher/subscription with the c/cpp typesupport for
  test_msgs::msg::array (#1074)

* validation result should be used to print the error message. (#1077)

* improve error msg of "rcl_expand_topic_name" (#1076)

* Use TRACETOOLS_ prefix for tracepoint-related macros (#1058)

* fix comment (#1073)

* localhost_only prevails auto discovery options if enabled. (#1069)

* Avoid dynamic allocation of message before sending over rosout
  (#1067)

* clarify "rcl_node_init" return code (#1066)

* Fix a format-security warning when building with clang. (#1064)

* Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard,
  Christopher Wecht, Eloy Briceno, Eric W, Felix Penzlin, G.A. vd.
  Hoorn, Hans-Joachim Krauch, Kenta Yonekura, Lee, Lucas Wendland,
  Michael Carroll, Minju, Thiemo Kohrt, Tomoya Fujita, h-suzuki-isp,
  jmachowinski, mergify[bot]

rcl_action
==========

* Generate version header using ament_generate_version_header(..)
  (#1141)

* add RCL_RET_TIMEOUT to action service response. (#1138) * add
  RCL_RET_TIMEOUT to action service response. * address review
  comment. ---------

* Update quality declaration documents (#1131)

* Remove most remaining uses of ament_target_dependencies. (#1102)

* Add "~/get_type_description" service (rep2011) (#1052)

* Modifies timers API to select autostart state (#1004)

* Contributors: Chris Lalancette, Christophe Bedard, Eloy Briceno,
  G.A. vd. Hoorn, Hans-Joachim Krauch, Tomoya Fujita

rcl_interfaces
==============

* Update the Log.msg constant types. (#161)

* Update the comments for SetParametersResult to reflect reality.
  (#159)

* Contributors: Chris Lalancette

rcl_lifecycle
=============

* Fixed warnings - strict-prototypes (#1148) (#1150)

* Generate version header using ament_generate_version_header(..)
  (#1141)

* Update quality declaration documents (#1131)

* Remove most remaining uses of ament_target_dependencies. (#1102)

* Use TRACETOOLS_ prefix for tracepoint-related macros (#1058)

* Contributors: Chris Lalancette, Christophe Bedard, G.A. vd. Hoorn,
  mergify[bot]

rcl_logging_interface
=====================

* Check allocator validity in some rcl_logging functions (#116) If the
  allocator is zero-initialized, it may cause a segfault when it is
  used later in the functions.

* Use (void) in declaration of param-less function (#114)

* add file_name_prefix parameter to external log configuration. (#109)

* Migrate to std::filesystem (#104)

* Remove the last uses of ament_target_dependencies in this repo.
  (#102)

* Contributors: Chris Lalancette, Christophe Bedard, Kenta Yonekura,
  Scott K Logan, Tomoya Fujita

rcl_logging_noop
================

* add file_name_prefix parameter to external log configuration. (#109)

* Remove the last uses of ament_target_dependencies in this repo.
  (#102)

* Contributors: Chris Lalancette, Tomoya Fujita

rcl_logging_spdlog
==================

* Check allocator validity in some rcl_logging functions (#116) If the
  allocator is zero-initialized, it may cause a segfault when it is
  used later in the functions.

* Cleanup the tests. (#115) * Cleanup the tests. There are a few
  different fixes in here: 1. Move away from using "popen" to get the
  list of files in a directory. Instead, switch to using the C++
  std::filesystem directory iterator and doing the work ourselves,
  which is portable and much less error-prone. 2. Set the ROS_LOG_DIR
  for all of the tests in here. This should make the test resistant
  to being run in parallel with other tests. 3. Consistently use
  rcpputils::set_env_var, rather than a mix of rcpputils and rcutils.

* Update quality declaration document (#112)

* Re-order rcl_logging_interface include (#111)

* add file_name_prefix parameter to external log configuration. (#109)

* Migrate to std::filesystem (#104)

* Remove the last uses of ament_target_dependencies in this repo.
  (#102)

* Contributors: Chris Lalancette, Christophe Bedard, Kenta Yonekura,
  Scott K Logan, Tomoya Fujita

rcl_yaml_param_parser
=====================

* Generate version header using ament_generate_version_header(..)
  (#1141)

* Update quality declaration documents (#1131)

* Fix for incorrect integer value conversion on Windows (#1126)

* Just remove rcpputils::fs dependency (#1105)

* Contributors: Christophe Bedard, G.A. vd. Hoorn, Kenta Yonekura,
  Michael Orlov

rclcpp
======

* add impl pointer for ExecutorOptions (#2523) (#2525) * add impl
  pointer for ExecutorOptions (cherry picked from commit
  343b29b617b163ad72b9fe3f6441dd4ed3d3af09) Co-authored-by: William
  Woodall <william@osrfoundation.org>

* Fixup Executor::spin_all() regression fix (#2517) (#2521) *
  test(Executors): Added tests for busy waiting Checks if executors
  are busy waiting while they should block in spin_some or spin_all. *
  fix: Reworked spinAll test This test was strange. It looked like, it
  assumed that spin_all did not return instantly. Also it was racy, as
  the thread could terminate instantly. * fix(Executor): Fixed
  spin_all not returning instantly is no work was available * Update
  rclcpp/test/rclcpp/executors/test_executors.cpp * test(executors):
  Added test for busy waiting while calling spin * fix(executor):
  Reset wait_result on every call to spin_some_impl Before, the method
  would not recollect available work in case of spin_some, spin_all.
  This would lead to the method behaving differently than to what the
  documentation states. * restore previous test logic for now *
  refactor spin_some_impl's logic and improve busy wait tests * added
  some more comments about the implementation --------- Co-authored-
  by: Janosch Machowinski <J.Machowinski@cellumation.com> Co-authored-
  by: jmachowinski <jmachowinski@users.noreply.github.com> Co-
  authored-by: Tomoya Fujita <Tomoya.Fujita@sony.com> Co-authored-by:
  William Woodall <william@osrfoundation.org>

* Revise the description of service configure_introspection() (#2511)
  (#2513)

* Remove references to index.ros.org. (#2504)

* Reduce overhead for inheriting from rclcpp::Executor when base
  functionality is not reused (#2506)

* [wjwwood] Updated "Data race fixes" (#2500) * Fix callback group
  logic in executor * fix: Fixed unnecessary copy of wait_set *
  fix(executor): Fixed race conditions with rebuild of wait_sets
  Before this change, the rebuild of wait set would be triggered after
  the wait set was waken up. With bad timing, this could lead to the
  rebuild not happening with multi threaded executor. * fix(Executor):
  Fixed lost of entities rebuild request * chore: Added assert for not
  set callback_group in execute_any_executable * Add test for cbg
  getting reset Co-authored-by: Janosch Machowinski
  <j.machowinski@nospam.org> * chore: renamed test cases to snake_case
  * style * fixup test to avoid polling and short timeouts * fix: Use
  correct notify_waitable_ instance *
  fix(StaticSingleThreadedExecutor): Added missing special case
  handling for current_notify_waitable_ * fix(TestCallbackGroup):
  Fixed test after change to timers --------- Co-authored-by: Janosch
  Machowinski <j.machowinski@cellumation.com> Co-authored-by: Michael
  Carroll <mjcarroll@intrinsic.ai> Co-authored-by: Janosch Machowinski
  <j.machowinski@nospam.org>

* fixup var names to snake case (#2501)

* Added optional TimerInfo to timer callback (#2343) Co-authored-by:
  Alexis Tsogias <a.tsogias@cellumation.com> Co-authored-by: Janosch
  Machowinski <J.Machowinski@cellumation.com>

* Fix uninitialized memory in test (#2498) When I added in the tests
  for large messages, I made a mistake and reserved space in the
  strings, but didn't actually expand it. Thus, we were writing into
  uninitialized memory. Fix this by just using the correct
  constructor for string, which will allocate and initialize the
  memory properly.

* Ensure waitables handle guard condition retriggering (#2483) Co-
  authored-by: Michael Carroll <mjcarroll@intrinsic.ai>

* fix: init concatenated_vector with begin() & end() (#2492) * this
  commit will fix the warning [-Wstringop-overflow=] #2461

* Use the same context for the specified node in rclcpp::spin
  functions (#2433) * Use the same conext for the specified node in
  rclcpp::spin_xx functions * Add test for spinning with non-default-
  context * Format code ---------

* Disable compare-function-pointers in test_utilities (#2489)

* address ambiguous auto variable. (#2481)

* Increase the cppcheck timeout to 1200 seconds (#2484)

* Removed test_timers_manager clang warning (#2479)

* Flaky timer test fix (#2469) * fix(time_source): Fixed possible race
  condition * fix(test_executors_time_cancel_behaviour): Fixed
  multiple race conditions --------- Co-authored-by: Janosch
  Machowinski <j.machowinski@nospam.org>

* Add tracepoint for generic publisher/subscriber (#2448)

* update rclcpp::Waitable API to use references and const (#2467)

* Utilize rclcpp::WaitSet as part of the executors (#2142) * Deprecate
  callback_group call taking context * Add base executor objects that
  can be used by implementors * Template common operations * Address
  reviewer feedback: * Add callback to EntitiesCollector constructor *
  Make function to check automatically added callback groups take a
  list * Lint * Address reviewer feedback and fix templates * Lint and
  docs * Make executor own the notify waitable * Add pending queue to
  collector, remove from waitable Also change node's
  get_guard_condition to return shared_ptr * Change interrupt guard
  condition to shared_ptr Check if guard condition is valid before
  adding it to the waitable * Lint and docs * Utilize rclcpp::WaitSet
  as part of the executors * Don't exchange atomic twice * Fix
  add_node and add more tests * Make get_notify_guard_condition follow
  API tick-tock * Improve callback group tick-tocking * Don't lock
  twice * Address reviewer feedback * Add thread safety annotations
  and make locks consistent * @wip * Reset callback groups for
  multithreaded executor * Avoid many small function calls when
  building executables * Re-trigger guard condition if buffer has data
  * Address reviewer feedback * Trace points * Remove tracepoints *
  Reducing diff * Reduce diff * Uncrustify * Restore tests * Back to
  weak_ptr and reduce test time * reduce diff and lint * Restore
  static single threaded tests that weren't working before * Restore
  more tests * Fix multithreaded test * Fix assert * Fix constructor
  test * Change ready_executables signature back * Don't enforce
  removing callback groups before nodes * Remove the "add_valid_node"
  API * Only notify if the trigger condition is valid * Only trigger
  if valid and needed * Fix spin_some/spin_all implementation *
  Restore single threaded executor * Picking ABI-incompatible executor
  changes * Add PIMPL * Additional waitset prune * Fix bad merge *
  Expand test timeout * Introduce method to clear expired entities
  from a collection * Make sure to call remove_expired_entities(). *
  Prune queued work when callback group is removed * Prune
  subscriptions from dynamic storage * Styles fixes. * Re-trigger
  guard conditions * Condense to just use watiable.take_data * Lint *
  Address reviewer comments (nits) * Lock mutex when copying *
  Refactors to static single threaded based on reviewers * More small
  refactoring * Lint * Lint * Add ready executable accessors to
  WaitResult * Make use of accessors from wait_set * Fix tests * Fix
  more tests * Tidy up single threaded executor implementation * Don't
  null out timer, rely on call * change how timers are checked from
  wait result in executors * peak -> peek * fix bug in next_waitable
  logic * fix bug in StaticSTE that broke the add callback groups to
  executor tests * style --------- Co-authored-by: Chris Lalancette
  <clalancette@gmail.com> Co-authored-by: William Woodall
  <william@osrfoundation.org>

* fix flakiness in TestTimersManager unit-test (#2468) the previous
  version of the test was relying on the assumption that a timer with
  1ms period gets called at least 6 times if the main thread waits
  15ms. this is true most of the times, but it's not guaranteed,
  especially when running the test on windows CI servers. the new
  version of the test makes no assumptions on how much time it takes
  for the timers manager to invoke the timers, but rather focuses on
  ensuring that they are called the right amount of times, which is
  what's important for the purpose of the test

* fix spin_some_max_duration unit-test for events-executor (#2465)

* refactor and improve the parameterized spin_some tests for executors
  (#2460) * refactor and improve the spin_some parameterized tests for
  executors * disable spin_some_max_duration for the
  StaticSingleThreadedExecutor and EventsExecutor * fixup and clarify
  the docstring for Executor::spin_some() * style * review comments
  ---------

* enable simulation clock for timer canceling test. (#2458) * enable
  simulation clock for timer canceling test. * move MainExecutorTypes
  to test_executors_timer_cancel_behavior.cpp. ---------

* Revert "relax the test simulation rate for timer canceling tests.
  (#2453)" (#2456) This reverts commit
  1c350d0d7fb9c7158e0a39057112486ddbd38e9a.

* relax the test simulation rate for timer canceling tests. (#2453)

* Fix TypeAdapted publishing with large messages. (#2443) Mostly by
  ensuring we aren't attempting to store large messages on the stack.
  Also add in tests. I verified that before these changes, the tests
  failed, while after them they succeed.

* Implement generic client (#2358) * Implement generic client * Fix
  the incorrect parameter declaration * Deleted copy constructor and
  assignment for FutureAndRequestId * Update codes after rebase *
  Address review comments * Address review comments from iuhilnehc-
  ynos * Correct an error in a description * Fix window build errors *
  Address review comments from William * Add doc strings to
  create_generic_client ---------

* Rule of five: implement move operators (#2425)

* Various cleanups to deal with uncrustify 0.78. (#2439) These should
  also work with uncrustify 0.72.

* Remove the set_deprecated signatures in any_subscription_callback.
  (#2431) These have been deprecated since April 2021, so it is safe
  to remove them now.
