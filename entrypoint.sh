#!/bin/bash
usermod -d /var/lib/mysql/ mysql
service mysql start
sleep 5
echo "start mysql"
mysql -u root -e "create database lebedevart CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
sleep 5
echo "create DB"
mysql -u root -e "create user 'user' identified by 'password'"
sleep 5
echo "create user for db"
mysql -u root -e "grant all privileges on lebedevart.* to 'user'"
sleep 5
echo "gratn privileges to user"
python3 ./artLebedev_testQuest/djangoProject/manage.py migrate
sleep 5
python3 ./artLebedev_testQuest/parser/main.py
python3 ./artLebedev_testQuest/djangoProject/manage.py runserver 0.0.0.0:8000
echo "start server on 8000"



