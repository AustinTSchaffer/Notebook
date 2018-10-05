#!/bin/bash

docker container run -d \
    -e POSTGRES_PASSWORD=superdupersecretpassword \
    -v postgres-data:/var/lib/postgresql/data \
    --name old-postgres-db postgres:9.6.1

sleep 10

docker container logs -f old-postgres-db

# 2018-10-05 03:39:08.365 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
# 2018-10-05 03:39:08.365 UTC [1] LOG:  listening on IPv6 address "::", port 5432
# 2018-10-05 03:39:08.382 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
# 2018-10-05 03:39:08.407 UTC [54] LOG:  database system was shut down at 2018-10-05 03:39:08 UTC
# 2018-10-05 03:39:08.417 UTC [1] LOG:  database system is ready to accept connections

docker container stop old-postgres-db

docker container run -d --rm \
    -e POSTGRES_PASSWORD=superdupersecretpassword \
    --volumes-from old-postgres-db \
    --name new-postgres-db postgres:9.6.10

sleep 10

docker container logs new-postgres-db

# LOG:  database system was shut down at 2018-10-05 03:47:16 UTC
# LOG:  MultiXact member wraparound protections are now enabled
# LOG:  autovacuum launcher started
# LOG:  database system is ready to accept connections
