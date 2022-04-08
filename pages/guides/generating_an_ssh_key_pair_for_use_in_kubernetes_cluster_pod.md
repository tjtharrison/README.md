# Generating an SSH Key Pair for use in Kubernetes Cluster pod

Below are instructions for creating an SSH key pair from an Ubuntu machine for use on a Kubernetes cluster without having to store the data or key files in plain text in Your Kubernetes configuration.

The first step is to generate Your SSH key pair:

```
ssh-keygen -t rsa -b 4096 -m PEM -f [ssh-k8s].key
```

You can enter a passphrase if appropriate for Your environment

This will generate a public and private key pair in the directory You are currently in, the public key will have the same name as the private key but with file extension key.pub

The next stage is to create a Kubernetes secret from this key pair, ensure to update the command with the namespace that You wish the key pair to be available in, adjust the filenames and provide an appropriate name for the secret.

```
kubectl create secret generic [secret-name] --from-file=ssh-k8s.key --from-file=ssh-k8s.key.pub -n [your-namespace]
```

Finally, You should update Your deployment with a volumeMount for the key pair. This is done by adding a volume to the yaml:

```
volumes:
  - name: ssh-key
    secret:
      secretName: [secret-name]
      defaultMode: 0600
```

Finally update the container spec with a volumeMount for the volume:

```
volumeMounts:
  - name: ssh-key
    readOnly: true
    mountPath: '/root/.ssh/'
```

Apply the configuration file and Your new ssh key pair will be mounted on Your container in the /root/.ssh/ directory – Note that the filenames will be as follows:

```
ssh-privatekey ssh-publickey
```