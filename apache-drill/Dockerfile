FROM centos:latest

RUN yum -y update && \
    yum install -y epel-release && \
    yum install -y python-pip wget && \
    yum install -y java-1.7.0-openjdk-devel && \
    wget http://apache.mirrors.hoobly.com/drill/drill-1.8.0/apache-drill-1.8.0.tar.gz && \
    tar -xvf apache-drill*.gz && \
    rm apache*.gz 

RUN wget http://package.mapr.com/tools/MapR-ODBC/MapR_Drill/MapRDrill_odbc_v1.2.1.1000/MapRDrillODBC-1.2.1.x86_64.rpm && \
    yum localinstall -y --nogpgcheck MapR*.rpm 
RUN yum install -y unixODBC-devel sqlite-devel gcc-c++ python-devel && \
    pip install pyodbc && \
    rm MapR*.rpm

RUN pip install awscli

# You can review and tweak the odbc connections as needed
ADD ./odbc_ini_files/odbc.ini /.odbc.ini 
ADD ./odbc_ini_files/odbcinst.ini /.odbcinst.ini
ADD ./odbc_ini_files/mapr.drillodbc.ini /.mapr.drillodbc.ini

# A simple Python connection to the local drill bit over ODBC
ADD ./tst.py /tst.py 
ADD ./data/test.csv /test.csv

ENV JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.111-2.6.7.2.el7_2.x86_64/bin
ENV ODBCINI=/.odbc.ini
ENV MAPRDRILLINI=/.mapr.drillodbc.ini
ENV LD_LIBRARY_PATH=/usr/local/lib:/opt/mapr/drillodbc/lib/64

EXPOSE 8047


    
