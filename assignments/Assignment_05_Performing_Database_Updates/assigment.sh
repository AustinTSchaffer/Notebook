#!/bin/bash

echo "======================"
echo "STARTING VERSION 9.6.1"
echo "======================"

docker container run -d \
    -v postgres-data:/var/lib/postgresql/data \
    --name old-postgres-db postgres:9.6.1

sleep 5; docker container logs old-postgres-db

# 2018-10-05 03:39:08.365 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
# 2018-10-05 03:39:08.365 UTC [1] LOG:  listening on IPv6 address "::", port 5432
# 2018-10-05 03:39:08.382 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
# 2018-10-05 03:39:08.407 UTC [54] LOG:  database system was shut down at 2018-10-05 03:39:08 UTC
# 2018-10-05 03:39:08.417 UTC [1] LOG:  database system is ready to accept connections


docker container stop old-postgres-db

echo "======================="
echo "STARTING VERSION 9.6.10"
echo "    VARIANT 1 of 2     "
echo "======================="

docker container run -d \
    --volumes-from old-postgres-db \
    --name new-postgres-db postgres:9.6.10

sleep 5; docker container logs new-postgres-db

# LOG:  database system was shut down at 2018-10-05 03:47:16 UTC
# LOG:  MultiXact member wraparound protections are now enabled
# LOG:  autovacuum launcher started
# LOG:  database system is ready to accept connections

docker container stop new-postgres-db
docker container rm old-postgres-db new-postgres-db

echo "======================="
echo "STARTING VERSION 9.6.10"
echo "    VARIANT 2 of 2     "
echo "======================="

docker container run -d \
    -v postgres-data:/var/lib/postgresql/data \
    --name new-new-postgres-db postgres:9.6.10

sleep 5; docker logs new-new-postgres-db
docker container rm -f new-new-postgres-db
docker volume rm postgres-data
