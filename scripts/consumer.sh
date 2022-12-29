kubectl exec -i $1 -- bash -c "python consumer.py; cat msg"

