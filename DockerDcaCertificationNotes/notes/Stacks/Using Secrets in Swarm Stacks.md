# Using Secrets in Swarm Stacks

**Note:** Your compose file version must be 3.1 or later.

```yml
# File: stack.yml
version: "3.1"

services:
  image: postgres
  secrets:
    - psql_password
    - psql_user
  environment:
    POSTGRES_PASSWORD_FILE: /run/secrets/psql_password
    POSTGRES_USER_FILE: /run/secrets/psql_user

secrets:
  psql_user:
    file: ./psql_user.txt
  psql_password:
    file: ./psql_pass.txt
#  some_other_secret:
#    external: my_super_secret_secret
```

Either specify secrets as files that exist in the same directory as your
stack.yml, or specify your secrets externally to your stack configuration,
either through the CLI or API, and pull them in using the `external` key under
the secret key.

Then, you assign the secrets container-by-container, specifying the need-to-know
of the individual secrets. This is the short form, but you can also specify the
access levels of the secrets within the container, for multi-user containers.

```bash
vim psql_user.txt psql_pass.txt stack.yml
docker stack deploy -c stack.yml mystack # Creates the secrets
docker stack rm mystack # Removes/deletes the secrets
```

If you're in a production environment, mIn In ake sure that whatever process you're
using to create the secrets on the server, also cleans up any residual instances
of that secret data.

- text files (delete them)
- bash history (truncate)

## Docker Compose

It's possible to use file-based secrets in Docker Compose. This allows you to
test your stacks locally, but you don't get any of the benefits of the stack
secrets. For one, you can't use external secrets, because there is no Raft DB to
store the secrets, so the secrets have to be written as local files. Also, the
secrets are not encrypted on disk, because compose just creates a bind mount
from the local file into `/run/secrets/`.

DOCKER COMPOSE IS ONLY FOR DEVELOPMENT PURPOSES.
