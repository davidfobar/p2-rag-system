# Running ROS 2 nodes in Docker [community-contributed]

Running ROS 2 nodes in Docker [community-contributed]
*****************************************************

Run two nodes in a single docker container
==========================================

Pull the ROS docker image with tag "rolling-desktop".

   $ docker pull osrf/ros:rolling-desktop

Run the image in a container in interactive mode.

   $ docker run -it osrf/ros:rolling-desktop

Your best friend is the "ros2" command line help now.

   $ ros2 --help

E.g. list all installed packages.

   $ ros2 pkg list
   (you will see a list of packages)

E.g. list all executables:

   $ ros2 pkg executables
   (you will see a list of <package> <executable>)

Run a minimal example of 2 C++ nodes (1 topic subscriber "listener", 1
topic publisher "talker") from the package "demo_nodes_cpp" in this
container:

   $ ros2 run demo_nodes_cpp listener &
   $ ros2 run demo_nodes_cpp talker

Run two nodes in two separate docker containers
===============================================

Open a terminal. Run the image in a container in interactive mode and
launch a topic publisher (executable "talker" from the package
"demo_nodes_cpp") with "ros2 run":

   $ docker run -it --rm osrf/ros:rolling-desktop ros2 run demo_nodes_cpp talker

Open a second terminal. Run the image in a container in interactive
mode and launch a topic subscriber (executable "listener" from the
package "demo_nodes_cpp") with "ros2 run":

   $ docker run -it --rm osrf/ros:rolling-desktop ros2 run demo_nodes_cpp listener

As an alternative to the command line invocation, you can create a
"docker-compose.yml" file (here version 2) with the following
(minimal) content:

   version: '2'

   services:
     talker:
       image: osrf/ros:rolling-desktop
       command: ros2 run demo_nodes_cpp talker
     listener:
       image: osrf/ros:rolling-desktop
       command: ros2 run demo_nodes_cpp listener
       depends_on:
         - talker

To run the containers call "docker compose up" in the same directory.
You can close the containers with "Ctrl+C".
