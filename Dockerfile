FROM ubuntu:latest
LABEL authors="Happy"




RUN apt-get update -qq && apt-get install -y mysql-server mysql-client
RUN /etc/init.d/mysql start
RUN mysql -u root -e "create database lebedevart";
RUN apt-get update -qq && apt-get install -y git
RUN apt-get install -y python3.11
RUN git clone https://github.com/Yaroslam/artLebedev_testQuest.git

RUN

EXPOSE 8000





