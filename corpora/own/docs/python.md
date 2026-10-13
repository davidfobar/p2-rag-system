# Writing Basic Tests with Python

Writing Basic Tests with Python
*******************************

Starting point: we'll assume you have a basic ament_python package set
up already and you want to add some tests to it.

If you are using ament_cmake_python, refer to the ament_cmake_python
docs for how to make tests discoverable. The test contents and
invocation with "colcon" remain the same.

Package Setup
=============

setup.py
--------

Your "setup.py" must have a test dependency on "pytest" within the
call to "setup(...)":

   tests_require=['pytest'],

Test Files and Folders
----------------------

Your test code needs to go in a folder named "tests" in the root of
your package.

Any file that contains tests that you want to run must have the
pattern "test_FOO.py" where "FOO" can be replaced with anything.

Example package layout:
~~~~~~~~~~~~~~~~~~~~~~~

   awesome_ros_package/
     awesome_ros_package/
         __init__.py
         fozzie.py
     package.xml
     setup.cfg
     setup.py
     tests/
         test_init.py
         test_copyright.py
         test_fozzie.py

Test Contents
=============

You can now write tests to your heart's content. There are plenty of
resources on pytest, but in short, you can write functions with the
"test_" prefix and include whatever assert statements you'd like.

   def test_math():
       assert 2 + 2 == 5 # This should fail for most mathematical systems

Running Tests
=============

See the tutorial on how to run tests from the command line for more
information on running the tests and inspecting the test results.

Special Commands
================

Beyond the standard colcon testing commands you can also specify
arguments to the "pytest" framework from the command line with the "--
pytest-args" flag. For example, you can specify the name of the
function to run with

Linux/macOS

   $ colcon test --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function

Windows

   $ colcon test --merge-install --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function

To see the pytest output while running the tests, use these flags:

   $ colcon test --event-handlers console_cohesion+
