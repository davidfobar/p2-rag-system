# Ubuntu (deb packages)

Ubuntu (deb packages)
*********************

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

Deb packages for ROS 2 Rolling Ridley are currently available for
Ubuntu Noble (24.04). The target platforms are defined in REP 2000.

Resources
=========

* Status Page:

  * ROS 2 Rolling (Ubuntu Noble 24.04): amd64, arm64

* Jenkins Instance

* Repositories

System setup
============

Set locale
----------

Make sure you have a locale which supports "UTF-8". If you are in a
minimal environment (such as a docker container), the locale may be
something minimal like "POSIX". We test with the following settings.
However, it should be fine if you're using a different UTF-8 supported
locale.

   $ locale # check for UTF-8

   $ sudo apt update && sudo apt install locales
   $ sudo locale-gen en_US en_US.UTF-8
   $ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
   $ export LANG=en_US.UTF-8

   $ locale # verify settings

Enable required repositories
----------------------------

You will need to add the ROS 2 apt repository to your system.

First ensure that the Ubuntu Universe repository is enabled.

   $ sudo apt install software-properties-common
   $ sudo add-apt-repository universe

The ros-apt-source packages provide keys and apt source configuration
for the various ROS repositories.

Installing the ros2-apt-source package will configure ROS 2
repositories for your system. Updates to repository configuration will
occur automatically when new versions of this package are released to
the ROS repositories.

   $ sudo apt update && sudo apt install curl -y
   $ export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
   $ curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
   $ sudo dpkg -i /tmp/ros2-apt-source.deb

Install development tools (optional)
------------------------------------

If you are going to build ROS packages or otherwise do development,
you can also install the development tools:

Warning:

  On Ubuntu 24.04 installs your apt sources may only include the base
  "noble" suite. This can cause dependency conflicts when installing
  "ros-dev-tools".Check "/etc/apt/sources.list.d/ubuntu.sources" and
  ensure the "Suites:" line includes "noble-updates" and "noble-
  backports":

     $ grep Suites /etc/apt/sources.list.d/ubuntu.sources

  If "noble-updates" or "noble-backports" are missing then edit the
  file and update the line to:

     Suites: noble noble-updates noble-backports

  Then run:

     $ sudo apt clean && sudo apt update && sudo apt full-upgrade -y

   $ sudo apt update && sudo apt install ros-dev-tools

Install ROS 2
=============

Update your apt repository caches after setting up the repositories.

   $ sudo apt update

ROS 2 packages are built on frequently updated Ubuntu systems. It is
always recommended that you ensure your system is up to date before
installing new packages.

   $ sudo apt upgrade

Desktop Install (Recommended): ROS, RViz, demos, tutorials.

   $ sudo apt install ros-rolling-desktop

ROS-Base Install (Bare Bones): Communication libraries, message
packages, command line tools. No GUI tools.

   $ sudo apt install ros-rolling-ros-base

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

  Replace ".bash" with your shell if you're not using bash. Possible
  values are: "setup.bash", "setup.sh", "setup.zsh".

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

   $ sudo apt remove '~nros-rolling-*' && sudo apt autoremove

You may also want to remove the repository:

   $ sudo apt remove ros2-apt-source
   $ sudo apt update
   $ sudo apt autoremove
   $ sudo apt upgrade # Consider upgrading for packages previously shadowed.

How to I install an older version of a distro?
   Use the snapshot repository.
