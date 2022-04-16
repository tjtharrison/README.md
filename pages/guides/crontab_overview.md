# Crontab Overview

Firstly, to edit your crontab, run the following command from your Linux terminal:

```
crontab -e
```

Once inside, you will see a file similar to the below. The only line you really need note is the last one which gives you the format in which you must enter your jobs into this file (highlighted below).

```
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h dom mon dow command
```

In order to clarify this, I have created the below table:

|m	| h |	dom | 	mon |	dow | 	command |
| --- | --- |--- | --- | ---  | ---|
|Minute (0-59) |	Hour (0-23)	| Day of Month (Date 1-31)	| Month (1-12)	| Day of Week (0 -6 – 0 is Sunday)| The command that you wish to run at defined time / date |

Further to just using numbers in your crontab, you have further options as below:

* = Every (Eg Every hour, day, month etc).

*/y = Y = How often within the period of time you would like to run the job. Eg */6 in the H column would mean every 6 hours.

This should suit for most requirements. For example, if you wished to reboot the server every day at 5 minutes past midnight you would enter the below to your crontab

m	h	dom	mon	dow	command
5	0	*	*	*	reboot
If you wished to reboot the server every 2 hours every Saturday you would use:

```
m	h	dom	mon	dow	command
*	*/2	*	*	6	reboot
```

|m	| h |	dom | 	mon |	dow | 	command |
| --- | --- |--- | --- | ---  | ---|
| * | */2 | *	| *	| 5 | reboot |
