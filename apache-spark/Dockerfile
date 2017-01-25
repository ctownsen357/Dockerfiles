FROM alpine:latest

RUN apk update && \
    apk add bash && \
    apk add python && \
    apk add py-pip && \
    apk add openjdk8-jre

ADD http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz /

RUN tar -xvf *.tgz && \
    rm *.tgz 

