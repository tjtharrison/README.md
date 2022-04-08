# Setting up a Check_MK user with limited host access

This guide should be used to setup a user on check_mk with access only to a subset of hosts monitored within Check_mk.

In this example, we will be creating a user that should ONLY have access to servers hosted on digital ocean).

## Reviewing Role Access:
First thing to do will be to review the roles in check_mk to confirm the role that you will be assigning to the new user has “See all host and services“ set to “no”. NOTE: The role will determine the access that the user has within check_mk (Eg permissions to perform actions on hosts) so this should be configured as per your requirement..

## Creating Contact Group:
Browse to “Contact Groups“ on the left hand side of Check_MK and click “New contact group“ at the top of the page.

Add a name and alias as required, eg


> Name: digitalOcean ## The internal name used by check_mk
> Alias: Digital Ocean ## The nice name visible within the UI.

Create the group and apply the config changes.

## Creating Contact Group Rules:
The next stage is to create a rule which will automatically add the required hosts to the Contact Group that will be used by our new user.Setting up a Check_MK user with limited host access

_NOTE: The below instructions should be adjusted depending on the setup, eg if you wish to only add servers with a tag of “database” – Use this in the CG Rule instead._

On the Contact Group page in Check_MK, click the “Rules“ button at the top of the page

On the following page, click on “Assignment of hosts to contact groups” and Create rule in folder at the bottom of the page.

Add a description for the rule (Eg Digital Ocean Servers) and apply conditions as appropriate for your check. In our example we will add all hosts from the “Folder“ DO (Digital Ocean):

## Applying CG to User:
Go to the users page from the link on the left hand panel and edit / create your user that you wish to apply these changes to.

Under the Contact Groups section, tick the box to add them to the newly created Contact group, ensure they are a member of the Role that you checked earlier and job done!
