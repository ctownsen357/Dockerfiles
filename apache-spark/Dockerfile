FROM alpine:latest

RUN apk update && \
    apk add bash && \
    apk add python3 && \
    apk add py-pip && \
    apk add openjdk8-jre && \
    apk add python-dev && \
    apk add gcc && \
    apk add g++ && \
    apk add openblas openblas-dev && \
    apk add libpng && \
    apk add freetype && \
    apk add freetype-dev

#this is a work-around for numpy install on alpine until upstream resolves
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install pip --upgrade

RUN pip install numpy pandas && \ 
    pip install scipy ipython && \
    pip install scikit-learn matplotlib

RUN apk add postgresql-dev && \
    apk add python3-dev && \
    apk add musl-dev
RUN pip install jupyter nltk psycopg2 boto3

ADD http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz /

RUN tar -xvf *.tgz && \
    rm *.tgz 

