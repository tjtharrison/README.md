# Using the Jira REST API

Jira API Tokens are user-specific, ie the Token that You create will be attached to Your user account and have the same permission as You do via the Web Interface. Eg if You have an admin account and You create an API token, You will have full permissions via the API.

## How to Generate an API Token:
To generate an API Token, click the below link:

https://id.atlassian.com/manage-profile/security/api-tokens

From this page, click the link to Create an API Token and supply an appropriate name (The Automation source You will be acting from – Eg Jenkins)

Once You click Create You will be provided with Your API token, make a note of this somewhere safe as You will not be shown this again.

## Using the Jira REST API:
The Jira REST API is very well documented (Link below), however, the general format for accessing the API with Your user and API Token is as follows:

```
curl -s https://[your-company].atlassian.net/rest/api/3/issue/[endpoint] --user [user@emailaddress.com]:[api-token]
```