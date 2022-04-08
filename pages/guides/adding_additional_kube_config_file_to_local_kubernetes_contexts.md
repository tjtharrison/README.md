# Adding Additional Kube config file to local Kubernetes contexts

How to add additional Kubernetes configurations to your local Kube config to access additional clusters.
Getting a list of current contexts:

```
tim@tjth-laptop:~/.kube$ kubectl config get-contexts
CURRENT NAME CLUSTER AUTHINFO NAMESPACE
* dev dev dev-admin 
 home kubernetes kubernetes-admin
```

Connect to your new Kubernetes Cluster Master via SSH and edit the ~/.kube/config file created during kubeadm init.

Update the following fields (To an appropriate name for the new cluster):

```
clusters:
 cluster:
  name: [update-this]
contexts:
 context:
  cluster: [same as cluster name]
  user: [clustername-admin]
 name: [same as cluster name]
users:
 -name: [same as user name above]
```

Now, copy this file to your local machine (Eg to ~/.kube/config-[env-name])

Now (After backing up the current config file) you must use kubeconfig to combine your existing kube config file with the new one, to create a new file “config-new” which you then replace the live config file with.

```
cd ~/.kube
cp config config-bak-$(date +%F)
KUBECONFIG=~/.kube/config:~/.kube/config-dev kubectl config view --merge --flatten > ~/.kube/config-all
rm -rf config
mv config-all config
```

If you run the get-contexts command again, you should now see your new Kubernetes cluster listed.
