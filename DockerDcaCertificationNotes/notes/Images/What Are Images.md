# What is an Image?


> **Official Definition:**
> An image is an ordered collection of root filesystem changes and the
> corresponding execution parameters for use within a container runtime.

In short, an image is an application's binaries, dependencies, and initial configurations,
and any of the metadata that is used to run the image.

Images are not a complete OS. There is no kernel and there are no kernel
modules, such as drivers. **The hostmachine provides the kernel!**

Images can be a single file, or they can be nearly complete Operating Systems,
such as an Ubuntu server with `apt`, Apache, PHP, and any other tech monolith
that is a required dependency of your application. Most programs do not need
Ubuntu as a base image, but a lot of images do use Ubuntu as the base image.
