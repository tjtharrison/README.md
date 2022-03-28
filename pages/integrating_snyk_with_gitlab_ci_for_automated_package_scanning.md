# Integrating Snyk with Gitlab CI for Automated package scanning

Snyk.io is a great online (Free for open source projects) tool for automated scanning of your project directories. It has built in integrations for various SCM and IDEs, however, I like to keep my projects SCM agnostic in case I decide to change in the future.

This guide will show you how to configure your Gitlab CI Runner (Cloud hosted) to run Snyk testing as part of your pipeline. If you do not yet have a pipeline configured, see this guide for a starter. TBC

## Generating API Token
The first hurdle that must be jumped to integrate your Gitlab CI runner with Snyk is to configure authentication. To allow for your automation platform to authenticate with Snyk (To save running snyk auth on each build) we will be using an API token stored in an environment variable.

https://app.snyk.io/account

Click the above link and click to show your API token, make a note of this somewhere secure.

## Testing
To test your API token from the CLI, run the following in your project directory to ensure your token works:

```
npm install -g snyk
export SNYK_TOKEN=TOKEN_FROM_SNYK
snyk test
```

You should now be given a report of your project security.

## Adding Variable to Gitlab CI
Now we need to save this as an environment variable available to the gitlab runner. Where you store this will depend on whether you wish this to be set on a project or group level. Go to the appropriate page on Gitlab for your requirement and go to Settings > CI/CD > Variables.

## Create a new variable as follows:

Key: SNYK_TOKEN 
Value: VALUE_FROM_SNYK

## Integrating into your Pipeline
This guide assumes you already have your gitlab-ci.yaml file written, if you do not – See here for a getting started guide for building a pipeline file for Gitlab CI and a nodejs and docker container.

Add the following into your gitlab-ci.yaml file (Assuming you are using a nodejs base image).
```
snyk:
  only:
    - master
  stage: "Testing"
  script:
    - npm install -g snyk
    - snyk test
``` 