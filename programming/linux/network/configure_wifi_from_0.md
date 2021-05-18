# Configuring the wi-fi
On this document we will explore the process of configuring the wi-fi in the worst case scenario, that is, when you have a broadcom internet chipset.

### Fundamental things
First we must ensure that we have some basic configurations. The first thing we must do is to determine an *hostname* for our computer. This is an identification for our machine in a local network. It functions similarly to an *URL* that symbolizes an *IP* address through an DNS provider.

You must ensure that this is properly configured in your machine. There must be two files, the `/etc/hostname` one, that must have only one word that is your *hostname*, and the other is the `/etc/hosts` file, that must have the following text:

```
# Static table lookup for hostnames.
# See hosts(5) for details.
127.0.0.1		localhost
::1					localhost
127.0.1.1 	hostname.localdomain	hostname
```

This file functions as a local *DNS server*. That is, whenever you enter this hostname text, the computer will interpret the dns specified.

### The driver situation
In an **Asus Z170-delux** motherboard with a **Broadcom Wireless Network Adapter [14e4:43a0] (rev 3)** chip set, You will need check your drivers. Please, read https://wiki.archlinux.org/index.php/broadcom_wireless and download the `sudo pacman -S broadcom-wl-dkms` package and disable some system modules that were conflicting with `sudo rmmod bcma wl` and  then enable the right one with `sudo modprobe wl`.
You can check what driver is being used with the `lspci -k` command. In my computer the following appears:

```
Network controller: Broadcom Inc. and subsidiaries BCM4360 802.11ac Wireless Network Adapter (rev 03)
	Subsystem: ASUSTeK Computer Inc. Device 8659
	Kernel driver in use: wl
	Kernel modules: bcma, wl
```

Notice that the wright one is being used. This must be assured.

### Setting up the inteface
Now that you know that the right driver is installed, you must set up the interface (the wireless one). For that, first, check the available ones with the `ip link` command. A wireless interface must be displayed. Normally it's name is something similar to `wlan0`.
Then you must turn on the interface with the `ip link set wlan0 on` command.
Now you can use any Internet manager program to scan and connect to a wifi access point.

