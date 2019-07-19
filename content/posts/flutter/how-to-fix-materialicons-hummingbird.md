Title: How to fix Material Icons for Flutter Web (Hummingbird)
Date: 07/18/2019
Authors: ptyagi
Category: Flutter
Tags: Material Icons, Hummingbird, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: At this point, Flutter Web (aka Hummingbird) doesn't render Material Icons for Web. In this post, we'll see how Material Icons can be rendered for WebApps developed using Flutter.

**Target Audience:** Beginner

**Recipe:** Material Icons for Flutter Web (Hummingbird).

**Focus Widget:** Material Icons

**Goal:** Fix MaterialIcon rendering for Flutter WebApps.

![Goal]({attach}../../images/flutter/web_material_icon.jpg)

[Watch full video here](https://youtu.be/bgLiVIIu3bA)

**[Before]** Default Material Icons rendering in Flutter WebApp:

![Material Icons Default rendering]({attach}../../images/flutter/web_materialicon_1.jpg)


**[After]** Fixed Material Icons rendering for Flutter WebApp:

![Fixed Material Icons rendering]({attach}../../images/flutter/web_materialicon_2.jpg)


### Lets's go! ###

#### Step #1. `pubspec.yaml` ####
Add material icon dependency in `pubspec.yaml`:
```
flutter:
  uses-material-design: true
```

#### Step #2. Download Material Icons font ####
Download MaterialIcons fonts from [here](https://github.com/google/material-design-icons/raw/master/iconfont/MaterialIcons-Regular.ttf). Copy `MaterialIcons-Regular.ttf` file under `web/assets/fonts` directory.

#### Step #3. `FontManifest.json` ####
Add `FontManifest.json` in `web/assets` directory.

```
[
  {
    "fonts": [
      {
        "asset": "fonts/MaterialIcons-Regular.ttf"
      }
    ],
    "family": "MaterialIcons"
  }
]
```

_Note:_ I've removed debug banner to be able to show Settings vertical dots. All you need to do is to set `debugShowCheckedModeBanner` flag to false in `MaterialApp` like below:
```
return new MaterialApp(
      debugShowCheckedModeBanner: false,
      ...
    );
```


**Source code repo:**
Source code is [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/popupmenubutton-web/flutter_widgets)


### References: ###
1. [This Github issue](https://github.com/flutter/flutter/issues/32540)
2. [Material Icons](https://github.com/google/material-design-icons/raw/master/iconfont/MaterialIcons-Regular.ttf)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
