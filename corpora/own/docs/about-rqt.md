# Overview and usage of RQt

Overview and usage of RQt
*************************

Table of Contents
^^^^^^^^^^^^^^^^^

* Overview

* System setup

  * Installing From debs

* RQt Components Structure

* Advantage of RQt framework

* Further Reading

Overview
========

RQt is a graphical user interface framework that implements various
tools and interfaces in the form of plugins. One can run all the
existing GUI tools as dockable windows within RQt. The tools can still
run in a traditional standalone method, but RQt makes it easier to
manage all the various windows in a single screen layout.

You can run any RQt tools/plugins easily by:

   $ rqt

This GUI allows you to choose any available plugins on your system.
You can also run plugins in standalone windows. For example, RQt
Python Console:

   $ ros2 run rqt_py_console rqt_py_console

Users can create their own plugins for RQt with either "Python" or
"C++". To see what RQt plugins are available for your system, run:

   $ ros2 pkg list

And then look for packages that start with "rqt_".

System setup
============

Installing From debs
--------------------

   $ sudo apt install ros-rolling-rqt*

RQt Components Structure
========================

RQt consists of two metapackages:

* *rqt* - core infrastructure modules.

* *rqt_common_plugins* - Commonly useful debugging tools.

Advantage of RQt framework
==========================

Compared to building your own GUIs from scratch:

* Standardized common procedures for GUI (start-shutdown hook, restore
  previous states).

* Multiple widgets can be docked in a single window.

* Easily turn your existing Qt widgets into RQt plugins.

* Expect support at Robotics Stack Exchange (ROS community website for
  the questions).

From system architecture's perspective:

* Support multi-platform (basically wherever QT and ROS run) and
  multi-language ("Python", "C++").

* Manageable lifecycle: RQt plugins using a common API makes
  maintenance & reuse easier.

Further Reading
===============

* ROS 2 Discourse announcement of porting to ROS 2)

* RQt for ROS 1 documentation

* Brief overview of RQt (from a Willow Garage intern blog post)
