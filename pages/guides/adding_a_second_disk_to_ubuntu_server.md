# Adding a second disk to Ubuntu Server

Add disk to your virtual machine to the size you require, choosing either thin or thick provisioning as appropriate. I typically do this while the machine is powered down so that it can be picked up when Ubuntu boots

Make yourself a mount point for your second drive. This can be wherever you chose, though I tend to create these points within the /media/ directory.

```
mkdir /media/[seconddiskname]
```

Make the disk and all subfolders accessible by all users (if required)

```
chmod -R 777 /media/[seconddiskname]
```

Typically your second disk will be sdb (/dev/sdb), though you can confirm this by running the below command to see all physical disks on the server:

```
fdisk -l
```

We will proceed with the below on the assumption that your second disk is sdb (Though adjust as required).
```
fdisk /dev/sdb
```

Create a new primary partition with all other default settings by following the below:

```
n > p > 1 > [enter] > [enter] > w
```

We now need to create a filesystem on the partition on the new disk in order to mount this to your virtual machine:

```
mkfs -t ext4 /dev/sdb1
```

We now need to set this partition to mount to your machine each time it starts, this is done by editing the fstab file.

```
nano /etc/fstab
```

Add a line to the bottom of the file similar to the below, though replacing relevant sections with your partitions / mount points as above.

```
/dev/sdb1 /media/[seconddiskname] ext4 defaults 0 0
```

Run the command below to ‘Mount all’ devices to the system (including your new parition). If this completes with no errors you are good to go. You can confirm this by running the command below and ensuring your mount point is listed:

```
mount -a
df -h
```

The result should be similar to the below, with your new drive at the bottom.:

```
Filesystem Size Used Avail Use% Mounted on
/dev/mapper/server--vg-root 15G 3.2G 11G 23% /
none 4.0K 0 4.0K 0% /sys/fs/cgroup
udev 1.5G 8.0K 1.5G 1% /dev
tmpfs 301M 552K 301M 1% /run
none 5.0M 0 5.0M 0% /run/lock
none 1.5G 0 1.5G 0% /run/shm
none 100M 0 100M 0% /run/user
/dev/sda1 236M 95M 129M 43% /boot
/dev/sdb1 50G 420M 47G 1% /media/seconddisk
```
