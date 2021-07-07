# Virtual box on arch linux
Simulate computers in your system is very usefull, to have access to plataform specific programs, or testing your software in different systems, or even trying other operating systems. For that we will use `virtualbox`.

First install the `virtualbox` package via `pacman` if you use arch linux or any derivative.

- for the linux kernel, choose `virtualbox-host-modules-arch`
- for any other kernel (including linux-lts), choose `virtualbox-host-dkms`

Then you must load the kernel modules if you don't want to reboot. For that, perform the `modprobe vboxdrv` command.

To access host USB devices in guest machines we need to add the user to the `vboxusers` group. For that you will need to performe the command:

```bash
sudo usermod -aG vboxusers fejori
```

Then you must install `virtualbox-guest-iso` to write to the guest image new information other than arch linux.

Then it's nice to download the extension pack (oracle extension pack) that provides aditional features. Lots of usefull stuff. But this is a non free license, only allowed for personal use.

## Installing an OS
Now you must download an ISO for your virtual machine. It can be other linux distribution or even windows, OpenBSD or MAC. Just remember researching the requirements for each OS.

