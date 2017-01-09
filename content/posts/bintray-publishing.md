Title: How did I publish Android Library to JCenter from Android Studio
Date: 2017-01-07 5:27PM
Authors: ptyagi
Category: Development
Tags: Bintray, Publishing, JCenter, Library, OpenSource, Dev
Summary: This article walks through the process of publishing an OpenSourced Android library to JCenter.

## Introduction
JCenter is a Maven Repository or file server hosted by [Bintray](https://bintray.com/) for
Android libraries. It’s a default repository for Android Studio. To demonstrate the process of
publishing an OpenSource Android library, I'm using [WebViewOverlay widget library](https://ptyagicodecamp.github.io/webviewoverlay-widget-library.html)
for example. After uploading to JCenter artifact repo, `WebViewOverlay` widget can be dropped-in to your
project like this:
```
compile 'org.ptyagicodecamp:WebViewOverlay:1.0.2'
```

##  Uploading Android library (in aar format) to Bintray
* Create log-in at [Bintray](https://bintray.com/). Scroll down to register for an open-source project.

* Create a new repo:
  ![Create Repo]({attach}../images/create_repo.png)


* Fill-in all required information and click "create repo". It'll redirect to "package" screen.
  ![Repo Created]({attach}../images/repo_created.png)


* Click on “Create Package”. Fill in your package name and click on "Add New Package":
![Add New Package]({attach}../images/add_new_package.png)


* It'll take you to enter package details. Fill-in details and click on "Create Package" at the bottom.
![Create Package]({attach}../images/create_package.png)

And you’re Done with registering your Maven repository on Bintray !

***Note***: Link your Github account from Bintray, if you want to upload library from `build.gradle` (Android Studio).
You can do this by going into your repository on Bintray and selecting "Import from Github” option.
It’ll guide you through with rest of the steps.

### Setting up Android Studio Project
* Create a new project in Android Studio.
* Module `WebViewOverlay` contains all the library code and module `app` has sample app to demonstrate the usage of library.
Make sure that you name module same as of artifact name configured at Bintray. `WebViewOverlay` in this example.
Refer to `WebViewOverlay` at [Github for source code](https://github.com/ptyagicodecamp/webview-overlay).
* Setup Android Studio project to be able to publish library to `jcenter()` Maven repo, and
add Bintray plugin to project’s `build.gradle`. Root level `build.gradle` will look like this:
```
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:2.2.3'
        classpath 'com.jfrog.bintray.gradle:gradle-bintray-plugin:1.4'
        classpath 'com.github.dcendents:android-maven-gradle-plugin:1.4.1'
    }
}

allprojects {
    repositories {
        jcenter()
    }
}
```

* Update Bintray related credentials in `local.properties` like this:
```
bintray.user=YOUR_BINTRAY_USERNAME
bintray.apikey=YOUR_BINTRAY_API_KEY
```
Note: Look for **API KEY** in your Profile section on Bintray.

* Add following in library module’s `build.gradle`. In this case `build.gradle` of `WebOverlay`:

```
apply plugin: 'com.android.library'

ext {
    bintrayRepo = 'WebViewOverlay'
    bintrayName = 'WebViewOverlay'

    publishedGroupId = 'org.ptyagicodecamp'
    libraryName = 'WebViewOverlay'
    artifact = 'WebViewOverlay'

    libraryDescription = 'A widget to load WebView as an Overlay.'

    siteUrl = 'https://github.com/ptyagicodecamp/webview-overlay'
    gitUrl = 'https://github.com/ptyagicodecamp/webview-overlay.git'

    libraryVersion = '1.0.0'

    developerId = 'developerId'
    developerName = 'Developer Name'
    developerEmail = 'developer@email.com'

    licenseName = 'The Apache Software License, Version 2.0'
    licenseUrl = 'http://www.apache.org/licenses/LICENSE-2.0.txt'
    allLicenses = ["Apache-2.0"]
}
```
Refer to [this `build.gradle`](https://github.com/ptyagicodecamp/webview-overlay/blob/master/WebViewOverlay/build.gradle)

* You would need to add these scripts in order to publish libraries to Bintray:
```
//Add these lines to publish library to bintray. This is the readymade scripts made by github user nuuneoi to make uploading to bintray easy.
//Place it at the end of the file
apply from: 'https://raw.githubusercontent.com/nuuneoi/JCenter/master/installv1.gradle'
apply from: 'https://raw.githubusercontent.com/nuuneoi/JCenter/master/bintrayv1.gradle'
```

That's all you ve to do in order to configure you Android Studio project.

### Uploading to Bintray:
CD to Root of Android Studio Project, and run these commands:
```
gradlew install
gradlew bintrayUpload
```

That’s it ! your artifact will be uploaded to Bintray.

### Link to JCenter
* Your package needs to be linked to JCenter to be able to be resolved.
![Add to JCenter]({attach}../images/add_to_jcenter.png)

* It'll take couple of hours to get request approved. Once approved, you'll see you package like this:
![Linked To JCenter]({attach}../images/linked_to_jcenter.png)

***Note***: You will have to wait for couple of hours before it'll be synced on JCenter.
You can check if its available by going to "http://jcenter.bintray.com/<path/to/package>"


### Start using your hosted library:

Now you can reference `WebViewOverlay` library from your project's `build.gradle` like this:
```
compile 'org.ptyagicodecamp:WebViewOverlay:1.0.0'
```


### References:
I followed [this tutorial](https://inthecheesefactory.com/blog/how-to-upload-library-to-jcenter-maven-central-as-dependency/en) to get me setup at Bintray.


