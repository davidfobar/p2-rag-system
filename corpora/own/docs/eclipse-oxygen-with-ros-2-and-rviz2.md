# Using Eclipse Oxygen with "rviz2" [community-contributed]

Using Eclipse Oxygen with "rviz2" [community-contributed]
*********************************************************

Table of Contents
^^^^^^^^^^^^^^^^^

* Setup

* Eclipse-indexer

* Debugging with eclipse

Setup
=====

This tutorial assumes Eclipse Oxygen, git, and Egit are already
installed.

Throughout the tutorial we name the eclipse workspace the same name as
the ros2 package, but this is not required.

HINT: We use nested projects and one Eclipse Workspace for each ROS-2
package.

[image]

Create a C++ Project.

[image][image]

Choose the ROS 2 package name as the Project Name. Choose a Makefile
Project and Other Toolchain.

[image]

Click on Finish

[image]

Our project should be shown in the "Project Explorer".

[image]

Inside our Project create a folder called "src".

[image]

Import a git repository.

[image]

Put in the repository URL.

[image]

IMPORTANT: Use the source folder of the project we created before as
the destination folder.

HINT: If you ran into problems choosing the destination folder path,
the Eclipse Dialog needs a name in the name field.

[image]

Import using the new project wizard.

[image]

Create a General->Project.

[image]

Use the git repository name as the project name. IMPORTANT: Use the
folder we cloned the git repository in as the "Location".

[image]

The git project and the new project should be visible in the Project
Explorer view. The same files are listed multiple times, but only one
project is linked with Egit.

[image]

Repeat this procedure again. Import git repository pluginlib.

[image]

IMPORTANT: Use a folder inside the source folder as
"Destination->Directory".

[image]

IMPORTANT: Use the folder we cloned the git repository in as the
location for the new project.

[image]

Run the same procedure with the tinyxml2_vendor git repository.

[image]

IMPORTANT: Again use a folder inside the source folder.

[image]

IMPORTANT: Use the location of the folder we cloned as the new project
folder.

[image]

Now all four Projects should be visible in the Project Explorer view.

[image]

Clicking in the top right cornder for the Project Explorer view allows
us to change the Project Presentation to Hierarchical view. Now it
looks like a ROS-2 project as it is on the hard drive. But this view
loses the linkage to Egit, so use the Flat Project Presentation. The
Egit linkage is good if you want to see e.g. which author wrote which
code-line, etc.

[image]

Go to "C/C++ build"-section and put "ament" into "Build command".

[image]

Go to "Behavior" tab and unselect "clean" and put "build" into Build
textbox.

[image]

Before "Build project" will work, we need to close Eclipse. Open a
shell and source the ROS-2 setup.bash file, then cd into the directory
of the eclipse project (here: /home/ubu/rviz2_ws/rviz2_ws) and start
Eclipse from inside this directory.

[image]

Now code completion, egit annotations, eclipse C/C++ Tools, etc.
should all work.

[image]

Eclipse-indexer
===============

Opening the main.cpp of rviz2 may show a lot of "unresolved inclusion"
warnings. To fix this, go to Project->Properties->C++ General->Path
and Symbols. Click on the "References" tab and select "ros2_ws".

[image]

Go to C/C++-General->Path-and-Symbols, click on the "Source locations"
tab and click on "Link folder". Choose the location of qt5 includes.

[image]

The next image should be shown. It is a good idea to add excludes to
the source locations, so that some directories (like "Build" and
"Install") don't get indexed.

[image]

Go to C++General->Preprocessor includes, select "CDT GCC Built in
compiler settings [Shared]" and enter in the "command to get compiler
specs" text box the following:

   -std=c++14

[image]

Go to "C/C++-General->Indexer" and select the following in the image.
E.g "index unused headers as c files" to resolve e.g. QApplication,
because the QApplication headers content is only "#include
"qapplication.h".

[image]

After running the indexer (which happens later, so you will see this
also later), you can see what it added

[image]

After that right-click on the rviz2 project and select
"Indexer->Rebuild", which will start rebuilding the index (there is an
icon in the lower right showing progress). Once the index is finished
rebuilding, it should be able to resolve all includes.

[image]

Debugging with eclipse
======================

Go to "C/C++-Build" and add to the build command:

   -DCMAKE_BUILD_TYPE=Debug

[image]

Then in eclipse go to "Run->Debug Configurations" and add the
following and click on "Debug".

[image]
