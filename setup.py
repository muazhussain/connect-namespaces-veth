import os

# Constants
VM = 'ubuntuvm'
NS1 = 'london'
NS2 = 'newyork'
VETH1 = 'red'
VETH2 = 'green'
IP_NS1 = '10.0.0.1/24'
IP_NS2 = '10.0.0.2/24'

# Launch Virtual Machines
os.system('multipass launch -c 2 -m 2G -d 10G -n ' + VM)

# Access Virtual Machines
os.system('multipass shell ' + VM)

# Create Namespaces
os.system('sudo ip netns add ' + NS1)
os.system('sudo ip netns add ' + NS2)

# Configure Interfaces
os.system('sudo ip link add ' + VETH1 + 'type veth peer name ' + VETH2)

# Assign Interfaces to Namespaces
os.system('sudo ip link set ' + VETH1 + 'netns ' + NS1)
os.system('sudo ip link set ' + VETH2 + 'netns ' + NS2)

# Configure IP Addresses
os.system('sudo ip netns exec ' + NS1 + ' ip addr add ' + IP_NS1 + ' dev ' + VETH1)
os.system('sudo ip netns exec ' + NS2 + ' ip addr add ' + IP_NS2 + ' dev ' + VETH2)

# Bring Up the Interfaces
os.system('sudo ip netns exec ' + NS1 + ' ip link set ' + VETH1 + ' up')
os.system('sudo ip netns exec ' + NS2 + ' ip link set ' + VETH2 + ' up')

# Test Connection
os.system('sudo ip netns exec ' + NS1 + 'ping -c 4 ' + IP_NS2)
os.system('sudo ip netns exec ' + NS2 + 'ping -c 4 ' + IP_NS1)