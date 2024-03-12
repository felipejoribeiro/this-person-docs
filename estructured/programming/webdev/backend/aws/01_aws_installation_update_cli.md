# Installing AWS CLI client
For managing your cloud solutions you can use the command line interface. But before that you must install it.

The best way of doing that is by downloading the official binaries and installer. You can do that by downloading the package:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

Than `unzip` the package with:

```bash
unzip awscliv2.zip
```

And then run the installer inside the folder that you downloaded:

```bash
./install
```

If you want to update the `CLI` app, just run:

```bash
./install --update
```

To remove the AWS CLI v2, delete the its installation and symlinks:
```
$ sudo rm -rf /usr/local/aws-cli
$ sudo rm /usr/local/bin/aws
$ sudo rm /usr/local/bin/aws_completer
```

And that's it. Happy hosting.

## Serverless framework
Other cli tool that is very important is the `serverless` cli tool. The best way of installin this utility is by using `npm`, with `node`. So, using this method, just run the following command:

```bash
sudo npm i -g serverless
```

And that is it. To update the package just run the `npm` update command.

