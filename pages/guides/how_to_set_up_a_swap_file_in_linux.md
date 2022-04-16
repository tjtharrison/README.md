# How to set up a Swap file in Linux

Swap files are useful if you need to run RAM intensive programs with limited RAM availability.
The first thing you will need to do when setting up a swap file on your system is to decide which partition is best to set this up on (Ensuring it will not impact on performance or force the disk to run out of space when used). To see your space availability run the below command

```
df -h
```

```
Filesystem Size Used Avail Use% Mounted on
/dev/mapper/thvm--vg-root 15G 2.3G 12G 16% /
none 4.0K 0 4.0K 0% /sys/fs/cgroup
udev 235M 8.0K 235M 1% /dev
tmpfs 50M 520K 49M 2% /run
none 5.0M 0 5.0M 0% /run/lock
none 246M 0 246M 0% /run/shm
none 100M 0 100M 0% /run/user
/dev/sda1 236M 95M 129M 43% /boot
```

From the above you can see in the root directory we have ~13GB free so plenty of space for our swap file. You can adjust this as per your requirement

The next thing we will need to do is create the actual swap file itself. This is done using the DD () command as below – You should adjust this as per your requirement. The typical rule followed for swap files is they should be roughly equal to the amount of RAM on your system (Eg if you have 2GB RAM, set up a 2GB swap file).

```
dd if=/dev/zero of=/INTENDEDLOCATIONOFYOURSWAPFILE bs=1024 count=2048k
```

eg the below would create a ~2GB SWAP file on my system in the root partition:

```
dd if=/dev/zero of=/swapfile bs=1024 count=2048k
```

We are now going to tell Linux that this area is available for SWAP and activate this file:

```
mkswap /swapfile
swapon /swapfile
```

Once this is done, if you run the TOP command, you should now see your SWAP area listed (Eg below)

```
top
top - 00:35:56 up 8 days, 14:49, 1 user, load average: 0.34, 0.47, 0.38
Tasks: 82 total, 3 running, 79 sleeping, 0 stopped, 0 zombie
%Cpu(s): 0.3 us, 0.3 sy, 0.0 ni, 99.4 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
KiB Mem: 501784 total, 449268 used, 52516 free, 5348 buffers
KiB Swap: 2617336 total, 6884 used, 2610452 free. 383696 cached Mem
```
