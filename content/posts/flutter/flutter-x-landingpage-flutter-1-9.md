Title: Migrating to Flutter 1.9: Implementing Cross-platform Firebase Login in Flutter Apps
Date: 09/23/2019
Authors: ptyagi
Category: Flutter
Tags: Flutter1.9, Flutter, Code-recipes, Android, Android Studio, iOS, Web, Mobile, Cross-platform
Summary: In this article, I'll show you how [Flutter 1.9 release](https://github.com/flutter/flutter/wiki/Release-Notes-Flutter-1.9.1) make developing cross-platform Flutter applications simple while maximizing code reuse.

###Background###
I've been experimenting with Flutter Web (aka Hummingbird earlier) since it was announced in [Google IO 2019](https://medium.com/flutter/bringing-flutter-to-the-web-904de05f0df0).

I remember submitting [pull request](https://github.com/flutter/samples/pull/78) to add instructions for running Flutter sample web apps. Since then I liked the challenge of exploring fast paced and ever changing Flutter Web.

I wrote couple of articles to design and implement a landing page in Flutter which can work seamlessly on all three platforms: Android, iOS and Web. I kept on improving upon this landing page to include login using Firebase, FactsBot, themes, and so on.

Please refer to previous related articles below:

1. [Designing Cross platform Flutter prototype for Landing Page](https://ptyagicodecamp.github.io/designing-cross-platform-flutter-prototype-for-landing-page.html)

2. [Making Cross-platform Flutter Landing Page Responsive](https://ptyagicodecamp.github.io/making-cross-platform-flutter-landing-page-responsive.html)

3. [Using Flutter Themes for Cross-platform Landing Page (Web-Hummingbird, Android, iOS)](https://ptyagicodecamp.github.io/using-flutter-themes-for-cross-platform-landing-page-web-hummingbird-android-ios.html)

4. [Implementing Flutter FactsBot using DialogFlow](https://ptyagicodecamp.github.io/implementing-flutter-factsbot-using-dialogflow.html)

5. [Implementing Login in Flutter Web (Hummingbird)](https://ptyagicodecamp.github.io/implementing-login-in-flutter-web-hummingbird.html)

**Checkout the companion video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/e32YsugXa6Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

###Introduction###
In this article, I'll show you how [Flutter 1.9 release](https://github.com/flutter/flutter/wiki/Release-Notes-Flutter-1.9.1) makes developing cross-platform Flutter applications simple while maximizing code reuse. I'll be using [my previous](https://github.com/ptyagicodecamp/x-flutter-landingpage/tree/login-web/landingpage) Flutter-to-Fly sample app to demonstrate this transition to Flutter 1.9.

### Migrating project to Flutter 1.9 ###

There is pretty good documentation on migrating existing project to Flutter 1.9 and / or creating a new Flutter project available on [official Flutter website](https://flutter.dev/docs/get-started/web). Basically, you would need to run these following commands in one directory level up of your project directory:
```
  $ flutter channel master
  $ flutter upgrade
  $ flutter config --enable-web
  $ cd <into project directory>
  $ flutter create .
  $flutter run -d chrome
```
**NOTE:** In case you run into [White screen issue](https://github.com/flutter/flutter/issues/40876#issuecomment-533506158), you may want to change your Flutter channel to `flutter channel dev`.

### Running X-platform apps from Android Studio ###

Starting from Flutter 1.9, you can run apps on Android, iOS, and Chrome right from Android Studio:

![plugins]({attach}../../images/flutter/as_running.jpg)


### Deploying Web App ###

Deploying Web App is just a command away:
```
 $ flutter build web
```

Above command will generate a `build` folder in the root directory. Copy its contents into `public` directory of your hosting site.


### Launching URL(s) ###

So far, we kept web and native codebase in separate branches to manage launching URL in web and mobile environments differently. Flutter 1.9 makes it possible to be able to keep both (web and mobile/native) codebase in one branch, and pick the right implementation by detecting the platform using `dart.library.html` for web and `dart.library.io` for mobile platform.

You can organize your code base for `plugins` as below as recommended by Flutter team:

![plugins]({attach}../../images/flutter/plugins.jpg)

Above screenshot shows two plugins:

1. `url_launcher`: Managing launching URLs based on target platform. Refer to complete source code [here](https://github.com/ptyagicodecamp/x-flutter-landingpage/tree/master-x/landingpage/lib/plugins/url_launcher)

2. `firetop`: Manages firebase related functionality for mobile and web platforms. We'll dive deeper into this plugin in next section. Refer to complete source code [here](https://github.com/ptyagicodecamp/x-flutter-landingpage/tree/master-x/landingpage/lib/plugins/firetop).

**pubspec.yaml:**

Following dependencies are needed for launching URLs from Flutter app.

```
dependencies:
  universal_html: ^1.1.0
  url_launcher: ^5.1.2

```

Let's see contents of `url_launcher.dart` below. This is where target platform is detected and appropriate implementation is used.

```
export 'unsupported.dart'
    if (dart.library.html) 'web.dart'
    if (dart.library.io) 'mobile.dart';

```


### Firebase login functionality ###

Flutter team is working on [fb_auth plugin](https://pub.dev/packages/fb_auth) to provide cross-platform Firebase support.

**pubspec.yaml:**

Following dependency is needed for adding cross-platform support for Firebase.

```
dependencies:

  fb_auth: 0.0.2+1

```


Let's checkout `fire_auth_service.dart` below. Please refer to [source code in Gihub repo](https://github.com/ptyagicodecamp/x-flutter-landingpage/tree/master-x/landingpage/lib/plugins/firetop) to refer other files.

```
export 'unsupported.dart'
    if (dart.library.html) 'web.dart'
    if (dart.library.io) 'mobile.dart';

```

You would notice that `web.dart` and `mobile.dart` are very similar and use `FBAuth()` to access Firebase functionality. We still need to keep them separate because not everything is available in [`fb_auth` plugin](https://pub.dev/packages/fb_auth). For example, [FireStore support is missing](https://github.com/flutter/flutter/issues/40360#issuecomment-531262594) for Flutter Web.

###Conclusion###
I kept this article short to give a quick update on most important changes that are happening in Flutter Web world. This article gave a peek into getting started with merging Flutter Web code branches into Native code, and how to target platform specific code. We saw how URLs can be launched for Web and Mobile apps using the same code base. Lastly, we covered integrating with Firebase from the one code base.


Keep Fluttering !

### Source code ###

Flutter-to-Fly sample app's source code is [available here](https://github.com/ptyagicodecamp/x-flutter-landingpage/tree/master-x/landingpage)


### References/Credits: ###
* [Flutter 1.9 release](https://github.com/flutter/flutter/wiki/Release-Notes-Flutter-1.9.1)
* [Getting started on Flutter Web](https://flutter.dev/docs/get-started/web)
* [Flutter-to-Fly App](https://flutter-to-fly.firebaseapp.com/#/)
* [fb_auth plugin](https://pub.dev/packages/fb_auth)
* [universal_html plugin](https://pub.dev/packages/universal_html)
* [url_launcher plugin](https://pub.dev/packages/url_launcher)
* [Designing Cross platform Flutter prototype for Landing Page](https://ptyagicodecamp.github.io/designing-cross-platform-flutter-prototype-for-landing-page.html)
* [Making Cross-platform Flutter Landing Page Responsive](https://ptyagicodecamp.github.io/making-cross-platform-flutter-landing-page-responsive.html)
* [Using Flutter Themes for Cross-platform Landing Page (Web-Hummingbird, Android, iOS)](https://ptyagicodecamp.github.io/using-flutter-themes-for-cross-platform-landing-page-web-hummingbird-android-ios.html)
* [Implementing Flutter FactsBot using DialogFlow](https://ptyagicodecamp.github.io/implementing-flutter-factsbot-using-dialogflow.html)
* [Implementing Login in Flutter Web (Hummingbird)](https://ptyagicodecamp.github.io/implementing-login-in-flutter-web-hummingbird.html)


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
