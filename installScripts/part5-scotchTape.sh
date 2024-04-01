export KUBECONFIG=~/.kube/main
export PATH=$PATH:$(go env GOPATH)/bin
export PATH="$HOME/.local/bin:$PATH"
kubectl apply -f ../roleSetup/serviceacc.yaml --namespace ns1
kubectl apply -f ../roleSetup/serviceacc.yaml --namespace ns2
kubectl apply -f ../roleSetup/rolebinder.yaml --namespace ns1
kubectl apply -f ../roleSetup/rolebinder.yaml --namespace ns2
kubectl apply -f ../backEndListener/backend-listener-1.yaml --namespace ns1
kubectl apply -f ../backEndListener/backend-listener-2.yaml --namespace ns2
kubectl create deployment frontend --image gemajlia/basicwebcontainer:latest --namespace ns1
kubectl create deployment frontend --image gemajlia/basicwebcontainer:latest --namespace ns2
kubectl expose deployment/frontend --port 8080 --target-port 80 --type LoadBalancer --namespace ns1
skupper expose deployment/backend-listener-2 -n ns2
