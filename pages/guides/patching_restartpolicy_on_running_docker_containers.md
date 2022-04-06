# Patching RestartPolicy on running Docker Containers

To view the current RestartPolicy for a running docker container, run the below command (Requires jq to be installed)

```
docker inspect [container-name] | jq -r '.[].HostConfig.RestartPolicy'
{
  "Name": "always",
  "MaximumRetryCount": 0
}
```

If the response is not correct for your requirement, you can patch the running container with the following command:

```
docker update --restart=[required-policy]:0 [container-name]
```