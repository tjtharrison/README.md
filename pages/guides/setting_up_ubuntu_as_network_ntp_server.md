# Setting up Ubuntu as network NTP Server

How to set up Ubuntu Server as an NTP Server for your network
The first stage will be to remove ntpdate from your server and install the NTP package.

```
apt-get remove ntpdate
apt-get purge ntpdate
apt-get install ntp
```

Once this is done, we will need to configure our NTP.conf file which is the main config file for NTP now running on your server. We can leave a majority of the settings in this file as they are, though I will highlight below changes to be made

```
nano /etc/ntp.conf
```

Add `iburst` next to server 0.ubuntu.pool.ntp.org. This will force NTP to first sync with this server before attempting to syncronise with the others – This helps with a faster start up of the service after restart / startup etc.

```
server 0.ubuntu.pool.ntp.org iburst
```

Add a line with the other restrictions as follows to allow access to NTP to clients on your network:

```
restrict [your network mask eg 192.168.1.0] mask 255.255.255.0 nomodify notrap
```

Once you have made these changes, restart your ntp service and you should now be able to configure your clients to point to your onsite NTP server.

```
service ntp restart
```
