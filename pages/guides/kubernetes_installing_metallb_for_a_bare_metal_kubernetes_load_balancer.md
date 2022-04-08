# Kubernetes Installing MetalLB for a Bare Metal Kubernetes Load Balancer

MetalLB (https://metallb.universe.tf/)[https://metallb.universe.tf/] is a great tool for installation on a bare metal Kubernetes Cluster to allow You to use Load Balancer yamls in Your dev environment before Your project is deployed to a Cloud Hosted service such as AWS (Which handle Load Balancers for You).

## Installation:
First – Apply the full Yaml from MetalLB repository:

```
kubectl apply -f https://raw.githubusercontent.com/google/metallb/v0.12.1/manifests/metallb.yaml
```

Once this deployment has completed, You should generate a configMap.yaml for Your Kubernetes Cluster. This should be updated with a range of IP addresses on Your subnet that can be assigned by MetalLB (Eg outside of Your DHCP range / not in use by other servers).

```
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: | 
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - 192.168.1.100-192.168.1.120
```

Apply this Yaml File and You will be able to create Load Balancer service types on Your cluster – To access the Load Balancers, after applying check kubectl get svc for the IP address allocated to your Balancer.
