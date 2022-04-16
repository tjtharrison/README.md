# Using Rsnapshot to backup your Ubuntu Servers

There are many options available for rsnapshot, in this guide I will be connecting via SSH to backup remote servers to a central location.
Firstly we will need to create an SSH key for passwordless connections from your backup server to the client machine.

Once you have passwordless SSH access to your client machine configured you are ready to install rsnapshot on your backup server.

```
apt-get install rsnapshot
```

We will now need to modify the main config file for Rsnapshot, this will give us the option to change the default backup destination (ie the folder in which you wish to save your backups amongst others.

You can review through the options in this file and adjust as per your requirement, typically I will have created a second disk on my Rsnapshot server to house the ISO files so I will change the “snapshot_root” option to the mount point of this second drive.

```
nano /etc/rsnapshot.conf
```

```
snapshot_root /media/backups/

## Uncomment the below lines
cmd_ssh /usr/bin/ssh
logfile /var/log/rsnapshot
```

You will want to go right down to the bottom of the file now to configure your local and remote server backups. I have put a few examples below for you to copy to backup as per your requirement for your remote servers. When changing these, ensure to leave a trailing / at the end of the path as per the note at the top of the rsnapshot.conf file:

```
# LOCALHOST
backup /home/ [localfoldername]/
backup /etc/ [localfoldername]/

# cacheserver
backup root@[cacheserver]:/ [localfoldername]/
```

The format for each of the above is basically [remoteserver]:[remotefolderlocation] [localfoldername]. Once you have happy with your commands above, you can save and close the file before checking the Rsnapshot config:

```
rsnapshot configtest
```

The final step of this guide will be to schedule the various Rsnapshot backups in the crontab. This is done by editing the crontab and pasting in the below to the bottom of the fil, adjusting the times at the start as required (If you are unsure about using crontab you can leave the below as default).

```
0 */4 * * * root /usr/bin/rsnapshot hourly
30 3 * * * root /usr/bin/rsnapshot daily
0 3 * * 1 root /usr/bin/rsnapshot weekly
30 2 1 * * root /usr/bin/rsnapshot monthly
```

Now save and close the crontab. We can kick off a manual backup now to confirm everything is working as it should by running the below command and watching your destination folder to ensure the folders hourly.0/[yourservername] has been created.

```
rsnapshot hourly
```
