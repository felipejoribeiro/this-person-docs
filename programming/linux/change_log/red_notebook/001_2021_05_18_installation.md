# Installation of the arch OS
The partitions  were created in a minimal manner. With one Swap partition (6G), the EFI FAT32 one (300M) and the linux file system (~450G). They where placed in the main *SSD* in the notebook.
`mkfs.fat -F32 /dev/sda1`
`mkswap /dev/sda2`
`swapon /dev/sda2`
`mkfs.ext4 /dev/sda3`


Then, it was installed the following packages:
- base
- base-devel
- linux
- linux-headers
- linux-firmware
- intel-ucode

```
    
    pacstrap /mnt base base-devel linux linux-headers linux-firmware intel-ucode

```

Then create the file system with:

`genfstab -U /mnt >> /mnt/etc/fstab`

Then enter the new arch machine:

`arch-chroot /mnt`

Then configured locales and language.

#### Setting our time zone
Now that we are in the right system we can set the timezone. For that you can reference the right region with the command `ln -sf /usr/share/zoneinfo/Brazil/East /etc/localtime` for my case given the place i reside. Than you can set the hardware clock with the command `hwclock --systohc`. Than you must define the locale by editing the file `/etc/locale.gen`. This can be done with vim, but you must install it first with `pacman -S vim`. Then find the right locale and uncomment it. After that you must run the command `locale-gen`. You can uncomment how much locales you need. You can see the ones activated with the command `locale -a`.

And, finally, create the file `/etc/locale.conf` with:
```
    LANG=en_US.UTF-8
```
And make the keyboard layout stay persistent in `/etc/vconsole.conf`:
```
    KEYMAP=us
```
Then I configured the hostname and hosts.

#### Setting the Host name
Now we will set the computer hostname editing a file again with vim. The file is `/etc/hostname` and you can set it to whatever you want. And we must add some other hosts locally adding the following lines in the file `/etc/hosts`:

```
    
    127.0.0.1   localhost
    ::1         localhost
    127.0.1.1   my_second_arch.localdomain    my_second_arch    

```
Then, I installed some programs
- git
- vi
- vim
- sudo

Then I created the my user and gave it sudo capabilities.

#### Creating a user and a password (for the root too)
Now we must create a user and a password for the user. And we must create a password for the root. So to do that we will run the `passwd` command that change the root password.

Now we will create the user and the user password as well. For that we run the command `useradd -m felipejoribeiro`. And then create the password for the user with `passwd felipejoribeiro`.

And finally, we must add the new user in some groups to give it permissions (to run the sudo command for example). For that we run the command `usermod -aG wheel,audio,video,optical,storage felipejoribeiro` 

#### Installing SUDO 
Them we can install the **sudo** program. With pacman by running the `pacman -S sudo` command. And after that you can edit the sudo configurations with the command `visudo`. Than search for the line `# %wheel ALL=(ALL) ALL` and uncomment it (line 82). That will give privileges to your new born user, as it is in the wheel group.

Then i installed the bootloader. I configured Grub and installed some grub utilities for ufi.

#### Installing the bootloader
The BIOS checks the Master Boot Record (MBR), which is a 512 byte section located first on the Hard Drive. It looks for a bootloader (like GRUB). The hard drive's partition tables are also located here. If you remember, we created a partition for the EFI with this exact size. We will install the bootloader there now.

- grub
- efibootmgr
- dosfstools
- os-prober
- mtools

After that we must make our EFI directory and our boot directory. For that we use the commands `mkdir /boot/EFI` to create the directory and `mount /dev/sda1 /boot/EFI` to mount the EFI partition to the newborn directory.

Remember, your bios must not be configured with the option `UEFI or legacy`. It must be set to `UEFI only`. If it's not the case the following command will result in an error. But the solution is to `exit`, and `shutdown now`. And then, configure your bios properly. After that, boot in your usb again, mount again `/dev/sda3 in /mnt` and do a `arch-chroot /mnt` again. And mount the `EFI` partition again to `/boob/EFI`. And repeat the bellow command.

And finally we can install grub in it with `grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck`. Than we must create a config file for the boot loader. That can be done with `grub-mkconfig -o /boot/grub/grub.cfg`. 


Then i configured grub to display the correct resolution editing the `/etc/default/grub` with:

```
GRUB_TIMEOUT_STYLE=hidden
GRUB_GFXMODE=1920x1080x32,1024x768x32,auto
GRUB_GXPAYLOAD_LINUX=keep
```

Then i disable the grub initial menu altering the `/etc/default/grub` file with a final `grub-mkconfig -o /boot/grub/grub.cfg` command.

Then I installed the internet manager:
- iwd
- networkmanager
- network-manager-applet
- wireless_tools

And you must enable iwd with `systemctl enable iwd` and `systemctl enable NetworkManager.service`.

Then i rebooted in the new system.

And connected to the internet with the nmcli utility with the commands that are available in the internet linux personal man.

Then, following the tips and tricks session of the nvidia arch wiki page i found a way of managing the low resolution in system startup for grub and initial prints. For that, i had to mount the `EFI` partition and create a file `/EFI/refind/refind.conf` in there with `use_graphics_for linux`. I had to do the same thing in the file `/etc/refind.d/refind.conf`.

Then i enabled the firewall installing and enabling ufw:
- ufw

`sudo ufw enable`
`sudo systemctl enable ufw.service`

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
- mesa
- xf86-video-intel


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

Them i installed the display server:
- xorg
- xorg-server
- xorg-xinit
- xorg-apps
- xorg-xrandr

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


Then, i created the file `/etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf` with:

```
Section "OutputClass"
    Identifier "intel"
    MatchDriver "i915"
    Driver "modesetting"
EndSection

Section "OutputClass"
    Identifier "nvidia"
    MatchDriver "nvidia-drm"
    Driver "nvidia"
    Option "AllowEmptyInitialConfiguration"
    Option "PrimaryGPU" "yes"
    ModulePath "/usr/lib/nvidia/xorg"
    ModulePath "/usr/lib/xorg/modules"
EndSection

```

And added the following to `.xinitrc`

```
xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
```

In this moment, it's possible to connect through HDMI with the television. Awesome stuff.

Then i configured the AUR helper with a yay installation.

Then i installed some more programs:
- blender
- gotop(AUR)

Cuda seems to be ok and the computer isn't heating in idle. Funny thing is that the 120Hz display is working out of the box. Nice.

Then i installed the brave browser with `yay -Syu brave-bin`.

Then i enabled the multilib repositories editing the `/etc/pacman.conf` file with:

```
[multilib]
Include=/etc/pacman.d/mirrorlist
```
And then updated the system with a `sudo pacman -Syyu` command.

And after 

- lib32-nvidia-utils
- lib32-mesa


I installed `inxi`(AUR) too, to get some information about the display drivers and screens. It can be done with the command `inxi -G`

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
- `pavucontrol`
- `pulseeffects-legacy-git`(aur)
- `dcaenc`(aur)

And I enabled the DTS alsa creating the file `/etc/asound.conf` with:

```
<confdir:pcm/dca.conf>
```
The sound is gorgeous now. Really pleasant. I didn't configured the pulseeffects. There are some settups you can explore in the internet.

And the sound is functional through the HDMI port, and this is truly amazing.

So i tried install steam, as it's the most demanding program i know.
- `steam`
- `ttf-ms-win8`(aur)
- `ttf-liberation`
- `wqy-zenhei`
- `steamcmd`(aur)
- `proton`(aur)

I tested some games and valheim runned smoothly. Dark souls 3 was nice too.

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

To turn on and off the touchpad you can see the xinput devices with the `xinput list` and then turn off the touchpad with `xinput disable <name>`. In the case of this keyboard it's `xinput disable 14`. But the cursor still on. To disable the cursor you must install the `unclutter` package. You run it with `unclutter -idle 1 -root`. And the mouse will be hidden when you don't move it for one second. I ended adding it to `.xprofile`.

May add the disable option to the keyboard hotkeys.

And that is it. Now the touchpad works flawlessly.

Then i configured the lightdm greatter. For that i installed:
- `lightdm`
- `lightdm-gtk-greeter`
And enabled the `lightdm` system service.
And then created the file `.xprofile` that will replace the `.xinitrc` when we initiate the computer with `lightdm`.

And remember to configure the Nvidia_only thing for lightdm. For that you need to create a file in `/etc/lightdm/display_setup.sh`:

```
#!/bin/sh
xrandr --setprovideroutputsource modesetting NVIDIA-0

# set up the two monitors for bspwm
my_laptop_external_monitor=$(xrandr --query | grep 'HDMI-0')
if [[ $my_laptop_external_monitor = *disconnected* ]]; then
	xrandr --auto
else
	if [[ $my_laptop_external_monitor = *connected* ]]; then
		xrandr --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal --output eDP-1-1 --primary --mode 1920x1080 --pos 0x1080 --rotate normal
	else
		xrandr --auto
	fi
fi
```
And make it runable with `chmod +x /etc/lightdm/display_setup.sh`.

And you need to edit the file `/etc/lightdm/lightdm.conf`:
rasgado

```
[Seat:*]
display-setup-script=/etc/lightdm/display_setup.sh
```

And one last thing was necessary. The nvidia module wasn't being loaded in boot. This was resulting in problems for the lightdm to access the Nvidia only config in the first xrandr commands. To solve that i configured the modules to be loaded in system boot. So before the lightdm execution, creating the `/etc/modules-load.d/nvidia.conf` file with `nvidia` in and `/etc/modules-load.d/nvidia-drm.conf` with `nvidia-drm`.

And you need to configure the `.xprofile` file with the following:
```
# Compositor
picom --experimental-backend &

# Background image
nitrogen --restore &

# Window manager
exec bspwm
```

And the results were stelar. Now the hdmi works perfectly with sound and everything.

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

Then i installed some archiving compressing software:
- `tar`
- `zip`
- `unzip`
- `p7zip`
- `gzip`
- `unrar`

And a better cp utility for large files:
- `rsync`

Then I installed an image viewer, the `vimiv` package and i choose a background image.

Then I did some initial config with picom. Copied the default configuration file in `~/.config/picom/` and made the terminal transparent.
To know the name of each window I installed the `xorg-xprop` package that allow us tu click in windows with the `xprop` command to know information about that window.

Then i changed the picom version. Installed the `picom-ibhagwan-git`(aur) one. To activate good blur.

Then i created the alacritty config and made a basic one. Installed And seted the Dracula theme with direct colors.

Then i configured the ssh servir in the machine. this was done with the installation of:
- `openssh`
- `ssh-audit`(aur)

And i configured some security things like disabling password inwards authentication and desanbling root logging. All this can be done in `/etc/ssh/sshd_config`

And then i had to manage the fan speed controll. For that i had to play a with the registers in the notebook that do that. Scary stuff. For that i had to install:

- `asus-fan-dkms-git`(aur)
- `nbfc`(aur)

And then the following commands start to function:

```
# ec-probe write 0x5e 0x80 # silent mode
# ec-probe write 0x5e 0x40 # balance mode
# ec-probe write 0x5e 0xC0 # performance mode
```

Then it is flawless. In the future i will try to implement this in the keyboard hotkeys.


Then i configured the nvidia-prime utility:

- nvidia-prime (for allowing us to run nvidia only in apps that require it)
- libglvnd

To execute a program with Nvidia graphics you must use the `prime-run` before the command. A way to test this feature is to install the `glxinfo` (AUR) package. When runned it just outputs the glx information about the environment. So, if you execute `glxinfo | grep "renderer"`, if everything is correct, the intel graphycs will appear, and if you execute `prime-run glxinfo | grep "renderer"` then the Nvidia graphics card will popup. Other choice is to use `inxi -G` too. I prefeer as it is smaller.

There seems to be some problem with the renderer. When i open the brave brownser there is some error mensages. And i can't open it with `prime-run`. I installed `hal`(aur) to try to solve but without success. But blender is fine and cuda is functional in blender, so it's something software specific.

This works with the external HDMI too but you have to exclude the nvidia config module you created in the `/etc/X11` folder. And the name of the screens change too, but i found that this is the perfect solution. Everything jus works. Like a charm. One thing is that now and then the nvidia driver isn't loaded resulting in the `nvidia-settings` not launching. This can be solved restarting the lightdm process, but i have too look up a batter solution. I thing the module isn't loaded before Xorg, os something. Will look at this more in the future.


Then i configured the polybar installing the `polybar`(AUR) package. Created the polybar config file. And copyied the `launch.sh` file in the config polybar directory. And finally I configured bspwm to call it on startup.

Then i configured `thunderbird` as my email client and configured some emails.

Then i installed and configured the fish shell. Registered it to open in alacritty. And installed some programs:
- `jq`
- `exa`
- `bat`

Then i configured the keyboard hotkeys with `ACPI` events. This was done installing the `acpid` package and starting it with `sudo systemctl enable/start acpid.service`.
Then you can make the `journalctl -f` command to listten what each button does, and configure the `/etc/acpi/handler.sh` to react accordingly to each keyboard command. As studied earlier, this can be used to change the fan profile and other things. And i configured each button with the right commands.

Mapped the fan to the mute mic for the moment.

Created a bunch of shell scripts to handle system things.

Installed:
- asus_fanmode
- acpid

There are buttons that are dead. Will check it later. The fun button is wrong too.

Then it was possible to make the mute and volume buttons functioning. For that i created files in `/etc/acpi/events/`, `vol-m`, `vol-u` and `vol-d`, there goes the `vol-m` as an example:

```
event=button/mute
action=runuser -u fejori -- amixer set Master toggle
```

Now these buttons are functioning great.

Then i installed the libbre office package:
- libreoffice-writer
- ttf-dejavu
- ttf-inconsolata

Then i installed rofi
- rofi
- ttf-meslo (aur)

Then in installed neovim:
- neovim-nightly-bin (aur)
- pip3 install neovim
- nodejs-lts-fermium
- npm install neovim -g
- python2
- python2-pip
- xclip
- ruby
- yarn
- gem install neovim
- pearl-git
- cpan & install Log:log4perl
- cpan & install Neovim::Ext

Created the `.config/nvim` folder.
Perl is massive. Didn't manage to install properly but was too afraid to uninstall it.

Then i installed zathura:
- zathura
- zathura-cb
- zathura-djvu
- zathura-pdf-mupdf
- zathura-ps
- zaread-git (aur)

The last one allows to read office/libreoffice documents with zathura. To run this just do `zaread /path/to/document.docx`.

Installed pandoc aswell as it was a dependency of zaread.
- pandoc


Then I checked how to see disk usage and maintenance with:
- ncdu

And installed a program to update the mirror list of pacman:
- reflector
and used it to create updated mirror lists.

Optimized the system to ssd activating weekly fstrim with the following command:
```
systemctl enable fstrim.timer
```
There is an option to do this continually, but this is bad for performance. anything had to be downloaded.

Then i configured some fonts in the system. For that i used font-matrix:
- fontmatrix (AUR)
Which is nice to navigate the fonts and compare then and experiment with the text. But everything can be solved in the terminal.
All your fonts are located in `/usr/share/fonts` or `~/.local/share/fonts`. There are the directories where all the `.ttf` files are located.
To isntall a font, just download the `.ttf` file and then move it to one of the two font directories just mentioned.
Then you need to run `sudo fc-cache -fv` and all the fonts in the two files will be installed and available to programs. 
To preview the fonts with the `display` command, that already was installed in my machine. Maybe it's a component of the kernel.
You can see all fonts that are present in the system with the command:
`fc-list`.

Insatlled some more locales to, en_CA and fr_CA.

Then, i fixed the cedilla letter by editing the configuration files:

```
sudo vim /usr/lib/gtk-3.0/3.0.0/immodules.cache

sudo vim /usr/lib/gtk-2.0/2.10.0/immodules.cache
```
There i found the lines with "cedilla" and "Cedilla", like:

```
"cedilla" "Cedilla" "gtk30" "/usr/share/locale" "az:ca:co:fr:gv:oc:pt:sq:tr:wa"
```
And added `:en` in the end in both cache files.

Then i created a backup file with the following command:

```
sudo cp /usr/share/X11/locale/en_US.UTF-8/Compose /usr/share/X11/locale/en_US.UTF-8/Compose.bak
```

And then i changed the compose file with the commands:

```
sudo sed 's/ć/ç/g' < /usr/share/X11/locale/en_US.UTF-8/Compose | sed 's/Ć/Ç/g' > Compose
sudo mv Compose /usr/share/X11/locale/en_US.UTF-8/Compose
```

and finally  i instructed the system to load the cedilla module writing the following in the `/etc/environment`:

```
GTK_IM_MODULE=cedilla
QT_IM_MODULE=cedilla
```
Now the cedilla works as it should.

Then i installed some new fonts as recomended by dt:
- ttf-inconsolata: Doesn't have italics. Well readable.
- nerd-fonts-source-code-pro: Has italics.
- otf-code-new-roman(aur):
- ttf-roboto-mono
- ttf-hack
- ttf-ubuntu-font-family
- ttf-mononoki(aur)
- noto-fonts-emoji
- ttf-twemoji(aur)
- otf-openmoji(aur)
- ttf-symbola(aur)

And to explore the fonts after installation I installed `font-manager`(aur).
And installed the emoji piker from rofi:
- rofimoji
- xdotool

And then i created a file `01-emoji.conf` in `~/.config/fontconfig/conf.d/` with the following code:

```
<?xml version="1.0"?>
  <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
  <fontconfig>

   <alias>
     <family>sans-serif</family>
     <prefer>
       <family>Hack</family>
       <family>Noto Color Emoji</family>
       <family>Twitter Color Emoji</family>
     </prefer> 
   </alias>

   <alias>
     <family>serif</family>
     <prefer>
       <family>Hack</family>
       <family>Noto Color Emoji</family>
       <family>Twitter Color Emoji</family>
     </prefer>
   </alias>

   <alias>
    <family>monospace</family>
    <prefer>
       <family>Hack</family>
       <family>Noto Color Emoji</family>
       <family>Twitter Color Emoji</family>
     </prefer>
   </alias>

  </fontconfig>
```

And this is it. Emojis are functioning correctly. Everything is awesome.

Then I installed the `Ranger` file manager and some dependencies:
- ueberzug
- transmission-cli
- calibre
- poppler
- imagemagick
- ffmpegthumbnailer
- w3m
- mediainfo
- openscad
- atool
- udev
- udisks2

And installed `vlc` and `obs-studio` packages.

Then i installed the print screen utilities:
- flameshot
- peek

Everything is configured very nicelly.

And other prograns:
- cbonsai

Then i configured latex, installing the following packages:
- texlive-most
- biber
- tllocalmgr-git
- latex-mk(aur)

Then I disabled the wpa_supplicant service, as i use other network utility.

Then i installed other file manager, the pcmanfm-gtk3.

- kde-gtk-config

Then I installed:
- lxappearance-gtk3

And was possible to configure the theme of gtk apps.

Then i installed the Unity idle:
- unityhub (aur)
- dotnet-runtime
- dotnet-sdk
- mono-msbuild
- mono
- ncurses5-compat-libs (aur)

```
"omnisharp.useGlobalMono": "always"
```

I created the shell script to execut `nvm` too and added the projects to unity. But it not worked at first. I had to install one of the tutorial projects to things work properlly. But now everything runs fine. About the Omnisharp, after some nasty stuff it came to work, don't know really how, but things got well.

Now, with everything perfect you need to configure a backup functionality. For that:
- timeshift (aur)

Then you can start the program in the terminal with `timeshift-gtk`. I couldn't run from rofi as it require sudo. But there wasn't enough space, strangely. Then i disabled all scheduled so that i could always umount the sda driver as i don't need to sync it.

Then i installed lollipop.

Then i configured automounting for pendrives. For that i installed:
- udisks2
- udiskie

There was a problem with the audio after an update, solved installing:
- alsa-lib

And deleting a file as asked in the error prompt trying to run alsa-mixer.

Then i configured pollybar to controll media:
- playerctl
- dbus-python (pip)







