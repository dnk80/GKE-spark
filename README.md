helm repo add spark-operator https://kubeflow.github.io/spark-operator
helm repo update
helm install spark-operator spark-operator/spark-operator --namespace pyfarm --create-namespace


helm repo add cloudnativeapp https://cloudnativeapp.github.io/charts/curated/
helm install spark-operator cloudnativeapp/sparkoperator --version 0.2.3 --namespace pyfarm --create-namespace


kubectl create secret generic gcs-bq  --from-file=comp.json -n pyfarm
