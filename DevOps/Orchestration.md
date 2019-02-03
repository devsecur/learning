# Orchestration

## HowTo

Following [ContainerMind], it is easy to get a first Kubernetes Cluster running on AWS. In the following steps, I will extract the necessary steps.

### Prerequisites

You need the following toolings:
* awscli
* kops
* kubectl
* helm (For deploy complex environments)
* kompose (For convert docker-compose to deployments)

### [AWS]

First we need to create an AWS Basic account. Then, we need to create a user with the following rights:
* AmazonEC2FullAccess
* AmazonRoute53FullAccess
* AmazonS3FullAccess
* AmazonVPCFullAccess
* IAMFullAccess

We need some variables for later:
```
bucket_name=<name>-kops-state-store
export KOPS_STATE_STORE=s3://${bucket_name}
export KOPS_CLUSTER_NAME=<name>.k8s.local
```

Then, awscli has to be configured:
```bash
aws configure

AWS Access Key ID [None]: AccessKeyValue
AWS Secret Access Key [None]: SecretAccessKeyValue
Default region name [None]: us-east-1
Default output format [None]:
```

We need an AWS S3 bucket for kops to persist its state with versioning:

```bash
aws s3api create-bucket \
--bucket ${bucket_name} \
--region us-east-1

aws s3api put-bucket-versioning --bucket ${bucket_name} --versioning-configuration Status=Enabled
```

Now we can create the cluster on AWS:

```bash
kops create cluster \
--node-count=2 \
--node-size=t2.medium \
--zones=us-east-1a \
--name=${KOPS_CLUSTER_NAME}

kops update cluster --name ${KOPS_CLUSTER_NAME} --yes
```

Now we may deploy the Kubernetes dashboard for management capabilities:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml
```

The dashboard can be accessed by extracting the master and add the path:
```bash
kubectl cluster-info
```

Open https://<master>/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/overview?namespace=default

First, you will need the PW for the HTTP Basic auth:
```bash
kops get secrets kube --type secret -oplaintext
```

Then you need the admin token getting via:
```bash
kops get secrets admin --type secret -oplaintext
```

## Projects

### [Kubernetes]

> Production-Grade Container Scheduling and Management https://kubernetes.io

### [Rancher]

> Complete container management platform http://rancher.com

[Kubernetes]: https://github.com/kubernetes/kubernetes
[Rancher]: https://github.com/rancher/rancher
[ContainerMind]: https://medium.com/containermind/how-to-create-a-kubernetes-cluster-on-aws-in-few-minutes-89dda10354f4
