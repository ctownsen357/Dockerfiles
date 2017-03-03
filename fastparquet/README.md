# fastparquet
Builds a simple Docker container with the latest Python 3 version and the following packages:
- numba
- numpy
- pandas
- cython
- six
- fastparquet

I'm using this for converting Stata data sets to the Parquet format to take advantage of compression and to allow SQL query access by Apache Drill.

```{bash}
docker build . -t <your_account>/<some_container_name>
docker run -it --rm -v /<some_host_path>:/code ctownsend/fastparquet bash
```

