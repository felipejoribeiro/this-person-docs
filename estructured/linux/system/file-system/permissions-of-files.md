# Permissions of files
When dealing with permissions there are thre things to consider: Identities, resources and permissions. So some basic initial commands must be to generate some users and groups so that you can train the concepts presented here yourself:

- `useradd user1`
- `useradd user2`
- `groupadd group1`
- `groupadd group2`

To set a password to a user, you can use the `psswd` command, followed by the user-name. To delete a user, in arch linux you can use the `userdel` command, in debian the better option is the `deluser` command. You can check all logged users with the `who` command, and you can check all processes running on each user using the `top -u` command, specifying the user in the end.

# Ownership
All files and directories have owners. The owner of a file is the user who created it, by default. You can change the owner of a file with the `chown <user> <file>` command. You can change to a group as well, just set its name like so:
`chown :<group> <file>`. If you want to change the owner user and group you can use `chown <user>:<group> <file>`.

To change the ownership of a directory, you can treat it as a file, a just use the `chown` command. If you want to apply to everything inside it, you can use the `-R` flag, like so: `chown -R <user>:<group> <file>`.

# Permission
A file has permissions associated with the capability of **read**, **write** and **execute**. This classification can be seen when you do a `ls -l` command, which shows all files with theyr respective permissions.

       - | - - - | - - - | - - - 
       t   r w x   r w x   r w x
             u       g       o

Here is an example:

```shell
drwxr-xr-x. 4 root root    68 Jun 13 20:25 tuned
-rw-r--r--. 1 root root  4017 Feb 24  2022 vimrc
```

The first digit is about the file type which can be a file or a directory. Then we have the permissions, for reading, writing and executing. For directories, executing means the ability to make the `cd` command into it. So, we can summaraize that:

- if a user doesn't have the **execution** permission to a directory he will not be able to `cd` into it;
- if a user doesn't have the **read** permission to a directory he will not be able to `ls` inside it;
- if a user doesn't have the **writing** permission to a directory he will not be able to create new files;

We have three permission sections for three identities: users permissions, group permissions and other's permissions. The `other's` permissions is about all other users besides the owner.
The `group's` permissions is about all other users that are in the group which is owner of the file.
The `user's` permissions is about the owner of the file.

You can change the permissions of a file or directory with the `chmod` command. The best way of doing that is using the '4 + 2 + 1' syntax:

      4     |      2      |       1
     read        write         execute

So, the command `chmod 745 <file>` will set the permissions as follows:

     Owner = 4 + 2 + 1 = 7 (read, write and execute) 
     Group = 4 + 0 + 0 = 4 (read)
     Others = 0 + 0 + 1 = (execute)

These are the permissions atributed to the file or directory. You can change the owner as well as seen before.
