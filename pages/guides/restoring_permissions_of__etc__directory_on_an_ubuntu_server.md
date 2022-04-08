# Restoring permissions of /etc/ directory on an Ubuntu Server

I recently had to look at an issue where the permissions of the /etc/ directory on an Ubuntu server had been blanket overwritten with 777 Permissions by a faulty script which was in development. This caused a whole host of issues (Starting with being unable to SSH to the server!).

After gaining access to the server via the Vmware console, I proceeded to investigate – Resolving permissions issues as I found them. As this was on one of my dev servers, I decided to simply copy the /etc/ directory from another server running the same OS release and copy the permissions as follows.

_NOTE: I definitely do not recommend doing this on a non-dev server as I am not sure what the long term concequences will be (Also it is far from a graceful solution).. This may not be the best way to achieve this but definitely got me out of a sticky situation!_

Once You have copied the /etc/ directory from another server to Your broken server (You will not be able to scp files from local > Remote (Eg from Your Desktop > Broken Server) but You should be able to scp remote > Local from the broken Server.

For this I stored the /etc/ directory from my old server in /tmp/recover-etc/etc/

Once Your /etc/ directory is restored on the server, You can run the below to see what Your server will be doing when You run the script to replicate the permissions:

```
for file in $(find /etc/ ); do echo chmod --reference=/tmp/recover-etc$file $file; done
```

This should print something similar to the following:

```
chmod --reference=/tmp/recover-etc/etc/rc4.d/S03lxcfs /etc/rc4.d/S03lxcfs
chmod --reference=/tmp/recover-etc/etc/rc4.d/S02acpid /etc/rc4.d/S02acpid
chmod --reference=/tmp/recover-etc/etc/rc4.d/S01rsyslog /etc/rc4.d/S01rsyslog
chmod --reference=/tmp/recover-etc/etc/rc4.d/S02atd /etc/rc4.d/S02atd
chmod --reference=/tmp/recover-etc/etc/rc4.d/S02mdadm /etc/rc4.d/S02mdadm
chmod --reference=/tmp/recover-etc/etc/rc4.d/S02cron /etc/rc4.d/S02cron
chmod --reference=/tmp/recover-etc/etc/rc4.d/S01open-vm-tools /etc/rc4.d/S01open-vm-tools
chmod --reference=/tmp/recover-etc/etc/binfmt.d /etc/binfmt.d
chmod --reference=/tmp/recover-etc/etc/host.conf /etc/host.conf
chmod --reference=/tmp/recover-etc/etc/hosts.allow /etc/hosts.allow
```

If You are happy with the output (Or has happy as You could be given the circumstances..) remove the `echo` from the loop and run to restore permissions from a safe instance.

Once you are complete, delete the recover-etc directory.
