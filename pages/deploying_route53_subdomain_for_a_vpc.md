# Deploying Route53 Subdomain for a VPC

How to create a Subdomain for a VPC (Eg [vpcname].int.[yourdomain].com).
This is useful for allowing ec2 instances to connect to each other with custom domain names rather than the internal DNS name automatically created by AWS when You create an ec2 instance.

## Setting up the Subdomain in Route 53:

* Open up Route53 Control Panel and Create a new Hosted Zone
* Enter Your Subdomain (Eg [vpcname].int.[yourdomain].com)
* Select Type “Private Hosted Zone for Amazon VPC”
* Select Your VPC ID

## Creating a Record:
* Select Your hosted zone via the Route 53 Hosted Zones Page
* Click “Create Record Set” at the top of the page
* Add Your DNS Record (Eg an A record for one of Your EC2 Instances)

## Setting up Your DNS Host:
* With Your Hosted Zone selected in the Route 53 panel, select the NS (NameServer) records and copy the 3 AWS Nameservers from the “value” field on the right hand side.
* Open up Your DNS Provider and create 3x DNS records with Your subdomain as the Host and the 4 Nameservers provided by AWS as the values for these records.

## Enabling the Hosted Zone in Your VPC:
* Open up the VPC Console and select Your VPC that You setup the Route 53 Endpoint for
* Go to the Tags page and create the following two tags:
  * enableDnsHostnames: true
  * enableDnsSupport: true

## Setting the FQDN Domain for the VPC:
In order to be able to resolve DNS names without the full fqdn (Eg resolving just “db” rather than having to use “db.myvpc.int.mydomain.com”) You need to update the DHCP Option Set for the VPC to provide this Domain via DHCP.

* Open the VPC Console and select “DHCP Options Set” on the left hand side
* Click “Create DHCP options set” at the top of the page and create a new Option set with the following settings configured:
  * Name: [Your VPC Name]
  * Domain Name: The full domain You created earlier (Eg [vpcname].int.[yourdomain].com)
  * Domain name servers: AmazonProvidedDNS
  * NTP Servers: 169.254.169.123
* Go back to the “Your VPC” page and select Your VPC that You setup the Route53 Subdomain for.
* Go to “Actions” and select “Edit DHCP Options set” and select Your new DHCP Option Set

To immediately test the DNS resolution You can reboot one of Your instances on the VPC and ensure You can ping one of the A records You created.