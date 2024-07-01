curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

helm version

minikube start

#nginx
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install nginx-ingress ingress-nginx/ingress-nginx

kubectl get service --namespace default nginx-ingress-ingress-nginx-controller --output wide --watch


