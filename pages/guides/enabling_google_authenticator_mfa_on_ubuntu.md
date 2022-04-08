# Enabling Google Authenticator MFA on Ubuntu

A quick guide on enabling the Google Authenticator App for SSH connections to Ubuntu 16.04 Servers.

_Note: Before proceeding, ensure you have the Google Authenticator app installed on your phone:_

Appstore (iPhone): https://apps.apple.com/gb/app/google-authenticator/id388497605
Play Store (Android): https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_GB

## Installing and Configuring in Ubuntu:
Firstly, install the package to your server:

```
sudo apt install -y libpam-google-authenticator
```

Now run the package to configure the MFA (Note: This should be run as the user on which you would like the MFA applied to). There will be a QR code displaying in the Terminal after running – Open up your Google Authenticator app and click “Add” to scan this barcode.

```
google-authenticator
```

Proceed through the settings, answering as appropriate.

_Note: You should backup the ~/.google_authenticator file in your user directory as this contains the recovery keys. It is also a good idea to ensure you have console access to your server (Or a way of restoring to a previous state) in the event of any of the below going wrong!_

Now run the below comamnds to update the SSH service to force MFA on login (Note: Should be run as root – sudo su included below):

```
sudo su
echo "auth required pam_google_authenticator.so" >> /etc/pam.d/sshd
sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
echo "UsePAM yes" >> /etc/ssh/sshd_config
echo "AuthenticationMethods publickey,password publickey,keyboard-interactive" >> /etc/ssh/sshd_config
sed -i 's/@include common-auth/#@include common-auth/g' /etc/pam.d/sshd
```

## Restart the SSH service to apply:

```
service ssh restart
```