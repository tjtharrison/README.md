# Using an alternative port for Gitlab Server oAuth with Gitlab.com

This is a quick page on how to resolve the below errorr if You run a Gitlab server onsite (Possibly docker hosted) and get this error when trying to setup Oauth integration with gitlab.com following this guide from Gitlab.

The redirect URI included is not valid Error Gitlab.com Oauth

I found in my docker hosted environment that this was caused by the Gitlab docker-compose file redirecting port 8000 to 80 so the Gitlab service believes it is listening on port 80 – Causing the oAuth integration to fail.

The fix for this is simply either to setup a reverse proxy for http://your-server.your-domain.com and skip the port in the Gitlab Application setup or to update your gitlab.rb file with the below option.

```
external_url 'http://your-server.your-domain.com:8001'
```

Once You have done this, update your docker-compose to forward to the correct port, eg:

```
 ports:
  - '8001:8001'
```