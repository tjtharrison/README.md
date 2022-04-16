# Installing SSL Certificate for Apache

A guide on how to install an SSL Certificate purchased from a registered provider (In this example I use Godaddy) and install this ready for use by Apache web server.
The first stage in this is to purchase an SSL certificate online, if you do not wish to purchase an SSL certificate – Ubuntu comes with a ‘Self-signed’ certificate already which can be found in the following directory:

```
SSLCertificateFile – /etc/ssl/certs/ssl-cert-snakeoil.pem
SSLCertificateKeyFile – /etc/ssl/private/ssl-cert-snakeoil.key
```

If you have already purchased your SSL certificate, the first thing we must do will be to generate a Certificate Signing Request (CSR) and enable the SSL mod for Apache2. This is done by running the following command from your Ubuntu Server:

```
a2enmod ssl
mkdir /etc/ssl/certificate
openssl req -new -newkey rsa:2048 -nodes -keyout /etc/ssl/certificate/servername.key -out /etc/ssl/certificate/servername.csr
```

While generating the CSR, you will have to enter details on your server, in order to ensure that your SSL certificate is valid – Ensure you enter this with the correct information. You can enter a passphrase if you wish, if you chose not to there may be security risks.

We will now need to copy the entire CSR file into your Certification issuer’s site – This will be different dependant on the provider but their site should be self explanitory. Run the following to print your CSR file:

```
cat /etc/ssl/certificate/servername.csr
```

Once you have uploaded your CSR file, you will likely have to validate your ownership of the domain (Either by creating a TXT DNS file entry or uploading a HTML file onto your webserver – Though this may change depending on your SSL provider). Once this has been verified, you will be able to download your SSL certificate – You will want to chose the option to Download for Apache if this is possible, though really as long as you have your CRT file that will be all that you require.

Download your SSL certificate onto your Web server and store it in a sensible location (We can use the `/etc/ssl/certificate directory` from before).

Firstly, ensure you have the unzip package installed on your server

```
apt-get install unzip
```

Then proceed to unzip the downloaded SSL certificate to the /etc/ssl/certificates directory:

```
mv [your unique code].zip /etc/ssl/certificates/
cd /etc/ssl/certificates/
unzip [your unique code].zip
```

Now we will need to configure our website to use this SSL certificate. You will now need to create / update your config file in Apache (This is dependant on your setup):

```
nano /etc/apache2/sites-enabled/yoursitename.conf
```
```
<VirtualHost *:443>
 ServerAdmin [youremailaddress]
 ServerName [yourwebsiteaddress]
DocumentRoot /var/www/[yourwebsite]
 ErrorLog ${APACHE_LOG_DIR}/error.log
 CustomLog ${APACHE_LOG_DIR}/access.log combined
 RewriteEngine On

SSLEngine on
SSLCertificateFile /etc/ssl/certificate/[yourcertificate].crt
SSLCertificateKeyFile /etc/ssl/certificate/[yourcertificate].key
</VirtualHost>
```

Once you have created this Apache config file, you will need to restart your apache service before browsing to your site and confirming the SSL certificate is functioning as required.

```
service apache restart
```
