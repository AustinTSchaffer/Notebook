# Assignment 10 - Create Stack with Secrets

- Fork Assignment 8 (compose-assignment-2)
- Use drupal:8.2 image
- Remove `build:`
- Add secret via `external:`
- Use environment variable `POSTGRES_PASSWORD_FILE`
- Add secret via `echo "<pw>" | docker secret create psql-pw`
- Copy compose to a swarm node and deploy.
