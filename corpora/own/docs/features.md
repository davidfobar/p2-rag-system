# Features Status

Features Status
***************

The features listed below are available in the current ROS 2 release.
Unless otherwise specified, the features are available for all
supported platforms (Ubuntu 24.04 (Noble), Windows 10), DDS
implementations (eProsima Fast DDS, RTI Connext DDS, and Eclipse
Cyclone DDS) and programming language client libraries (C++ and
Python). For planned future development, see the Roadmap.

+-----------------------------------+-----------------------------------+-----------------------------------+
| Functionality | Link | Fine print |
|===================================|===================================|===================================|
| Discovery, transport and | Article | |
| serialization over DDS | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Support for multiple DDS | Concept, How-to Guide | Currently Eclipse Cyclone DDS, |
| implementations, chosen at | | eProsima Fast DDS, and RTI |
| runtime | | Connext DDS are fully supported. |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Common core client library that | Details | |
| is wrapped by language-specific | | |
| libraries | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Publish/subscribe over topics | Sample code, Article | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Clients and services | Sample code | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Set/retrieve parameters | Sample code | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| ROS 1 - ROS 2 communication | Tutorial | Available for topics and |
| bridge | | services, not yet available for |
| | | actions. |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Quality of service settings for | Demo | |
| handling non-ideal networks | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Inter- and intra-process | Demo | Currently only in C++. |
| communication using the same API | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Composition of node components at | Demo | Currently only in C++. |
| compile, link, load, or run time | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Multiple executors (at level of | Demo | Only in C++. |
| callback groups) in same node | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Support for nodes with managed | Demo | Currently only in C++. |
| lifecycles | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| DDS-Security support | Demo | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Command-line introspection tools | Concept | |
| using an extensible framework | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Launch system for coordinating | Tutorial | |
| multiple nodes | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Namespace support for nodes and | Article | |
| topics | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Static remapping of ROS names | How-to Guide | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Demos of an all-ROS 2 mobile | Demo | |
| robot | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Preliminary support for real-time | Demo, demo | Linux only. Not available for |
| code | | Fast RTPS. |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Preliminary support for "bare- | Wiki | |
| metal" microcontrollers | | |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Content filtering subscription | Demo | Currently only in C++. |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Service Introspection | Demo | |
+-----------------------------------+-----------------------------------+-----------------------------------+

Besides core features of the platform, the biggest impact of ROS comes
from its available packages. The following are a few high-profile
packages which are available in the latest release:

* gazebo_ros_pkgs

* image_transport

* navigation2

* rosbag2

* RQt

* RViz2
