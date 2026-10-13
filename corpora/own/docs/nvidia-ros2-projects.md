# NVIDIA ROS 2 Projects

NVIDIA ROS 2 Projects
*********************

NVIDIA Jetson is working towards developing ROS 2 packages to ease the
development of AI applications for robotics.

ROS Projects
============

* Isaac ROS Nvblox : Hardware-accelerated 3D scene reconstruction and
  Nav2 local costmap provider using nvblox.

* Isaac ROS Object Detection : Deep learning model support for object
  detection including DetectNet.

* Isaac ROS DNN Inference : This repository provides two NVIDIA GPU-
  accelerated ROS 2 nodes that perform deep learning inference using
  custom models. One node uses the TensorRT SDK, while the other uses
  the Triton SDK.

* Isaac ROS Visual SLAM : This repository provides a ROS 2 package
  that estimates stereo visual inertial odometry using the Isaac
  Elbrus GPU-accelerated library.

* Isaac ROS Argus Camera : This repository provides monocular and
  stereo nodes that enable ROS developers to use cameras connected to
  Jetson platforms over a CSI interface.

* Isaac ROS image_pipeline : This metapackage offers similar
  functionality as the standard, CPU-based image_pipeline metapackage,
  but does so by leveraging the Jetson platform's specialized computer
  vision hardware.

* Isaac ROS Common : Isaac ROS common utilities for use in conjunction
  with the Isaac ROS suite of packages.

* Isaac ROS AprilTags : ROS 2 node uses the NVIDIA GPU-accelerated
  AprilTags library to detect AprilTags in images and publish their
  poses, ids, and additional metadata.

* ROS and ROS 2 Docker Images : Docker images for easy deployment on
  the NVIDIA Jetson platform, consisting of ROS 2, PyTorch, and other
  important machine learning libraries.

* ROS and ROS 2 DockerFiles: Dockerfiles for ROS 2 based on l4t which
  all you to build your own Docker image.

* ROS 2 Packages for PyTorch and TensorRT: ROS 2 packageis for
  classification and object detection tasks using PyTorch and NVIDIA
  TensorRT. This tutorial is a good starting point AI integration with
  ROS 2 on NVIDIA Jetson.

* ROS / ROS 2 Packages for Accelerated Deep Learning Nodes: Deep
  learning image recognition, object detection, and semantic
  segmentation inference nodes and camera/video streaming nodes for
  ROS/ROS 2 using the jetson-inference library and NVIDIA Hello AI
  World tutorial.

* ROS 2 Package for Human Pose Estimation: A ROS 2 package for human
  pose estimation.

* ROS 2 Package for Hand Pose Estimation and Gesture Classification: A
  ROS 2 package for real-time hand pose estimation and gesture
  classification using TensorRT.

* GPU accelerated ROS 2 Packages for Monocular Depth Estimation: ROS 2
  package for NVIDIA GPU-accelerated torch2trtxb examples such as
  monocular depth estimation and text detection.

* ROS 2 Package for Jetson stats: ROS 2 package for monitoring and
  controlling your NVIDIA Jetson [Xavier NX, Nano, AGX Xavier, TX1,
  TX2].

* ROS 2 Packages for DeepStream SDK: ROS 2 package for NVIDIA
  DeepStream SDK.

Simulation Projects
===================

* Isaac Sim Nav2 : In this ROS 2 sample, we are demonstrating
  Omniverse Isaac Sim integrated with the ROS 2 Nav2 project.

* Isaac Sim Multiple Robot ROS 2 Navigation : In this ROS 2 sample, we
  are demonstrating Omniverse Isaac Sim integrated with the ROS 2 Nav2
  stack to perform simultaneous multiple robot navigation.

References
==========

More updates on NVIDIA Jetson ROS 2 can be found here.
