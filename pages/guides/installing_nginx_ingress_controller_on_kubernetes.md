# Installing nginx ingress controller on Kubernetes

Run the below to install the Nginx ingress controller on a Kubernetes Cluster:

```
git clone https://github.com/nginxinc/kubernetes-ingress/
cd kubernetes-ingress/deployments/helm-chart
git checkout v1.9.0
```

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
kubectl create namespace ingress
helm install nginx ingress-nginx/ingress-nginx --set rbac.create=true -n ingress --version 3.7.1
```

Reference: https://docs.nginx.com/nginx-ingress-controller/installation/installation-with-helm/


## Failed to update lock: configmaps “ingress-controller-leader”

```
Failed to update lock: configmaps "ingress-controller-leader" is forbidden: User "system:serviceaccount:ingress:nginx-ingress-nginx" cannot update resource "configmaps" in API group "" in the namespace "ingress"
```

If you run into the above error on the ingress deployment, this is due to the ingress user not having permissions to update the configmap for the custom deployment. This is fixed by the below steps:

Run the following command to get the name of your ingress controller config map:

```
kubectl get cm -n ingress | grep "[environment]"
```

(Make a note of this)

Now edit the role created by the helm installation:

```
kubectl edit role -n ingress nginx-ingress-nginx
```

Above the section “ingress-controller-leader-nginx”, add the following:

```
- apiGroups:
 - ""
 resourceNames:
  - ingress-controller-leader-[environment]
 resources:
  - configmaps
 verbs:
  - get
  - update
```

Restart the deployment to pick up the change and the errors should subside:

```
kubectl rollout restart deployment [environment]-ingress-controller -n ingress
```