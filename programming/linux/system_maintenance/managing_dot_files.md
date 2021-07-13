# Managing dot files
In this document we will discuss how to manage our dear dot files. These files configure all sorts of software in our system and manage then can become a hassle when the volume of programs configured is big.

The objective of this way of organizing your work is to keep track of changes in these configurations and making you able to change then, make experimental branches and test new things without the worry of breaking something. This can be achieved with `GIT`, the best version controll softare out there (and the only one in know atm).

Besides that, we will have to know a way of keeping track of these files with `GIT`. We can't just make our home directory a git repository, there are too much files and would be too hands on manage the massive `.gitignore` file that would be necessary.

`Symlinks` are a option as well, but they require, again, too laborous work to manage each instance of file linked and broken symbolic links are prone to terrible things to happen. Besides that, such configuration turns alt pretty plataform dependent and complex to manage with scale.

So the way that will be shown in here is with `stow`. This is a program made to manage binaries that were compiled from source. So the way it works is, you create a directory called `stow` inside `/usr/local/bin/`, for example, and place there all the binaries that you compiled from source. Then, when you `stow` a directory there, it will create a `symlink` file inside the target directory. So `stow` is nothing more than a `symlink` manager. It will never delete a real file but it will manager various symlinks and manage then for you.

## Some important options
The `stow` package offers some good options when dealing with packages. We will see some:

- `--dotfiles` : This options enables a feature that replaces `dot-` part of a package inside the `stow` directory with a real dot. This is good as managing real dot files would end up with lots of hidden files inside your stow directory.
- `--adopt` : This option will see the end location of a file and copy it inside the stow directory and create the symlink. So it will do all the hard work if you pretend to take files that already exist inside `stow`.
- `-D --delete`: Wil `unstow` a installed package, that is, delete the symlink.
- `-S --stow` : Will stow the package to the target directory.
- `-t <DIR> --target=<DIR>` : Default is the parent directory, but you can specify other one.
- `-n --no` : Don't perform any operation, just show what would happen.

Some aditional opeions are present in the `man` page.

## Some practical examples

