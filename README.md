```
# Add the Helm repository
helm repo add spark-operator https://kubeflow.github.io/spark-operator
helm repo update
```

```
# Install the operator into the spark-operator namespace and wait for deployments to be ready
helm install spark-operator spark-operator/spark-operator \
    --namespace pyfarm --create-namespace --wait
```
```
# Create an example application in the default namespace
kubectl apply -f https://raw.githubusercontent.com/kubeflow/spark-operator/refs/heads/master/examples/spark-pi.yaml
```
```
# Get the status of the application - Example
kubectl get sparkapp spark-pi
```

```
# Create Secret form credential file
kubectl create secret generic gcs-bq  --from-file=comp.json -n pyfarm
```
