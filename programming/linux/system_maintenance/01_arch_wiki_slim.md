# System maintenance by arch wiki
Here is a report based in the arch wiki about system maintenance.

Two commands that are very important are:
- `systemctl --failed`: See if any system service got a failed state.
- `journalctl -p 3 -b`: Looks for errors in `/var/log` and systemd journal.

### Backups
It's highly advised to make backups of the system as a routine. So that, if you do any thing regretable, you can go back in time in a simple manner.

Its interesting to maintain a list of installed packages. You can do this with the followint command:

```
pacman -Qqetn > file.txt
```

This will print a list of all programs installed with pacman.

```
pacman -Qqem > file.txt
```

And  this will print all packages installed with `yay` or other methods.

You can automate this operation creating a `hook`. A Hook is something pacman can perform in a given situation. This is done by creating a file in `/etc/pacman.d/hooks/`. More directories can be specified with `HookDir` option in pacman.conf. So create a file there, like `package_info.hook`. With the following contents:

```
[Trigger]
Operation = Install
Operation = Remove
Type = Package
Target = *

[Action]
When = PostTransaction
Exec = /bin/sh -c '/usr/bin/pacman -Qqe > /where/to/write.txt'
```

And you can make the same thing for `AUR` packages.


### Installing and update packages
To update packages use the `pacman -Syyu` command. Not always the mirrorlist is up to date. To upadate the mirror list install the `reflector` package, that download all best mirrors.

After that, backup the miror present miror list with:

```
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
```
Check the countries where mirrors are available:

```
sudo curl -o /etc/pacman.d/mirrorlist https://www.archlinux.org/mirrorlist/all/
```

And then run the program:

```
sudo reflector --verbose -p https --country 'us' -l 5 --sort rate --save /etc/pacman.d/mirrorlist
```

But i found that my country doesn't have https servers, so i setted for US mirrors.

Other thing worth mention is that when you update with `yay -Syyu` it will update all package from user repositories and main repositories.

It's good to remove cached files from previous installations too. For doing that you can execute `sudo pacman -Sc` and `yay -Sc`, same thing as before in relation to reach of each command.

And be carefull with .pacnew and .pacsave files. Mor information about the topic in https://wiki.archlinux.org/title/Pacman/Pacnew_and_Pacsave compile here in the future. ( TODO ) 

### Managing space

If you want to delete everything in the cache you can use `sudo pacman -Scc` and `yay -Scc`.

To delete all unwanted dependencies you can use `yay -Yc`.

Other thing that worth mentioning is that you have a `.cache/` directory that can became very massive with time. You can delete everything in it without problem if storage is a problem.

You can delete old logs too, with the following command:

```
journalctl --vacuum-time=2weeks
```

This will clean all log files that are older than 2 weeks. With months this directory can become massive, so this is important.

you can use the `ncdu` package to check size of files and directories.







