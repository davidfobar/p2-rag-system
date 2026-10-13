# RMW implementations

RMW implementations
*******************

By default, ROS 2 uses DDS as its middleware. It is compatible with
multiple DDS or RTPS (the DDS wire protocol) vendors. There is
currently support for eProsima's Fast DDS, RTI's Connext DDS, Eclipse
Cyclone DDS, and GurumNetworks GurumDDS.

It also supports non DDS RMW implementations such as Zenoh.

See REP-2000 for supported RMW vendors by distribution.

The default RMW vendor is eProsima's Fast DDS.

Review all the possible options:

* DDS implementations explains how to use DDS.

* Non DDS implementations explains how to use non DDS implementations.
