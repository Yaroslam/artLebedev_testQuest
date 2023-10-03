FROM ubuntu:latest
LABEL authors="Happy"




RUN apt-get update -qq && apt-get install -y mysql-server mysql-client
ENV MYSQL_DATABASE marvel
ENV MYSQL_ROOT_PASSWORD password
RUN /etc/init.d/mysql start
RUN mysql -u root -e "create database ";

#RUN apt-get update -qq && apt-get install -y git
#RUN apt-get install -y python3.11
#RUN git clone https://github.com/Yaroslam/artLebedev_testQuest.git


#FROM mysql:latest
#ENV MYSQL_DATABASE marvel
#ENV MYSQL_ROOT_PASSWORD password





