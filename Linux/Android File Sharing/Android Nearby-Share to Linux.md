---
tags: [Linux, Android, Bluetooth, FileSharing]
---

# Android Nearby Share to Linux

It is possible (and pretty easy) to send files from an Android device to a Linux laptop over Bluetooth. For my testing, I used a **Google Pixel 4a on Android 11** and a **Dell XPS 15 laptop running Ubuntu 20.10**.

- Pair the Linux/Android devices via Bluetooth
- From Android to Linux:
    - On the Android device, select a file and use "Share"
    - Select "Bluetooth"
    - The transfer should start. On Ubuntu 20.10 (Gnome Shell), the default destination is `~/Downloads`
- From Linux to Android:
    - Select the android device in the "Bluetooth" menu
    - Select "send files"
    - Select the files to send and send them
    - Accept the file share on the Android device
- From Linux to Android via Bash

```bash
# Provided by Gnome, allows you to provide partial info as to what you want to transfer where.
# Asks the user for additional info via a GUI when necessary. File transfers unfortunately
# fail if the file extension is not recognized by the Android device.
bluetooth-sendto
```

This was pretty seamless without any tweaks or additional installs. YMMV, but this should work on any Linux device with a comparable Bluetooth menu. It looks like you can also send files to non-paired devices over Bluetooth, you just need to make sure the destination device is ready to accept the file transfer.

![](./Accepting%20Files%20over%20Bluetooth%20without%20Device%20Pairing.png)

## "Air Drop" and "Nearyby Share"

Android has a feature equivalent to Apple's/iOS's "Air Drop", allowing you to send files over-the-"air", without pairing the 2 devices. The feature is called "Nearby Share". Based on the wording of the feature's menu, it appears that it sends the files over Bluetooth, but a blog post from Google specifies that it could use any number of protocols.

> Once you select the receiver, they will be notified with the option to either accept or decline the file. Nearby Share then automatically chooses the best protocol for fast and easy sharing using **Bluetooth, Bluetooth Low Energy, WebRTC or peer-to-peer WiFi** — allowing you to share even when you’re fully offline.
>
> Source: https://blog.google/products/android/nearby-share/

This indicates that "Nearby Share" is more complicated, probably faster, and probably more secure than a Bluetooth file transfer. The menu for Nearby Share also indicates a whole host of features that are exclusive to "Nearby Share". See the screenshots in this directory for how that all looks. Some quick searches on Google showed that Google may be adding the feature to `/Chrom(e|ium)/`, which would allow you to "Nearby Share" to practically any Bluetooth-enabled device supported by Chrome.

## Bluetooth Transfer Speeds

I transferred a couple of 0.5MB to 1MB files over Bluetooth and was surprised by the time it took to complete each transfer. The latest (Jan 2021) iteration of Bluetooth is Bluetooth 5.2. The specification for Bluetooth 5.2 states:

> There are two forms of Bluetooth wireless technology systems: Basic Rate (BR) and Low Energy (LE). Both systems include device discovery, connection establishment and connection mechanisms. The Basic Rate system includes optional Enhanced Data Rate (EDR) Alternate Media Access Control (MAC) and Physical (PHY) layer extensions. The Basic Rate system offers synchronous and asynchronous connections with data rates of **721.2 kb/s for Basic Rate, 2.1 Mb/s for Enhanced Data Rate and high speed operation up to 54 Mb/s with the 802.11 AMP**

The specifications for Bluetooth 5.1 and 5.0 have the same advertised data rates. `hciconfig -a` shows that my laptop is running Bluetooth 5.1. I tried to use `adb shell` to check `hciconfig -a` on my Pixel 4a as well, but it does not appear that Android 11 has that program installed. I instead connected my phone to my laptop via Bluetooth, used `hcitool con` to get my phone's Bluetooth address, then used `hcitool info <addr>` to get information about my phone's Bluetooth version.

```bash
$ hciconfig -a
hci0:	Type: Primary  Bus: USB
	BD Address: XX:XX:XX:XX:XX:XX  ACL MTU: 1021:4  SCO MTU: 96:6
	UP RUNNING PSCAN ISCAN 
	RX bytes:2156491 acl:6498 sco:0 events:11769 errors:0
	TX bytes:1083329 acl:1008 sco:0 commands:7136 errors:0
	Features: 0xbf 0xfe 0x0f 0xfe 0xdb 0xff 0x7b 0x87
	Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
	Link policy: RSWITCH SNIFF 
	Link mode: SLAVE ACCEPT 
	Name: 'austin-ub-xps'
	Class: 0x3c010c
	Service Classes: Rendering, Capturing, Object Transfer, Audio
	Device Class: Computer, Laptop
	HCI Version: 5.1 (0xa)  Revision: 0x100
	LMP Version: 5.1 (0xa)  Subversion: 0x100
	Manufacturer: Intel Corp. (2)

$ hcitool con
Connections:
	> ACL YY:YY:YY:YY:YY:YY handle 256 state 1 lm MASTER AUTH ENCRYPT 

$ hcitool info YY:YY:YY:YY:YY:YY
Requesting information ...
	BD Address:  60:B7:6E:50:2E:B8
	OUI Company: Google, Inc. (60-B7-6E)
	Device Name: Pixel 4a
	LMP Version: 5.0 (0x9) LMP Subversion: 0x2be
	Manufacturer: Qualcomm (29)
	Features page 0: 0xff 0xfe 0x8f 0xfe 0xd8 0x3f 0x5b 0x87
		<3-slot packets> <5-slot packets> <encryption> <slot offset> 
		<timing accuracy> <role switch> <hold mode> <sniff mode> 
		<RSSI> <channel quality> <SCO link> <HV2 packets> 
		<HV3 packets> <u-law log> <A-law log> <CVSD> <paging scheme> 
		<power control> <transparent SCO> <broadcast encrypt> 
		<EDR ACL 2 Mbps> <EDR ACL 3 Mbps> <enhanced iscan> 
		<interlaced iscan> <interlaced pscan> <inquiry with RSSI> 
		<extended SCO> <AFH cap. slave> <AFH class. slave> 
		<LE support> <3-slot EDR ACL> <5-slot EDR ACL> 
		<sniff subrating> <pause encryption> <AFH cap. master> 
		<AFH class. master> <EDR eSCO 2 Mbps> <extended inquiry> 
		<LE and BR/EDR> <simple pairing> <encapsulated PDU> 
		<non-flush flag> <LSTO> <inquiry TX power> <EPC> 
		<extended features> 
	Features page 1: 0x0f 0x00 0x00 0x00 0x00 0x00 0x00 0x00
	Features page 2: 0x55 0x03 0x00 0x00 0x00 0x00 0x00 0x00
```

Now that we've verified that both of my devices use Bluetooth 5, we check the math to show that Bluetooth 5's "Basic Rate" of 721.2 kb/s would take about 11 seconds to transfer a 1MB file. This lines up with my experience, though a bit optimistic. My testing with a 1MB file showed a progress bar that lasted at least 20 seconds.

Wait hold on, Bluetooth 5 has speeds advertised up to 54 Mb/s in High Speed mode. The Linux kernel has build options for enabling High Speed mode. If I check my `/boot/config-*`, I should be able to see if my Kernel was build with `CONFIG_BT_HS=y`. I checked, and it is in fact NOT enabled.


```bash
$ cat "/boot/config-$(uname -r)" | grep CONFIG_BT_HS
# CONFIG_BT_HS is not set
```

This appears to be due to not being "widely adopted" and "also been referenced upstream by BleedingTooth vulnerability"

Bummer.

Refs:
- https://core.docs.ubuntu.com/en/stacks/bluetooth/bluez/docs/reference/enablement/kernel-configuration-options
- https://www.spinics.net/linux/fedora/fedora-kernel/msg09378.html


## A Faster Open device-to-device Transfer Method?

At this stage there are a few of tradeoffs and problems:

- There isn't really an open standard for device-to-device data transfer, which is why Google and Apple have filled that void with proprietary solutions.
- Using Bluetooth to transfer files works for smaller files, but is much too slow for pretty much anything larger than 1MB.
- You could use a Freemium service like Google Drive to share files, but you're limited by your upload speeds and the space provided to you by a 3rd party. That's also not a great experience if you're standing next to someone and want to wirelessly hand them a PDF.
- Email often has max file size limits, and again, that's not peer-to-peer, device-to-device. You're not going to be sending someone a movie over email.
- If you're at home on your network, you could set up a public file share location on dedicated hardware. That's kind of like using Google Drive, but the transfer speeds will likely be faster. This does also tethers your data transfer to a network you own, takes planning, setup, maintenance, also you have to help your friend get connected.


## Snapdrop

https://snapdrop.net/

This site appears to help devices find each other, then allows the devices to send files to each other P2P using WebRTC. Neat! Works really well. Unfortunately requires a 3rd party for device discovery, but at least the data moves locally-ish. It appears to require both devices to be on the same network.
