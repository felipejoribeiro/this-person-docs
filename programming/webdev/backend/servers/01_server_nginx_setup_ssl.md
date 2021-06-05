# Nginx with SSL certification setup
Here we will see how to configure a `Nginx` server from the ground up. For that you will need a domain name (if you don't have that, it's fine, just skip the first section of this document), a `cloud server` with `Debian 10` stable installed.

### Server setup
first, login in your server via `ssh` and copy your public ssh key to it in `~/.ssh/authorized_keys`. Then configure it to not accept password validation for `ssh` connections, as it is unsafe. Then, that is it, it is a minimal config.

### Configuring Domain name
Now we will configure the `Domain name` to point out to our server. For that create two entries in DNS registers with:

- A @ <server_ipv4> ttl menor possível.
- AAAA @ <server_ipv6> ttl menor possível.

And create a Nameserver child apontando www.domainname para domainname.

And that is it. Wait for the changes to take effect as there is the `propagation` process to take effect.

### Installing the server
Now we will install some programs:

- nginx
- certbot
- python-certbot-nginx

The configuration files for nginx are located in `/etc/nginx/sites-available/default` you can copy it to `/etc/nginx/sites-available/felipejoribeiro_config` and in the file you can create this minimal config:

```
server {
        listen 80 ;
        listen [::]:80 ;
        root /var/www/felipejoribeiro;
        index index.js index.html index.htm index.nginx-debian.html;
        server_name felipejoribeiro.com www.felipejoribeiro.com;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

Then you must create a symbolic link from this file with the following command:

```
ln -s /etc/nginx/sites-available/felipejoribeiro_config /etc/nginx/sites-enabled/
```

And create the `/var/www/felipejoribeiro` directory but with a name of your liking. And you can populate this with index.html and create a basic webpage.

And then, just restart `nginx` with `systemctl reload nginx`.

### Enabling ssl certificate.
Just execute the `certbot` utility with the command `certbot --nginx` and follow the prompts. And configure to redirect all traffic to `https`. And that is it! now your site is encripted. Congrats.
The certificate will inspire with a couple of months. To create a new one you must run `certbot renew`. But it's good practice to automate this instruction.
For doing that just run `crontab -e` and it will open a file for you to edit. Then append a line in the end with `1 1 1 * * certbot renew`. And it will run this command at the beginning of each month.

### Conclusion
And that is it. You can serve static pages really easily in this way. If you want to make something more complex with `nodejs`, there are more things that must be done, but here we have a greate start from the basics. A react app can be created farely simply.
