# RHEL (binary)

RHEL (binary)
*************

Table of Contents
^^^^^^^^^^^^^^^^^

* System requirements

* System setup

  * Set locale

  * Enable required repositories

  * Install prerequisites

  * Install development tools (optional)

* Install ROS 2

  * Install dependencies using rosdep

  * Install additional RMW implementations (optional)

* Setup environment

* Try some examples

* Next steps

* Troubleshoot

* Uninstall

This page explains how to install ROS 2 on RHEL from a pre-built
binary package.

Note:

  The pre-built binary does not include all ROS 2 packages. All
  packages in the ROS base variant are included, and only a subset of
  packages in the ROS desktop variant are included. The exact list of
  packages are described by the repositories listed in this ros2.repos
  file.

There are also RPM packages available.

System requirements
===================

We currently support RHEL 9 64-bit.

System setup
============

Set locale
----------

Make sure you have a locale which supports "UTF-8". If you are in a
minimal environment (such as a docker container), the locale may be
something minimal like "C". We test with the following settings.
However, it should be fine if you're using a different UTF-8 supported
locale.

   $ locale # check for UTF-8

   $ sudo dnf install langpacks-en glibc-langpack-en
   $ export LANG=en_US.UTF-8

   $ locale # verify settings

Enable required repositories
----------------------------

The rosdep database contains packages from the EPEL and PowerTools
repositories, which are not enabled by default. They can be enabled by
running:

   $ sudo dnf install 'dnf-command(config-manager)' epel-release -y
   $ sudo dnf config-manager --set-enabled crb

Note:

  This step may be slightly different depending on the distribution
  you are using. Check the EPEL documentation

Install prerequisites
---------------------

There are a few packages that must be installed in order to get and
unpack the binary release.

   $ sudo dnf install tar bzip2 wget -y

Install development tools (optional)
------------------------------------

If you are going to build ROS packages or otherwise do development,
you can also install the development tools:

   $ sudo dnf install -y \
     cmake \
     gcc-c++ \
     git \
     make \
     patch \
     python3-colcon-common-extensions \
     python3-mypy \
     python3-pip \
     python3-pydocstyle \
     python3-pytest \
     python3-pytest-repeat \
     python3-pytest-rerunfailures \
     python3-rosdep \
     python3-setuptools \
     python3-vcstool \
     wget

   ~ install some pip packages needed for testing and
   ~ not available as RPMs
   $ python3 -m pip install -U --user \
     flake8-blind-except==0.1.1 \
     flake8-class-newline \
     flake8-deprecated

Install ROS 2
=============

* Go to the releases page

* Download the latest package for RHEL; let's assume that it ends up
  at "~/Downloads/ros2-package-linux-x86_64.tar.bz2".

  * Note: there may be more than one binary download option which
    might cause the file name to differ.

* Unpack it:

     $ mkdir -p ~/ros2_rolling
     $ cd ~/ros2_rolling
     $ tar xf ~/Downloads/ros2-package-linux-x86_64.tar.bz2

Install dependencies using rosdep
---------------------------------

ROS 2 packages are built on frequently updated RHEL systems. It is
always recommended that you ensure your system is up to date before
installing new packages.

   $ sudo dnf update

   $ sudo rosdep init
   $ rosdep update
   $ rosdep install --from-paths ~/ros2_rolling/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps iceoryx_binding_c rti-connext-dds-6.0.1 urdfdom_headers"

Install additional RMW implementations (optional)
-------------------------------------------------

The default middleware that ROS 2 uses is "Fast DDS", but the
middleware (RMW) can be replaced at runtime. See the guide on how to
work with multiple RMWs.

Setup environment
=================

Set up your environment by sourcing the following file.

   $ . ~/ros2_rolling/ros2-linux/setup.bash

Note:

  Replace ".bash" with your shell if you're not using bash. Possible
  values are: "setup.bash", "setup.sh", "setup.zsh".

Try some examples
=================

In one terminal, source the setup file and then run a C++ "talker":

   $ . ~/ros2_rolling/ros2-linux/setup.bash
   $ ros2 run demo_nodes_cpp talker

In another terminal source the setup file and then run a Python
"listener":

   $ . ~/ros2_rolling/ros2-linux/setup.bash
   $ ros2 run demo_nodes_py listener

You should see the "talker" saying that it's "Publishing" messages and
the "listener" saying "I heard" those messages. This verifies both the
C++ and Python APIs are working properly. Hooray!

Next steps
==========

Continue with the tutorials and demos to configure your environment,
create your own workspace and packages, and learn ROS 2 core concepts.

Troubleshoot
============

Troubleshooting techniques can be found here.

Uninstall
=========

1. If you installed your workspace with colcon as instructed above,
   "uninstalling" could be just a matter of opening a new terminal and
   not sourcing the workspace's "setup" file. This way, your
   environment will behave as though there is no Rolling install on
   your system.

2. If you're also trying to free up space, you can delete the entire
   workspace directory with:

      $ rm -rf ~/ros2_rolling
