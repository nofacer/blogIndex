## 前置需求
* Microk8需要enable下面3个组件
```
microk8s enable ingress storage dns
```
* Github上要配两个Secret：`DOCKER_TOKEN`和`KUBE_CONFIG_DATA`

* Microk8s上要手动
```
kubectl apply -f pv.yaml -n blog-indexer
kubectl apply -f secret.yaml -n blog-indexer
```