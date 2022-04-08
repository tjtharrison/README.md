# Setting DNS Search Domain in Ubuntu Desktop

To set the DNS search domain on Ubuntu Desktop – Simply run the below commands (Adjusting the second line with your internal domain suffix:

```
nmcli c show
nmcli c modify "Wired connection 1" ipv4.dns-search "example.com"
nmcli c down "Wired connection 1" && nmcli c up "Wired connection 1"
```