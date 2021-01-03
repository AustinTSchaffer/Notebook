# Update Kernel Notes

Source: https://www.linux.org/threads/kernel-update-with-nvidia.19323/

Author: https://www.linux.org/members/jarret-b.29858/

For all Linux users there are times when you want to update the Linux Kernel.
The task is an easy one when using a program like UKUU. And for most kernel
updates it is a very simple procedure. For those systems with proprietary video
drivers, such as NVIDIA, the process is not as easy. When rebooting the system
you end up with a black screen or a strange screen resolution. I am not saying
the process isn’t simple, but it requires more time to fix than if there wasn’t
a proprietary video driver.

## Proprietary Video Drivers

Some drivers used by Linux are loaded into the Kernel. To see a list of Kernel
Hardware Drivers use the command:

```bash
lspci -k
```

If the command produces a list which shows a NVIDIA video driver, then you may
have issues updating the Kernel. What happens is that when some proprietary
drivers are installed the initramfs file is modified to include the new driver.
Once GRUB passes control to the Kernel, the Kernel uses drivers from the
initramfs. If the driver is not contained in the initramfs then they cannot be
loaded by the Kernel during boot. When you install a new Kernel then a new
initramfs file is also downloaded for the kernel and stored in the /boot folder.
When specific proprietary drivers are installed they are copied into the
initramfs file so the drivers can be loaded during boot. For specific hardware,
such as RAID devices and especially video cards, the drivers are very important.
The video drivers are very important since they provide the display for the
Graphical User Interface (GUI). To install the video drivers without the GUI you
need to go to a command-line prompt.

**NOTE:** If you have a simple screen resolution issue then you need to
uninstall and reinstall the NVIDIA drivers.

## Booting to a Command Prompt

The following steps are performed after installing and booting from a new
Kernel. When GRUB starts you need to press the ‘e’ key to edit the menu. Select
the line which loads the new Kernel and press ‘e’ again. The command being
executed by GRUB to load the specified kernel will be shown and you need to add
a 3 at the end of the line which starts with the word ‘linux’. Once completed
press ‘CTRL-X’ or ‘F10’ to boot the newly edited command. The system may take a
little bit to load, but should come to a command prompt asking for your user
name and password to log into the Linux OS.

**NOTE:** Be sure that before you update the Kernel you download the proper
driver for your proprietary hardware. Also check to make sure that the GRUB menu
is displayed long enough for you to press the ‘e’ key. If you do not download
the proper files then be sure you can get them from the Internet at a command
prompt.

## Changing GRUB Boot Delay

There are two lines in the GRUB configuration file which need to be changed. The
GRUB configuration file is found at etc/default/grub and you need to use sudo to
change the file. The two lines to look for are:

```
#GRUB_TIMEOUT_STYLE="hidden"
GRUB_TIMEOUT="10"
```

The lines may be different than these two, but the GRUB_TIMEOUT_STYLE must be
commented out with a ‘#’ sign at the beginning. The GRUB_TIMEOUT value should be
set to 10 or more. Save the file and close your editor. After the file is
changed then GRUB should be updated with the following command:

```bash
sudo update-grub2
```

When the GRUB files are updated then the changes will take effect at the next
boot. Reboot the system and perform the previous steps to boot to a
command-line.

## Installing Proprietary Drivers

Perform the installation of the drivers as instructed by the driver
manufacturer. During installation the drivers should update the initramfs file.
For NVIDIA drivers be sure you run the nvidia-config command to configure the
drivers. You may also want to install the CUDA drivers as well. You can perform
your own update of the initramfs by using the following command:

```
sudo update-initramfs
```

The NVIDIA drivers can be installed as follows:

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-graphics-drivers-396 nvidia-modprobe nvidia-settings
```

**NOTE:** You could install the nvidia-graphics-drivers-390 instead of version
3.96.

You can also install the CUDA drivers as follows:

```
sudo apt-get install nvidia-cuda-toolkit libcudart9.1 libnvrtc9.1
```

Once the drivers are all installed you will need to update the GRUB menu with
the command:

```
sudo update-grub2
```

If your proprietary hardware is something other than an NVIDIA card you need to
perform its required installation procedure and update the initramfs and GRUB.
Once the drivers and kernel are all updated you can reboot and make sure to
choose the newest driver from the GRUB menu.

**NOTE:** If the update does not work properly you can reboot and at the GRUB
prompt you can load an older kernel version. Once loaded you can remove the
newer but failed kernel.

## Removing a Kernel Version

To delete a kernel you can use UKUU as found in the article Kernel Updates. If
you prefer not to use the program you can remove a kernel from the command-line.
To start the process open a Terminal and type the command:

```
dpkg --list | grep linux-image
```

The output shows a listing of all available kernels. You should not remove the
currently running Kernel. To find out the current running version of the Kernel
use the command:

```
uname -r
```

To remove a kernel from the system use the command:

```
sudo apt-get purge linux-image-x.x.x-x-generic
```

Fill in the x’s with the appropriate version numbers from the list of installed
kernels you want to remove. After you have removed all Kernels that you wish to
remove from your system you need to update the GRUB file again with the command:

```
sudo update-grub2
```

The update-grub2 command will remove all of the now deleted Kernel entries in
the GRUB menu so they cannot be accidentally selected since they do not exist.
For everyone who has an NVIDIA card with proprietary drivers and wants to update
their Linux Kernel, I hope this article helps.
