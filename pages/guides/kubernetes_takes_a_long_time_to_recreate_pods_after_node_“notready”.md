# Kubernetes takes a long time to recreate pods after node “NotReady”

While testing Kubernetes redundancy and testing the Cluster’s reaction to a node becoming unavailable – I found that the cluster took over 5 minutes to recreate pods after stopping the Kubelet service on one of the nodes.

This is due to the default pod-eviction-timeout level in Kubernetes being set to 5 minutes. To save delving into the default Kubelet configuration this can be bypassed simply by adding the below spec to Your Kubernetes deployment configuration:

```
  template:
    tolerations:
        - key: "node.kubernetes.io/unreachable"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 5
        - key: "node.kubernetes.io/not-ready"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 5
```

Applying this configuration will cause Your pods to be recreated on a healthy node after 5 seconds of the Node being in status “NotReady”
