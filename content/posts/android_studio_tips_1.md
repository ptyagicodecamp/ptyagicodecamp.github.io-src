Title: How to get SHA1 fingerprint for digitally signed APK
Date: 2017-4-13 1:06PM
Authors: ptyagi
Category: Development
Tags: Android, Android Studio, Tips & Tricks
Summary: How to get SHA1 fingerprint for digitally signed APK


## How to get SHA1 fingerprint for digitally signed APK

* Open terminal in Android Studio
* Run Keytool utility to get SHA1 for your APK:

```
keytool -exportcert -alias <your_alias> -keystore <path-to-keystore> -list -v
```
