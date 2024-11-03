---
id: 1726149526-apple-certificates-and-profiles
aliases:
  - Apple certificates and profiles
  - apple-certificates-and-profiles
tags: []
---

# Apple certificates and profiles

Uploading apps to the apple app store can be done by following these steps:

- register the `Bundle ID`;
  - you can create an app in `xcode` and the `Bundle ID` will be created automatically;
- create app record in the `App Store Connect`;
  - select the `Bundle ID` created;
- configure the app in the `App Store Connect`;
  - add the app icon, screenshots, description, etc;
- create a certificate;
- create a provisioning profile;
- register the devices;
- upload the app to the `App Store Connect`;

To send apple apps to the app store, you need to create a certificate and a provisioning profile. This is a simple guide to create these files.

## Certificates

To create a certificate, you need to follow these steps:

1. Go to the [Apple Developer](https://developer.apple.com/) website;
2. Go to the **Certificates, Identifiers & Profiles** section;
3. Go to the **Certificates** section;
4. Click on the **+** button to create a new certificate;
5. Select the type of certificate you want to create;
6. Follow the steps to create the certificate;

You can create a certificate directly from Xcode, and by logging in with your Apple ID of a developer account it will upload the certificate to the Apple Developer website for you.

You can create the certificate manually as well and upload it to the Apple Developer website. Following the following steps:

1. Go to the **Keychain Access** app;
2. Go to the **Keychain Access** menu;
3. Go to the **Certificate Assistant** menu;
4. Click on the **Request a Certificate from a Certificate Authority...** option;
5. Fill in the information;
6. Click on the **Save to disk** option;
7. Upload the certificate to the Apple Developer website;

More information in the [Apple Developer](https://developer.apple.com/help/account/create-certificates/create-a-certificate-signing-request) website.

## Provisioning Profile

Before creating a provisioning profile, you need to create a identifier for your app. Than can be done directly in Xcode, by signing in with your Apple ID of a developer account and opening the project settings. The bundle identifier will be created and uploaded for you.

To create a provisioning profile, you need to follow these steps:

1. Go to the [Apple Developer](https://developer.apple.com/) website;
2. Go to the **Certificates, Identifiers & Profiles** section;
3. Go to the **Provisioning Profiles** section;
4. Click on the **+** button to create a new provisioning profile;
5. Select the type of provisioning profile you want to create;
6. Follow the steps to create the provisioning profile;

> **Note**: For distribution certificates in apple store connect you don't need an apple device.

Here you approve capabilites for the apps published as well. For that, go in "Identifiers" and select or create a new one. Then select capabilites and app services that are required in your app. After this you can add these capabilites in Xcode without problems.

Then, in Xcode, disable the **Automatically manage signing** option and select the provisioning profile you just created for direct distribution. Than you can send versions through **TestFlight** or **App Store Connect**.

## Devices

It's important to register the devices you will use for development. You can do that in the **Devices** section of the **Certificates, Identifiers & Profiles** section of the Apple Developer website.

To register a device, you need to follow these steps:

1. Go to the [Apple Developer](https://developer.apple.com/) website;
2. Go to the **Certificates, Identifiers & Profiles** section;
3. Go to the **Devices** section;
4. Click on the **+** button to register a new device;
5. Fill in the information;
6. Click on the **Register** button;

You can find the **UUID** of the device by clicking on **options** in the keyboard and selecting **System information** in the apple button in the left top corner of the screen. Then go to the **Hardware** and check the `Hardware UUID` value.

## Conclusion

This is a simple guide to create certificates and provisioning profiles for Apple apps. You can find more information in the [Apple Developer](https://developer.apple.com/) website.
