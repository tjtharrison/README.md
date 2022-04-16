# Setting up Ubuntu Apt-cacher

## Configuring Apt-cacher server:
Install required pre-requisits:

```
apt-get install apt-mirror apache2 samba
```

Create a folder which is to be used as your update cache location. I typically do this on a separate disk to the main OS install to ensure if it runs out of space that there is no OS corruption.

We now need to edit the apt-cacher config file in order to ensure that it stores cached files to the correct directory.

```
nano /etc/apt-cacher/apt-cacher.conf
```

In the above file, find the line 'cache_dir' and change this to your folder as assigned above. Eg:
`cache_dir = /media/aptcacher`

## Configuring Clients:

Run the below commands from your clients that you wish to have their updates cached on the cacher server.

```
nano /etc/apt/apt.conf.d/01proxy
```

Enter text as below (substituting appropriate sections as per your setup).

`Acquire::http::proxy "http://[yourservername]:3142"` 
Once saved and exited, run an update on your client to ensure it updates properly

```
apt-get update
```
