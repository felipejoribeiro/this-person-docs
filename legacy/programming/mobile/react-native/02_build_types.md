# Adding build variants to our react-native project
Addapting an app to `business-to-business` sales is possible by creating new building variants that account to these new apps. When such setup is configured, we than have the ability of changing launch icon, splash screen and everything else. Making the experience particular to each business contractor.

When the process is finished, we are able to build and distribute each variant differently. With different store fronts, icons and theme colors but keeping the same codebase. This allows us to unify the project from a build and source code perspective.

The following topics will be discussed:
- Is this **buildVariants** scalable?
- How to implement buildVariants to handle the native part of our app variations?
- How to implement these variants in our javascript code?
- How to deal with different OneSignal and Sentry clients?
- HOw to integrate with our **CI/CD**?

-------------------------------------

## ♧  Scalability remarks
With proper build type selection (based on environment variables) and build configuration managing 9 (with build scripts and configuration scripts to handle the build types creation), everything can run smooth.

The native part of the app is responsible for **icon apearance**, **displayname** of the app, **package signing** and **push notifications configuration**.

Besides these, everything else is only defined by javascript code, that can be configured to account to different contexts. So everything becomes dependent only on feature flags whell configured, by even the build process itself and appropriate condinuous deployment and continuous integration pipelines.

-------------------------------------

## ♧  Native implementation
To stablish different apps within a same codebase, one must add some aditional **buildTypes**. Let's check how that can be acomplished:

### 🤖 ANDROID:
First, you must declare the build types inside the `@/android/app/build.gradle`. Initialy, probably, it should have only one build type called **release** and **debug**, which are the ones that comes preconfigured, like so:

```
buildTypes {
  debug {
    signingConfig signingConfigs.debug
  }
  release {
    signingConfig signingConfigs.debug
    minifyEnabled enableProguardInReleaseBuilds
    proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"
  }
}
```
So you should modify this part, by adding the new build types:

```
buildTypes {
  // ... the rest of the code
  beHonest {
    signingConfig signingConfigs.debug
    minifyEnabled enableProguardInReleaseBuilds
    proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"
  }
}
```

Then you can change some native properties like icon photo by changing the arguments inside the target **BuildType**:
```
buildTypes {
  beHonest {
    signingConfig signingConfigs.debug
    minifyEnabled enableProguardInReleaseBuilds
    proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"

    // adding particular indentifiers to the package
    applicationIdSuffix ".beHonest"
    resValue "string", "app_name", "beHonest"

    // Configuring the icon
    resValue "string", "app_icon", "@drawable/ic_launcher"
  }
}
```
And in your android manifest change to use the new value:
```
//...
<application
  android:usesCleartextTraffic="true"
  android:name=".MainApplication"
  android:label="@string/app_name"

  // android:icon="@mipmap/ic_launcher" // change this line with bellow
  android:icon="@string/app_icon"

  android:roundIcon="@mipmap/ic_launcher_round"
  //...

```
And then you can add the personalized icon assets by creating inside your **res** folder a `drawable-beHonest` folder with your icons. And the correct folder will be chosed when building this build type.

This way we can configure the native values in a easy way, making the app unique to the store front as well.

### 🍎 IOS:
First you must define build configurations in your Xcode project. For that, click in your projects in the file explorer inside Xcode. Then, click in the project name in the side bar. Finally, click on "info" (it's selected by default), and then you will have a field called "configurations". It will have something like "Debug" and "Release", you can click on **+** to add a new one. And you can add one "beHonest" there, the same way you added to build.gradle for android.


![xcodeImage](xcode_1.png)


Then, you can select the target in the left tab and go to build settings. One of the build settings is **"Product Bundle Identifier"** which defines the app name. Now you can set one value to each bundle configuration.

In the case of the bundle identifier, you can even use:
```
com.mycompany.myapp.$(CONFIGURATION)
```
Which will apend the configuration name to the package name.

To customize the app name displayed in the app launcher and other places, you can create a separate Info.plist file for each build configuration. To do this, duplicate the existing Info.plist file and rename it to include the build configuration name. For example, you can use the following names for the Info.plist files:

```
Info-Store.plist
Info-beHonest.plist
```
And then you can set set the individual Info.plist files to each build target by changing the **"Info.plist File"** build setting. You can do something like:

```
$(PROJECT_DIR)/MyApp/Info-$(CONFIGURATION).plist
```

To configure different icons to each app, first locate your **images.xcassets** file in your xcode file browser. Inside it you will find some asset like **AppIcon** and **BootSplashLogo**. You can create new entries as desired for each new build configuration. Follow the name convention and create a new entry. Something like `AppIcon-beHOnest`.

Now, in each `.plist` file, you can configure to use different media sources by adding edditing the following key:

```
<key>CFBundleIconFiles</key>
<array>
    <string>AppIcon-beHonest</string>
</array>
```

Now, in your project's build settings (same place where you modified the `.plist` path), change the key named **ASSETCATALOG_COMPILER_APPICON_NAME**, with something like `AppIcon-$(CONFIGURATION)` so that it uses the asset-set you just created. 

Then, in the **General** pannel of your target, you can just change the AppIcon configuration to show the desired one to each build type:

![xcode_general](xcode_2.png)

-------------------------------------

## ♧  Javascript Implementation:
Besides the native part of our code, we need to configure the javascript side as well so that we can account to different business identities throughout our app.

To acomplish that, the following measures will be taken:
- Create separate theme files to each company, with the proper colors and chosen typography;
- Create an asset manager class that includs all assets and changes the images to apropriate ones when changed the theme.  
- Analyse the text on the entire app and change where it's possible to account to different companies.

For this to be possible we must identify what build type we are from the javascritp code. For that we can use the **react-native-config** package:

```javascript
import Config from 'react-native-config';
const BUILD_VARIANT = Config.BUILD_VARIANT
```

Then we can fetch the current build variant form the current `.env` file, which we configure in buildTime, in our `CI/CD` pipeline. 

-------------------------------------

## ♧  Dealing with externous integrations like Sentry and OneSignal
To deal with these libraries, we only need to change credentials if we create new instances for each new store, or create new tags and keep using the same oneSignal account. Both solutions are possible, if new accounts are created it's only a metter of changing the `.env` file t specify the new credentials and we are all set.

-------------------------------------

## ♧  Integrating this buildTypes to our CI/CD
To ensure that our **CI/CD** is able to build all build types, we must make sure that it's easely and reliable configurable. In appcenter its pretty easy:

![appcenter_1](appcenter_1.png)
