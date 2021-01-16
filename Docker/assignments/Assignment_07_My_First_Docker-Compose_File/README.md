---
tags: [Docker, Docker-Compose, Assignment]
---


# Assignment 7 - Building a Docker-Compose File

- build a basic compose file for a Drupal CMS website.
- Use the `drupal` image along with a `postgres` image
- Use `ports` to expose the Drupal server on 8080 on the host machine.
- Be sure to set `POSTGRES_PASSWORD` for postgres
- Drupal assumes that DB is on `localhost`. Make sure it is using the POSTGRES
  container
- Extra Credit: Use volumes to store Drupal's unique data.

## Solution

I also added `adminer` to the solution. This allowed me to debug connections to
the db image, because I'm unfamiliar with Postgres, along with any command line
utilities for connecting to Postgres. I also wanted to see how `adminer` worked,
since I've seen it on so many sample `docker-compose.yml` files.
