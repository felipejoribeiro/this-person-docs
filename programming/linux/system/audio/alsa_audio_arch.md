# Minimalistic sound configuration for arch linux
In distros like *Gentoo* and *Arch* you must configure your audio setup. The least bloated way of seting your sound is with `Alsa` for the sound output. It is the foundation of sound in linux. Any other setup is composed of `Alsa` plus something. But `Alsa` alone can be used to listen to music, youtube or any media consuption. There are some aplications, like steam, that can not interface directly with alsa, needing additional software, such as others. Those need a middleware called `PulseAudio`. Many people consider this bloat, but even if you need it, you can follow these words to set up alsa and then install `PulseAudio`, as it is built on top of alsa and configuring it write still a must.

First we need to enable sound in our kernel for watever specific sound cards you have. If you have a binary distro, that comes with the default kernel, it is already done. If you are on Gentoo or you wrote your oun kernel than you want to pay attention to these options:

- You need to enable some drivers for specific hardware. So search it with the string `audio` with the command `lspci | grep -i audio`. Then go to `/usr/src/linux` as root and do the command `make menuconfig` as root. But this is only possible with full kernel source code, if you have a binary distro like `Arch`, this step is not necessary. Then You will enter a menu with some kernel options. You must go to `Device drivers` and then you must go to `sound card support` and then co go the `Advanced Linux Sound Architecture` that stands for `Alsa` and go to `PCI sound devices` and select the one you found with the first command and enable that. Then, return to the previous menu and go to `HD-Audio` and enable `Build Realtek HD-audio codec support` and you also want to enable `Silicon Labs 3054 HD-modem codec support`. And, if you have a big number of sound outputs, with more than 8 video cards with lots of HDMI output sources you must check the option `Dynamic device file minor numbers` as well. And then you can set the `Max number of sound cards`, but the default value is ok for must setups. Then performe the `make` command to compile the kernel.

- Now is the time to install `Alsa`. With arch this can be done with `pacman -S alsa`. It commes with a mixer that can be accessed with `alsamixer` command. You can test your sound too with the `speaker-test` command.