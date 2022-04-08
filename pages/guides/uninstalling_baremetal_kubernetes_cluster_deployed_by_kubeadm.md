# Uninstalling Baremetal Kubernetes Cluster deployed by Kubeadm

This guide will show first how to reset a Kubernetes environment (Deployed by kubeadm) and then how to uninstall Kubernetes completely from the cluster.

## Resetting Kubeadm deployed cluster
If the Kubernetes cluster was deployed via kubeadm. The following command should be run on a cluster to remove from a cluster.

_NOTE: The command will need to be run on all nodes and masters to completely destroy the cluster configuration_

```
kubeadm reset
```

## Uninstalling Kubernetes
To uninstall Kubernetes from the cluster completely, uninstall and purge configuration by running the below.

_NOTE: The command will need to be run on all nodes and masters to completely remove all packages from all servers involved._

```
apt remove --purge kubelet kubeadm kubectl kubernetes-cni
```
