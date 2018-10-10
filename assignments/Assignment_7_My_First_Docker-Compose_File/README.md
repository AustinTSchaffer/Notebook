# Assignment 7 - Building a Docker-Compose File

- build a basic compose file for a Drupal CMS website.
- Use the `drupal` image along with a `postgres` image
- Use `ports` to expose the Drupal server on 8080 on the host machine.
- Be sure to set `POSTGRES_PASSWORD` for postgres
- Drupal assumes that DB is on `localhost`. Make sure it is using the POSTGRES
  container
- Extra Credit: Use volumes to store Drupal's unique data.
