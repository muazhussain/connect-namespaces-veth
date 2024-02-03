# Virtual Networking Setup Script

This script automates the setup of a virtual network with two namespaces using `multipass` and `ip` commands. The network consists of two namespaces (`london` and `newyork`) connected by a pair of veth interfaces (`red` and `green`), each with an assigned IP address in the `10.0.0.0/24` subnet.
