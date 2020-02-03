Title: Loading PDF file from Firebase Storage in Flutter App (Android, iOS & Web)
Date: 02/03/2020
Authors: ptyagi
Category: Flutter
Tags: FirebaseStorage, PDF, Flutter Web, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Code recipe to demonstrate loading PDF file from Firebase Storage on multiple platforms (Android, iOS, and Web) using Flutter.

**Target Audience:** Beginner

**Recipe:** Load PDF file from Firebase Storage on Flutter Native and Flutter WebApp.

**Goal:** In this code recipe, we'll do following:

* Review Firebase Project and configuration setup.
* Checkout availability of PDF file in [FirebaseStorage](https://firebase.google.com/docs/storage) using Firebase Console.
* Fetching PDF from Firebase Storage.
* Checkout code for loading pdf in native and web app environments.

**Flutter Cookbook:**
![Flutter-Cookbook]({attach}../../images/flutter/cookbook_index_pdf.jpg)

**Android:**

![Flutter-Native-Android]({attach}../../images/flutter/pdf_fire_android_1.jpg)

![Flutter-Native-Android2]({attach}../../images/flutter/pdf_fire_android_2.jpg)

---
**iOS:**

![Flutter-Native-iOS]({attach}../../images/flutter/pdf_fire_ios_1.jpg)
![Flutter-Native-iOS2]({attach}../../images/flutter/pdf_fire_ios_2.jpg)

---
**Flutter Web:**

![Flutter-Web1]({attach}../../images/flutter/pdf_fire_web_1.jpg)
![Flutter-Web2]({attach}../../images/flutter/pdf_fire_web_2.jpg)

---
**Checkout the Youtube video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Introduction ###

This code recipe would demonstrate loading PDF file from Firebase Storage in Flutter Native and Web Apps. I'm using [my Flutter talks's](https://www.siliconvalley-codecamp.com/Presenter/2019/priyanka-tyagi-1447) slides as PDF file. I've this PDF available in Firebase Storage already.

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


**Images in Firebase Storage Console:**

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
  await FireStorageService.loadFromStorage(context, image).then((downloadUrl) {
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

  static Future<dynamic> loadFromStorage(BuildContext context, String image) {
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

  static Future<dynamic> loadFromStorage(BuildContext context, String image) async {
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

* Recipe source code is available [here]()

* Code recipe project's source code is available [here]()

---


### References: ###

1. [Related article about loading image from FirebaseStorage]() about supporting web and native app's from single source code
2. [Configure Firebase project for Flutter Native Android app](https://firebase.google.com/docs/android/setup)
3. [Configure Firebase project for Flutter Native iOS app](https://firebase.google.com/docs/ios/setup)
4. [Configuring Firebase project for Flutter Web app](https://firebase.google.com/docs/web/setup)
4. .



Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
