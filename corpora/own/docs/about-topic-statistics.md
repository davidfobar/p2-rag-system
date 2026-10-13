# Topic statistics

Topic statistics
****************

Table of Contents
^^^^^^^^^^^^^^^^^

* Overview

* How statistics are calculated

* Types of statistics calculated

* Behavior

* Comparison to ROS 1

* Support

Overview
========

ROS 2 provides integrated measurement of statistics for messages
received by any subscription. Allowing a user to collect subscription
statistics enables them to characterize the performance of their
system or aid in diagnosis of any present issues.

The measurements provided are the received message age and received
message period. For each measurement the statistics provided are the
average, maximum, minimum, standard deviation, and sample count. These
statistics are calculated in a moving window.

How statistics are calculated
=============================

Each statistic set is calculated in constant time and constant memory
by using the utilities implemented in the libstatistics_collector
package. When a new message is received by a subscription, this is a
new sample for calculation in the current measurement window. The
average calculated is simply a moving average. The maximum, minimum,
and sample count are updated upon receipt of each new sample, whereas
the standard deviation is calculated using Welford's online algorithm.

Types of statistics calculated
==============================

* Received message period

  * Units: milliseconds

  * Uses the system clock to measure the period between received
    messages

* Received message age

  * Units: milliseconds

  * Requires a message to have a timestamp populated in the header
    field in order to calculate the age of the message as sent from a
    publisher

Behavior
========

By default, Topic Statistics measurements are not enabled. After
enabling this feature for a specific node via the subscription
configuration options, both received message age and received message
period measurements are enabled for that specific subscription.

The data is published as a statistics_msg/msg/MetricsMessage at a
configurable period (default 1 second) to a configurable topic
(default "/statistics"). Note that the publishing period also serves
as the sample collection window period.

Since received message period requires a message timestamp in a header
field, empty data is published. That is, all statistics values are NaN
if no timestamp is found. Publishing NaN values instead of not
publishing at all avoids the absence of a signal problem and is meant
to explicitly show that a measurement could not be made.

The first sample of each window for the received message period
statistic does not yield a measurement. This is because calculating
this statistic requires knowing the time the previous message arrived,
so subsequent samples in the window yield measurements.

Comparison to ROS 1
===================

Similar to ROS 1 Topic Statistics, both message age and message period
are calculated, albeit from the subscription side. Other ROS 1
metrics, e.g., the number of dropped messages or traffic volume, are
currently not provided.

Support
=======

This feature is currently supported in ROS 2 Foxy for C++ only
(rclcpp). Future work and improvements, such as Python support, can be
found here.
