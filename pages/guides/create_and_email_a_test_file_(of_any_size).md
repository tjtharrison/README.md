# Create and email a test file (of any size)

This comes in handy when testing email filesize filtering on a new mailserver.

First we need to install sendmail (The program we will be using to send the email).

```
apt-get install sendemail
```

The next step will be to browse to an appopriate directory (eg /tmp/) and create a file for you to use to send your mail (Ensure you have sufficient storage space available if you are looking to send very large files!)

```
cd /tmp/
dd if=/dev/zero of=file.txt count=[number of BLOCKS] bs=[Read / Write BYTES at a time]
```

EG:
```
tim@thvm:/tmp$ dd if=/dev/zero of=file.txt count=4096
4096+0 records in
4096+0 records out
2097152 bytes (2.1 MB) copied, 0.0146288 s, 143 MB/s
```

Now we just need to send an email with the created file attached:

```
sendemail -f test@example.com -t example@test.com -m “This is a test message” -u “Subject” -a /tmp/file.txt
```

-f = From
-t = To
-m = The message body
-u = The message subject
-a = The location of the attachment you wish to send
