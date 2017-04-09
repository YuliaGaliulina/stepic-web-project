#! /bin/bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database mydatabase"
cd ~/web/ask
python manage.py makemigrations
python manage.py migrate
gunicorn -b 0.0.0.0:8000 ask.wsgi:application -D
cd ~/web
gunicorn -b 0.0.0.0:8080 hello:app -D

