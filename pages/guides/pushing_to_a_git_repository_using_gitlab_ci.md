# Pushing to a git repository using Gitlab CI

Recently I have been migrating a Jenkins environment to Gitlab CI for automated builds. One thing that was not immediately clear from the documentation on how to push back to your Git repository during the build pipeline.

This process was used heavily throughout the process to automate the bumping of versions in npm package.json files and committing these back to the git branch once bumped.

The first step to acheive this is to create a Personal access token for your account with read and write access to your projects. On Gitlab.com you can use the link below:

[https://gitlab.com/-/profile/personal_access_tokens](https://gitlab.com/-/profile/personal_access_tokens)

Make a note of your access token once generated as this will not be displayed again!

The next stage is to go to the Settings > CI/CD > Variables for either your project or the containing group if you wish to use this key across multiple projects.

Create a new variable here named CI_ACCESS_TOKEN (Or similar, if you use something different here – Ensure you make a note!) with the value as the access token you generated in the previous step. With this being a password you should ensure to mask the variable so that it is not printed in your CI logs.

The below is a very simple gitlab-ci.yaml file which simply clones your repository, bumps using the npm version command, before pushing the changes back to the master branch on Gitlab.

```
image: node:latest
stages:
  - "Git checkout"
  - "Prepare Build"
  - "Bump Version"
  - "commit"
git-pull:
  stage: "Git checkout"
  script:
    - git checkout $CI_COMMIT_BRANCH
    - git pull
    - git status
npm-bump:
  ## Bump the project version
  stage: "Bump Version"
  script:
    - echo "Bumping project version"
    - npm version --no-git-tag-version patch
commit-files:
  ## Commit new files back to master branch
  stage: commit
  before_script:
    - git config --global user.email "gituser@example.com"
    - git config --global user.name "Gitlab CI"
  script:
    - echo "Committing updated files to git"
    - cat package.json
    - git add package.json
    - git commit -m "Bumped package to $SERVICE_VERSION" 
    ## Push back to Gitlab using secret token created earlier with "skip-ci" option to stop builds triggering in a loop
    - git push "https://${GITLAB_USER_NAME}:${CI_ACCESS_TOKEN}@${CI_REPOSITORY_URL#*@}" "HEAD:${CI_COMMIT_REF_NAME}" -o skip-ci
```