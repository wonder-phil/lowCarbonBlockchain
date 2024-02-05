Apply serviceaccount.yaml first to the namespace
```
kubectl apply -f serviceaccount.yaml --namespace ns1
kubectl apply -f serviceaccount.yaml --namespace ns2
```

Then apply the role binder to both namespaces
```
kubectl apply -f rolebinder.yaml --namespace ns1
kubectl apply -f rolebinder.yaml --namespace ns2
```
