
kubectl exec -i $1 -- bash -c "kafka-topics.sh --create --topic locations --bootstrap-server=kafka-service:9092"