# Set up Fail2Ban

Fail2Ban is a security package for Linux which polls log files and blocks suspect IP addresses for X minutes based on a defined set of rules (Eg 5 incorrect SSH password attempts).
The first stage is to install fail2ban

```
apt-get install fail2ban
```

This should start the service automatically but you can double check by checking the status:

```
root@linx:/etc/ service fail2ban status
 * Status of authentication failure monitor 
* fail2ban is running
```

Once fail2ban is installed and running you should setup policies based on applications installed on your server. All configuration files are stored in the `/etc/fail2ban/` directory.

```
nano /etc/fail2ban/jail.conf
```

Scroll down and ensure that the appropriate services for your server are enabled (SSH example below)

```
[ssh]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 6
```

Fail2ban by default supports various linux services (eg postfix, apache etcetc). After changes made to this file you should restart the fail2ban service to ensure these services are being monitored

```
service fail2ban restart
```
