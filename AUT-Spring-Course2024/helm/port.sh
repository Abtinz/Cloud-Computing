#external ip
kubectl get svc --namespace default -l app.kubernetes.io/name=ingress-nginx

kubectl get pods --namespace default -l app.kubernetes.io/name=ingress-nginx

minikube tunnel