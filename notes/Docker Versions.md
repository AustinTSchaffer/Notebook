# Docker Versions

Dozen or more editions of Docker. Which one should I use?

Docker is more that just a "container runtime", a lot of complexity has been
added over the years. The tech moves fast, so the version number is very
important.

## 3 Major Types of Installs

- Direct
	- Linux Distros
	- Windows Server 2016
	- Raspberry Pi
- Mac / Windows
	- Mac required some special tweaks to get Docker working
	- Windows spins up a VM for Docker
- Cloud
	- AWS
	- Azure
	- Google Cloud
	- Each come with features specific to those platforms

For linux, Docker is different based on the distro. Don't use the default
package!

## CE vs EE

Docker CE (Community Edition) vs Docker EE (Enterprise Edition). The enterprise
version is a paid (non-free) version and is typically for larger companies.
EE is pay-per-node. Support and extra products; monthly and yearly
subscriptions. [Pricing](https://docker.com/pricing).

## Stable vs Edge

Edge means Beta. Gets new features first. Gets new features (and fixes) every
month, and each version is only supported for one month.

Stable comes out once per quarter. There's about 1 month of overlap between
the previous and new versions, once the new version comes out.

EE is supported for way longer.

