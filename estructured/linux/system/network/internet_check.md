# Internet availability checks

To verivy if the internet connection of your linux machine is healthy you can follow some guidelines. These can be followed for troubleshooting as well, as they cover some important topics about name resolution and DNS servers.

There are three very important files on this matter:
- `/etc/hosts`
- `/etc/resolv.conf`
- `/etc/nsswitch.conf`

The first one lists some hosts that are local of your machine (they reside inside your system, like `localhost`). The second one has a list of addresses that are used for name resolution when a name can't be found in `/etc/hosts`. Finally, the third describes how the computer must behave when resolving host names, it states that the computer must first check in hosts, then in where resolv.conf points to.

## General troubleshooting guidelines
First ping a host that is whell regarded as very stable, like `archlinux.org` or `www.debian.org`. Then, if the ping command fails than there is something wrong with your internet configuration. The fist course of action is to check if there is a problem with your name resolution, to check that, find the `IP` address of the host you just did the ping command. You can do that with the `nslookup archlinux.org` (if you don't have this package installed, you can have it by running `sudo pacman -Sy bind`, which includes the tool, assuming you are on archlinux).

After finding the ip address, then try to ping it direclty. If things go smooth then we found your problem, it's on name resolution. Then check the files mentioned before for errors.

If it didn't respond with the `IP` address, then check if your machine has an ip address. You can do that with the `ifconfig` (if you don't have this tool installed, you can get it with `sudo pacman -Sy net-tools`).

If you have a `IP` then check if you have connection with your Gateway. Worth noticing that if you are in a Wireless connection that would be your router. You can do that with the `netstat -rnv` command.

You can check a specific port as well using the `telnet 95.217.163.246 80` which will check the port 80 of the `archlinux.org` website's server. This package can be found by installing the `inetutils` package inside arch repositories. With this command you can check if there's a service running http on the target port.

If your problem is with ssh connections, check `/etc/ssh/sshd_config` for bad configs.

Another interesting file is `/etc/passwd`, which has important Users information. For example the shell used for login with such user.

Do not forget to check firewall solutions that might be operating in your client system or getway or server as well.

By performing these steps you will be well-informed about the problem. And will be better suited to problem-solving.
