# Mounting a Windows share to Ubuntu

In this example I will be using my network share for the purposes of backing up my Ubuntu server using Mondo backup.

Firstly we will need to install required packages.

```
apt-get install cifs-utils
```

Make a directory to be used as a mount point for this directory. This is where your network share will be available to on your system.

```
mkdir /media/serverbackup
```

We will need to now edit our fstab file to ensure that this network share mounts each time we boot our server. Edit your fstab file as follows:

```
nano /etc/fstab
//[servername]/[sharename]          /media/serverbackups cifs username=WINDOWSUSERNAME,password=PASSWORD,iocharset=utf8,sec=ntlm 0 0
```

Now confirm that everything is set up correctly by manually mounting all available mount points running the below command. If you wish to check the auto-mount functionality you can also just reboot your server. If there are no errors you should be good to go

```
mount -a
```
