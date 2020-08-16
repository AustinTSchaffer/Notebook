# Using Secrets in Swarm Services

## Creating Secrets

```bash
ls
# psql_username.txt
cat psql_username.txt
# mypsqluser
docker secret create psql_user psql_username.txt
# someidentifier1
echo "myDBpassWORD" | docker secret create psql_pass -
# someidentifier2
docker secret ls
# someidentifier1   psql_user   ...
# someidentifier2   psql_pass   ...x
docker secret inspect psql_user
```

## Reading Secrets

It's kind of hard to get the info from a secret after it has been created.
That's part of what makes it secret.

To get the secrets back out, you need to specify the secrets that a service uses
when the service is created. You then have to also tell the service which
file(s) hold(s) the the secret information, which will be stored in
`/run/secrets/`. This means that the images have to be designed with files in
mind, not ENV variables, when handling sensitive information.

```bash
docker service create \
    --name psql \
    --secret psql_user \
    --secret psql_pass \
    -e POSTGRES_USER_FILE=/run/secrets/psql_user \
    -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
    postgres

# Go to the node that has the container

docker exec -it psql ls /run/secrets
# psql_user
# psql_pass
docker exec -it psql cat /run/secrets/*
# mypsqluser
# myDBpassWORD
```

## Removing Secrets

You can remove and add secrets to an existing service, but this will cause the
service to completely redeploy all containers. If you want to update your DB
passwords, you may need to come up with a different solution. For now, just know
that you can remove and add secrets to a service.

```bash
docker service update --secret-rm
docker service update --secret-add
```
