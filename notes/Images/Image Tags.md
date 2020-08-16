# Images Are Tagged, Not Named

Technically speaking, images do not have names. Images have IDs, but can be
referred to by up to 4 different "name" components. In full, image names contain
the following pieces of information:

- Container Registry
- User
- Repository
- Tag

using the following format:

`<registry>/<user or product or organization>/<repository>:<tag>`

The only required field is `<repository>`. If no `<tag>` is specified, then
Docker assumes that you were referring to the `:latest` tag. If no registry or
"user" is specified, then Docker assumes that you are referring to an official
Docker image, hosted on https://hub.docker.com. Is no registry is specified,
then the same applies where Docker assumes that the image is hosted on
https://hub.docker.com.

For example, there is an official `mysql` image, which refers to a image
containing a MySQL server installation. There is also a `mysql` user in the
Docker hub. If you `docker pull mysql`, you will get an official image from the
`mysql` repository, created and maintained by Docker themselves. The `mysql`
user's (organization's) MySQL server images are stored in the
`mysql/mysql-server` repository, so to get those images, you have to
`docker pull mysql/mysql-server`.

## Tags

Tags pseudo-version tags, pseudo-release tags. They work a lot like git tags.
All they do is point to a specific image ID. The tags can be re-pointed and
pushed to your target container registry at any time.

This is important, because the Docker runtime / Docker daemon only really cares
about the image and layer IDs. The tags are just to help users refer to specific
image IDs, allowing them and Docker to communicate back and forth. As a result,
Docker can be smart about what is pushed and pulled, without worrying about the
human-readable tags.

If you pull a new tag for an existing image, but you already have the image
downloaded under a different tag, Docker will be able to determine that the
image already exists in your local cache, so it does not have to download
anything. After performing this check, you can `docker image ls`, to see that
you can use either tag to refer to the same image.

For example, looking at the official nginx, there are 4 tags that all refer to
the current, non-alpine image of nginx. You can `docker pull` all 4 of those
tags, but it will only result in 1 download. If you pull or run any of those 4
tags later, you may have to download some new images or new image layers,
because the tags may have been repointed by the docker team. This is why it can
be important to refer to a specific "point release"
(breaking.major.minor.release.etc) when building a container stack in
production.

## Adding / Repointing Tags

You can "copy" an image within a single repo, across different repos, or even
between different CRs, without increasing your local filesystem usage with
`docker image tag`.

```bash
docker image tag existingrepo mystuff/myrepo
docker image tag mystuff/myrepo mystuff/myrepo2
docker image tag mystuff/myrepo:2.0.1 mystuff/myrepo:latest-alpine
docker image tag mystuff/myrepo:latest-alpine mysecretcr.azurecr.io/mystuff/myrepo:latest-alpine
```

Using the same command from above, you can tage one existing tag as another
existing tag, overwriting the 2nd pointer specified.

## Notes on `:latest`

`:latest` is just the default tag. You can technically tag anything as
`:latest`, even if it's not actually the latest version of the image for the
specified software. It is generally safe to trust that `:latest` is the true
latest when using an official docker repository from the Docker hub, but it's
always a good idea to read the release notes when pulling an unfamiliar image.

Also, your local latest may not be the actual latest, so be careful when
re-tagging the local latest. Running a `:latest` is more safe, because docker
will automatically check the server to see if the local and remote ":latest"
tags refer to the same image ID.

## Size

When you `docker image ls`, you can see that every tag has its own specified
Size. This size refers to how large the image is if it is isolated from all
other images. If you pull multiple versions of nginx, you'll see that most say
they take 150MB or more. Keep in mind that you cannot determine the total size
of your local cache by summing this column, since it is likely that some of the
images share layers. In fact, if you pull multiple tags that all point to the
same image ID, you'll see them all declare the same number of MB, when in
reality, they all share the exact same layers.

## Loggin In

You can log in to the docker hub, or your own container registry, from the
docker CLI. You only need to login to push images to a public repository on a
public CR, since pulling works like a git clone. If you're using a private
repository on a public CR, or an entirely private CR, you will need to log in
for pulls as well.

```bash
docker login
docker image push me/myimage
```

Login will write your CR credentials to a local file. Obviously, don't use an
untrusted computer when logging in (ya dingus), but if you're not using your own
computer, make sure your docker logout when you are done pushing or pulling your
own images. This will remove the credentials from the local file.

Some CR hosts will have their own login procedures, which could also write to
that local file. For example, AzureCR uses the `az` CLI for CR logins.

```bash
az login
az acr login
docker image push myprivatecr.azurecr.io/me/myimage
```
