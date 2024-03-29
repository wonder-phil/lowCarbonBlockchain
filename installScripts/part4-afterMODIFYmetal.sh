export KUBECONFIG=~/.kube/main
curl https://skupper.io/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
kubectl apply -f metal.yaml
kubectl create namespace ns1
kubectl create namespace ns2
skupper init -n ns1
skupper init -n ns2
skupper token create ./SECRET.yaml --uses 100 -n ns1
skupper link create ./SECRET.yaml -n ns2