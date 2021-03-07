---
tags: Filesystem, Backups, Docker, Docker-Compose, Containers
---

# Setting up a Self-Hosted NAS

This document outlines my journey with setting up a self-hosted solution for on-network backups of my files.

## Samba

Sorry for the lack of details here, I wrote this way after the fact.

At this point, the only hardware I owned that made sense for me to use was a single Raspberry Pi 3B+. This device was already running Pi-hole and Portainer using docker-compose on my network, so I figured what's another service? I added an old laptop HDD to my Pi using a **USB 3.0 to 2.5" SATA III Hard Drive Adapter** and mounted it under `/mnt/drives/shared`. (It's basically just a USB/SATA dongle.)

Unfortunately, the documentation on "Samba in a container" seemed to require a lot of knowledge on how Samba works in general. I instead went the route of setting up Samba as a service running on the underlying OS. This required some configuration

Samba worked as advertised, but after 1 month of setting it up, I had completely forgotten everything I did and whether I had edited any system config files. Also there's no graphical web-based management interface, and you have to set up users/passwords on the underlying OS. This makes it a pain to manage and redeploy.

## Nextcloud

This was the next step in my chain of thinking. It's not really supposed to be used as a NAS, but I don't really have the bandwidth (or hardware) right now to set up FreeNAS, TrueNAS, or OpenMediaVault as the base OS.

Nextcloud let you get straight to setting up users, resetting passwords, viewing files, all through the web browser. Nextcloud also lets you connect via WebDav, which is supported by Deja Dup (which uses `duplicity` on the backend), so that all seems to be working fine. This has been a gentle introduction to what I can use Nextcloud for (I'm also using it to backup photos from my phone), but I max out all of my Pi's compute resources when I try to load thumbnails.

## NAS Backups with Duplicity

I set up `duplicity` (http://duplicity.nongnu.org/) on my RaspberryPi NAS to backup all of my data in Nextcloud. The remote storage destination is a bucket in Backblaze (B2), which was pretty easy to set up and cheaper AWS S3. I currently have about 50GB of documents/pics/vids in my Nextcloud, which will cost me about $0.25/mo to keep it in B2. Even if I had gone with S3 standard infrequent-access (IA), it would have been about 3x the price. Only S3 Glacier would have been cheaper.

Some implementation details, `duplicity` generates and uploads `.difftar.gz` volumes as files are added/modified. To be honest, I wasn't happy with the installation process on my Pi since it's a Python app and the Debian apt-get package version of it is old and uses Python2 apparently. Since it's a diffing backup program, you can put the backup program on a cron without ballooning your storage costs. It's also the same backup system that Ubuntu uses by default, so I was already familiar with it.

## Future Ideas

In the future I may try to use BorgBackup (https://www.borgbackup.org/), which is a file de-duplicating backup program which could theoretically reduce the overall backup size if you have duplicate videos/photos. I didn't try it with this first iteration, since it doesn't look like it supports backing up directly to B2. You have to have an intermediate step where data is backed up to a secondary on-prem location.
