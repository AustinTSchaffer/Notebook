---
tags: Linux, Filesystem, Backups
---

# File Backups and Snapshots

I'm currently using "Déjà Dup" for creating backups on my Ubuntu laptop. The backups are being saved to my Raspberry Pi B3+, which is running Nextcloud among other things. Yes, I'm Nextcloud as a NAS, deal with it.

Up to this point I've been trusting that Ubuntu/Gnome has the best-in-breed in terms of usability for backups. I like the interface, but the software is limited in terms of features. You can only configure a single backup location, and the schedule is only either daily or weekly.

Similar to `rsync`, there's `rsnapshot`, which could be useful for configuring smarter/better backups of my personal data. I could also use this software on my self-hosted NAS to add a centralized endpoint for offsite backups.

- https://rsnapshot.org/
- https://github.com/rsnapshot/rsnapshot
