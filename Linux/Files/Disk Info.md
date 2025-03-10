---
tags: Linux, Filesystem, Bash
---

# Linux Disk Info

There's a few GNU Coreutils that you can use to get information about the filesystem and the physical hardware underlying the filesystem.

```bash
# List all block devices and their mount point, essentially
# shows where one disk begins and the other ends
lsblk

# Lists all filesystems, including their sizes/capacities
# using -h to show the size info in a human-readable format.
# This also shows mount points.
df -h

# Gets the disk usage summary of all objects in the current directory,
# human readable output, and sorts the output based on size.
du -sh * | sort -hr

# Finds the size of all directories named "site-packages" or "venv" or "node_modules"
du -h | egrep '/site-packages$'
du -h | egrep '/venv$'
du -h | egrep '/node_modules$'
du -h | egrep '/(venv|node_modules)$'
```
