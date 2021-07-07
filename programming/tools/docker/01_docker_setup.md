# Docker setup on Arch linux
Here we will see how to setup docker on Arch linux. The first thing you must do is to install te package with `sudo pacman -S docker`. Then enable and start `docker.service`.

Notice that if you are using a `VPN` probably there will be a `IP` conflict between the `VPN` and the Docker's bridge. In this case you can disconnect the `VPN` or try to end the conflict with the IP with [1](https://stackoverflow.com/questions/45692255/how-make-openvpn-work-with-docker) or [2](https://github.com/docker/compose/issues/4336#issuecomment-457326123)

Then, you can test the docker instance with `docker info` o check the version of the package and you can run a test container with:

```bash
sudo docker run -it --rm archlinux bash -c "echo hello world"
```
To run the command above you will need `sudo` privileges, if you want to execute this command without it you can add your user to the `docker` group. But be carefull, any user in the `docker` will be equal to a `root` user, as it can run `docker run --privileged` commands without any password requirement.

Besides the `docker` package, you will need the `docker-machine` and `docker-compose` packages as well with `pacman`.


