Title: Loading image from Firebase Storage in Flutter App (Android, iOS & Web)
Date: 11/22/2019
Authors: ptyagi
Category: Flutter
Tags: FirebaseStorage, Flutter Web, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Code recipe to demonstrate image Loading from Firebase Storage on multiple platforms (Android, iOS, and Web) using Flutter and Flutter Web.

**Target Audience:** Beginner

**Recipe:** Implement loading image from Firebase Storage on Flutter Native and Flutter WebApp.

**Goal:** In this code recipe, we'll do following:

* Touch basing Firebase Project and configuration setup.
* Touch basing availability of two sample images in Storage using Firebase Console.
* Fetching one of the image randomly from Firebase Storage.
* Checkout code for loading image in native and web app.

**Android:**

![Flutter-Native-Android]({attach}../../images/flutter/image_fb1.jpg)

![Flutter-Native-Android2]({attach}../../images/flutter/image_fb2.jpg)

---
**iOS:**

![Flutter-Native-iOS]({attach}../../images/flutter/image_fb_ios.jpg)

---
**Flutter Web:**

![Flutter-Web]({attach}../../images/flutter/image_fb3_web.jpg)

---
**Checkout the companion video tutorial:**
<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Lets's go! ###

This code recipe would demonstrate image Loading from Firebase Storage in Flutter Native and Web Apps.

### Step #1. `pubspec.yaml` dependencies ###

Flutter plugin for accessing images in FirebaseStorage for Native apps:

```
dependencies:
  firebase_storage: ^3.0.8
  firebase_core: ^0.4.0+9
  firebase_analytics: ^5.0.6
```

Flutter plugin for accessing files in Firebase Storage for Web apps:
```
dependencies:
  firebase: ^5.0.4
```

---

### Step #2. Firebase Project review ###

**Project Setup:**

Make sure that your Firebase project is configured for all three platforms.

* Android: Checkout [this link](https://firebase.google.com/docs/android/setup) to configure Firebase project for Android app.  
* iOS: Checkout [this link](https://firebase.google.com/docs/ios/setup) to configure Firebase project for iOS app.
* Web: Checkout [this link](https://firebase.google.com/docs/web/setup) to configure Firebase project for Flutter Web app.


**Images in Storage:**

I've uploaded two images in Storage as shown in screenshot below.

![Flutter-Console]({attach}../../images/flutter/image_fb_console1.jpg)

Don't forget to tune Firebase Storage files 'Rules' depending on your usage. For demonstration purposes for this code recipe, I want to let user read images regardless of their authentication status. So, I'm making images readable to all as shown in screenshot below:

![Flutter-Console]({attach}../../images/flutter/image_fb_console2.jpg)

---

### Step #3. Code Structure for loading image ###

I'll be using `StatefulWidget` to load image since I'll be toggling between two images available in my FirebaseStorage bucket. `FutureBuilder` widget is used to fetch the image from the Storage, and display the image depending on the connectionState and successful image retrieval.

```
class LoadFirbaseStorageImage extends StatefulWidget {
  @override
  _LoadFirbaseStorageImageState createState() =>
      _LoadFirbaseStorageImageState();
}

class _LoadFirbaseStorageImageState extends State<LoadFirbaseStorageImage> {
  ...

  Expanded(
    ...
    //Image Loading code goes here
    child: FutureBuilder(
            future: _getImage(context, image),
            builder: (context, snapshot) {
              if (snapshot.connectionState ==
                  ConnectionState.done)
                return Container(
                  height:
                      MediaQuery.of(context).size.height / 1.25,
                  width:
                      MediaQuery.of(context).size.width / 1.25,
                  child: snapshot.data,
                );

              if (snapshot.connectionState ==
                  ConnectionState.waiting)
                return Container(
                    height: MediaQuery.of(context).size.height /
                        1.25,
                    width: MediaQuery.of(context).size.width /
                        1.25,
                    child: CircularProgressIndicator());

              return Container();
            },
          ),
        ),
        ...
        //This is button to toggle image.
        loadButton(context),
}
```

`_getImage(...)` is responsible for directing the call to appropriate library targeted to specific platform. For example, native or web. `FireStorageService` is the interface that internally fetches image using the correct platform specific library.

```
Future<Widget> _getImage(BuildContext context, String image) async {
  Image m;
  await FireStorageService.loadImage(context, image).then((downloadUrl) {
    m = Image.network(
      downloadUrl.toString(),
      fit: BoxFit.scaleDown,
    );
  });

  return m;
}
```

Checkout [this plugins](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/plugins/firetop/storage) directory to familiarize yourself with the platform specific call re-direction.

![Flutter-Plugins]({attach}../../images/flutter/image_fb_plugin.jpg)

File `file_storage_service.dart` uses `dart.library` to decide on redirecting calls to native vs web implementation for `FireStorageService`.

```
export 'unsupported_storage.dart'
    if (dart.library.html) 'web_storage.dart'
    if (dart.library.io) 'mobile_storage.dart';

```

Any platform which is not web or native falls back to `unsupported_storage.dart` file:

```
import 'package:flutter/material.dart';

class FireStorageService extends ChangeNotifier {
  FireStorageService._();
  FireStorageService();

  static Future<dynamic> loadImage(BuildContext context, String image) {
    throw ("Platform not found");
  }
}

```


***Note:*** [Checkout my previous article](https://ptyagicodecamp.github.io/migrating-to-flutter-19-implementing-cross-platform-firebase-login-in-flutter-apps.html) about plugins directory structure in details, and supporting web and native app's from single source code.

---

### Step #4. Loading Image in Flutter Native App ###

Let's take a look at Native variant of `FireStorageService` in `mobile_storage.dart` file below:

```
import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/material.dart';

class FireStorageService extends ChangeNotifier {
  FireStorageService();

  static Future<dynamic> loadImage(BuildContext context, String image) async {
    return await FirebaseStorage.instance.ref().child(image).getDownloadURL();
  }
}

```

---

### Step #5. Loading Image in Flutter Web App ###

Let's move on to Web variant of `FireStorageService` in `web_storage.dart` file below:

```
import 'package:firebase/firebase.dart';
import 'package:flutter/material.dart';

class FireStorageService extends ChangeNotifier {

  FireStorageService() {
    initializeApp(
        apiKey: "AIzaSyDEktNdn4CsMUxeOyVkPFBnaoAdNhcpEPc",
        authDomain: "fir-recipes-b5611.firebaseapp.com",
        databaseURL: "https://fir-recipes-b5611.firebaseio.com",
        projectId: "fir-recipes-b5611",
        storageBucket: "fir-recipes-b5611.appspot.com",
        messagingSenderId: "728428768644");
  }

  static Future<dynamic> loadImage(BuildContext context, String image) async {
    var url = await storage().ref(image).getDownloadURL();
    return url;
  }
}

```

Please note that you would need to provide Firebase web project configuration to access `storage()` instance for web.


Checkout the source code for detailed implementation. As usual, this code recipe is linked from main [flutter_widgets](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/) code recipes sample app.

---

### Source code repo ###

* Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/images)

* Code recipe project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)

---

### References: ###

1. [Configure Firebase project for Flutter Native Android app](https://firebase.google.com/docs/android/setup)
2. [Configure Firebase project for Flutter Native iOS app](https://firebase.google.com/docs/ios/setup)
3. [Configuring Firebase project for Flutter Web app](https://firebase.google.com/docs/web/setup)
4. [Previous article](https://ptyagicodecamp.github.io/migrating-to-flutter-19-implementing-cross-platform-firebase-login-in-flutter-apps.html) about supporting web and native app's from single source code.


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
