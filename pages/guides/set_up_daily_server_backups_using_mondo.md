# Set up daily server backups using Mondo

Mondo can be used to take full backups of your server and store them in ISO format. If Server recovery is required you can restore by booting a new server with ISO attached.
The first stage is to add the Mondo repositories to your Sources.list file used by Apt and install other prerequisits.

```
cd /tmp
apt-get instal cifs-utils screen
wget ftp://ftp.mondorescue.org/debian/6/mondorescue.sources.list
cat mondorescue.sources.list >> /etc/apt/sources.list
```

We must now edit these sources as they are slightly different using Ubuntu server 12.04 onwards.

```
nano /etc/apt/sources.list
```

Remove .0 from mondo entries at the bottom
We must now update our server and install Mondo.

```
sudo apt-get update
sudo apt-get install mondo
```

We will now need to set up a repeating cron job to run your server backups. I have opted to run this daily but this can be added to your cron.hourly, cron.weekly directories as required. The script below will create a new directory inside the folder /media/serverbackups (In this instance this is my mounted network share) with the servername and today’s date before proceeding to run the server backup. This is a great way of keeping a 7 day retention on your backups. We will then need to make the file executable (Chmod command below).

```
nano /etc/cron.daily/mondo
mkdir -p /media/serverbackups/[servername]/`date +%A` && \
screen -d -m mondoarchive -OiNG -d /media/serverbackups/[servername]/`date +%A` -p [servername] -s 20g
chmod +x /etc/cron.daily/mondo
```

We can now try running the file manually to confirm this is going to work (This can take some time depending on the size and performance of your server).

```
cd /etc/cron.daily/
./mondo
```
