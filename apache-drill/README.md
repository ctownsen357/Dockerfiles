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

