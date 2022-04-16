# Replicating Two Folders using Rsync

How to set up Rsync to syncronise two folders and schedule this as a repeating task using Cron
In order to syncronise two folders on my ubuntu servers and workstations I use the tool Rsync with the following flags.

```
rsync -avu /media/sourcefolder/ /media/destinationfolder/
```

These options do the following:

-a = Copy symbolic links as symbolic links rather than the files themselves, while preserving information about the file (creation date etc).

-v = Provide a running status of the copy (Ie you can see the file that is currently being processed).

-u = Update the folder, this is useful when running this job using Cron as it will save each file being copied each time, if it finds that the same file exists in both the source and destination it will not copy this again.

It is important in the above example to note the trailing / at the end of the source directory. This ensures that a folder called ‘sourcefolder’ is not created within your destination. If you leave off this / the end result would be all of your data being copied to the following directory:

```
/media/destinationfolder/sourcefolder/
```

Once the above has completed, you will have an exact copy of your data from /sourcefolder/ in /destinationfolder/. We can now look to schedule this job to run on an automated schedule using Cron.

Firstly, we will need to make a bash script to run your rsync job as above.

```
nano /usr/sbin/[yourjobname]
```

Inside this file we will need to put the following

```
#!/bin/bash

rsync -avu /media/serverbackups/ /media/serverbackup/
```

Once you have saved and closed this file, we will need to make it executable before continuing with automation via cron.

```
chmod +x /usr/sbin/[yourscript]
```

To edit the Crontab you will need to run the following command:

```
crontab -e
```

Once inside this file you will need to add a line at the bottom to schedule your sync to run on a schedule. Obviously this is dependent on your requirement, for this example I have set the rsync to occur every 6 hours. I include more information on editing the crontab here.

```
0 */6         * * *           /usr/sbin/rsyncjob > /var/log/rsyncjob.log 2>&1
```

Once you have saved and closed the crontab your job should now run on a regular basis, outputting to the log file as stated above (/var/log/rsyncjob.log – You can adjust this as required).
