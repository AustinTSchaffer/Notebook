---
tags: Docker, Docker-Swarm, Secrets, Assignment
---

# Assignment 10 - Create Stack with Secrets

- Fork Assignment 8 (compose-assignment-2)
- Use drupal:8.2 image
- Remove `build:`
- Add secret via `external:`
- Use environment variable `POSTGRES_PASSWORD_FILE`
- Add secret via `echo "<pw>" | docker secret create psql-pw`
- Copy compose to a swarm node and deploy.

## Notes

Bash history is written on logout. Also, if you start a command with a space, it
won't be written to the history, as long as `HISTCONTROL=ignoreboth`. If you
forget this, you can commit the history to file, truncate bash history, then log
out and back in.

```bash
# Scorch the Earth method
export HISTCONTROL=ignoreboth
 echo "mypsqlpassword123!!!" | docker secret create mypsqlpassword -
history -a
truncate --size 0 ~/.bash_history
truncate --size 0 ~/.history
exit
```

When specifying external secrets in the stack compose file, you can either use
the boolean syntax, or the mapping syntax. The boolean syntax specifies that the
external secret has the same name as the stack secret.

```yml
secrets:
  external_secret:
    external: true
  mapped_external_sectret:
    name: some_external_secret
```
