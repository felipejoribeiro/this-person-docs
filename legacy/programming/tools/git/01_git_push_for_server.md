# Push for a machine
On this document we will see how to push commits for a machine.
That is, if you have a raspberry pi, we will se how to use it as a git server like github, but without the UI stuff.

First you must init an empty repository in your cloud box, it can have any name. Do this with the `git init` command inside a empty repository. Then, you must configure it to receive the commits with the `git config receive.denyCurrentBranch updateInstead` command.

Then, you can go to your computer and enter the repository you want to send to your remote server.
Now, in the repository, run the following command:

```
git remote add new_remote_name user_name@ip_number:/path/to/empty/repo
```

And, finally, you can just make your push command as normal:

```
git push new_remote_name
```

You can check your new remote alongside your github one with the `git remote -v` command (well, if you cloned it from github of course).

And this is it. You will send the commits to the the repository that you initialized there.

If your remote server has the `SSH` service listening to a `PORT` other than `22` (that is the default), you will need to create a `host` entry. This can be done inserting in the `~/.ssh/config` file in your computer (the place from with you want to send stuff) the following:

```
Host name_of_host
	HostName ip_number
	Port port_number
	User user_in_remote
```

And then you just need to create the remote as previously explained:

```
git remote add new_remote_name <name_of_host>:/path/to/empty/repo
```

## Auto deploying
If you want to deploy your project when you push something to your server, one thing you can do is use `git hooks`. Navigate ( in your server ) to the repository where the project is. Now, go to `.git/hooks/`, then create the file `post-receive` (no extencion) with the following text:

```

npm build /path/to/your/project

```
If your project is a react app. If it isn't then adapt the command to the right one, for build. And that is it. The mensages of the deployment will even appear in your console when you run `git push <remote_name>`. Awesome stuff. 


So this is it. Happy pushing!
