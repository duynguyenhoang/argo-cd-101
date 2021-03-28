ARGO CD HelloWorld
=======================

# Installation

## Softwares

- minikube
- kubectl
- argocd command line

## Argocd login

```
kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2
argocd login localhost:8080
```
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
