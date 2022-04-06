# Setting up Docker access to ECR

How to configure Your local Docker client to Authenticate with AWS ECR (Elastic Container Registry) for accessing Docker images.

This guide assumes You have programatic access to AWS via Access Token etc. If You are setting up a shared machine, use credentials stored in keepass for docker-registry.

Firstly install configure Your aws cli client (Note, this requires the unzip package to be installed):

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure
```

When Your aws cli is configured, run the below to Authenticate Your Docker with the AWS ECR:

```
aws ecr get-login-password --region [your region] | docker login --username AWS --password-stdin https://[your account].dkr.ecr.[your region].amazonaws.com
```

