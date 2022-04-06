# Issues with DNS resolution on Openvpn from Windows 10

This guide will resolve issues with DNS resolution on Windows 10 when connected to Openvpn.

## Symptoms:
Unable to resolve internal DNS names on the VPN destinaton network.

DNS Server for the machine is an external DNS server (Eg below should report the DNS server to be the internal DNS server).

```
C:\Users\User>nslookup 
Default Server:  cache1.service.virginmedia.net 
Address:  194.168.4.100 
```

## The Cause:
This is caused by Windows incorrectly assigning the metrics for the interfaces so the VPN does not take priority over the internal network.

## The Fix:
The fix for this is to manually set the metric for the VPN NIC to be lower than that of the local NIC.

Edit the VPN NIC, disable “Automatic metric“ and set the metric to “1“ or some other low number

If this does not fix the issue, edit the NIC used for the local network and repeat the process, setting the metric higher (Eg “15“).