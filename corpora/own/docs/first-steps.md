# First steps with ROS - learning path

First steps with ROS - learning path
************************************

ROS (Robot Operating System) is an open-source ecosystem that provides
framework, tools, and libraries for building, deploying, running, and
maintaining robotic applications. This page presents a set of articles
and hands-on activities to introduce the main concepts behind the ROS
framework. Working through these will give you the essential knowledge
needed to start developing applications with ROS.

**Area: ROS-framework | Content-type: learning-path | Experience:
beginner**

Contents
^^^^^^^^

* Summary

* Prerequisites

* Steps

  * 1 Learn about fundamental concepts behind ROS

  * 2 Install ROS and turtlesim

  * 3 Try out working with the main communication components of the
    ROS framework

  * 4 Learn about introspection with logs

  * 5 Learn about using launch files

  * 6 Learn about data recording and playback

* Next steps

Summary
=======

The ROS framework is the “plumbing” which makes communication between
different parts of a robot possible. It includes messaging, standard
interfaces, and support for multiple programming languages and
platforms.

You need to understand the fundamental concepts of the framework
before you can work with ROS to develop or maintain applications. The
turtlesim tool and the tutorials in this site will help you get up to
speed.

Prerequisites
=============

None. The steps outlined in this article will guide you through
downloading and installing everything you need to learn the basics of
ROS.

Steps
=====

1 Learn about fundamental concepts behind ROS
---------------------------------------------

* About ROS

* Nodes

* Interfaces (topics, services, actions)

* Parameters

2 Install ROS and turtlesim
---------------------------

ROS installation includes the essential packages for working with ROS.
If you're familiar with Linux, our recommended platform is Ubuntu (deb
packages). Otherwise, a good alternative installation platform is
Windows (binaries): Installation options

With turtlesim, a lightweight 2D simulation tool designed for
beginners, you can learn core ROS concepts in a simple visual
environment: Install and set up turtlesim

3 Try out working with the main communication components of the ROS framework
-----------------------------------------------------------------------------

Use turtlesim to familiarize yourself with the main communication
components and try out messaging in the ROS framework.

1. Complete the nodes tutorial: Understanding nodes

2. Complete the topics tutorial: Understanding topics

3. Complete the services tutorial: Understanding services

4. Complete the parameters tutorial: Understanding parameters

5. Complete the actions tutorial: Understanding actions

4 Learn about introspection with logs
-------------------------------------

Introspection enables you to see information about how a system is
operating. Nodes use logs to output messages concerning events and
status in a variety of ways.

To see introspection through logs in action, complete the rqt_console
tutorial: Using rqt_console to view logs

5 Learn about using launch files
--------------------------------

Launch files allow you to start and configure a number of processes
containing ROS nodes simultaneously, instead of opening multiple
terminals and re-entering configuration details for each node.

Complete the launch files tutorial: Launching nodes

6 Learn about data recording and playback
-----------------------------------------

Sometimes it's useful to replay data to reproduce the results of your
tests and experiments, to debug your robot's behaviour, or to share
your work with others.

Complete the recording and playback tutorial: Recording and playing
back data

Next steps
==========

To complete your knowledge of the ROS framework, we recommend
familiarizing yourself with ROS client libraries: Beginner: Client
libraries
