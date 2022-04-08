# Giving other users access to EKS Cluster

By default, only the IAM user who created the EKS Cluster will have access – Follow the below instructions to provide other AWS users access to the Cluster.

## Getting the ARN for the new user
Login to the AWS Console and open the IAM page and find the user who you wish to provide access to the EKS cluster.

When opening the User’s page you will see their IAM ARN at the top of the page – Make a note of this, eg:

```
arn:aws:iam::123456789012:user/example.user
```

## Providing Access
When deploying your EKS cluster via this guide – You will have created a file in your Code Versioning software called “aws-auth-cm.yaml”. This is the file that determines which users have access to the EKS Cluster.

Open this file and add the ARN copied earlier under “mapUsers”. Eg:

```
 - userarn: arn:aws:iam::123456789012:user/example.user
   username: example.user
   groups:
     - system:kubelet-api-admin
     - system:masters
```

Save this file into your Code Versioning and apply the file to your EKS Cluster:

```
kubectl apply -f aws-auth-cm.yaml
```
