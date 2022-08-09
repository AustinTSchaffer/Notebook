---
tags: Docker, Assignment, Databases, Volumes
---

# Assignment 5 - Performing Database Upgrades using Volumes

- Database upgrades with containers
- Create a `postgres` container with named volume `psql-data` using image tag
  `9.6.1`.
- User Docker Hub documentation to learn VOLUME path and versions needed to run
  it.
- Check logs until container is done starting up. Stop the container.
- Create a new postgres container with the same named volume, but using
  `postgres` version `9.6.2`
- Check new logs


## Notes

This is a SQL database. The first container must be stopped before mounting the
volume in the second. DBs cannot have multiple DB Daemons, typically.

You cannot jump versions too quickly (i.e. v1 to v99). This is a limitation of
Postgres and other DB systems, not Docker.


## Environment Variables

**PGDATA.** This optional environment variable can be used to define another
location - like a subdirectory - for the database files. The **default is
/var/lib/postgresql/data**, but if the data volume you're using is a fs
mountpoint (like with GCE persistent disks), Postgres initdb recommends a
subdirectory (for example /var/lib/postgresql/data/pgdata ) be created to
contain the data.

**POSTGRES_PASSWORD.** This environment variable is recommended for you to use
the PostgreSQL image. This environment variable sets the superuser password for
PostgreSQL. The default superuser is defined by the POSTGRES_USER environment
variable.
