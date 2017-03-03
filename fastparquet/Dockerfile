FROM python:latest
RUN apt-get update
RUN apt-get install -y clang lldb python-llvm libedit-dev
RUN easy_install numpy
RUN easy_install numba
RUN easy_install pandas
RUN easy_install Cython
RUN easy_install six
RUN easy_install snappy
RUN pip fastparquet
