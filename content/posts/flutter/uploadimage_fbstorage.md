Title: Uploading Image to Firebase Storage in Flutter App (Android & iOS)
Date: 08/16/2020
Authors: ptyagi
Category: Flutter
Tags: FirebaseStorage, Flutter Web, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Code recipe to demonstrate image uploading from Flutter app to Firebase Storage on Android & iOS platforms.

![FlutterUpload-banner]({attach}../../images/flutter/upload_image_banner.jpg)

**Target Audience:** Beginner

**Recipe:** Implement uploading image to Firebase Storage on Flutter Native.

**Goal:** In this code recipe, we'll pick an image from from device camera or gallery and upload it to the Firebase Storage.
***Note:*** I'll be using Android emulator to demonstrate this code recipe. The camera functionality doesn't work in iOS simulator. You need an iOS device to use camera.

**Pick Image**

![FlutterUpload-addphoto]({attach}../../images/flutter/image_upload1.jpg)


**Upload Image**

![FlutterUpload-displayphoto]({attach}../../images/flutter/image_upload2.jpg)


---
**Checkout the Youtube video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/nfrr5zdINSQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Step #1. `pubspec.yaml` dependencies

Flutter plugin for accessing images in FirebaseStorage for Native apps:

```
dependencies:
  firebase_storage: ^3.0.8
  firebase_core: ^0.4.0+9
  firebase_analytics: ^5.0.6
```

Image picker plugin to select an image from device or emulator:

```
dependencies:
  #Picking image from gallery
  image_picker: ^0.6.7+4
```

***Note:*** This code recipe should work on Flutter Web and/or Desktop to upload image as far as it's able to get reference to the `File` on device. The `image_picker` plugin to select an image is only supported on Android and iOS platforms.

---

# Step #2. Firebase Project review

Check out my previous article on [loading image from Firebase Storage](https://ptyagicodecamp.github.io/loading-image-from-firebase-storage-in-flutter-app-android-ios-web.html) to set up Firebase project.
In this code recipe, you'll need to configure firebase rule to write to the FirebaseStorage.

---

# Step #3. Picking Image

An image file `_imageFile` is selected on device and/or emulator using `ImagePicker` Fluter plugin.

```
class UploadingImageToFirebaseStorage extends StatefulWidget {
  @override
  _UploadingImageToFirebaseStorageState createState() =>
      _UploadingImageToFirebaseStorageState();
}

class _UploadingImageToFirebaseStorageState
    extends State<UploadingImageToFirebaseStorage> {
  File _imageFile;

  ///NOTE: Only supported on Android & iOS
  ///Needs image_picker plugin {https://pub.dev/packages/image_picker}
  final picker = ImagePicker();

  Future pickImage() async {
    final pickedFile = await picker.getImage(source: ImageSource.camera);

    setState(() {
      _imageFile = File(pickedFile.path);
    });
  }
  ...
}
```
---

# Step #4 Uploading Image to FirebaseStorage

Once an image is selected using ImagePicker, it will be displayed in the screen. Clicking on 'Upload Image' button on screen will upload the image to Firebase Storage. Make sure that FirebaseStorage `write` rules are configured appropriately. I'm temporarily enabling write access on FirebaseStorage access using `allow write: if true;`. Make sure to disable it once you've confirmed the functionality. It's always good idea to put write access behind the successful user login.

The following code will take the image file on device and upload it to the `uploads` folder in the FirebaseStorage.

```
class _UploadingImageToFirebaseStorageState
    extends State<UploadingImageToFirebaseStorage> {
  File _imageFile;

  ...

  Future uploadImageToFirebase(BuildContext context) async {
    String fileName = basename(_imageFile.path);
    StorageReference firebaseStorageRef =
        FirebaseStorage.instance.ref().child('uploads/$fileName');
    StorageUploadTask uploadTask = firebaseStorageRef.putFile(_imageFile);
    StorageTaskSnapshot taskSnapshot = await uploadTask.onComplete;
    taskSnapshot.ref.getDownloadURL().then(
          (value) => print("Done: $value"),
        );
  }
  ...
}
```

---

##iOS Info.list

Don't forget to add camera related permissions to `Info.plist`.

```
<key>NSCameraUsageDescription</key>
<string>Need to access your camera to capture a photo add and update profile picture.</string>

<key>NSPhotoLibraryUsageDescription</key>
<string>Need to access your photo library to select a photo add and update profile picture</string>
```

---

### Source code repo ###

* Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/images/upload_image.dart)

* Flutter Cookbook Project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)

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
