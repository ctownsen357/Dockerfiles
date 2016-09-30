# apache-spark

This creates a generic Apache Spark image that may be run on a cluster as services.  I need to tweak my start up command but I've tested with the following commands and have run a distributed Spark job on a cluster.

### From the manager node (create a manager node as a service):
```{bash}
docker service create --replicas 1 --network my-app-network --name spark-master ctownsend/spark /bin/bash -c "/spark-2.0.0-bin-hadoop2.7/sbin/start-master.sh; trap 'exit 0' INT TERM; while true; do echo Hello World; sleep 10; done"
```

### From the manager node start up at least one worker as a service; ideally starting them in such a way that there is one per node in the cluster:
```{bash}
docker service create --replicas 1 --network my-app-network --name spark-slave ctownsend/spark /bin/bash -c "/spark-2.0.0-bin-hadoop2.7/sbin/start-slave.sh spark://spark-master:7077; trap 'exit 0' INT TERM; while true; do echo Hello World; sleep 10; done"
```

Once running find out where the master service is running and you can submit jobs from that Docker container:
```{bash}
docker service ps spark-master
```

