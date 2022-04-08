# Using LVM Snapshots to create rollback points on Ubuntu

For the completeness of this guide, I have added a second disk to my Ubuntu server to store the lvm snapshots on (See here for doing this without rebooting in a vitual environment). For this guide I will be taking / restoring Snapshots of my root partition (Eg which could be used to rollback after update installation) though you can adjust the necessary commands below to use any LVM volume you require.

## Adding another disk to Volume Group:
Create a new partition on the second disk (Eg /dev/sdb1)

Make this disk into a physical disk availabe to lvm

```
pvcreate /dev/sdb1
```

You can now add this to your Volume Group for the Logical Volume that you will be taking a snapshot of – You can get the name of this from vgscan:

```
root@tjth-ubuntu:/home/tim# vgscan
VG #PV #LV #SN Attr VSize VFree 
ubuntu-vg 1 2 0 wz--n- <10.00g 36.00m
vgextend ubuntu-vg /dev/sdb1
```

You will see now that there is an additional 10GB of storage available now for snapshots:

```
root@tjth-ubuntu:/home/tim# vgscan
VG #PV #LV #SN Attr VSize VFree 
ubuntu-vg 2 2 0 wz--n- 19.99g 10.03g
```

We are now ready to take a snapshot of our Logical Volume onto the new storage in the Volume Group.

## Taking a Snapshot:
Snapshots can be created any size in the available space but note that it will only allow for this many file changes to be recoverable in the event of a restore. Eg if you create a 1GB snapshot volume but change 1.5GB of data the snapshot restore point will become invalid. It is possible to monitor and extend the snapshot volume (see here for instructions) so adjust the below as necessary to create a suitable size snapshot for your requirement:

To get a list of your Logical Volumes, run the below command:

```
root@tjth-ubuntu:/home/tim# lvscan
ACTIVE '/dev/ubuntu-vg/root' [<9.01 GiB] inherit
ACTIVE '/dev/ubuntu-vg/swap_1' [976.00 MiB] inherit
```

You can now create your snapshot using the logical volume name from the above

```
lvcreate --size 5G --snapshot --name ubuntu_snap /dev/ubuntu-vg/root
```

You can confirm this has been taken successfully by running lvscan again

```
root@tjth-ubuntu:/home/tim# lvscan
ACTIVE Original '/dev/ubuntu-vg/root' [<9.01 GiB] inherit
ACTIVE '/dev/ubuntu-vg/swap_1' [976.00 MiB] inherit
ACTIVE Snapshot '/dev/ubuntu-vg/ubuntu_snap' [5.00 GiB] inherit
```

## Deleting the Snapshot:
To delete the snapshot and keep all of the changes since the snapshot was taken, you can use the lvremove command:

```
lvremove /dev/ubuntu-vg/ubuntu_snap
```

## Reverting to the Snapshot:
To revert to the snapshot, run the below command. Note: Active partitions (Eg currently mounted) will be reverted after a server reboot. To avoid this, you can unmount the volume before reverting (unless you are working with the root volume).

```
lvconvert --merge /dev/ubuntu-vg/ubuntu_snap
```