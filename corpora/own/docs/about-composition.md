# Composition

Composition
***********

Table of Contents
^^^^^^^^^^^^^^^^^

* ROS 1 - Nodes vs. Nodelets

* ROS 2 - Unified API

* Component Container

* Writing a Component

* CMake Registration Macros

  * "rclcpp_components_register_node"

  * "rclcpp_components_register_nodes"

* Using Components

* Practical application

ROS 1 - Nodes vs. Nodelets
==========================

In ROS 1 you can write your code either as a ROS node or as a ROS
nodelet. ROS 1 nodes are compiled into executables. ROS 1 nodelets on
the other hand are compiled into a shared library which is then loaded
at runtime by a container process.

ROS 2 - Unified API
===================

In ROS 2 the recommended way of writing your code is similar to a
nodelet - we call it a "Component". This makes it easy to add common
concepts to existing code, like a life cycle. Having different APIs,
which was the biggest drawback in ROS 1, is avoided in ROS 2 since
both approaches use the same API.

Note:

  It is still possible to use the node-like style of "writing your own
  main" but for the common case it is not recommended.

By making the process layout a deploy-time decision the user can
choose between:

* running multiple nodes in separate processes with the benefits of
  process/fault isolation as well as easier debugging of individual
  nodes and

* running multiple nodes in a single process with the lower overhead
  and optionally more efficient communication (see Intra Process
  Communication).

Additionally "ros2 launch" can be used to automate these actions
through specialized launch actions.

Component Container
===================

A component container is a host process that allows you to load and
manage multiple components at runtime within the same process space.

As of now, the following generic component container types are
available:

* component_container

  * The most generic component container that uses a single
    "SingleThreadedExecutor" to execute all components.

* component_container_mt

  * Component container that uses a single "MultiThreadedExecutor" to
    execute the components.

* component_container_isolated

  * Component container that uses a dedicated executor for each
    component: either "SingleThreadedExecutor" (default) or
    "MultiThreadedExecutor".

For more information about the types of executors, see the Types of
Executors. For more information about the options of each component
container, see Component container types in the composition tutorial.

Writing a Component
===================

Since a component is only built into a shared library, it doesn't have
a "main" function (see Talker source code). A component is commonly a
subclass of "rclcpp::Node". Since it is not in control of the thread,
it shouldn't perform any long running or blocking tasks in its
constructor. Instead, it can use timers to get periodic notifications.
Additionally, it can create publishers, subscriptions, servers, and
clients.

An important aspect of making such a class a component is that the
class registers itself using macros from the package
"rclcpp_components" (see the last line in the source code). This makes
the component discoverable when its library is being loaded into a
running process - it acts as kind of an entry point.

Additionally, once a component is created, it must be registered with
the index to be discoverable by the tooling.

   add_library(talker_component SHARED src/talker_component.cpp)
   rclcpp_components_register_nodes(talker_component "composition::Talker")
   # To register multiple components in the same shared library, use multiple calls
   # rclcpp_components_register_nodes(talker_component "composition::Talker2")

For an example, check out this tutorial

Note:

  In order for the component_container to be able to find desired
  components, it must be executed or launched from a shell that has
  sourced the corresponding workspace.

CMake Registration Macros
=========================

ROS 2 provides two CMake macros for registering components, each
serving a different purpose:

"rclcpp_components_register_node"
---------------------------------

This macro registers a component and generates a standalone
executable. Use this when you want both composability and the ability
to run the node as a standalone process.

   add_library(talker_component SHARED src/talker_component.cpp)
   rclcpp_components_register_node(talker_component
     PLUGIN "composition::Talker"
     EXECUTABLE talker)

"rclcpp_components_register_nodes"
----------------------------------

This macro registers one or more components for runtime composition
**without** creating standalone executables. Use this when you want
pure component libraries that will be loaded into component containers
at runtime.

   add_library(talker_component SHARED src/talker_component.cpp)
   rclcpp_components_register_nodes(talker_component "composition::Talker")

Using Components
================

The composition package contains a couple of different approaches on
how to use components. The three most common ones are:

1. Start a (generic container process) and call the ROS service
   load_node offered by the container. The ROS service will then load
   the component specified by the passed package name and library name
   and start executing it within the running process. Instead of
   calling the ROS service programmatically you can also use a command
   line tool to invoke the ROS service with the passed command line
   arguments

2. Create a custom executable containing multiple nodes which are
   known at compile time. This approach requires that each component
   has a header file (which is not strictly needed for the first
   case).

3. Create a launch file and use "ros2 launch" to create a container
   process with multiple components loaded.

Practical application
=====================

Try the Composition demos.
