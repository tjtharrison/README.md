# Converting Ubuntu 12.04 Desktop to Server

I have done this in the past though find it ‘cleaner’ to install the server from scratch if this is your aim.
Firstly we will need to install tasksel which will be completing the job of converting for us.

```
apt-get install tasksel
```

We will now need to uninstall the Ubuntu-Desktop module and install Server.

```
tasksel remove ubuntu-desktop (Note: this may take a few minutes to complete)
tasksel install server
apt-get install linux-server linux-image-server
```

Now that we are no longer using Ubuntu-Desktop we can remove lightdm (The display manager for Ubuntu Desktop):

```
apt-get –purge remove lightdm
```

Grub will need to be configured to use the command line (Where before it had the nice splash screen before login) add the below to your /etc/default/grub file:

```
nano /etc/default/grub
```

```
GRUB_TIMEOUT=5
( Comment out ‘GRUB_HIDDEN_TIMEOUT’ )
GRUB_CMDLINE_LINUX_DEFAULT=””
GRUB_TERMINAL=console ( only for PC )
sudo update-grub
```
