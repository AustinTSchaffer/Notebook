#!/bin/bash

docker container run -p 80:80 --name webserv -d nginx
docker container run -p 3306:3306 --name db -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql
docker container run -p 8080:80 --name apache -d httpd

echo "Waiting for a bit..."
sleep 15

echo "Dumping the mysql logs"
docker container logs db | grep -i password

docker container stop webserv db apache
docker container rm webserv db apache
docker container ls -a

