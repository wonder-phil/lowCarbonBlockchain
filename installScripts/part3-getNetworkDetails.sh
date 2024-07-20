sudo chmod 666 /var/run/docker.sock
export PATH=$PATH:$(go env GOPATH)/bin
export KUBECONFIG=~/.kube/main
kind create cluster --name scotch
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml
kubectl wait --namespace metallb-system                 --for=condition=ready pod                 --selector=app=metallb                 --timeout=90s
docker network inspect -f '{{.IPAM.Config}}' kind
# This will get us the 


