The first thing that you must do is to install the `supervisor` package.

Then we must create the configuration file that will define the behavior that we want. These config files (`app1.conf`, `app2.conf`) must be located in `/etc/supervisor/conf.d`.

There is a general config file called `supervisord.conf` that is located in `/etc/supervisor/`.

Here is an example of configuration file:

```conf
[program:qr]
command=sh /opt/ivare/qr.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/qr.err.log
stdout_logfile=/var/log/qr.out.log
```

(O processo tem o nome do arquivo `.sh`).
