# Migrating Parameters

Migrating Parameters
********************

Table of Contents
^^^^^^^^^^^^^^^^^

* Global Parameter Server

* Migrating YAML Parameter Files

  * YAML file example

  * Feature parity

* Parameter Atomic Operation

In ROS 1, parameters are associated with a central server that allowed
retrieving parameters at runtime through the use of the network APIs.
In ROS 2, parameters are associated per node and are configurable at
runtime with ROS services.

* See ROS 2 Parameter design document for more details about the
  system model.

* See ROS 2 CLI usage for a better understanding of how the CLI tools
  work and its differences with ROS 1 tooling.

Global Parameter Server
=======================

In ROS 1, the "roscore" acted like a global parameter blackboard where
all nodes could get and set parameters. Since there is no central
"roscore" in ROS 2, that functionality no longer exists. The
recommended approach in ROS 2 is to use per-node parameters that are
closely tied to the nodes that use them. If a global blackboard is
still needed, it is possible to create a dedicated node for this
purpose. ROS 2 ships with one in the "ros-rolling-demo-nodes-cpp"
package called "parameter_blackboard"; it can be run with:

   $ ros2 run demo_nodes_cpp parameter_blackboard

The code for the "parameter_blackboard" is here.

Migrating YAML Parameter Files
==============================

This guide describes how to adapt ROS 1 parameters files for ROS 2.

YAML file example
-----------------

YAML is used to write parameters files in both ROS 1 and ROS 2. The
main difference in ROS 2 is that node names must be used to address
parameters. In addition to the fully qualified node name, we use the
key "ros__parameters" to signal the start of parameters for the node.

For example, here is a parameters file in ROS 1:

   lidar_name: foo
   lidar_id: 10
   ports: [11312, 11311, 21311]
   debug: true

Let's assume that the first two parameters are for a node named
"/lidar_ns/lidar_node_name", the next parameter is for a node named
"/imu", and the last parameter we want to set on both nodes.

We would construct our ROS 2 parameters file as follows:

   /lidar_ns:
     lidar_node_name:
       ros__parameters:
         lidar_name: foo
         id: 10
   imu:
     ros__parameters:
       ports: [2438, 2439, 2440]
   /**:
     ros__parameters:
       debug: true

Note the use of wildcards ("/**") to indicate that the parameter
"debug" should be set on any node in any namespace.

Feature parity
--------------

Some features of ROS 1 parameters files do not exist in ROS 2:

* Mixed types in a list is not supported yet (related issue)

* "deg" and "rad" substitutions are not supported

Parameter Atomic Operation
==========================

When migrating parameter groups from ROS 1 to ROS 2, there are
important differences to consider. In ROS 1, "dynamic_reconfigure"
handles parameter groups atomically, meaning all parameters in a
reconfiguration request are processed together in a single callback.
In ROS 2, the "set_parameters" service processes each parameter
individually, which may lead to multiple callback invocations. To
maintain atomic behavior when migrating from "dynamic_reconfigure",
use the "set_parameters_atomically" service, which validates and
applies all parameters as a single operation. If any parameter fails
validation, no parameters will be updated.
