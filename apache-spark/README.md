# apache-spark

This creates a generic Apache Spark image that may be run on a cluster as services. New compute nodes that automatically pick up work may be added by executing a simple Docker command:
```{bash}
docker swarm join --token <some_token> <manager_ip>
``` 

### From the manager node (create a manager node as a service):
```{bash}
docker service create --replicas 1 --network my-app-network --publish 8080:8080 --name master --hostname master ctownsend/apache-spark /bin/bash -c "/spark-2.1.0-bin-hadoop2.7/bin/spark-class org.apache.spark.deploy.master.Master"
```

### From the manager node start up workers as a service:
```{bash}
docker service create --mode global --network my-app-network --name worker ctownsend/apache-spark /bin/bash -c "/spark-2.1.0-bin-hadoop2.7/bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077"
```
Note that the `--mode global` flag is set on the worker service instead of replicas.  Using the `--mode global` option will run one copy of the service on each node of the cluster and automatically run it on any new node that joins the cluster after creation.  This allows worker nodes to join and start working without having to do any additional configuration.

Once running find out where the master service is running and you can submit jobs from that Docker container:
```{bash}
docker service ps master
```

