# Creating a bootable USB drive.

Here we will study how to create an arch bootable usb drive that we can use to install arch linux.
The first thing that must be done is to download the newest arch linux iso from the main web page of the distribution, in the downloads page: https://archlinux.org/download/

### Preparing the usb drive

Then, you will have an .iso file that we must burn in a usb drive.
So, you now must plug the usb in your linux computer and perfor the `sudo fdisk -l` command. There you will identify the usb that you plugged the machine by the name. Like `/dev/sdb`, for example.
Then we must format it. For that you will need _dosfstools_ that can be installed with `sudo pacman -S dosfstools` in archlinux.

Now we umount it with the `sudo umount /dev/sdb` command and format it with the `sudo mkfs.vfat -I /dev/sdb` command. Notice that everything in the pendrive will be erased. Procede with caution.

Now that the media is formated we can burn the iso in it with the command:

```
sudo dd bs=4M if=/path_to_iso.iso of=/dev/sdd
```

With this command the iso will be copied to the pendrive and finally you can run the command `sync` and end the process. Your bootable pendrive is ready to action.

### The ALSA package

It is important to remember that the only thing available is the tty as the arch linux distribution doesn't come with a graphical interface, and the system in the pendrive isn't persistent. If you want these features you must use other application, the _Alma_ package.
A usefull scenario for this is wen your computer requires broadcom drivers to access wi-fi. These aren't available in the default arch iso (a nightmare as a ethernet cable is necessary). But, as the alma bootable pendrive is a persistent arch linux install, you can install the drivers there and make it work. Other advantages are in the possibility to open internet browsers along side the installation for example.

Tu use _Alsa_, the first thing is to install it with the `yay -S alma`. An aditional good thing to download is a configuration file that was already written. It can be found in `https://github.com/jamesmcm/arch-i3-usb`. So clone the project to your computer. Then you run the following command to generate the _iso_ file:

```
ALMA_USER="test" TIMEZONE="Europe/Madrid" sudo -E alma create --presets ./arch-i3-usb/preset --image 5GiB image_name.img
```

This will create the iso with an _arch_ linux instance that have a display server installed and other good features, like a tiling window manager called _i3_, the _Firefox_ web browser and _Neovim_, and other many things. You will be prompted to create a password. This will be your _sudo_ password. Other options of the iso creation can be seen in the _github_ repo.
After created the iso you just cen just follow the previous steps to copy it to the pendrive.
Done.
