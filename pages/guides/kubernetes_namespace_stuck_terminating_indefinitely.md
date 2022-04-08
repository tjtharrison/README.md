# Kubernetes Namespace stuck Terminating indefinitely

I came accross this issue while testing Rancher in my dev Kubernetes Cluster. Trying to delete the cattle-system namespace caused the Namespace to get stuck on Terminating for +24 hours before I decided to investigate further.

Attempting to delete the namespace with –force –grace-period=0 had no affect.

After some time digging, I came across the below article which advised to edit the namespace to check for a “finalizer” field being set in the yaml config. Removing the below two lines and saved allowed the namespace to terminate immediately after closing the file.

```
spec:
finalizers:
- kubernetes
```

https://github.com/kubernetes/kubernetes/issues/60807