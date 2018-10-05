# Persistent Data using Bind Mounts

Bind Mounts map a host file or directory to a container file or directory.
Basically adds a link from a Docker container to a host file. This skips the UFS
and the host files take precedence of the files that are in the Docker
container.

Docker can tell the difference between bind mounts and named volumes, based on
how the host path is specified:

    Create a named volume
    -v "myfile:/myfile"

    Create a bind mount
    -v "$(pwd)/myfile:/myfile"

Bind mounts cannot be specified as part of the image, and have to be specified
when the container is run/created.

Specifying bind mounts in Windows can be annoying:

    -v //c/Users/Etc

If you're using Docker compose, or some other tool like that, you have the
option to use locally rooted file paths like `./`. If you're using Docker run,
you'll likely have to use paths from root `/`.

Remember, HOST ALWAYS WINS. You can bind mount overtop of an existing volume, so
be careful. There's potential to destroy data with careless bind mounting and
careless volume mounting.

## Nginx

```bash
docker container run -d --rm -p 80:80 \
    --name nginx \
    -v "$(pwd):/usr/share/nginx/html" \
    nginx

echo "<h1>Hello!</h1>" > ./index.html
curl localhost
# <h1>Hello!</h1>

echo "<h1>Goodbye!</h1>" > ./index.html
curl localhost
# <h1>Goodbye!</h1>

docker container rm -f nginx

# Bonus, binds are not volumes
docker volume ls
```
