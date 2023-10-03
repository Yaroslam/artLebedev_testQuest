FROM ubuntu:latest
LABEL authors="Happy"




RUN apt-get update -qq && apt-get install -y mysql-server
RUN service mysql stop
RUN usermod -d /var/lib/mysql/ mysql
RUN service mysql start
RUN apt-get update -qq && apt-get install -y git
RUN apt-get install -y python3.11




