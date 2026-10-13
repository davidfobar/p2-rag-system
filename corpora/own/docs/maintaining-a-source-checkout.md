# Maintain source checkout

Maintain source checkout
************************

* Update your repository list

  * Latest ROS 2 Rolling branches

* Update your repositories

* Download the new source code

* Rebuild your workspace

* Inspect your source checkout

If you have installed ROS 2 from source, there may have been changes
made to the source code since the time that you checked it out. To
keep your source checkout up to date, you will have to periodically
update your "ros2.repos" file, download the latest sources, and
rebuild your workspace.

Update your repository list
===========================

Each ROS 2 release includes a "ros2.repos" file that contains the list
of repositories and their version for that release.

Latest ROS 2 Rolling branches
-----------------------------

If you wish to checkout the latest code for ROS 2 Rolling, you can get
the relevant repository list by running:

Linux

   $ cd ~/ros2_rolling
   $ mv -i ros2.repos ros2.repos.old
   $ wget https://raw.githubusercontent.com/ros2/ros2/rolling/ros2.repos

macOS

   $ cd ~/ros2_rolling
   $ mv -i ros2.repos ros2.repos.old
   $ wget https://raw.githubusercontent.com/ros2/ros2/rolling/ros2.repos

Windows

Use a Windows command line interface:

   $ cd \dev\ros2_rolling
   $ curl -sk https://raw.githubusercontent.com/ros2/ros2/rolling/ros2.repos -o ros2.repos

Or a powershell:

   $ cd \dev\ros2_rolling
   $ curl https://raw.githubusercontent.com/ros2/ros2/rolling/ros2.repos -o ros2.repos

Update your repositories
========================

You will notice that in the ros2.repos file, each repository has a
"version" associated with it that points to a particular commit hash,
tag, or branch name. It is possible that these versions refer to new
tags/branches that your local copy of the repositories will not
recognize as they are out-of-date. Because of this, you should update
the repositories that you have already checked out with the following
command:

   $ vcs custom --args remote update

Download the new source code
============================

You should now be able to download the sources associated with the new
repository list with:

Linux

   $ vcs import src < ros2.repos
   $ vcs pull src

macOS

   $ vcs import src < ros2.repos
   $ vcs pull src

Windows

In a Windows command line interface:

   $ vcs import --input ros2.repos src
   $ vcs pull src

Or in powershell:

   $ vcs import --input ros2.repos src
   $ vcs pull src

Rebuild your workspace
======================

Now that the workspace is up to date with the latest sources, remove
your previous install and rebuild your workspace with, for example:

   $ colcon build --symlink-install

Inspect your source checkout
============================

During your development you may have deviated from the original state
of your workspace from when you imported the repository list. If you
wish to know the versions of the set of repositories in your
workspace, you can export the information using the following command:

Linux

   $ cd ~/ros2_rolling
   $ vcs export src > my_ros2.repos

macOS

   $ cd ~/ros2_rolling
   $ vcs export src > my_ros2.repos

Windows

   $ cd \dev\ros2_rolling
   $ vcs export src > my_ros2.repos

This "my_ros2.repos" file can then be shared with others so that they
can reproduce the state of the repositories in your workspace.
