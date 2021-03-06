# Deleting an image from the Docker Registry

There is no inbuilt method within the docker provided docker registry so follow the below process to delete images from the registry:

Project repository: [https://github.com/burnettk/delete-docker-registry-image](https://github.com/burnettk/delete-docker-registry-image)

## Downloading Script:
```
curl https://raw.githubusercontent.com/burnettk/delete-docker-registry-image/master/delete_docker_registry_image.py | sudo tee /scripts/delete-docker-image.py >/dev/null
sudo chmod a+x /scripts/delete-docker-image.py
```

## Setting up the Script:

In order to setup the script, you will need to export the environment variable used within the script to specify the Docker registry directory – Adjust this as appropriate for your registry.

Note: This should be set to one level up from the “registry” directory which contains one directory per-docker image on the server.
```
export REGISTRY_DATA_DIR=/mnt/docker-registry/data/docker/registry/v2/
```

Eg my Docker images are stored within `/mnt/docker-registry/data/docker/registry/v2/repositories/`

## Running the Script:

Before attempting to delete images you should first stop the Docker container to ensure there are no race conditions (Note this from the Documentation for the Project).

```
sudo docker-compose stop
```

Once the container is stopped, you can run the `delete-docker-image.py` script with the `–dry-run` flag to simply print what images and layers will be deleted before removing the flag and running it for real (If you are satisfied with the output).

```
/scripts/delete-docker-image.py --image example-image --dry-run
/scripts/delete-docker-image.py --image example-image
```

Once the files have deleted you can start the registry once more:

```
sudo docker-compose up -d
```