# Working with Google Docker Image Registry

A brief overview of my experience working with the GCP Hosted Google Docker Registry.

## Registration:
To register for the Google Docker Registry, you can sign up with any Google Account and you will be given $300 credit to spend over the next 12 months. Pricing for the Google Docker registry is very reasonable () so it won’t cost the earth even once this credit has expired.

## Creating the Registry:
The first step will be to to create your docker image registry on GCP. If you don’t have one – Create an account on Google Cloud Platform. I won’t provide details on how to do this here..

https://console.cloud.google.com/

When you have registered and signed into your account, the first thing you should do is create a project (To not store your images in the default project). To do this, click on the dropdown menu at the top (Displaying “My First Project”) and click “New Project”.

On the popup window, type an appropriate name and create your project. Ensure it’s selected at the top of the screen.

Now browse down to “Container Registry” on the left hand side of the screen.

## Signing into your Google Account from your Docker host:
This guide assumes your docker host runs Ubuntu but you can adjust as appropriate for other Operating Systems.

The first stage is to install the latest Google Cloud SDK (https://cloud.google.com/sdk/docs/)

```
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates gnupg
sudo apt-get install -y google-cloud-sdk
```

You should now run the below to setup your Google Account. Select the project you created above for your images when prompted.

```
gcloud init
```

Once the above has completed, you can run the below to Authenticate Docker with the Google Cloud:

```
gcloud auth configure-docker
```

## Signing into Google Image Registry from Kubernetes:
This process is required when you are running a baremetal Kubernetes cluster with images hosted in Google Cloud.

Firstly, from your Google Cloud Account – Create a new Service Account. Browse to “APIs and Services” on the left hand side and select “Credentials”.

On the following page, select “Create credentials” tand Service account key.

Give your account an appropriate namd and select Storage >  Source Repository Administrator as the Role – Download as a json.

Now run the below kubectl command to create the secret:

```
kubectl create secret docker-registry gcp-registry \
--docker-server=eu.gcr.io \
--docker-username=_json_key \
--docker-password="$(cat [your-downloaded-file.json])" \
--docker-email=your@email.address
```

Now, in your deployment yamls, ensure to include the below to use these credentials when pulling images from the GCP registry:

```
spec:
 imagePullSecrets:
  - name: gcp-registry
```

Finally, patch your default service account to use this secret:

```
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "gcp-registry"}]}'
```