# RHEL (RPM packages)

RHEL (RPM packages)
*******************

Table of Contents
^^^^^^^^^^^^^^^^^

* Resources

* System setup

  * Set locale

  * Enable required repositories

  * Install development tools (optional)

* Install ROS 2

  * Install additional RMW implementations (optional)

* Setup environment

* Try some examples

* Next steps

* Troubleshoot

* Uninstall

RPM packages for ROS 2 Rolling Ridley are currently available for RHEL
9. The target platforms are defined in REP 2000.

Resources
=========

* Status Page:

  * ROS 2 Rolling (RHEL 9): amd64

* Jenkins Instance

* Repositories

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

You will need to enable the EPEL repositories and the PowerTools
repository:

   $ sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E %rhel).noarch.rpm
   $ sudo env FORCE_DNF=1 crb enable

Note:

  This step may be slightly different depending on the distribution
  you are using. Check the EPEL documentation

Next, download the "ros2-release" package and install it:

   $ sudo dnf install curl
   $ export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
   $ sudo dnf install "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-release-${ROS_APT_SOURCE_VERSION}-1.noarch.rpm"

The ros2-release package provides keys and repo configuration for the
various ROS repositories. Updates to repository configuration will
occur automatically when new versions of this package are released to
the ROS repositories.

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
     python3-flake8-blind-except \
     python3-flake8-class-newline \
     python3-flake8-deprecated \
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

Install ROS 2
=============

ROS 2 packages are built on frequently updated RHEL systems. It is
always recommended that you ensure your system is up to date before
installing new packages.

   $ sudo dnf update

Desktop Install (Recommended): ROS, RViz, demos, tutorials.

   $ sudo dnf install ros-rolling-desktop

ROS-Base Install (Bare Bones): Communication libraries, message
packages, command line tools. No GUI tools.

   $ sudo dnf install ros-rolling-ros-base

Install additional RMW implementations (optional)
-------------------------------------------------

The default middleware that ROS 2 uses is "Fast DDS", but the
middleware (RMW) can be replaced at runtime. See the guide on how to
work with multiple RMWs.

Setup environment
=================

Set up your environment by sourcing the following file.

   $ source /opt/ros/rolling/setup.bash

Note:

  Replace ".bash" with your shell if you're not using console.
  Possible values are: "setup.bash", "setup.sh", "setup.zsh".

Try some examples
=================

If you installed "ros-rolling-desktop" above you can try some
examples.

In one terminal, source the setup file and then run a C++ "talker":

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_cpp talker

In another terminal source the setup file and then run a Python
"listener":

   $ source /opt/ros/rolling/setup.bash
   $ ros2 run demo_nodes_py listener

You should see the "talker" saying that it's "Publishing" messages and
the "listener" saying "I heard" those messages. This verifies both the
C++ and Python APIs are working properly. Hooray!

If you want to use other RMW implementations, you can check the guide.

Next steps
==========

Continue with the tutorials and demos to configure your environment,
create your own workspace and packages, and learn ROS 2 core concepts.

Troubleshoot
============

Troubleshooting techniques can be found here.

Uninstall
=========

If you need to uninstall ROS 2 or switch to a source-based install
once you have already installed from binaries, run the following
command:

   $ sudo dnf remove ros-rolling-*

To remove the repository configuration run

   $ sudo dnf remove ros2-release
