ARGO CD HelloWorld
=======================

# Installation

## Softwares

- minikube
- kubectl
- argocd command line

## Argocd login

Port forward to argocd server

```
kubectl port-forward svc/argocd-server -n argocd 8080:44
```

Argocd login

```
# Get the password, it is the pod name
kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2

# User: admin, Password: above result
argocd login localhost:8080
```

## Minikube and Nodeport service

Start following command to access NodePort Service

```
minikube service hello-world -n k102
```

It will open default browser automatically

## Build Hello world images

Build these images locally to simulate different images for different deployments

```
docker build -t hello-world:1.0  --build-arg VERSION=1.0 ./k101
docker build -t hello-world:1.1  --build-arg VERSION=1.1 ./k101
docker build -t hello-world:1.2  --build-arg VERSION=1.2 ./k101
```

# Run

## First deployment

Create a new project

```
argocd app create -f helloworld/helloworld-argocd-project.yaml
```

Go to https://localhost:8080/ to see argocd UI, play with it.

## Create new deployment

Modify ConfigMap in helloworld-deployment.yaml and image tag.

Go to Argocd UI and see the change, click `Sync` to sync project again.

Check configMap value and web server to see the new result.
