# Nodes

Nodes
*****

A node is a participant in the ROS 2 graph, which uses a client
library to communicate with other nodes. Nodes can communicate with
other nodes within the same process, in a different process, or on a
different machine. Nodes are typically the unit of computation in a
ROS graph; each node should do one logical thing.

Nodes can publish to named topics to deliver data to other nodes, or
subscribe to named topics to get data from other nodes. They can also
act as a service client to have another node perform a computation on
their behalf, or as a service server to provide functionality to other
nodes. For long-running computations, a node can act as an action
client to have another node perform it on their behalf, or as an
action server to provide functionality to other nodes. Nodes can
provide configurable parameters to change behavior during run-time.

Nodes are often a complex combination of publishers, subscribers,
service servers, service clients, action servers, and action clients,
all at the same time.

Connections between nodes are established through a distributed
discovery process.
