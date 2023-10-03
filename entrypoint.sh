#!/bin/bash
service mysql start
echo "start mysql"
mysql -u root -e "create database lebedevart CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
echo "create DB"
mysql -u root -e "create user 'user' identified by 'password'"
echo "create user for db"
mysql -u root -e "grant all privileges on lebedevart.* to 'user'"
echo "gratn privileges to user"
python3 ./artLebedev_testQuest/djangoProject/manage.py migrate
python3 ./artLebedev_testQuest/parser/main.py



