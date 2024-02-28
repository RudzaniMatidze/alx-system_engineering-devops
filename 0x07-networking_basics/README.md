# 0x07-networking_basics

## Tasks:

### File: [0-OSI_model](./0-OSI_model)
#### Questions:
<u>What is the OSI model?</u>
1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology
<u>How is the OSI model organized?</u>
1. Alphabetically
2. From the lowest to the highest level
3. Randomly
### File: [1-types_of_network](./1-types_of_network)
#### Questions:
<u>What type of network a computer in local is connected to?</u>
1. Internet
2. WAN
3. LAN
<u>What type of network could connect an office in one building to another office in a building a few streets away?</u>
1. Internet
2. WAN
3. LAN
<u>What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?</u>
1. Internet
2. WAN
3. LAN
### File: [2-MAC_and_IP_address](./2-MAC_and_IP_address)
#### Questions:
<u>What is a MAC address?</u>
1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface
<u>What is an IP address?</u>
1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks
### File: [3-UDP_and_TCP](./3-UDP_and_TCP)
#### Questions:
<u>Which statement is correct for the TCP box:</u>
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process
<u>Which statement is correct for the UDP box:</u>
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process
<u>Which statement is correct for the TCP worker:</u>
1. Have you received boxes x, y, z?
2. May I increase the rate at which I am sending you boxes?
### File: [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports)
#### Questions:
<While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:
- 22 for SSH
- 80 for HTTP
- 443 for HTTPS
Note that a specific IP + port = socket.>
<u>Write a Bash script that displays listening ports:</u>
- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs
### File: [5-is_the_host_on_the_network](./5-is_the_host_on_the_network)
#### Questions:
<The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.>
<u>Write a Bash script that pings an IP address passed as an argument.
Requirements:</u>
- Accepts a string as an argument
- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
- Ping the IP 5 times
