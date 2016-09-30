# apache-drill
This sets up a 1.8.x version of Apache Drill with ODBC as a Docker image.  I use this along with Python or R to process terabytes of binary and/or CSV data on on AWS.

### Build:
```{bash}
docker build -t ctownsend/apache-drill .
```

### Run a Drill Bit and Map a local folder into the container:
```{bash}
docker run -i -t -v /your/host/path:/container/path ctownsend/apache-drill /bin/bash -c "/apache-drill-1.8.0/bin/drill-embedded
```


### Run a Drill Bit as a service on a cluster:
```{bash}
docker service create --publish 8047:8047 \
--mount type=bind,src=/home/rancher/data,dst=/home/rancher/data \
--replicas 1 --name apache-drill \
ctownsend/apache-drill /bin/bash -c "trap 'exit 0' INT TERM; while true; do echo Hello World; sleep 10; done"
```
In this example I've hacked an entry point to keep it alive but the Drill software doesn't start.  I use this when I want to run it on a cluster.  I'll be circling back to add a proper entry point to launch the drill bit.
