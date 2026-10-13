# Testing Your Code with the ROS Build Farm

Testing Your Code with the ROS Build Farm
*****************************************

The ROS 2 Build Farm is incredibly powerful. In addition to creating
binaries, it will also test pull requests by compiling and running all
the tests for your ROS packages before the PR is merged.

There are four prerequisites.

   * The GitHub user @ros-pull-request-builder must have access to the
     repository.

   * The GitHub repository must have the webhooks set up.

   * Your package must be indexed in rosdistro

   * The "test_pull_requests" flag must be true.

GitHub Access
=============

You can give access to the PR Builder either at the GitHub
organization level OR just to the single GitHub repository.

GitHub Organization
-------------------

1. Open https://github.com/orgs/%YOUR_ORG%/people (while replacing
   "%YOUR_ORG%" with the appropriate organization)

2. Click "Invite Member" and enter "ros-pull-request-builder"

GitHub Repository
-----------------

1. Open https://github.com/%YOUR_ORG%/%YOUR_REPO%/settings/access
   (while replacing "%YOUR_ORG%/%YOUR_REPO$" with the appropriate
   organization/repo)

2. Click "Add people" and enter "ros-pull-request-builder"

3. Select "Admin" or "Write" for their role. (see next section)

WebHooks
========

If you grant full administrative rights to "ros-pull-request-builder",
it will automatically setup the hooks.

Alternatively, you can avoid the need for full administrative rights
by setting them up with only **write** permissions.

1. Open https://github.com/%YOUR_ORG%/%YOUR_REPO%/settings/hooks/new)

2. Enter ""https://build.ros2.org/ghprbhook/" as the Payload URL

3. Check the following options:
      * Let me select individual events.

      * Issue comments

      * Pull requests

test_pull_requests
==================

For each ROS distro that you want pull request testing for, you must
enable the "test_pull_requests" flag in the appropriate section of the
rosdistro.

   * **Option 1** - You have the option when running bloom to turn on
     pull request testing.

   * **Option 2** - You can **carefully** manually edit the
     appropriate file in the rosdistro repo, and make a new pull
     request. Example. Documented in REP 143.

Note that after the pull request has been added, the job will usually
not be created until the nightly Jenkins reconfiguration.
