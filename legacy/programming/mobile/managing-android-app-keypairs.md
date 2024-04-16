# Here we will see how to manage keypairs
To sign android apps we need a keypair, with which we will sign each build so that the store can know that it was us that uploaded that app build. In mac you must find where your **JDK** bin folder is localized.

```bash
/usr/libexec/java_home
```

With the output of this command you have the path. Navigate to it with a `cd` command, and then you can execute the following command to generate the key:

```bash
keytool -genkeypair -v -storetype PKCS12 -keystore my-upload-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
```

If you are in linux or windows, look for the keytool in your system, if the binary isn't in path, locate it in your system;

Remeber of assiging a good alias name, as it will be important further. The key has 10000 days of validity, which is more than 27 years (hopefully enough). You will be prompted to insert some information, one of then is the keystore password that you will use during the signIn of your app.

## Signing your app
To sign your app you must add the following code to your `android/app/build.gradle`:

```gradle
android {
    ...
    defaultConfig { ... }
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {
                storeFile file(MYAPP_UPLOAD_STORE_FILE)
                storePassword MYAPP_UPLOAD_STORE_PASSWORD
                keyAlias MYAPP_UPLOAD_KEY_ALIAS
                keyPassword MYAPP_UPLOAD_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            ...
            signingConfig signingConfigs.release
        }
    }
}
```

And you must have these values inside your android/gradle.properties:

```
MYAPP_UPLOAD_STORE_FILE=my-upload-key.keystore
MYAPP_UPLOAD_KEY_ALIAS=my-key-alias
MYAPP_UPLOAD_STORE_PASSWORD=*****
MYAPP_UPLOAD_KEY_PASSWORD=*****
```
