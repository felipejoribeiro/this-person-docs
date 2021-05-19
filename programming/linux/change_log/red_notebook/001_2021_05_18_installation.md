# Installation of the arch OS
The partitions  were created in a minimal manner. With one Swap partition (6G), the EFI FAT32 one (300M) and the linux file system (~450G). They where placed in the main *SSD* in the notebook.

Then, it was installed the following packages:
- base
- base-devel
- linux-lts
- linux-lts-headers
- linux-firmware
- intel-ucode
- git
- vim
- sudo
- dialog

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

Configured the AUR helper
It installed go in the process. But i got rid of it with the command:

`sudo pacman -Rns $(pacman -Qtdq)`

Then, i installed the graphical interface. For that i installed the Nvidia drivers:
- nvidia-lts
- nvidia-utils
- nvidia-settings
- mesa

Faltaram os pacotes de 32 bits:
- lib32-nvidia-utils
- lib32-mesa

Them i installed the display server:
- xorg
- xorg-server
- xorg-xinit
- xorg-apps
- bumblebee

Them copied the configuration file.

`cp /etc/X11/xinit/xinitrc /home/<user>/.xinitrc`

Them, installed the window manager and the compositor:
- bspwm
- picom

