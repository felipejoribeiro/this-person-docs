# Configuring ssh by project
Configuring ssh keys per project is necessary for managing projects with various authentication methods.

## Creating ssh keys
The first thing that you must do is to create your `ssh` keys. If you don't have any one (you can check that looking in `~/.ssh/` for keys), you can create the default one with the `ssh-keygen -t rsa` command.

Than you can create others wih the following command:

```bash
ssh-keygen -t rsa -C "email@work_mail.com" -f "id_rsa_work_user1"
```

Now you have two different keys, you can copy the content of each one with the `pbcopy < ~/.ssh/id_rsa.pub`. And you can paste the public key in github, for example, too have access to the repositories without the need of password, or you can copy for a remote server with `ssh-copy-id -i ~/.ssh/mykey user@host` to enter the server without password, as well.

## Register the keys
Now that we have keys to use, we must register then with `ssh-agent`, with the following commands:
Remember initiating the `ssh-agent` with the bash `eval $(ssh-agent)` command.

```bash
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa_work_user1
```
Now we must configure `ssh` to use each key for the proper `host`. This host is a `url` or a website name like, `github.com`.

To configure this, you must create a `ssh` configure file in `~/.ssh/config` and enter the following configuration inside:

```
# Personal account, - the default config
Host github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa
   
# Work account-1
Host my-account-name.github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_work_user1
```

The `work_user-1` is the github user id for the work account. And that is it.

## Cloning projects
Now that everything is configured, you can clone the project with the following command:

```bash
git clone git@my-account-name.github.com:github-account/repository.git
```
Notice that we cloned with the ssh address option. And watch out! The text between `@` and `:` must be equal to the `Host` value in your `ssh` configuration file. Now it will download the project using the ssh key configured in that config entry. So remember registering this ssh key in your work account. And, if you are working in a organization, make sure the organization enabled you working in the project.

By cloning the repository in this way, it will register the link as a remote, and further steps are not needed. But, if you have a project that is already there and you want to enable the other ssh key, just modify the remotes of your repository. You can see then with thee `git remote -v` command and you can remove or add then, so just remove the one with `@git.github.com:` and add the one with `@my-account-name.github.com:`. This can be done with the `git remote add origin <new link>` and `git remote rm origin` commands.


