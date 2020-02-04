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

---

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

Flutter plugins for accessing files from FirebaseStorage for Native apps are similar to previous article about [Loading images from Firebase Storage](https://ptyagicodecamp.github.io/loading-image-from-firebase-storage-in-flutter-app-android-ios-web.html)

```
dependencies:

  #http to download PDF
  http: ^0.12.0+4
  #Open PDF in a viewer
  flutter_full_pdf_viewer: ^1.0.6

  #Firebase related
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

### Firebase Project review ###

**Project Setup:**

Make sure that your Firebase project is configured for all three platforms.

* Android: Checkout [this link](https://firebase.google.com/docs/android/setup) to configure Firebase project for Android app.  
* iOS: Checkout [this link](https://firebase.google.com/docs/ios/setup) to configure Firebase project for iOS app.
* Web: Checkout [this link](https://firebase.google.com/docs/web/setup) to configure Firebase project for Flutter Web app.


**Images in Firebase Storage Console:**

I've uploaded Flutter presentation's slides as PDF in Firebase Storage as shown in screenshot below.

![Flutter-Console]({attach}../../images/flutter/pdf_fb_console1.jpg)

Don't forget to tune Firebase Storage files 'Rules' depending on your usage. For demonstration purposes for this code recipe, I want to let user read images regardless of their authentication status. So, I'm making pdf bucket readable to all as shown in screenshot below:

![Flutter-Console]({attach}../../images/flutter/pdf_fb_console2.jpg)

---

### Code Structure for loading PDF ###

I want to fetch PDF from firebase as the first thing. For this purpose I'll be fetching it in `initState()` method. `file` variable holds the path of the pdf file in FirebaseStorage. `fileName` variable is used to display the name for the PDF in app bar.
First, `LaunchFile.loadFromFirebase(context, file)` method fetches the PDF file from FirebaseStorage, and then it is passed to `LaunchFile.createFileFromPdfUrl(url)` to take appropriate action on the targeted platform. For Native platform, remote pdf is downloaded on the disk and named as `flutterSlides.pdf`. On Web platform, PDF file's url is opened in another tab.

```
String file = "pdfs/slides.pdf";
String fileName = "Flutter Slides";

class LoadFirbaseStoragePdf extends StatefulWidget {
  @override
  _LoadFirbaseStoragePdfState createState() => _LoadFirbaseStoragePdfState();
}

class _LoadFirbaseStoragePdfState extends State<LoadFirbaseStoragePdf> {
  static String pathPDF = "";
  static String pdfUrl = "";

  @override
  void initState() {
    super.initState();

    //Fetch file from FirebaseStorage first
    LaunchFile.loadFromFirebase(context, file)
        //Creating PDF file at disk for ios and android & assigning pdfUrl for web
        .then((url) => LaunchFile.createFileFromPdfUrl(url).then(
              (f) => setState(
                () {
                  if (f is File) {
                    pathPDF = f.path;
                  } else if (url is Uri) {
                    //Open PDF in tab (Web)
                    pdfUrl = url.toString();
                  }
                },
              ),
            ));
  }
  ...
}  
```

Once the app has information about the PDF file, 'Open PDF' button will open it another screen:

```
FlatButton(
          onPressed: () {
            setState(() {
              LaunchFile.launchPDF(
                  context, "Flutter Slides", pathPDF, pdfUrl);
            });
          },
          child: Text(
            "Open PDF",
            style: TextStyle(fontSize: 20),
          ),
        )
```

File `launch_pdf.dart` uses `dart.library` to decide on redirecting calls to native vs web implementation for `LaunchFile`.
```
export 'unsupported_pdf.dart'
    if (dart.library.html) 'web_pdf.dart'
    if (dart.library.io) 'mobile_pdf.dart';

```

`web_pdf.dart` has web related implementations while `mobile_pdf.dart` file addresses native platforms (Android & iOS). Anything else goes to `unsupported_pdf.dart`.


Let's checkout each of these files below:

### `unsupported_pdf.dart`

For every platform that's not supported by our application will throw appropriate exceptions.

```
import 'package:flutter/material.dart';

class LaunchFile {
  static void launchPDF(
      BuildContext context, String title, String pdfPath, String pdfUrl) {
    throw ("Platform not found");
  }

  static Future<dynamic> loadFromFirebase(BuildContext context, String url) {
    throw ("Platform not found");
  }

  static Future<dynamic> createFileFromPdfUrl(dynamic url) async {
    throw ("Platform not found");
  }
}

```

---

### Loading Image in Flutter Web App (`web_pdf.dart`) ###

Web platform uses following implementation for the `LaunchFile` class:

```
import 'package:flutter/material.dart';
import 'package:flutter_widgets/plugins/firetop/storage/fire_storage_service.dart';
import 'package:flutter_widgets/plugins/url_launcher/url_launcher.dart';

class LaunchFile {
  static void launchPDF(
      BuildContext context, String title, String pdfPath, String pdfUrl) async {
    UrlUtils.open(pdfUrl);
  }

  static Future<dynamic> loadFromFirebase(
      BuildContext context, String url) async {
    return FireStorageService.loadFromStorage(context, url);
  }

  static Future<dynamic> createFileFromPdfUrl(dynamic url) async {
    return url;
  }
}

```

* `launchPDF(...)`: [`url_launcher` plugin](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/plugins/url_launcher) will open the PDF in browser tab for Flutter Web. It uses `pdfUrl` parameter.

* `loadFromFirebase(...)`: Checkout [`firetop` plugin](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/plugins/firetop/storage) directory to familiarize yourself with the platform specific call re-direction for accessing FirebaseStorage.

* `createFileFromPdfUrl(...)`: This method simply return the url for the PDF to help open the file in browser's tab.


---

### Loading PDF file in Flutter Native App (`mobile_pdf.dart`) ###

```
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_widgets/pdf/load_pdf.dart';
import 'package:flutter_widgets/pdf/pdf_screen.dart';
import 'package:path_provider/path_provider.dart';
import 'package:flutter_widgets/plugins/firetop/storage/fire_storage_service.dart';

class LaunchFile {
  static void launchPDF(
      BuildContext context, String title, String pdfPath, String pdfUrl) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => PDFScreen(title, pdfPath, pdfUrl),
      ),
    );
  }

  static Future<dynamic> loadFromFirebase(
      BuildContext context, String url) async {
    return FireStorageService.loadFromStorage(context, file);
  }

  static Future<dynamic> createFileFromPdfUrl(dynamic url) async {
    final filename =
        'flutterSlides.pdf'; //I did it on purpose to avoid strange naming conflicts
    print(filename);
    var request = await HttpClient().getUrl(Uri.parse(url));
    var response = await request.close();
    var bytes = await consolidateHttpClientResponseBytes(response);
    String dir = (await getApplicationDocumentsDirectory()).path;
    File file = new File('$dir/$filename');
    await file.writeAsBytes(bytes);
    return file;
  }
}

```

* `launchPDF(...)`: On native platform, this method opens the PDF file in a Flutter screen as below:

```
import 'package:flutter/material.dart';
import 'package:flutter_full_pdf_viewer/flutter_full_pdf_viewer.dart';
import 'package:flutter_full_pdf_viewer/full_pdf_viewer_scaffold.dart';

class PDFScreen extends StatelessWidget {
  String title = "";
  String pdfPath;
  String pdfUrl;
  PDFScreen(this.title, this.pdfPath, this.pdfUrl);

  @override
  Widget build(BuildContext context) {
    return PDFViewerScaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: Text(title),
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.share),
              onPressed: () {},
            ),
          ],
        ),
        path: pdfPath);
  }
}

```

* `loadFromFirebase(...)`: Checkout [`firetop` plugin](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/plugins/firetop/storage) directory to familiarize yourself with the platform specific call re-direction for accessing FirebaseStorage.

* `createFileFromPdfUrl(...)`: This method downloads the pdf file from FirebaseStorage to a local file at disk. This local pdf file is later opened in `PDFScreen` later.

That's all you need to load a PDF file from FirebaseStorage into your Flutter application.

**Note:** [Checkout my previous article](https://ptyagicodecamp.github.io/migrating-to-flutter-19-implementing-cross-platform-firebase-login-in-flutter-apps.html) about plugins directory structure in details, and supporting web and native app's from single source code.

---

### Source code repo ###

* Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/pdf)

* Flutter Cookbook project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)

---


### References: ###

1. [Related article about loading image from FirebaseStorage]() about supporting web and native app's from single source code
2. [Configure Firebase project for Flutter Native Android app](https://firebase.google.com/docs/android/setup)
3. [Configure Firebase project for Flutter Native iOS app](https://firebase.google.com/docs/ios/setup)
4. [Configuring Firebase project for Flutter Web app](https://firebase.google.com/docs/web/setup)



Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
