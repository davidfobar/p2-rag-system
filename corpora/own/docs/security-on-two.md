# Ensuring security across machines

Ensuring security across machines
*********************************

**Goal:** Make two different machines communicate securely.

**Tutorial level:** Advanced

**Time:** 5 minutes

Contents
^^^^^^^^

* Background

* Create the second keystore

* Copy files

* Launch the nodes

Background
==========

Before proceeding ensure you have completed the Setting up security
tutorial.

The previous tutorials have used two ROS nodes on the same machine
sending all network communications over the localhost interface. Let's
extend that scenario to involve multiple machines, since the benefits
of authentication and encryption then become more obvious.

Suppose that the machine with the keystore created in the previous
demo has a hostname "Alice", and that we want to also use another
machine with hostname "Bob" for our multi-machine "talker/listener"
demo. We need to move some keys from "Alice" to "Bob" to allow SROS 2
to authenticate and encrypt the transmissions.

Create the second keystore
==========================

Begin by creating an empty keystore on "Bob"; the keystore is actually
just an empty directory:

Linux

   $ ssh Bob
   $ mkdir ~/sros2_demo
   $ exit

MacOS

   $ ssh Bob
   $ mkdir ~/sros2_demo
   $ exit

Windows

   $ ssh Bob
   $ md C:\dev\ros2\sros2_demo
   $ exit

Copy files
==========

Next copy the keys and certificates for the "talker" program from
"Alice" to "Bob". Since the keys are just text files, we can use "scp"
to copy them.

Linux

   $ cd ~/sros2_demo/demo_keystore
   $ scp -r talker USERNAME@Bob:~/sros2_demo/demo_keystore

MacOS

   $ cd ~/sros2_demo/demo_keystore
   $ scp -r talker USERNAME@Bob:~/sros2_demo/demo_keystore

Windows

   $ cd C:\dev\ros2\sros2_demo\demo_keystore
   $ scp -r talker USERNAME@Bob:/dev/ros2/sros2_demo/demo_keystore

Warning:

  Note that in this case the entire keystore is shared across the
  different machines which may not be the desired behavior, as it may
  result in a security risk. Please refer to Deployment Guidelines for
  more information in this regard.

That will be very quick, since it's just copying some very small text
files. Now, we're ready to run a multi-machine talker/listener demo!

Launch the nodes
================

Once the environment is set up, run the talker on "Bob":

   $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker

and launch the listener on "Alice":

   $ ros2 run demo_nodes_py listener --ros-args --enclave /talker_listener/listener

Alice will now be receiving encrypted messages from Bob.

With two machines successfully communicating using both encryption and
authentication, you can use the same procedure to add more machines to
your ROS graph.
