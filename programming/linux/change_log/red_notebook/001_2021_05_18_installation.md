# Installation of the arch OS
The partitions  were created in a minimal manner. With one Swap partition (6G), the EFI FAT32 one (300M) and the linux file system (~450G). They where placed in the main *SSD* in the notebook.

Then, it was installed the following packages:
- base
- base-devel
- linux
- linux-headers
- linux-firmware
- intel-ucode
- git
- vim
- sudo

Then configured locales and language.

Then I configured the hostname and hosts.

Then I created the my user and gave it sudo capabilities.

Then I configured Grub and installed some grub utilities for ufi.
- grub
- efibootmgr
- dosfstools
- os-prober
- mtools

Then I installed the internet manager:
- iwd
- networkmanager
- network-manager-applet
- wireless_tools

And connected to the internet with the nmcli utility with the commands that are available in the internet linux personal man.

Then i disable the grub initial menu altering the `/etc/default/grub` file with the `GRUB_TIMEOUT=0` change with a final `grub-mkconfig -o /boot/grub/grub.cfg` command.

Then i enabled the firewall installing and enabling ufw:
- ufw

No rules where added.

Checked kernel errors and errors in the system journal and with the commands:

- `sudo systemctl --failed`
- and `sudo journalctl -p 3 -xb`

And found problems with the *ACPI BIOS*, then i updated the bios trying to mitigate the problem but this was not solved. But seams like this will not be a very serious problem.

Installed some other programs:
- htop
- neofetch

Then, i installed the graphical interface. For that i installed the Nvidia drivers:
- nvidia
- nvidia-utils
- nvidia-settings
- nvidia-prime (for allowing us to run nvidia only in apps that require it)
- mesa

To execute a program with Nvidia graphics you must use the `prime-run` before the command. A way to test this feature is to install the `glxinfo` (AUR) package. When runned it just outputs the glx information about the environment. So, if you execute `glxinfo | grep "renderer"`, if everything is correct, the intel graphycs will appear, and if you execute `prime-run glxinfo | grep "renderer"` then the Nvidia graphics card will popup.

Them i installed the display server:
- xorg
- xorg-server
- xorg-xinit
- xorg-apps

Them copied the configuration file.

`cp /etc/X11/xinit/xinitrc /home/<user>/.xinitrc`

Them, installed the window manager, compositor and some other stuff:
- bspwm
- sxhkd
- picom
- nitrogen
- arandr
- alacritty

Them i copied the configuration files for the bspwm and sxhkd and edited the sxhkd one to open the alacritty terminal. And then i edited the .xinitrc file to open the bspwm window manager and initiate picom.

Then i configured the AUR helper with a yay installation.


Then i installed some more programs:
- blender
- gotop

Cuda seems to be ok and the computer isn't heating in idle.




