# Forcing Windows Servers to sync NTP Time more frequently

By default, Windows will only sync it’s NTP time every 17 minutes. To update the server to sync time more often this can be set via Group Policy (Either locally if the machine is not joined to a domain or centrally if in a Domain controlled environment).

## Group Policy setting:
Instructions will be the same for Domain Controlled and local Group Policy (gpedit.exe):

* Open up Group Policy settings
* Go to: Local Computer Policy > Computer Configuration > Administrative Templates > System > Windows Time Service
* Double click on Global Configuration Settings
    * Select “enabled” at the top of the Window
    * Scroll down to MinPollInterval and MaxPollInterval and set these as appropriate (minimum is 2 min /3 max ). NOTE: These times are in base-2

## Apply the Group Policy change
Run the below to update Group Policy on the server:

```
gpupdate /force
```

## Confirm current time sync status / sync time:
To confirm that the setting has applied, run the following and check the final line in the output:

```
C:\Users\Administrator>w32tm /query /status
Leap Indicator: 0(no warning)
Stratum: 4 (secondary reference - syncd by (S)NTP)
Precision: -6 (15.625ms per tick)
Root Delay: 0.0314484s
Root Dispersion: 7.7758595s
ReferenceId: 0xA9FEA97B (source IP: 169.254.169.123)
Last Successful Sync Time: 26/03/2020 19:37:22
Source: 169.254.169.123,0x9
Poll Interval: 2 (4s)
```
