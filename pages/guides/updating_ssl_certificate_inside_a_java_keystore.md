# Updating SSL certificate inside a Java Keystore

## Updating Certificate within jks Keystore (eg For Logstash):
To update the certificate, follow the below process.

The first step is to generate the p12 keystore ready for the jks keystore required by Logstash (The example files are downloaded from the SSL provider)

When prompted, enter a password for your p12 keystore (Store this securely).

```
cat certificate.crt ca-bundle > ssl-all.pem 
openssl pkcs12 -export -name [fqdn] -in ssl-all.pem -inkey certificate.key -out keystore-$(date +%Y).p12
```

We will now convert

```
keytool -importkeystore -destkeystore keystore.jks -srckeystore keystore$(date +%Y).p12 -srcstoretype pkcs12 -alias [fqdn]
```

You will be prompted here for the import and export passwords for your two keystores. If you have done everything correctly you will be prompted if you wish to overwrite the existing certificate. Confirm and commit the new file to git.

## Example import:

```
keytool -importkeystore -destkeystore keystore.jks -srckeystore keystore$(date +%Y).p12 -srcstoretype pkcs12 -alias my.domain.com
Importing keystore keystore2021.p12 to keystore.jks... 
Enter destination keystore password:   
Enter source keystore password:   
Existing entry alias my.domain.com exists, overwrite? [no]:  yes 
```

If you wish to visualise the keystore, there is a handy UI tool called Keystore Explorer – [Download link](http://keystore-explorer.org/downloads.html)