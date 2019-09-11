Title: Implementing Login in Flutter Web (Hummingbird)
Date: 09/10/2019
Authors: ptyagi
Category: Flutter
Tags: FirebaseAuth, Flutter, Code-recipes, Android, Android Studio, iOS
Summary: In this article, we'll make use of [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) to implement login functionality in [Flutter-to-Fly](https://flutter-to-fly.firebaseapp.com/) WebApp built using Flutter Web - Hummingbird.

###Background###
In this article, we'll make use of [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) to implement login functionality in [Flutter-to-Fly](https://flutter-to-fly.firebaseapp.com/) WebApp built using Flutter Web - Hummingbird. Design has been evolved since I wrote my first article about [Designing Cross platform Flutter prototype for Landing Page (Web-Hummingbird, Android, iOS)](https://ptyagicodecamp.github.io/designing-cross-platform-flutter-prototype-for-landing-page-web-hummingbird-android-ios.html). This article focuses on implementing Login functionality in Hummingbird only. Please refer to [this youtube video](https://youtu.be/Sr1dn3j5tz0) for implementing same login functionality in Android & iOS.

We'll implement LogIn button shown below:

![FirebaseAuth-Login]({attach}../../images/flutter/login_ftf1.jpg)

Please refer to previous related articles below:

1. [Designing Cross platform Flutter prototype for Landing Page](https://ptyagicodecamp.github.io/designing-cross-platform-flutter-prototype-for-landing-page.html)
2. [Making Cross-platform Flutter Landing Page Responsive](https://ptyagicodecamp.github.io/making-cross-platform-flutter-landing-page-responsive.html)
3. [Using Flutter Themes for Cross-platform Landing Page (Web-Hummingbird, Android, iOS)](https://ptyagicodecamp.github.io/using-flutter-themes-for-cross-platform-landing-page-web-hummingbird-android-ios.html)
4. [Implementing Flutter FactsBot using DialogFlow](https://ptyagicodecamp.github.io/implementing-flutter-factsbot-using-dialogflow.html)

**Checkout the companion video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/mK90EXsy6CA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

###Introduction###
In this article, we'll make our login button work. I'll use Firebase authentication to implement email and password authentication. First, setup Firebase Project as mentioned [here](https://firebase.google.com/docs/storage/web/start). We need to add configuration details in Flutter app to be able to communicate with Firebase.

We'll add two more pages to WebApp.

1. **LogIn Page**: Clicking on "LogIn" button will take user to LogIn Page where either they can login using their credentials or register. Registering a user creates a user record in [FireStore](https://firebase.google.com/docs/firestore).
2. **User Profile Page**: Logged in users can see their display name, profile picture placeholder, and SignOut button. This is only for demonstration purposes, and doesn't do much at this point.

### `pubspec.yaml` ###
Following dependencies need to be added to `pubspec.yaml` to interact with Firebase. [Provider](https://pub.dev/packages/provider) package is used for dependency injection and state management.
```
dependencies:
  firebase: any
  service_worker: ^0.2.0
  googleapis_auth: ^0.2.3+5
  provider: any

dependency_overrides:
  provider:
    git:
      url: https://github.com/kevmoo/provider
      ref: flutter_web
  firebase:
    git:
      url: https://github.com/FirebaseExtended/firebase-dart
```

**Web entry point:** As we know that Flutter Web apps' entry point is `web/main.dart` which is compiled to javascript, and referred from `web/index.html`. Let's checkout code in both files:

**`web/main.dart`:**
```
main() async {
  try {
    await config();

    fb.initializeApp(
      apiKey: apiKey,
      authDomain: authDomain,
      databaseURL: databaseUrl,
      storageBucket: storageBucket,
      projectId: projectId,
    );

    await ui.webOnlyInitializePlatform();
    app.main();
  } on fb.FirebaseJsNotLoadedException catch (e) {
    print(e);
  }
}
```

**`web/index.html`:**
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <script src="https://www.gstatic.com/firebasejs/6.4.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/6.4.0/firebase-firestore.js"></script>
    <script src="https://www.gstatic.com/firebasejs/6.4.0/firebase-auth.js"></script>
    <script src="https://www.gstatic.com/firebasejs/6.4.0/firebase-storage.js"></script>
    <script defer src="main.dart.js" type="application/javascript"></script>
</head>
<body>
</body>
</html>
```

**Firebase Configuration:**

`fb.initializeApp` needs Firebase App's configuration parameters. We need to add this information in `package:firebase/src/assets/config.json` file. There's a sample  `config.json.sample` file available for you for reference:

```
{
  "_FYI": "https://firebase.google.com/docs/web/setup",
  "_COPY_TO": "config.json",
  "API_KEY": "TODO",
  "AUTH_DOMAIN" : "TODO",
  "DATABASE_URL": "TODO",
  "STORAGE_BUCKET": "TODO",
  "PROJECT_ID": "TODO",
  "MESSAGING_SENDER_ID": "TODO",
  "SERVER_KEY": "TODO",
  "VAPID_KEY": "TODO",
}

```
Get parameters from Firebase console for your project, and update values in `config.json`.

###LogIn Page###

I'll not be explaining the UI code in this tutorial. However, please take a look at source code. Feel free to reach out to me if you need explanation with any part.

**LogIn Form:**

![LogIn-form]({attach}../../images/flutter/login_ftf2.jpg)

**Register Form:**

![Register-form]({attach}../../images/flutter/login_ftf3.jpg)

**Authenticating using FirebaseAuthService:**

`FirebaseAuthService` is a `ChangeNotifier`, which means if any sign-in or sign-out happens in this class, all other subscribed classes are notified. I've abstracted all APIs using `BaseAuthService`.
```
abstract class BaseAuthService with ChangeNotifier {
  Future<User> currentUser();
  Future<User> signIn(String email, String password);
  Future<User> googleSignIn();
  Future<User> updateUser(User user);
  Future<User> createUser(
      String firstName, String lastName, String email, String password);
  Future<void> signOut();
}
```

`FirebaseAuthService` extends `BaseAuthService`:

```
class FireAuthService extends BaseAuthService {
  final Auth _firebaseAuth = fb.auth();

  //Get currently logged-in user
  @override
  Future<User> currentUser() async {
    return await _firebaseAuth.currentUser;
  }

  //Sign-in using email and password, notifies all subscribers.
  @override
  Future<User> signIn(String email, String password) async {
    try {
      var auth =
          await _firebaseAuth.signInWithEmailAndPassword(email, password);

      notifyListeners();
      return auth.user;
    } catch (e) {
      throw Exception(e);
    }
  }

  //This method is called from register form. A user account is created in FirebaseAuth
  @override
  Future<User> createUser(
      String firstName, String lastName, String email, String password) async {
    var auth =
        await _firebaseAuth.createUserWithEmailAndPassword(email, password);

    var info = fb.UserProfile();
    info.displayName = '$firstName $lastName';
    await auth.user.updateProfile(info);

    updateUser(auth.user);

    return auth.user;
  }

  //A record is created at Firestore to keep track of all personalized data for each user.
  @override
  Future<User> updateUser(User user) async {
    final CollectionReference ref = fb.firestore().collection('users');

    String displayName = user.displayName;
    String photoUrl = user.photoURL;

    if (displayName == null) {
      displayName = "No Name yet";
    }

    if (photoUrl == null) {
      photoUrl = "";
    }

    var newData = {
      'uid': user.uid,
      'displayName': displayName,
      'photoUrl': photoUrl,
      'email': user.email,
      'lastActive': DateTime.now()
    };

    await ref.doc(user.uid).set(newData, SetOptions(merge: true));

    return user;
  }

  //Sign-out
  @override
  Future<void> signOut() async {
    _firebaseAuth.signOut();
    notifyListeners();
  }

  @override
  Future<User> googleSignIn() async {
    //TODO
  }
}
```
**Checking for a logged-in user:** Following code will check-in whether a user is already signed-in. If so, then `UserProfilePage` is displayed. Otherwise `LogInPage` is rendered.

```
return FutureBuilder<User>(
      future: Provider.of<FireAuthService>(context).currentUser(),
      builder: (context, AsyncSnapshot<User> snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          if (snapshot.error != null) {
            return Text(snapshot.error.toString());
          }

          if (snapshot.hasData) {
            return UserProfilePage(context, snapshot.data);
          }

          return LogInPage(title: 'Login');
        } else {
          return Container(
            child: CircularProgressIndicator(),
          );
        }
      },
    );
```

###User Profile Page###

A `UserProfilePage` displays very basic information about the logged-in user. Right now, it shows: welcoming user with their email used as display name, placeholder for profile picture and sign-out button. Please refer to source code for details of implementing user interface.

![UserProfile-page]({attach}../../images/flutter/login_ftf4.jpg)

###A note on iOS Firebase integration###
You may run into trouble building your code for iOS complaining about Firebase imports as shown in screenshot below:

![ios-firebase]({attach}../../images/flutter/ios_firebase_issue.jpg)

**Solution:**
I found [this StackOverflow post](https://stackoverflow.com/questions/41709912/error-could-not-build-objective-c-module-firebase) useful to debug and fix this issue:

![ios-firebase-fix]({attach}../../images/flutter/ios_firebase_issue_fix.jpg)



###Conclusion###
We learned how to implement Firebase authentication in Flutter Web / Hummingbird for 'Login' button in our demo web app. We overviewed dependencies, and ChangeNotifier responsible for authentication, registering and creating user, and creating a user record in FireStore. Please refer to code below for Web and Native (Android & iOS) implementations.

Keep Fluttering !

### Source code ###

* Hummingbird / Flutter Web implementation's source code is [available here](https://github.com/ptyagicodecamp/x-flutter-landingpage/tree/login-web)
* Android & iOS implementation's source code is [available here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/login)


### References/Credits: ###
* [Setup Firebase Project](https://firebase.google.com/docs/storage/web/start)
* [Android & iOS LogIn implementation](https://youtu.be/Sr1dn3j5tz0)
* [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth)
* [Firebase Web](https://pub.dev/packages/firebase_web)
* [Firebase](https://pub.dev/packages/firebase)
* [Firebase Dart](https://github.com/FirebaseExtended/firebase-dart)
* [Designing Cross platform Flutter prototype for Landing Page](https://ptyagicodecamp.github.io/designing-cross-platform-flutter-prototype-for-landing-page.html)
* [Making Cross-platform Flutter Landing Page Responsive](https://ptyagicodecamp.github.io/making-cross-platform-flutter-landing-page-responsive.html)
* [Using Flutter Themes for Cross-platform Landing Page (Web-Hummingbird, Android, iOS)](https://ptyagicodecamp.github.io/using-flutter-themes-for-cross-platform-landing-page-web-hummingbird-android-ios.html)
* [Implementing Flutter FactsBot using DialogFlow](https://ptyagicodecamp.github.io/implementing-flutter-factsbot-using-dialogflow.html)

### Image Credits ###
* [Bird logo](https://www.vecteezy.com/vector-art/604578-hummingbird-icon-logo-and-symbols-template-vector)
* [Landing page image](https://icons8.com/ouch/illustration/fogg-page-under-construction)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
