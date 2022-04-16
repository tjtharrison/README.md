# Setting up DHCP on Ubuntu Server

How to set up and manage DHCP on Ubuntu Server using ISC-DHCP.
Firstly, we should ensure there are no updates available for the server before installing isc dhcp server.

```
apt-get update && apt-get upgrade
apt-get install isc-dhcp-server
```

Once this has been installed, the service will not start by default so you are able to configure your DHCP server settings before letting it loose on the network. The server that I will be running ISC from currently have 4 network adapters connected to it, though I only wish to accept DHCP requests from one (The main LAN). In order to do this I must edit the main isc config file and ensure that it only listens on eth0. If you wish for ISC to listen on multiple interfaces, you need only separate these with a space between each interface on the INTERFACES=”” line in the file.

```
nano /etc/default/isc-dhcp-server
INTERFACES="eth0"
```

Once this has been done, we will need to define our DHCP options. This is done in the main conf file for ISC – It is best to make a copy of this config file before making any changes so you are able to revert if anything goes wrong.

cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.bak
I tend to delete the original .conf file now and start from scratch using my notes below due to the sheer amount of information included in commented lines, though if you wish to simply modify the existing file with your network requirements that will work fine too.

```
nano /etc/dhcp/dhcpd.conf
```

Enter the below to the file:

```
###### Authoritative DHCP Server ######
authoritative;

###### My LAN DHCP Settings ######
subnet 192.168.1.0 netmask 255.255.255.0 {
range 192.168.1.10 192.168.1.100;
option domain-name "example.org";
option domain-name-servers ns1.example.org;
option routers 192.168.1.1;
option broadcast-address 192.168.1.255;
default-lease-time 600;
max-lease-time 7200;
}
```

Adjust the above for your network requirement, restart the DHCP service on the server and you should be good to go!

```
service isc-dhcp-server start
```

In order to ensure that your DHCP server is handing out IP addresses as required, you can run the below command to watch your syslog file for DHCP log entries. If you reboot / request a DHCP address while watching this log file you should see an address be given out

```
tail -f /var/log/syslog | grep "dhcpd"
```
