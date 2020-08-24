# Ubuntu Installing Mainline Kernel Builds

Source: https://wiki.ubuntu.com/Kernel/MainlineBuilds

## Introduction

By default, Ubuntu systems run with the Ubuntu kernels provided by the Ubuntu
repositories. However it is handy to be able to test with unmodified upstream
kernels to help locate problems in Ubuntu kernel patches, or to confirm that
upstream has fixed a specific issue. To this end we now offer select upstream
kernel builds. These kernels are made from unmodified kernel source but using
the Ubuntu kernel configuration files. These are then packaged as Ubuntu .deb
files for simple installation, saving you the time of compiling kernels, and
debugging build issues.

These kernels are not supported and are not appropriate for production use.

## How do I install an upstream kernel?

Following these steps in order will help you successfully test an upstream
kernel.

### Prepare OS to install an upstream kernel

First, if one is using select proprietary or out-of-tree modules (e.g. bcmwl,
fglrx, NVIDIA proprietary graphics drivers, VirtualBox, etc.) unless there is an
extra package available for the version you are testing, you will need to
uninstall the module first, in order to test the mainline kernel. If you do not
uninstall these modules first, then the upstream kernel may fail to install, or
boot.

Choose the proper upstream kernel files

The build directories are nicely organized into per architecture groups. For
example, if one is using a 64-bit/amd64 architecture and wants the `generic`
kernel version you would want those files marked **A**, from the appropriate
group. If you want the `low latency` version, **B**.

```
  Build for amd64 succeeded (see BUILD.LOG.amd64):
AB  linux-headers-4.19.0-041900_4.19.0-041900.201810221809_all.deb
A   linux-headers-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
B   linux-headers-4.19.0-041900-lowlatency_4.19.0-041900.201810221809_amd64.deb
A   linux-image-unsigned-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
B   linux-image-unsigned-4.19.0-041900-lowlatency_4.19.0-041900.201810221809_amd64.deb
A   linux-modules-4.19.0-041900-generic_4.19.0-041900.201810221809_amd64.deb
B   linux-modules-4.19.0-041900-lowlatency_4.19.0-041900.201810221809_amd64.deb
```

### Download upstream kernel files from the Ubuntu archive

Ubuntu Mainline Kernel Archive (sorted by most recent build):
https://kernel.ubuntu.com/~kernel-ppa/mainline/?C=N;O=D

Few things can compromise the security of a Linux system worse than a
compromised kernel. We urge you to carefully verify the integrity of any and all
downloaded kernel packages as explained below.

The Mainline kernel archive has a directory for each tagged release version,
with packages for the generic and lowlatency configurations inside.

Note: If you are testing to isolate a bug or regression, please do not use the
daily folder. Instead, use the latest mainline kernel at the top from the link
above.

### Install all upstream kernel files

Execute the following command against each of the downloaded files in a terminal of your choosing:

    sudo dpkg -i FILENAME.deb

If no errors show up, reboot while holding Shift then select "Advanced options
for Ubuntu", then select and boot into the new entry that looks something like:

    *Ubuntu with Linux 5.5.13-050513-generic


## Problems installing upstream kernels

### Virtualbox

Some errors that may occur while attempting to install an upstream kernel are
the result of VirtualBox being installed. For example,

    '''Error!'''

    Bad return status for module build on kernel: `3.7.0-030700rc2-generic (x86_64)`
    Consult `/var/lib/dkms/virtualbox/4.1.18/build/make.log` for more information.

As per above, you need to either install the modules-extra package, if
available, or uninstall VirtualBox.

### Unsatisfied dependencies

A failure to install can also result from the installed version of Ubuntu
lacking the newer packages the upstream kernel is dependent on for the install
to succeed. For example,

    ...depends on libssl1.1 (>= 1.1.0); however: Package libssl1.1 is not installed.

If you already have the package referenced by the error message (in this
instance, libssl1.1) installed but the version number is beneath the new
kernel's requirements, then you would first need to upgrade your Ubuntu
installation to a newer release. However, if libssl1.1 is not installed at all,
and the version that comes with your release is sufficient, then install
libssl1.1.

### Other install errors

If for some reason the kernel you attempted to build failed, and it's not due to
the above, then continue to test the next most recent kernel version until you
can test to the issue.


## Uninstalling upstream kernels

The upstream kernels have their own ABI namespace, so they install side by side
with the stock Ubuntu kernels (each kernel has a separate directory under
/lib/modules/VERSION for example). This means that you can keep several mainline
and Ubuntu stock kernels installed at the same time and select the one you need
from the GRUB boot menu.

If you want to uninstall an upstream kernel once your need for installing it has
abated, execute the following to find the exact name of the kernel packages you
need to uninstall:

    dpkg -l | grep "linux\-[a-z]*\-"

and then execute the following to uninstall them:

    sudo apt purge ''<KERNEL_PACKAGES_TO_REMOVE>''

Remember that several packages can belong to one kernel version; common headers
plus the architecture specific headers, image and modules are to be expected at
a minimum.


## Mainline kernel build toolchain

These kernels are built with the toolchain (gcc, g++, etc.) from the previous
Ubuntu LTS release. (e.g. Ubuntu 14.04 "Trusty Tahr" / 16.04 "Xenial Xerus" /
18.04 "Bionic Beaver", etc.) Therefore, out-of-tree kernel modules you already
have built and installed for use with your release kernels are not likely to
work with the mainline builds.


## Mainline kernel mapping to Ubuntu kernel

The Ubuntu kernel is not bit-for-bit the same as the mainline. However, one may
find the upstream release that the Ubuntu kernel is based on via the Ubuntu to
mainline mapping table.


## Support (BEWARE: there is none)

The mainline kernel builds are produced for debugging purposes and therefore
come with no support. Use them at your own risk.


## Kernel source code trees

In each directory of the above-linked archive there is a file named
<kbd>COMMIT</kbd> which defines the base commit in Linus Torvalds' master tree
from which they were built. The patches in the same directory ????-* are applied
on top of this commit to make the build tree. A mirror of Linus' tree is
available from git://kernel.ubuntu.com/virgin/linux.git.

First download the COMMIT and patch files ????-* from the mainline build in
question to a temporary directory:

    git clone git://kernel.ubuntu.com/virgin/linux.git mainline && cd mainline
    git checkout -b $(cat ${MAINLINE}/COMMIT)
    git am ${MAINLINE}/????-*


## Verifying mainline build binaries

To provide verification that the published builds are 1. built by the Ubuntu
mainline build system, and 1. are bit-for-bit identical copies of the files on
the server,

the individual files are checksummed and the results are published as a file
named <kbd>CHECKSUMS</kbd> in the same directory. This file is in turn signed by
the mainline builder using the GPG key below, which can be validated against its
record from the Ubuntu Keyserver.

```
pub   2048R/17C622B0 2008-05-01
    Key fingerprint = 60AA 7B6F 3043 4AE6 8E56  9963 E50C 6A09 17C6 22B0
uid                  Kernel PPA <kernel-ppa@canonical.com>
```

The verification can be done by running the following commands:

1. Import the above public key to your keyring (if you haven't already done that):

```bash
gpg --keyserver hkps://pgp.mit.edu --recv-key "60AA7B6F30434AE68E569963E50C6A0917C622B0"
```

2. Download the CHECKSUMS and CHECKSUMS.gpg files from the build directory and
   verify if the CHECKSUMS is signed with the above key:

```bash
gpg --verify CHECKSUMS.gpg CHECKSUMS
# gpg: Signature made .... using RSA key ID 17C622B0
# gpg: Good signature from "Kernel PPA <kernel-ppa@canonical.com>"
# gpg: WARNING: This key is not certified with a trusted signature!
# gpg:          There is no indication that the signature belongs to the owner.
```

3. Verify the checksums of downloaded deb files:

```bash
shasum -c CHECKSUMS 2>&1 | grep 'OK$'
```

You should get a line ending with "OK" for each of downloaded deb file and each type of checksums that are given in the CHECKSUMS file. 


## Upstream kernel details

We currently build five sets of upstream kernels. All formal tags from Linus'
tree and from the stable trees, plus:

- the daily tip of Linus' linux kernel source tree,
- the tip of the drm-next head of Dave Airlie's linux repository daily,
- the tip of the drm-intel-next head of Keith Packard's linux repository daily
  until 2012, after which it has been taken over by Daniel Vetter at
  http://cgit.freedesktop.org/drm-intel/, and in particular, the drm-intel-next
  branch, the tip of the master branch of the debloat-testing tree daily,
- tags from the combined v2.6.32.x.y tree (by StefanBader) which is v2.6.32.x
  with DRM from 2.6.33.y.

This makes these kernels closer to the Lucid kernels which are based on 2.6.32
kernels with DRM backported from the 2.6.33 series.

The tagged releases (as made by Linus and the stable maintainers) are found
under a directory matching their tag name and which kernel configuration they
were built with (<tag>-<series>).

Daily tip of the tree builds are found in the daily sub-directory named for the
date they were made.

Each build directory contains the header and image .deb files for the generic
flavour i386 and amd64 architectures, as well lowlatency.


## Can I install and use a mainline kernel in a live environment?

No. One has two choices to use a mainline kernel:

1. Install the mainline kernel in an installed environment, restart, and choose
   this newly installed kernel.
2. Build a live environment with the new kernel in it. Given the amount of
   effort involved in doing this, it is easiest to use an installed OS to test
   the mainline kernel.
