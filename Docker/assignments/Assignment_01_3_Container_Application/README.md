---
tags: [Docker, Assignment]
---

# Assignment 1 - 3 Container Application

- Run `nginx`, `mysql`, `httpd` (apache) servers
- Detach all of them and give them all a name.
- Port mappings
    - nginx: 80:80
    - httpd: 8080:80
    - mysql: 3306:3306
- Use `--env` to generate a random root password for the mysql instance in the
  mysql container. Use `docker container logs` to get that password.
- Use docker container stop and docker container rm to clean up afterward.
- Use docker container ls to show that everything is cleaned up.
