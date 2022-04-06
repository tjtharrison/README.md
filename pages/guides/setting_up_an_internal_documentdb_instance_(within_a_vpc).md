# Setting up an internal DocumentDB instance (Within a VPC)

Follow these instructions to setup an AWS documentDB instance (or replicaset) within a VPC.

* First create two subnets in your required VPC (VPC > Subnets > Create Subnet)
    * Name the subnets [environment]-db-[purpose]-[number] (Eg production-testingdb1|2)
    * Determine two /24 subnet that is not in use within the VPC (Eg 10.10.1.0/24, 10.10.2.0/24)
    * Specify multiple AZs to use (One per Subnet)
* Apply the “Private“ routing table to the subnets to allow internal access from Hemel networks
    * Go to VPC > Route Tables
    * Find the “Private” route table for your Subnet (Eg production Private)
    * Go to “Subnet Associations“ and edit
    * Add your two new subnets
* Create a network ACL for the subnet (Name the same as the subnet, Eg production-db-testingdb)
    * Create inbound rules 27017 from the subnets you require access from (Eg your server IP)
    * Create outbound rules for all TCP to the subnets you require access from (Eg your server IP) to allow ephemeral connectivity.
    * Assign the ACL to your subnets.
    * Select subnet associations at the bottom and add your two subnets.
* Finally in the VPC module, create a Security Group for your Cluster.
    * The Security Group should be named as standard by now [environment]-db-[purpose]
    * This should be tailored for the requirement (Only inbound rules should be required on port 27017 from required networks)
    * Make a note of the security group ID
* Go to documentDB module and create a Subnet Group for your DB
    * The name should match the subnet configuration ([environment]-db-[purpose])
    * Ensure you attach both subnets created previously
* Now go to the Dashboard and click Create Cluster
    * Scroll to the bottom of the page to enable advanced settings
    * Cluster identifier should match the name used throughout the guide ([environment]-db-[purpose])
    * Specify the number of instances required for your cluster
    * Create a strong, secure password for the master account and document this securely!
    * Specify the Security Group required for the databases (Created earlier)
    * Click Create!

## Connecting to the Cluster:
Once your cluster is created, you can connect using the mongo shell. Do not enter your mongodb password as this will be stored plain text in your shell history. Leave the password field blank and you will be prompted for this after pressing return.

You can get the connection string for your cluster from documentDB

NOTE: The below works only for mongo-clients version 4. Greater than this requires TLS (not tested) and older versions complain about a version mismatch.

```
wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
 mongo --ssl --host [cluster-address]:27017 --sslCAFile rds-combined-ca-bundle.pem --username [your username] --password [DO NOT ENTER PASSWORD HERE]
 ```

## Creating additional users in the cluster

Connect to the cluster using mongo tools and create a user as follows:

```
db.createUser(
     {
         user: "username",
         pwd: "password",
        roles:
            [{"db":"admin", "role":"dbAdminAnyDatabase" }]
    }
)
```
 
## Granting users Database access:
In order for a user to be able to read/write data to a specific database, access must be granted for this. Options include: read, readWrite, readAnyDatabase and clusterAdmin

Eg to grant a user readWrite permissions on a specific database, run the following:

```
db.grantRolesToUser( "USERNAME", [{ role: "readWrite", db: "DATABASE_NAME" }])
```