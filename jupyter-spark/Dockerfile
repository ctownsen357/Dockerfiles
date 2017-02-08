FROM jupyter/pyspark-notebook
USER root
#RUN   apt-get install python-psycopg2
#RUN   apt-get install python3-psycopg2
RUN REPO=http://cdn-fastly.deb.debian.org \
 && echo "deb $REPO/debian jessie main\ndeb $REPO/debian-security jessie/updates main" > /etc/apt/sources.list \
 && apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
     libpq-dev \
 && apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN   pip install psycopg2 nltk boto3
RUN   pip3 install psycopg2 nltk boto3

USER $NB_USER


