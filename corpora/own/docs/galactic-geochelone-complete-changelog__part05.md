# Galactic Geochelone changelog (part 5 of 8)

* skip test relying on source timestamps with Connext (#615)

* Use the rpyutils shared import_c_library function. (#610)

* Add ability to configure domain ID (#596)

* Use absolute parameter events topic name (#612)

* Destroy event handlers owned by publishers/subscriptions when
  calling publisher.destroy()/subscription.destroy() (#603)

* Default incompatible qos callback should be set when there's no user
  specified callback (#601)

* relax rate jitter test for individual periods (#602)

* add QoSProfile.__str__ (#593)

* Add useful debug info when trying to publish the wrong type (#581)

* Pass rcutils_include_dirs to cppcheck (#577)

* wrap lines to shorten line length (#586)

* fix moved troubleshooting url (#579)

* improve error message if rclpy C extensions are not found (#580)

* Add message lost subscription event (#572)

* Fix executor behavior on shutdown (#574)

* Add missing rcutils/macros.h header (#573)

* Add "topic_name" property to Subscription (#571)

* Add "topic_name" property to publisher (#568)

* Fix and document rclpy_handle_get_pointer_from_capsule() (#569)

* Fix docstrings (#566)

* Contributors: Addisu Z. Taddese, Alejandro Hernández Cordero, Andrea
  Sorbini, Audrow, Audrow Nash, Barry Xu, Chris Lalancette, Claire
  Wang, Dereck Wonnacott, Dirk Thomas, Emerson Knapp, Greg Balke,
  Gökçe Aydos, Ivan Santiago Paunovic, Jacob Perron, Loy, Michel
  Hidalgo, Scott K Logan, Shane Loretz, Tomoya Fujita, Tully Foote,
  Zhen Ju, ksuszka, ssumoo, tomoya

rcpputils
=========

* Update quality declaration links (#130)

* Add functions for getting library path and filename (#128)

* Add path equality operators (#127)

* Add create_temp_directory filesystem helper (#126)

* Use new noexcept specifier. (#123)

* Add stream operator for paths to make it easier to log (#120)

* Path join operator is const (#119)

* No windows.h in header files (#118)

* Fix rcpputils::SharedLibrary tests. (#117)

* Update QD to QL 1 (#114)

* Make sure to not try to index into an empty path. (#113)

* Fix working with filesystem parent paths. (#112)

* Cleanup mislabeled BSD license (#37)

* overload functions for has_symbol and get_symbol with raw string
  literal (#110)

* Add an ASSERT to the pointer traits tests. (#111)

* replace custom get env login into rcutils_get_env(). (#99)

* Removed Github Actions (#105)

* Update the package.xml files with the latest Open Robotics
  maintainers (#102)

* Make sure that an existing path is a directory for
  create_directories (#98)

* Transfer ownership to Open Robotics (#100)

* Ensure -fPIC is used when building a static lib (#93)

* Removed doxygen warnings (#86) (#87)

* Add clamp header (#85)

* Removed doxygen warnings (#86)

* Split get_env_var() into header and implementation (#83)

* Add cstring include for strcmp (#81)

* filesystem helpers: adding remove_all to remove non-empty
  directories (#79)

* Add scope_exit helper (#78)

* Bump setup-ros to 0.0.23, action-ros-lint to 0.0.6, action-ros-ci to
  0.0.17 (#77)

* Fix parent_path() for empty paths and paths of length one (#73)

* Add get_executable_name() function (#70)

* Address memory leak in remove pointer test (#72)

* Add current_path to filesystem_helpers (#63)

* Align path combine behavior with C++17 (#68)

* Update quality declaration to QL 2 (#71)

* Contributors: Alejandro Hernández Cordero, Chen Lihui, Chris
  Lalancette, Christophe Bedard, Devin Bonnie, Dirk Thomas, Emerson
  Knapp, Hunter L. Allen, Ivan Santiago Paunovic, Jacob Perron,
  Karsten Knese, Louise Poubel, Michael Jeronimo, Michel Hidalgo,
  Nikolai Morin, Scott K Logan, Simon Honigmann, Stephen Brawner,
  Tully Foote, Victor Lopez, William Woodall, tomoya

rcutils
=======

* Declare dependency on libatomic (#338)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#335)

* Quiet down a warning in release mode. (#334)

* Make the logging separate char an implementation detail. (#332)

* Performance tests demo (#288)

* Remove references of __xstat (#330)

* Update the documentation to be more consistent. (#331)

* Shorten some excessively long lines of CMake (#328)

* qnx-support: include sys/link.h & avoid using dlinfo (#327)

* QNX uses XSI-compliant (#326)

* Add an API for directory iteration (#323)

* Fix a leak during error handling in dir size calculation (#324)

* Fix rcutils_shared_library_t path on Windows. (#322)

* Check linker flags instead of assuming compiler correlation. (#321)

* Improve shared library relative paths handling (#320)

* Update rcutils_calculate_directory_size() to support recursion
  (#306)

* Updating QD to QL 1 (#317)

* Address unused return values found in scan-build (#316)

* use one copy for continuous area instead of loop copy (#312)

* use a better way to check whether string is empty (#315)

* Use helper funciton to copy string (#314)

* Disable a Windows platform warning. (#311)

* Fix format of code description on document (#313)

* Make sure to check the return values of rcutils APIs. (#302)

* Add rcutils_expand_user() to expand user directory in path (#298)

* Update the maintainers. (#299)

* Remove the temporary variable in RCUTILS_LOGGING_AUTOINIT (#290)

* Add RCUTILS_NO_FAULT_INJECTION() macro. (#295)

* Inject faults on rcutils_get_env() and rcutils_set_env() call.
  (#292)

* env.h and get_env.h docblock fixes (#291)

* Introduce rcutils_strcasecmp, case insensitive string compare.
  (#280)

* Stop using fprintf to avoid using file handles by changing as few
  lines of code as possible. (#289)

* Defines QNX implementation for rcutils_get_platform_library_name
  (#287)

* Add RCUTILS_CAN_SET_ERROR_MSG_AND_RETURN_WITH_ERROR_OF() macro.
  (#284) To fault inject error messages as well as return codes.

* Change rcutils_fault_injection_set_count to use int64_t (#283)

* adds QNX support for rcutils_get_executable_name (#282)

* Add fault injection hooks to default allocator (#277)

* Fault injection macros and functionality (plus example) (#264)

* ensure -fPIC is used when building a static lib (#276)

* Drop vsnprintf mocks entirely. (#275) Binary API is not portable
  across platforms and compilation config.

* Fix vsnprintf mocks for Release builds. (#274)

* Improve test coverage mocking system calls (#272)

* Use mimick/mimick.h header (#273)

* Add mock test for rcutils/strerror (#265)

* Add compiler option -Wconversion and add explicit casts for
  conversions that may alter the value or change the sign (#263) See
  https://github.com/ros2/rcutils/pull/263#issuecomment-663252537.

* Removed doxygen warnings (#266) (#268)

* Removed doxygen warnings (#266)

* Force _GNU_SOURCE if glibc is used. (#267)

* Add parenthesis around the argument in time conversion macros
  defined in time.h (#261)

* Add token join macros (#262)

* Add rcutils_string_array_sort function (#248)

* Add rcutils_string_array_resize function (#247)

* Increase testing coverage of rcutils to 95% (#258)

* Update QUALITY_DECLARATION to reflect QL 2 status (#260)

* Update version stability section of quality declaration for 1.0
  (#256)

* Contributors: Ahmed Sobhy, Alejandro Hernández Cordero, Barry Xu,
  Chen Lihui, Chris Lalancette, Christophe Bedard, Dirk Thomas, Felix
  Endres, Homalozoa X, Ivan Santiago Paunovic, Johannes Meyer, Jorge
  Perez, Karsten Knese, Michel Hidalgo, Scott K Logan, Stephen
  Brawner, Steven! Ragnarök, brawner, shonigmann, tomoya

resource_retriever
==================

* Throw exception if package name is empty (#54)

* Update maintainers (#53)

* Add .hpp header and deprecate .h (#51)

* Add pytest.ini so local tests don't display warning (#48)

* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob
  Perron, Shane Loretz

rmw
===

* Document which QoS policies are correctly read by
  rmw_get_publishers/subscriptions_info_by_topic (#308)

* Unique network flows (#294)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#307)

* Introduce RMW_DURATION_INFINITE constant and API return value
  promise (#301)

* Add declaration for function to check QoS profile compatibility
  (#299)

* Update the rmw_take_sequence documentation. (#297)

* Update rmw QD to QL 1 (#289)

* Extend rmw_qos_policy_kind_t, add functions to convert it to/from a
  string (#285)

* Add functions to convert between qos policy values and strings
  (#284)

* Update maintainers (#282)

* Update service request/response API documentation (#279)

* Update rmw_get_serialized_message_size docblock (#281)

* Update rmw_service_server_is_available doc (#280)

* Update wait and wait sets' API documentation (#275)

* Update graph API documentation (#272)

* Update service server/client creation/destruction API documentation.
  (#276)

* Update rmw_*_*_allocation return values (#278)

* Update gid API documentation (#274)

* Do not link against pthread on Android (#267)

* Update taking API documentation (#271)

* Update publishing API documentation (#270)

* Add fault injection macros for use in other packages (#254)

* Add bad_alloc return to topic_endpoint_info functions (#269)

* Update publisher/subscription matched count API documentation (#262)

* Update publisher/subscription QoS query API documentation (#263)

* Extend rmw_serialized_message_t tests (#261)

* Update serialization/deserialization API documentation (#258)

* Update subscription API documentation (#256)

* Update publisher creation/destruction API documentation (#252)

* Add actual domain id to rmw_context_t (#251)

* Update node creation/destruction API documentation. (#249)

* Correct parameter names to match documentation (#250)

* Remove domain_id and localhost_only from node API (#248)

* Require enclave upon rmw_init() call. (#247)

* Update init/shutdown API documentation. (#243)

* Update init options API documentation. (#244)

* Add message lost subscription event (#232)

* Move statuses definitions to rmw/events_statuses/*.h (#232)

* Increase rmw testing coverage above 95% (#238)

* Handle zero-length names_and_types properly (#239)

* Add missing RMW_PUBLIC to security_options_set_root_path (#236)

* Update Quality Declaration for QL 2 (#233)

* Add Security Vulnerability Policy pointing to REP-2006. (#230)

* Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna,
  Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Ivan Santiago
  Paunovic, Jacob Perron, Karsten Knese, Michel Hidalgo, Scott K
  Logan, Stephen Brawner, brawner, shonigmann

rmw_connextdds
==============

* Use rmw_qos_profile_unknown when adding entity to graph (#28)

* Resolve issues identified while investigating #21 (#22)

* Use Rolling in README's Quick Start

* Improved implementation of client::is_service_available for Connext
  Pro

* Only add request header to typecode with Basic req/rep profile

* Remove commented/unused code

* Avoid topic name validation in get_info functions

* Reduce shutdown period to 10ms

* Pass HistoryQosPolicy to graph cache

* Reset error string after looking up type support

* Remove DDS-based WaitSet implementation

* Merge pull request #13 from Ericsson/unique_network_flows

* Refactor common API

* Update branch "master" to support Rolling only (#15)

* Add ability to override of endpoint qos settings based on topic
  name.

* Optimize QoS for reliable large data.

* Only trigger data condition if samples were loaned from reader.

* Alternative WaitSet implementation based on C++ std, selectable at
  compile-time.

* Add "<buildtool_export_depend>" for "ament_cmake".

* Use default "dds.transport.UDPv4.builtin.ignore_loopback_interface".

* Renamed environment variables
  ("RMW_CONNEXT_USE_DEFAULT_PUBLISH_MODE",
  "RMW_CONNEXT_LEGACY_RMW_COMPATIBILITY_MODE").

* Support a list of initial peers via "RMW_CONNEXT_INITIAL_PEERS".

* Initial release.

* Contributors: Ananya Muddukrishna, Andrea Sorbini, Ivan Santiago
  Paunovic, William Woodall

rmw_connextdds_common
=====================

* Correctly detect empty messages (#33)

* Use rmw_qos_profile_unknown when adding entity to graph (#28)

* Resolve issues identified while investigating #21 (#22)

* Use Rolling in README's Quick Start

* Improved implementation of client::is_service_available for Connext
  Pro

* Only add request header to typecode with Basic req/rep profile

* Remove commented/unused code

* Avoid topic name validation in get_info functions

* Reduce shutdown period to 10ms

* Pass HistoryQosPolicy to graph cache

* Reset error string after looking up type support

* Remove DDS-based WaitSet implementation

* Merge pull request #13 from Ericsson/unique_network_flows

* Remove superfluous header inclusion

* Remove conflicting linkage

* Further remove feature-based exclusion

* Remove feature-based exclusion

* Uncrustify

* Refactor common API

* Include required headers if feature is enabled

* Add conditional compilation support

* Prefer more generic file name

* Restrict unique flow endpoint check to versions beyond Foxy

* Indicate missing support for unique network flows

* Update branch "master" to support Rolling only (#15)

* Add ability to override of endpoint qos settings based on topic name
  (Pro).

* Optimize QoS for reliable large data (Pro).

* Only trigger data condition if samples were loaned from reader.

* Alternative WaitSet implementation based on C++ std, selectable at
  compile-time.

* Add "<buildtool_export_depend>" for "ament_cmake".

* Use default "dds.transport.UDPv4.builtin.ignore_loopback_interface".

* Don't log an error on WaitSet::wait() timeout.

* Initial release.

* Contributors: Ananya Muddukrishna, Andrea Sorbini, Ivan Santiago
  Paunovic, William Woodall

rmw_connextddsmicro
===================

* Use rmw_qos_profile_unknown when adding entity to graph (#28)

* Resolve issues identified while investigating #21 (#22)

* Use Rolling in README's Quick Start

* Remove commented/unused code

* Avoid topic name validation in get_info functions

* Pass HistoryQosPolicy to graph cache

* Reset error string after looking up type support

* Remove DDS-based WaitSet implementation

* Merge pull request #13 from Ericsson/unique_network_flows

* Refactor common API

* Update branch "master" to support Rolling only (#15)

* Only trigger data condition if samples were loaned from reader.

* Alternative WaitSet implementation based on C++ std, selectable at
  compile-time.

* Add "<buildtool_export_depend>" for "ament_cmake".

* Initial release.

* Contributors: Ananya Muddukrishna, Andrea Sorbini, Ivan Santiago
  Paunovic, William Woodall

rmw_cyclonedds_cpp
==================

* Fix the history depth for KEEP_ALL. (#305)

* Use the macros from Cyclone DDS to work with sample payload when
  using SHM (#300)

* Add loaned sample zero-copy API support (#297)

* Indicate missing support for unique network flows (#282)

* Take and return new RMW_DURATION_INFINITE correctly (#288)

* Add RMW function to check QoS compatibility (#286)

* Fix use-after-free in error handling bug

* Drop compatibility with ancient cyclone versions

* Update to use Cyclone's renamed ddsi_sertype

* Use init-on-first-use for global state (#275)

* Make sure to reset the error when a typesupport can't be found.

* Switch to using the generic functions for the typesupport handles.

* Handle typesupport errors on fetch. (#271)

* Handle potential divide by 0 (#267)

* Fix incorrect log message(rmw_fastrtps_shared_cpp ->
  rmw_cylonedds_cpp) (#260)

* Update maintainers (#254)

* Change wrong use of %ld to print std::size_t to %zu

* Return RMW_RET_UNSUPPORTED in rmw_get_serialized_message_size (#250)

* Update service/client request/response API error returns (#249)

* Updated publisher/subscription allocation and wait set API return
  codes (#246)

* Fix array "get_function" semantics (#248)

* Update service/client construction/destruction API return codes.
  (#247)

* Update gid API return codes. (#244)

* Update graph API return codes. (#243)

* Check for message_info on take where appropriate. (#245) Fix for
  regression introduced in #241.

* Updated error returns on rmw_take_serialized() and
  rmw_take_with_message_info() (#242)

* Updated error returns on rmw_take() (#241)

* Add quality declaration for Cyclone DDS (#218)

* Fix that not to delete some objects after destroying functions
  (#236)

* Update rmw_publish_serialized_message() error returns (#240)

* Update rmw_publish() error returns (#239)

* Remove public declarations (#230)

* Use quotes for non-system includes (#231)

* Use correct functions to resize and get an item, avoiding memory
  leaks in typesupport code (#228)

* Fix context cleanup. (#227)

* Fix memory leak that type support not deleted. (#225)

* Ensure compliant matched pub/sub count API. (#223)

* Fix memory leak that string not deleted. (#224)

* Change RET_WRONG_IMPLID() to return RMW_RET_INCORRECT_IMPLEMENTATION
  (#226)

* Fix bad conditional in rmw_serialize(). (#217)

* Ensure compliant subscription API. (#214)

* Ensure compliant publisher API (#210)

* rmw_destroy_node must remove node from graph cache (#213)

* Add space between 'ROS' and '2' (#195)

* Set context actual domain id (#208)

* Ensure compliant node construction/destruction API (#206)

* Remove domain_id and localhost_only from node API (#205)

* Amend rmw_init() implementation: require enclave. (#204)

* Ensure compliant init/shutdown API implementations. (#202)

* Ensure compliant init options API implementations. (#200)

* Finalize context iff shutdown. (#196)

* Handle RMW_DEFAULT_DOMAIN_ID. (#194)

* Add support to message lost event (#192)

* Mitigate lost service responses discovery issue (#187)

* Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna, Chen
  Lihui, Chris Lalancette, Christophe Bedard, Dan Rose, Emerson Knapp,
  Erik Boasson, Ivan Santiago Paunovic, Jacob Perron, Joe Speed, Jose
  Tomas Lorente, Lobotuerk, Michel Hidalgo, Scott K Logan, Stephen
  Brawner, Sumanth Nirmal, Sven Brinkmann, eboasson, pluris

rmw_dds_common
==============

* Fix one more instance of index.ros.org. (#49)

* updating quality declaration links (re: ros2/docs.ros2.org#52) (#46)

* Add function for checking QoS profile compatibility (#45)

* Shorten some excessively long lines of CMake (#44)

* Fix test_graph_cache ASAN errors (#41) (#42)

* Update QD to QL 1 (#38)

* Create a utility function to limit rmw_time_t to 32-bit values (#37)

* Update maintainers (#34)

* Updated performance section QD (#30)

* Update Quality Declaration to QL2 (#31)

* Added benchmark test to rmw_dds_common (#29)

* Fix potential memory leak (#28)

* Add fault injection macro unit tests (#27)

* Fixed some doxygen warnings (#26)

* Update Quality Declaration to QL3 (#24)

* Update QD and documentation (#23)

* Contributors: Alejandro Hernández Cordero, Chen Lihui, Chris
  Lalancette, Ivan Santiago Paunovic, Jacob Perron, Michael Jeronimo,
  Michel Hidalgo, Scott K Logan, Stephen Brawner, shonigmann, y
  -okumura-isp

rmw_fastrtps_cpp
================

* Refactor to use DDS standard API (#518)

* Unique network flows (#502)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#520)

* Add RMW function to check QoS compatibility (#511)

* Capture cdr exceptions (#505)

* Load profiles based on topic names (#335)

* Set rmw_dds_common::GraphCache callback after init succeeds. (#496)

* Handle typesupport errors on fetch. (#495)

* Check for correct context shutdown (#486)

* New environment variable to change easily the publication mode
  (#470)

* Discriminate when the Client has gone from when the Client has not
  completely matched (#467) * Workaround when the client is gone
  before server sends response * Change add to the map to listener
  callback

* Update the package.xml files with the latest Open Robotics
  maintainers (#459)

* Update Quality Declarations and READMEs (#455) * Add QD links for
  dependencies to rmw_fastrtps_cpp QD * Provide external dependencies
  QD links * Update rmw_fastrtps README to use Fast DDS * Update
  rmw_fastrtps_cpp QD: Fast DDS & unit test * Update README
  rmw_fastrtps_cpp to QL2

* Perform fault injection in all creation/destruction APIs. (#453)

* Ensure rmw_destroy_node() completes despite run-time errors. (#458)

* Update rmw_fastrtps_cpp and rmw_fastrtps_shared_cpp QDs to QL2.
  (#456)

* Return RMW_RET_UNSUPPORTED in rmw_get_serialized_message_size (#452)

* Updated publisher/subscription allocation and wait set API return
  codes (#443)

* Added rmw_logging tests (#442)

* Make service/client construction/destruction implementation
  compliant (#445)

* Make sure type can be unregistered successfully (#437)

* Add tests for native entity getters. (#439)

* Avoid deadlock if graph update fails. (#438)

* Call Domain::removePublisher while failure occurs in
  create_publisher (#434)

* Ensure compliant matched pub/sub count API. (#424)

* Ensure compliant publisher QoS queries. (#425)

* Ensure compliant subscription API. (#419)

* Ensure compliant publisher API. (#414)

* Set context actual domain id (#410)

* Ensure compliant node construction/destruction API. (#408)

* Remove domain_id and localhost_only from node API (#407)

* Amend rmw_init() implementation: require enclave. (#406)

* Update Quality Declarations to QL3. (#404)

* Ensure compliant init/shutdown API implementation. (#401)

* Update Quality Declaration to QL3. (#403)

* Finalize context iff shutdown. (#396)

* Make service wait for response reader (#390)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Eduardo Ponz
  Segrelles, Ignacio Montesino Valle, Ivan Santiago Paunovic,
  JLBuenoLopez-eProsima, Jacob Perron, Jaime Martin Losa, José Luis
  Bueno López, Michael Jeronimo, Michel Hidalgo, Miguel Company,
  shonigmann

rmw_fastrtps_dynamic_cpp
========================

* Refactor to use DDS standard API (#518)

* Unique network flows (#502)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#520)

* Add RMW function to check QoS compatibility (#511)

* Capture cdr exceptions (#505)

* Load profiles based on topic names in rmw_fastrtps_dynamic_cpp
  (#497)

* Set rmw_dds_common::GraphCache callback after init succeeds. (#496)

* Handle typesupport errors on fetch. (#495)

* Check for correct context shutdown (#486)

* New environment variable to change easily the publication mode
  (#470)

* Discriminate when the Client has gone from when the Client has not
  completely matched (#467) * Workaround when the client is gone
  before server sends response * Change add to the map to listener
  callback

* Update the package.xml files with the latest Open Robotics
  maintainers (#459)

* Update Quality Declarations and READMEs (#455) * Add QL of external
  dependencies to rmw_fastrtps_dynamic_cpp QD * Add QD links for
  dependencies to rmw_fastrtps_dynamic_cpp QD * Provide external
  dependencies QD links * Add README to rmw_fastrtps_dynamic * Add QD
  for rmw_fastrtps_dynamic

* Ensure rmw_destroy_node() completes despite run-time errors. (#458)

* Return RMW_RET_UNSUPPORTED in rmw_get_serialized_message_size (#452)

* Updated publisher/subscription allocation and wait set API return
  codes (#443)

* Added rmw_logging tests (#442)

* Fix array "get_function" semantics (#448)

* Make service/client construction/destruction implementation
  compliant (#445)

* Make sure type can be unregistered successfully (#437)

* Add tests for native entity getters. (#439)

* Avoid deadlock if graph update fails. (#438)

* Call Domain::removePublisher while failure occurs in
  create_publisher (#434)

* Avoid memory leaks and undefined behavior in
  rmw_fastrtps_dynamic_cpp typesupport code (#429)

* Ensure compliant matched pub/sub count API. (#424)

* Ensure compliant publisher QoS queries. (#425)

* Ensure compliant subscription API. (#419)

* Ensure compliant publisher API. (#414)

* Set context actual domain id (#410)

* Ensure compliant node construction/destruction API. (#408)

* Remove domain_id and localhost_only from node API (#407)

* Amend rmw_init() implementation: require enclave. (#406)

* Ensure compliant init/shutdown API implementation. (#401)

* Finalize context iff shutdown. (#396)

* Make service wait for response reader (#390)

* Contributors: Alejandro Hernández Cordero, Barry Xu, Eduardo Ponz
  Segrelles, Ignacio Montesino Valle, Ivan Santiago Paunovic,
  JLBuenoLopez-eProsima, Jacob Perron, Jaime Martin Losa, José Luis
  Bueno López, Michael Jeronimo, Michel Hidalgo, Miguel Company,
  shonigmann

rmw_fastrtps_shared_cpp
=======================

* Refactor to use DDS standard API (#518)

* Unique network flows (#502)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#520)

* Take and return new RMW_DURATION_INFINITE correctly (#515)

* Add RMW function to check QoS compatibility (#511)

* Capture cdr exceptions (#505)

* Make sure to lock the mutex protecting client_endpoints_. (#492)

* Use interface whitelist for localhost only (#476)

* Make use of error return value in decrement_context_impl_ref_count
  (#488)

* Remove unnecessary includes (#487)

* Use new time_utils function to limit rmw_time_t values to 32-bits
  (#485)

* New environment variable to change easily the publication mode
  (#470)

* Remove unused headers MessageTypeSupport.hpp and
  ServiceTypeSupport.hpp (#481)

* Discriminate when the Client has gone from when the Client has not
  completely matched (#467) * Workaround when the client is gone
  before server sends response * Change add to the map to listener
  callback

* Update the package.xml files with the latest Open Robotics
  maintainers (#459)

* Update Quality Declarations and READMEs (#455) * Add QD links for
  dependencies to rmw_fastrtps_shared_cpp QD. * Provide external
  dependencies QD links. * Update rmw_fastrtps_shared_cpp QD: Fast DDS
  * Update README rmw_fastrtps_shared_cpp to QL2

* Perform fault injection in all creation/destruction APIs. (#453)

* Ensure rmw_destroy_node() completes despite run-time errors. (#458)

* Handle too large QoS queue depths. (#457)

* Update rmw_fastrtps_cpp and rmw_fastrtps_shared_cpp QDs to QL2.
  (#456)

* checked client implementation and return
  RMW_RET_INCORRECT_RMW_IMPLEMENTATION (#451)

* Update service/client request/response API error returns (#450)

* Updated publisher/subscription allocation and wait set API return
  codes (#443)

* Added rmw_logging tests (#442)

* Add tests for RMW QoS to DDS attribute conversion. (#449)

* Make service/client construction/destruction implementation
  compliant (#445)

* Inject faults on __rmw_publish() and run_listener_thread() call.
  (#441)

* Update gid API return codes. (#440)

* Update graph API return codes. (#436)

* Update rmw_take_serialized() and rmw_take_with_message_info() error
  returns (#435)

* Update rmw_take() error returns (#432)

* Update rmw_publish() error returns (#430)

* Update rmw_publish_serialized_message() error returns (#431)

* Improve __rmw_create_wait_set() implementation. (#427)

* Ensure compliant matched pub/sub count API. (#424)

* Ensure compliant publisher QoS queries. (#425)

* Fix memory leak that wait_set might be not destoryed in some case.
  (#423)

* Avoid unused identifier variable warnings. (#422)

* Fix trying to get topic data that was already removed. (#417)

* Ensure compliant subscription API. (#419)

* Use package path to TypeSupport.hpp headers in ServiceTypeSupport
  and MessageTypeSupport (#415) Use package in path to TypeSupport
  header for ServiceTypeSupport/MessageTypeSupport

* Ensure compliant publisher API. (#414)

* Set context actual domain id (#410)

* Add missing thread-safety annotation in ServicePubListener (#409)

* Ensure compliant node construction/destruction API. (#408)

* Update Quality Declarations to QL3. (#404)

* Do not use string literals as implementation identifiers in tests.
  (#402)

* Ensure compliant init options API implementations. (#399)

* Finalize context iff shutdown. (#396)

* Handle RMW_DEFAULT_DOMAIN_ID. (#394)

* Make service wait for response reader (#390)

* Contributors: Alejandro Hernández Cordero, Chen Lihui, Chris
  Lalancette, Emerson Knapp, Ivan Santiago Paunovic, JLBuenoLopez-
  eProsima, Jacob Perron, Jaime Martin Losa, Jose Luis Rivero, Jose
  Tomas Lorente, José Luis Bueno López, Lobotuerk, Michael Jeronimo,
  Michel Hidalgo, Miguel Company, Stephen Brawner, shonigmann

rmw_implementation
==================

* Unique network flows (#170)

* updating quality declaration links (re: ros2/docs.ros2.org#52)
  (#185)

* Remove rmw_connext_cpp. (#183)

* Add support for rmw_connextdds (#182)

* Add function for checking QoS profile compatibility (#180)

* Shorten some excessively long lines of CMake (#179)

* Add rmw_fastrtps_dynamic_cpp to the explicit group deps (#177)

* Accept any RMW implementation, not just the default (#172)

* Defer path resolution of rmw implementation libraries to dynamic
  linker. (#169)

* Update QD to QL 1 (#166)
