# Installing ISTIO on Kubernetes

This guide will walk You through the basics of installing all ISTIO features via the “Demo” deployment.

This guide assumes You have a fully functioning Kubernetes Cluster and are running Ubuntu on Your Desktop to install the istioctl package.

## Installing Istioctl
Run the following commands to install istioctl on your Desktop (By downloading the Directory via the ISTIO installation script and creating a symbolic link to your bin directory:

```
cd /opt/
curl -L https://istio.io/downloadIstio | sh -
mv istio-1.4.3 istio && cd istio
ln -s $PWD/istioctl /usr/bin/
```

You can verify that istio is installed by running the following:

```
istioctl help
```

## Installing ISTIO on Your Kubernetes Cluster:
There are various options when it comes to installing Istio (Varying in features). If You are just starting out, it is best to deploy the demo configuration (With all packages) So you can test all of the features before deciding which You will continue to use.

To install the demo ISTIO configuration, run the below istioctl command:

```
istioctl manifest apply --set profile=demo
```

This will take some time to download and deploy all of the ISTIO services – You can watch the progress by running the following (Based on a default install):

```
watch -n 0.2 kubectl get pods -n istio-system
```

Once the Pods have deployed You are ready to go!

## Enabling ISTIO for Your Namespace:
By default, ISTIO will not be enabled on any Namespaces so you will not start getting metrics / monitoring information from Your cluster until it is enabled.

Istio Namespace deployment is acheived by adding a tag to your Namespace as follows (Adjust namespace as required for your Cluster) before restarting the pods in Your Namespace:

```
kubectl label namespace [namespace] istio-injection=enabled
namespace=[namespace]; kubectl rollout restart deployment $(kubectl get deployments -n $namespace | awk {'print $1'}) -n $namespace
```

To disable again if You encounter issues with the default configuartion, simply run the same command with “disabled” Eg:

```
kubectl label namespace [namespace] istio-injection=disabled
```

Accessing Services:
Typically on my Kubernetes Clusters I will use LoadBalancers to access external services. If you are running a Bare Metal cluster – See my guide here on installing MetalLB to run Load Balancers in a Bare Metal Environment.

To access one of the Dashboards (Eg Kiali) via a Load Balancer, simply edit the service and change the Type to “LoadBalancer” (As below) – You will then get an external address from which to Log in.

```
kubectl edit svc -n istio-system kiali

 type: LoadBalancer

tim@tjth-desktop:/opt$ kubectl get svc -n istio-system | grep "kiali"
kiali LoadBalancer 10.96.249.239 192.168.1.102 20001:30388/TCP 20m
```

## Uninstalling Istio:

To uninstall Istio (Provided You used the istioctl installation command above) You can simply run the following:

```
istioctl manifest generate --set profile=demo | kubectl delete -f -
```