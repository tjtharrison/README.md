# Setting up command shortcuts (Aliases) in Ubuntu

This is handy if you have a repetitive task that requires entering the same command over and over.
Rather than typing out the whole command to restart apache each time a change was made you can simply complete the below.

Gracefully restart Apache:

```
apachectl -k graceful
```

To save having to type this in each time you wish to do this you can simply run the following command:

```
alias agrace="apachectl -k graceful"
```

This will create an ‘alias’ system shortcut for your server, so the next time you type ‘agrace’ your system will know to run the full command ‘apachectl -k graceful’
