# Makoa Mata-mata (codename "makoa"; May, 2027)

Makoa Mata-mata (codename "makoa"; May, 2027)
*********************************************

*Makoa Mata-mata* is the thirtienth release of ROS 2. It is a regular
release, and is supported until December 2028.

* TODO - link installation docs

* Makoa Mata-mata Release Timeline

* Makoa Mata-mata Supported Platforms

New Features in Makoa
=====================

TODO

Changes since the Lyrical release
=================================

Removed RMW for Fast DDS with dynamic typesupport
-------------------------------------------------

Package "rmw_fastrtps_dynamic_cpp" has been removed. This means that
users will no longer be able to select
"RMW_IMPLEMENTATION=rmw_fastrtps_dynamic_cpp". Users are encouraged to
use "RMW_IMPLEMENTATION=rmw_fastrtps_cpp" instead.
