# Android development on arch linux with vim is something else
Here we will see how to work on front end development with some rather strange tools:

- The operating system that we will be using is a **linux** distribution called **Arch-linux**, which is known by it's hardness to install and maintain but praised by it's simplicity and leaness. Such qualities enables incredible personalization of the system, granting infinit power to the user to change watever he likes.
- The code editor we will be using is the **neovim**, which is the second iteration from **vi**, it's grampa. The code editor is known for it's simplicity as well, which enables the developer to adapt it entirelly to one's liking. Which describes the common theme of this article: How infinit customization affects one's workflow?

Both tools are alien to the **front-end** community, being more commonly used inside servers by **back-end** personnel. Inside **secure shell**, where there isn't **GUI**, these type of editors are the only option in most cases.

## You will need to install:
- jdk-8-openjdk
- android-studio

Set some ambient variables as well.


## Android Studio setup
```bash
sdkmanager --licenses
```

```bash
avdmanager create avd -n snackin_app -k "system-images;android-24;google_apis;x86" -b x86 -c 100M -d 7 -f
```

```bash
/opt/android-sdk/tools/emulator -list-avds
/opt/android-sdk/tools/emulator -avd <name>
```

```bash
sdkmanager "system-images;android-24;google_apis;x86"
```

