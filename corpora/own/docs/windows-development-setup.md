# Windows (source)

Windows (source)
****************

Table of Contents
^^^^^^^^^^^^^^^^^

* System requirements

  * Language support

* Create a location for the ROS 2 installation

* Increase the Windows maximum path length

* Install prerequisites

  * Install MSVC

  * Install pixi

  * Install dependencies

* Build ROS 2

  * Source the MSVC compiler

  * Source the pixi environment

  * Get ROS 2 code

  * Install additional RMW implementations (optional)

  * Build the code in the workspace

* Setup environment

  * Source the pixi environment

  * Source the ROS 2 environment

* Try some examples

* Next steps

* Stay up to date

* Troubleshoot

* Uninstall

This page explains how to setup a development environment for ROS 2 on
Windows.

System requirements
===================

Only Windows 10 is supported.

Warning:

  We recommend using a clean Windows environment for the build, such
  as a fresh install, Docker container, or Virtual Machine. This is
  because existing software, such as other Python versions, can
  pollute the build configuration and cause compilation errors.

Language support
----------------

Make sure you have a locale which supports "UTF-8". For example, for a
Chinese-language Windows 10 installation, you may need to install an
English language pack.

Create a location for the ROS 2 installation
============================================

This location will contain both the installed binary packages, plus
the ROS 2 installation itself.

Start a powershell session (usually by clicking on the start menu,
then typing "powershell").

Then create a directory to store the installation. Because of Windows
path-length limitations, this should be as short as possible. We'll
use "C:\dev" for the rest of these instructions.

   $ md C:\dev

Increase the Windows maximum path length
========================================

By default, Windows is restricted to a maximum path length (MAX_PATH)
of 260 characters. The ROS 2 build will use significantly longer path
lengths, so we will increase that. Using the powershell session you
started above, run the following:

   $ New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force

You can read more about this limitation in Microsoft's documentation.

Install prerequisites
=====================

Install MSVC
------------

In order to compile the ROS 2 code, the MSVC compiler must be
installed. Currently it is recommended to use MSVC 2019.

Continue using the previous powershell session, and run the following
command to download it:

   $ irm https://aka.ms/vs/16/release/vs_buildtools.exe -OutFile vs_buildtools_2019.exe

Now install MSVC 2019:

   $ .\vs_buildtools_2019.exe --quiet --wait --norestart --add Microsoft.Component.MSBuild --add Microsoft.Net.Component.4.6.1.TargetingPack --add Microsoft.Net.Component.4.8.SDK --add Microsoft.VisualStudio.Component.CoreBuildTools --add Microsoft.VisualStudio.Component.Roslyn.Compiler --add Microsoft.VisualStudio.Component.TextTemplating --add Microsoft.VisualStudio.Component.VC.CLI.Support --add Microsoft.VisualStudio.Component.VC.CoreBuildTools --add Microsoft.VisualStudio.Component.VC.CoreIde --add Microsoft.VisualStudio.Component.VC.Redist.14.Latest --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 --add Microsoft.VisualStudio.Component.Windows10SDK --add Microsoft.VisualStudio.Component.Windows10SDK.19041 --add Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core --add Microsoft.VisualStudio.Workload.MSBuildTools --add Microsoft.VisualStudio.Workload.VCTools

Note:

  The installation of MSVC can take a long time, and there is no
  feedback while it is progressing.

Install pixi
------------

ROS 2 uses conda-forge as a backend for packages, with pixi as the
frontend.

Continue using the previous powershell session, and use the
instructions from https://pixi.sh/latest/ to install "pixi". Once
"pixi" has been installed, close the powershell session and start it
again, which will ensure "pixi" is on the PATH.

Install dependencies
--------------------

Download the pixi configuration file in the existing powershell
session:

   $ cd C:\dev
   $ irm https://raw.githubusercontent.com/ros2/ros2/refs/heads/rolling/pixi.toml -OutFile pixi.toml

Install dependencies:

   $ pixi install

You should now close the powershell session, as the rest of the
instructions will use the Windows command prompt.

Build ROS 2
===========

Start a new Windows command prompt, which will be used for the build.

Source the MSVC compiler
------------------------

This is required in the command prompt you'll use to compile ROS 2,
but it is *not* required when running:

   $ call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64

Source the pixi environment
---------------------------

This is required in every command prompt you open to set up paths to
the dependencies:

   $ cd C:\dev
   $ pixi shell

Get ROS 2 code
--------------

Now that we have the development tools we can get the ROS 2 source
code.

Setup a development folder, for example "C:\dev\rolling":

   $ md C:\dev\rolling\src
   $ cd C:\dev\rolling

Get the "ros2.repos" file which defines the repositories to clone
from:

   $ vcs import --input https://raw.githubusercontent.com/ros2/ros2/rolling/ros2.repos src

Install additional RMW implementations (optional)
-------------------------------------------------

The default middleware that ROS 2 uses is "Fast DDS", but the
middleware (RMW) can be replaced at build or runtime. See the guide on
how to work with multiple RMWs.

Build the code in the workspace
-------------------------------

To build the "\rolling" folder tree:

   $ colcon build --merge-install

Note:

  We're using "--merge-install" here to avoid a "PATH" variable that
  is too long at the end of the build. If you're adapting these
  instructions to build a smaller workspace then you might be able to
  use the default behavior which is isolated install, i.e. where each
  package is installed to a different folder.

Note:

  Source installation can take a long time given the large number of
  packages being pulled into the workspace.

Setup environment
=================

Start a new Windows command prompt, which will be used in the
examples.

Source the pixi environment
---------------------------

This is required in every command prompt you open to set up paths to
the dependencies:

   $ cd C:\dev
   $ pixi shell

Source the ROS 2 environment
----------------------------

This is required in every command prompt you open to setup the ROS 2
workspace:

   $ call C:\dev\rolling\install\local_setup.bat

This will automatically set up the environment for any DDS vendors
that support was built for.

It is normal that the previous command, if nothing else went wrong,
outputs "The system cannot find the path specified." exactly once.

Try some examples
=================

Note that the first time you run any executable you will have to allow
access to the network through a Windows Firewall popup.

You can run the tests using this command:

   $ colcon test --merge-install

Note:

  "--merge-install" should only be used if it was also used in the
  build step.

Afterwards you can get a summary of the tests using this command:

   $ colcon test-result

To run the examples, first open a clean new "cmd.exe" and set up the
workspace by sourcing the "local_setup.bat" file. Then, run a C++
"talker":

   $ call install\local_setup.bat
   $ ros2 run demo_nodes_cpp talker

In a separate command prompt you can do the same, but instead run a
Python "listener":

   $ call install\local_setup.bat
   $ ros2 run demo_nodes_py listener

You should see the "talker" saying that it's "Publishing" messages and
the "listener" saying "I heard" those messages. This verifies both the
C++ and Python APIs are working properly. Hooray!

Note:

  It is not recommended to build in the same cmd prompt that you've
  sourced the "local_setup.bat".

Next steps
==========

Continue with the tutorials and demos to configure your environment,
create your own workspace and packages, and learn ROS 2 core concepts.

Stay up to date
===============

See Maintain source checkout to periodically refresh your source
installation.

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

      $ rmdir /s /q C:\dev\rolling
