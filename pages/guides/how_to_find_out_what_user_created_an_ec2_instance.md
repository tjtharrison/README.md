# How to find out what User created an EC2 Instance

To investigate who created an EC2 Instance on AWS – Follow the below procedure:

* Get the Instance ID and the date on which it was created from the EC2 Management interface .
* Open up Cloudtrail in AWS Console
* Select Event History on the left hand side
* Select “Resource Name“ on the Filter dropdown and enter Your EC2 Instance ID

