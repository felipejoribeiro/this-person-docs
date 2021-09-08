# How to maintain your arch system?
This document contain instructions to keep your arch system health and with bugs to the minimum.

### System health now
Some useful commands you can perform for a quick health check are:

- Check if any system service entered in a failed state: `systemctl --failed`
- Look for general errors of programs that are stored in `var/log/`: `journalctl -p 3 -xb`

# Backup and statistics
You can see some important information with these commands:

- See a list of all packages installed: `pacman -Qqe`
-
