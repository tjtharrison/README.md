# Running Windows from Dual-Boot in Ubuntu OS

If you, like I, have a Windows machine on your Ubuntu Desktop for dual-booting (Eg for playing games or running Windows-Only apps) I have always wanted to quickly access my Windows Machine without having to reboot into it.

To do this I installed Virtualbox on my Ubuntu Desktop and mounted the physical disk running Windows onto the Virtual Machine which allows me to quickly spin up the VM to test / run something in Windows without having to shutdown my Ubuntu install.

NOTE: It is possible for something to go wrong here so ensure that, before proceeding, you have backed up any data from your Windows disk. 

## Installing Virtualbox
If you don’t have it installed already, go here to download the latest version of Virtualbox onto your Ubuntu Desktop – Download Virtualbox.

## Creating a Virtual Disk file for your Physical Disk
The next step will be to create a virtual disk file to mount your Physical Disk from. Firstly you should get the disk name of your Windows installation on your Ubuntu Desktop – To do this, use fdisk to get a list of your Disks and make a note of the ID for your Windows install (You should be able to tell from the disk size) if not you can remove the grep to see the partition sizes.

```
tim@tjth-desktop:~$ sudo fdisk -l | grep "Disk /dev/sd"
Disk /dev/sda: 111.8 GiB, 120034123776 bytes, 234441648 sectors
Disk /dev/sdb: 55.9 GiB, 60022480896 bytes, 117231408 sectors
Disk /dev/sdc: 223.6 GiB, 240057409536 bytes, 468862128 sectors
```

Once you have the disk name – Run the below Virtualbox command to create a virtual disk file for your physical disk (Replacing the location in which you wish to store the file and the disk name:

```
sudo VBoxManage internalcommands createrawvmdk -filename /mnt/virtualbox/win10-os.vmdk -rawdisk /dev/sdb
```

## Creating the Virtual Machine
The next step is to create a Virtual Machine in the Virtualbox GUI. Open the package and click “New” at the top of the Window – Give your VM an appropriate name and select a location to store the configuration.

When you get to the Disk section, select the Folder icon under “USe an existing virtual hard disk file” and click “Add” to find your virtual disk file created earlier.

Select the Virtual disk file and click “Choose”.

## Booting the Virtual Machine
Once you have configured your machine, select it from the Homescreen and select “Start” to boot!