FROM centos:latest

RUN yum -y update && \
    yum install -y which && \
    yum install -y epel-release 

RUN yum -y install wget make zlib zlib-devel

RUN yum install -y unixODBC-devel sqlite-devel gcc-c++ python34-devel.x86_64 boost-devel

RUN yum install -y openssl openssl-devel

RUN wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz && \
	tar -xvf Python*.tgz && \    
	rm Python*.tgz && \
	cd Python-3.6.2 && \
	./configure && \
	make && \
	make install && \
	cd .. && \
	rm -Rf Python-3.6.2

RUN wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie" http://ftp.wsisiz.edu.pl/pub/pc/pozyteczne%20oprogramowanie/java/jdk-8u131-linux-x64.rpm && \
    yum localinstall -y --nogpgcheck jdk*.rpm && \
	rm jdk*.rpm	

RUN wget http://www-eu.apache.org/dist/drill/drill-1.10.0/apache-drill-1.10.0.tar.gz && \
    tar -xvf apache-drill*.gz && \
    rm apache*.gz 

RUN wget http://package.mapr.com/tools/MapR-ODBC/MapR_Drill/MapRDrill_odbc_v1.3.8.1030/maprdrill-1.3.8.1030-1.x86_64.rpm && \
	yum localinstall -y --nogpgcheck mapr*.rpm && \ 
	rm mapr*.rpm

RUN pip3 install pyodbc && \
	pip3 install pandas && \
	pip3 install pyarrow && \
	pip3 install turbodbc && \
	pip3 install awscli

# You can review and tweak the odbc connections as needed
ADD ./odbc_ini_files/odbc.ini /.odbc.ini 
ADD ./odbc_ini_files/odbcinst.ini /.odbcinst.ini
ADD ./odbc_ini_files/mapr.drillodbc.ini /.mapr.drillodbc.ini

# A simple Python connection to the local drill bit over ODBC
ADD ./tst.py /tst.py 
ADD ./tst.py /tst_turbo.py 
ADD ./data/test.csv /test.csv
ADD ./dfs.sys.drill /tmp/drill/sys.storage_plugins/dfs.sys.drill

ENV JAVA_HOME=/usr/bin/java
ENV ODBCINI=/.odbc.ini
ENV MAPRDRILLINI=/.mapr.drillodbc.ini
ENV LD_LIBRARY_PATH=/usr/local/lib:/opt/mapr/drillodbc/lib/64

EXPOSE 8047
