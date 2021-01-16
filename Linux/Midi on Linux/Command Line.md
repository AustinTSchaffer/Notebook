---
tags: [Linux, Audio, MIDI]
---

# Command Line

There are some cool command line utilities for midi recording and playback. Pretty much all of them work by specifying the port number of a midi device, performing some action in tandem with the MIDI device. You can get all of these programs from the `alsa-utils` package.

```
Package: alsa-utils
Version: 1.2.3-1ubuntu1
Priority: optional
Section: sound
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Debian ALSA Maintainers <pkg-alsa-devel@lists.alioth.debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 2,507 kB
Provides: audio-mixer
Depends: kmod (>= 17-1~), lsb-base (>= 3.0-9), libasound2 (>= 1.2.1), libatopology2 (>= 1.2.2), libc6 (>= 2.29), libfftw3-single3 (>= 3.3.5), libncursesw6 (>= 6), libsamplerate0 (>= 0.1.7), libtinfo6 (>= 6)
Suggests: dialog
Homepage: https://www.alsa-project.org/
Task: ubuntu-desktop-minimal, ubuntu-desktop, ubuntu-desktop-raspi, kubuntu-desktop, xubuntu-core, xubuntu-desktop, lubuntu-desktop, ubuntustudio-desktop-core, ubuntustudio-desktop, ubuntukylin-desktop, ubuntu-mate-core, ubuntu-mate-desktop, ubuntu-budgie-desktop
Download-Size: 1,021 kB
APT-Manual-Installed: no
APT-Sources: http://us.archive.ubuntu.com/ubuntu groovy/main amd64 Packages
Description: Utilities for configuring and using ALSA
 Included tools:
  - alsactl: advanced controls for ALSA sound drivers
  - alsaloop: create loopbacks between PCM capture and playback devices
  - alsamixer: curses mixer
  - alsaucm: alsa use case manager
  - amixer: command line mixer
  - amidi: read from and write to ALSA RawMIDI ports
  - aplay, arecord: command line playback and recording
  - aplaymidi, arecordmidi: command line MIDI playback and recording
  - aconnect, aseqnet, aseqdump: command line MIDI sequencer control
  - iecset: set or dump IEC958 status bits
  - speaker-test: speaker test tone generator
 .
 ALSA is the Advanced Linux Sound Architecture.
```
