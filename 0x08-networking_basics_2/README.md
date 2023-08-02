This file contains description for the 0x08-networking_basics_2 task.

#0x08-networking_basics_2



- 0-what-is-my-id: A Bash script that displays the machine's current IPv4 address. The script uses ifconfig to show all active IPv4 IPs attached to the network interfaces.

- 1-show_attached_IPs: A Bash script that displays all active IPv4 IPs on the machine it's executed on. The script uses hostname -I to get all active IPv4 addresses and then uses cut to extract the first IP address.

- 100-port_listening_on_localhost: A Bash script that listens on port 98 on localhost. The script uses netcat (nc) to listen on port 98 and wait for incoming connections.
