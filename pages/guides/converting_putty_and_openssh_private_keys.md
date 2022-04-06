# Converting Putty and Openssh Private Keys

This is something that I have had to do time and time again, to convert between openssh and putty private keys for Windows users who also dabble with linux servers.

All of these commands should be run on an Ubuntu server.

Before proceeding, ensure you have both openssh and putty-tools installed:

```
sudo apt-get install openssh-server putty-tools
```

## Converting from Putty PPK to Openssh:
-O specifies the output type, -o specifies the output filename:

```
puttygen id_rsa.ppk -O private-openssh -o id_rsa
```

## Converting Openssh private key to Putty PPK:

```
puttygen id_rsa -o id_rsa.ppk
```