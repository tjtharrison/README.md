# Setting up Ubuntu as a Bridged Wireless Access Point

Setting up your Ubuntu Server as a stand-alone Wireless Access Point with supported Wireless Dongles.
Before starting this guide, you should ensure that your machine (either virtual or physical) has a network card attached as well as your Wireless Dongle.

Firstly you should ensure that the Wireless dongle that you have connected to your ubuntu server is compatible with the following guide. This is done using the iw package. You can install and run this as follows:

```
apt-get install iw 
```

Now to find your Wireless Dongle available options you can run the following:

```
iw list
```

Within this you will find a section "Supported interface modes" which will look similar to the following:

```
Supported interface modes:
* IBSS
* managed
* AP
* AP/VLAN
* WDS
* monitor
* mesh point
```

If you see AP listed you will be okay to continue using this guide to create your standalone Wireless Access Point on Ubuntu Server.

We will now need to install hostapd which will be the package distributing and managing Wireless connections:

```
apt-get install hostapd
nano /etc/hostapd/hostapd.conf
```

```
ssid=[The intended name of your wireless network]
wpa_passphrase=[Passphrase for your wireless network]
interface=wlan0
bridge=br0
auth_algs=3
channel=7
driver=nl80211
hw_mode=g
logger_stdout=-1
logger_stdout_level=2
max_num_sta=5
rsn_pairwise=CCMP
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP CCMP
```

Once you have saved and closed the above file (After changing Wireless SSID name and passphrase) we will need to ensure hostapd knows where it’s config file is for the Hostapd Daemon

```
nano /etc/default/hostapd
DAEMON_CONF=”/etc/hostapd/hostapd.conf”
```

Once you have started the Daemon, if you use a Mobile phone / Laptop you should now see a Wireless network appear with your SSID configured above.

We will now need to configure a network bridge between the newly created Wireless network and your current network connection (this will typically be eth0).

```
apt-get install bridge-utils
```

We will now need to edit our network configuration file on the server to disable eth0 configuration and set up our new bridge network (br0). Open up the interfaces file and enter the following details for br0 (Leaving eth0 configuration in place).

```
nano /etc/network/interfaces
```

```
auto br0
iface br0 inet dhcp
bridge-ports eth0 wlan0
```

If you wish for your Wireless server to have a static IP address, this should be configured on the br0 interface and eth0 left as DHCP.

Once we have done this, we should start the hostapd daemon and ensure we can connect to the Wireless network and network requests (Eg DHCP, DNS) are being forwarded to our internal Network management servers as appropriate.

```
service hostapd start
```
