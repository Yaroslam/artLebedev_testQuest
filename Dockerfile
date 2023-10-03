FROM ubuntu:latest
LABEL authors="Yaroslam"


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -y mysql-server mysql-client
RUN apt-get update -qq && apt-get install -y git
RUN apt-get install -y ufw
RUN apt-get install -y pkg-config
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN apt-get install -y mysql-client libssl-dev
RUN ufw allow 8000
RUN git clone https://github.com/Yaroslam/artLebedev_testQuest.git
RUN pip install -r ./artLebedev_testQuest/requirements.txt
EXPOSE 8000
ENTRYPOINT ["sh", "./artLebedev_testQuest/entrypoint.sh"]




