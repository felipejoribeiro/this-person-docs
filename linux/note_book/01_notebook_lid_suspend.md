# Avoid auto suspend closing lid
Here we will see how to disable the default behavior of suspending the computar when the lid is closed.

The first thing you must do is editing the `/etc/systemd/logind.conf` file. It has a bunch of directives of what to do when some system event happens. So find and modify the following line:

```conf
HandleLidSwitch=ignore
```

You will see that the default behavior was set to `suspend`. Then, restart the `systemd-logind` to make the changes take effect.

This is very useful, as it allows the user to, using `acpi`, customize the suspend function.
