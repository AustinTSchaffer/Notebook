# Android Nearby Share to Linux

It is possible (and pretty easy) to send files from an Android device to an Ubuntu laptop over Bluetooth. For my testing, I used a **Google Pixel 4a on Android 11** and a **Dell XPS 15 laptop running Ubuntu 20.10**.

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

This was pretty seamless without any tweaks or additional installs. YMMV, but this should work on any Linux device with a comparable Bluetooth menu. It looks like you can also send files to non-paired devices over Bluetooth, you just need to accept the file transfer.

![](./Accepting%20Files%20over%20Bluetooth%20without%20Device%20Pairing.png)

Android has a feature equivalent to Apple's/iOS's "Air Drop", allowing you to send files over-the-"air", without pairing the 2 devices. The feature is called "Nearby Share". Based on the wording of the feature's menu, it appears that it sends the files over Bluetooth, but a blog post from Google specifies that it could use any number of protocols.

> Once you select the receiver, they will be notified with the option to either accept or decline the file. Nearby Share then automatically chooses the best protocol for fast and easy sharing using **Bluetooth, Bluetooth Low Energy, WebRTC or peer-to-peer WiFi** — allowing you to share even when you’re fully offline.
>
> Source: https://blog.google/products/android/nearby-share/

This indicates that "Nearby Share" is much more complicated, and by extension more secure, than just a Bluetooth file transfer. The menu for Nearby Share also indicates a whole host of features that are exclusive to "Nearby Share". See the screenshots in this directory for how that all looks. Some quick searches on Google showed that Google may be adding the feature to `/Chrom(e|ium)/`, which would allow you to "Nearby Share" to practically any Bluetooth-enabled device supported by Chrome.

In a pinch, a simple anonymous Bluetooth file share does the trick.
