# Creating an audio studio in your arch linux machine.
If you want to use your computer to music production there are a set of steps that you must take.
First, install with pacman:

- jack2
- lib32-jack2
- jack2-dbus
- pulseaudio-jack (if you have pulseaudio installed)

Then install with pacman for creating the "realtime" group with the right permissions:
- realtime-privileges

Then add your user to the `realtime` group with

```
sudo usermod -aG realtime <user>
```

Then restart your computer. Now you can install a front end to configure JACK:
- cadance

You can open it and configure it to use pulse audio through the interface.
Select the sound input and output too. To test the tool you can run the volume tool if it works you are good to go.

Then you can install with pacman:
- ardour
- xjadeo
- harvid

This is a mult-track recording tool that works with jack. You can initiate it and set it to work with jack and if it works everythink as done correctly and you are good to proceed.

then you can install plugins from the AUR:
- zyn-fusion
- calf
- lsp-plugins
- tap-plugins
- dragonfly-reverb
- carla
- dpf-plugins
- ebumeter
- drumgizmo
- eq10q
- geonkick
- guitarix
- helm
- ir.lv2
- jack_capture
- liquidsfz
- mda.lv2
- ninjas2
- noise-repellent
- samplv1
- setbfree
- sherlock.lv2
- sonic-visualiser
- swh-plugins
- wolf-shaper
- wolf-spectrum
- x42-plugins
- zam-plugins
- zita-ajbridge
- zita-njbridge
- zita-rev1
- invada-studio-plugins-lv2

You should install audacity with pacman as well. Good program.
You can install vcvrack too
