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
```
