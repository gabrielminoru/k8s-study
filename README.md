# k8s-study
studying kubernetes

# Requirements
Requirements are `Docker`, `kind` and `kubectl`.
- kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
- kind
```bash
# For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
# For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

ref: https://kind.sigs.k8s.io/docs/user/quick-start


# Cluster setup
1. Create cluster
`kind create cluster --config=kind/kind.yml --name=hello-cluster`

2. Set `kubectl` context
`kubectl config set current-context kind-hello-cluster`

# Deploy
`kubectl apply -f k8s/current/`

# Acessar com port forward
`kubectl port-forward svc/hello-app 9000:1234` expõe em `localhost:9000`.
