# ROS 2 on Raspberry Pi

ROS 2 on Raspberry Pi
*********************

ROS 2 is supported on both 32 bit (arm32) and 64 bit (arm64) ARM
processors. However, you can see here that arm64 receives Tier 1
support, while arm32 is Tier 3. Tier 1 support means distribution
specific packages and binary archives are available, while Tier 3
requires the user to compile ROS 2 from source.

The fastest and simplest way to use ROS 2 is to use a Tier 1 supported
configuration.

This would mean either installing 64 bit Ubuntu on to the Raspberry
Pi, or using the 64 bit version of Raspberry Pi OS and running ROS 2
in Docker.

Ubuntu Linux on Raspberry Pi with binary ROS 2 install
======================================================

Ubuntu for Raspberry Pi is available here.

Make sure to confirm that you have selected the correct version as
described in REP-2000.

Ubuntu for Raspberry Pi doesn't include the *backports* and *updates*
software suites by default, which are required for the ROS 2 binary
install to work.

So, please check and edit the "/etc/apt/sources.list.d/ubuntu.sources"
file on your Raspberry Pi before installing ROS 2.

For example, the Ubuntu 24.04 "Noble Numbat" release should have an
entry that looks like this:

   Types: deb
   URIs: http://ports.ubuntu.com/ubuntu-ports/
   Suites: noble noble-updates noble-backports # <-- IMPORTANT LINE
   Components: main universe restricted multiverse
   Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

You can now install ROS 2 using the normal binary installation
instructions for Ubuntu Linux.

Raspberry Pi OS with ROS 2 in docker
====================================

Raspberry Pi OS 64 bit version is available here.

Raspberry Pi OS is based on Debian which receives Tier 3 support, but
it can run Ubuntu docker containers for Tier 1 support.

After flashing the OS, install Docker.

The official ROS 2 Docker images can be found here.

You may choose from ros-core, ros-base, or perception. See here for
more information on these variants.

Fetch and run an image:

   $ docker pull ros:rolling-ros-core
   $ docker run -it --rm ros:rolling-ros-core

You can also build images yourself:

Clone the docker_images git repo onto the Raspberry Pi, change in to
the directory linked above, then to the directory with your preferred
variant.

Inside of the directory, build the container with:

   $ docker build -t ros_docker .

On a supported system it will only take a minute or two to build the
docker containers, as the source code is already built in to binaries.
