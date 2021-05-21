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
- lib32-nvidia-utils
- nvidia-settings
- nvidia-prime (for allowing us to run nvidia only in apps that require it)
- mesa
- lib32-mesa
- xf86-video-intel
- libglvnd

Then i configured nvidia to update initramfs after any driver update. For that i created the file `/etc/pacman.d/hooks/nvidia.hook`, with:
```
[Trigger]
Operation=Install
Operation=Upgrade
Operation=Remove
Type=Package
Target=nvidia
Target=linux
# Change the linux part above and in the Exec line if a different kernel is used

[Action]
Description=Update Nvidia module in initcpio
Depends=mkinitcpio
When=PostTransaction
NeedsTargets
Exec=/bin/sh -c 'while read -r trg; do case $trg in linux) exit 0; esac; done; /usr/bin/mkinitcpio -P'
```

To execute a program with Nvidia graphics you must use the `prime-run` before the command. A way to test this feature is to install the `glxinfo` (AUR) package. When runned it just outputs the glx information about the environment. So, if you execute `glxinfo | grep "renderer"`, if everything is correct, the intel graphycs will appear, and if you execute `prime-run glxinfo | grep "renderer"` then the Nvidia graphics card will popup.

I installed `inxi`(AUR) too, to get some information about the display drivers and screens. It can be done with the command `inxi -G`

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

Cuda seems to be ok and the computer isn't heating in idle. Funny thing is that the 120Hz display is working out of the box. Nice.

Then, following the tips and tricks session of the nvidia arch wiki page i found a way of managing the low resolution in system startup for grub and initial prints. For that, i had to mount the `EFI` partition and create a file `/EFI/refind/refind.conf` in there with `use_graphics_for linux`. I had to do the same thing in the file `/etc/refind.d/refind.conf`.

Then i configured grub to display the correct resolution editing the `/etc/default/grub` with:

```
GRUB_GFXMODE=1920x1080x32,1024x768x32,auto
GRUB_GXPAYLOAD_LINUX=keep
```

Then i installed the brave browser with `yay -Syu brave-bin`.

Then i enabled the multilib repositories editing the `/etc/pacman.conf` file with:

```
[multilib]
Include=/etc/pacman.d/mirrorlist
```
And then updated the system with a `sudo pacman -Syyu` command.

Then i configured audio, installing:
- `alsa-utils`
- `sof-firmware`
- `alsa-ucm-conf`
- `pulseaudio`
- `pulseaudio-alsa`
- `pulseaudio-jack`
- `pulseaudio-equalizer`
- `pulsemixer`
- `lib32-libpulse`
- `lib32-alsa-plugins`
- `pulseeffects-legacy-git`(aur)
- `dcaenc`(aur)

And I enabled the DTS alsa creating the file `/etc/asound.conf` with:

```
<confdir:pcm/dca.conf>
```
The sound is gorgeous now. Really pleasant. I didn't configured the pulseeffects. There are some settups you can explore in the internet.

Then i configured the touchpad of the notebook installing these programs:
- `xf86-input-libinput`
- `xorg-xinput`

And you will need to create a conf file `/etc/X11/xorg.conf.d/30-touchpad.conf`:

```
Section "InputClass"
    Identifier "touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    Option "Tapping" "on"
		Option "NaturalScrolling" "true"
    Option "TappingButtonMap" "lmr"
EndSection
```

And that is it. Now the touchpad works flawlessly.

And then i had to manage the fan speed controll. For that i had to play a with the registers in the notebook that do that. Scary stuff. For that i had to install:

- `asus-fan-dkms-git`(aur)
- `nbfc`(aur)

And then the following commands start to function:

```
# ec-probe write 0x5e 0x80 # silent mode
# ec-probe write 0x5e 0x40 # balance mode
# ec-probe write 0x5e 0xC0 # performance mode
```

Then it is flawless. In the future i will try to implement this in the polybar or something like that.

Then i discovered a way of controlling the battery charging process. The battery controllers are all present in `/sys/class/power_supply/BAT1/` and here you can see the power level, and set the maximum battery level to charge. Really cool stuff. But this value is reseted at system boot. So to activate it we must create a `service` file, as proposed in the arch wiki. This file must be created in `/etc/systemd/system/battery-charge-threshold.service`:

```
[Unit]
Description=Set the battery charge threshold
After=multi-user.target
StartLimitBurst=0

[Service]
Type=oneshot
Restart=on-failure
ExecStartPre=/bin/sleep 10
ExecStart=/bin/bash -c 'echo 60 > /sys/class/power_supply/BAT1/charge_control_end_threshold'

[Install]
WantedBy=multi-user.target
```
And then enable it. Then you can change `60` for whatever percentage you like. There are more options to deal with hibernation, but i didn't bother to setup now as i rarely use this feature. But if you want this in the future, just take a look in the Asus arch wiki man page.

There seems to be some problem with the renderer. When i open the brave brownser there is some error mensages. And i can't open it with `prime-run`. I installed `hal`(aur) to try to solve but without success. But blender is fine and cuda is functional in blender, so it's something software specific.

So i tried install steam, as it's the most demanding program i know.
- `steam`
- `ttf-ms-win8`(aur)
- `ttf-liberation`
- `wqy-zenhei`
- `steamcmd`(aur)
- `proton`(aur)

I tested some games and valheim runned smoothly. Dark souls was nice too.

Then i installed some archiving compressing software:
- `tar`
- `zip`
- `unzip`
- `p7zip`
- `gzip`
- `rar`(aur)
- `unrar`

And a better cp utility for large files:
- `rsync`

Then I installed an image viewer, the `vimiv` package and i choose a background image. Of a squid and i setted it as default.

Then I disabled the grub initial menu and hided the initial logs with:

```
GRUB_CMDLINE_LINUX_DEFAULT=quiet
GRUB_CMDLINE_LINUX="console=tty2"
```
Then saved the changes with `grub-mkconfig -o /boot/grub/grub.cfg`.

Then I did some initial config with picom. Copied the default configuration file in `~/.config/picom/` and made the terminal transparent.
To know the name of each window I installed the `xorg-xprop` package that allow us tu click in windows with the `xprop` command to know information about that window.

Then i changed the picom version. Installed the `picom-ibhagwan-git`(aur) one. To activate good blur.

Then i created the alacritty config and made a basic one. Installed `powerline-fonts` and `powertline` as new fonts. And seted the Dracula theme with direct colors.

Then i configured the ssh servir in the machine. this was done with the installation of:
- `openssh`
- `ssh-audit`(aur)

And i configured some security things like disabling password inwards authentication and desanbling root logging. All this can be done in `/etc/ssh/sshd_config`

Then i cloned this notes repository and started making these registers in the notebook.

Then i configured the lightdm greatter. For that i installed:
- `lightdm`
- `lightdm-gtk-greeter`
And enabled the `lightdm` system service.
And then created the file `.xprofile` that will replace the `.xinitrc` when we initiate the computer with `lightdm`.

Then i configured the polybar installyng the `polybar`(AUR) package. Created the polybar config file. And copyied the `launch.sh` file in the config polybar directory. And finally I configured bspwm to call it on startup.

Then i configured `thunderbird` as my email client.

Then i configured the keyboard hotkeys with `ACPI` events. This was done installing the `acpid` package and starting it with `sudo systemctl enable/start acpid.service`.
Then you can make the `journalctl -f` command to listten what each button does, and configure the `/etc/acpi/handler.sh` to react accordingly to each keyboard command. As studied earlier, this can be used to change the fan profile and other things.


