Title: Implement Flutter themes using Provider
Date: 09/12/2019
Authors: ptyagi
Category: Flutter
Tags: Provider, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Implementing switching from light to dark theme and vice versa using [Provider plugin](https://pub.dev/packages/provider) for dependency injection and state management.

**Target Audience:** Beginner

**Recipe:** Toggle Flutter themes from one type to another using Provider dependency injection and state management package.

**Focus Widget:** [Provider plugin](https://pub.dev/packages/provider)

**Goal:** Implementing themes using Provider plugin. Implement a simple UI with an image, text and a button to switch themes. Page's default theme is light. Clicking on "Switch Theme" button will apply dark theme to page, and vice versa.

![switching-themes-animation-Android]({attach}../../media/flutter/themes_inaction.mp4)

**Light Theme:**

![light-theme]({attach}../../images/flutter/ios-themes2.jpg)


**Light Theme:**

![dark-theme]({attach}../../images/flutter/ios-themes3.jpg)



### What is Provider ###
[Provider](https://pub.dev/packages/provider) is a plugin/package that provides dependency injection and state management solution for a Flutter App. It's built with robust and scalable Flutter widgets.

### Step #1. `pubspec.yaml` ###
Add package dependency in `pubspec.yaml`:
```
dependencies:
  flutter:
    sdk: flutter

  #Dependency for Provider plugin
  provider: ^3.1.0 #ChangeNotifier, Consumer, Providers
```

### Step #2. Implement theme ChangeNotifier ###

I'll be using two themes: Light and Dark. Let's use `enum` to declare these two themes:
```
enum MyThemes { light, dark }
```

Now, I need a `ChangeNotifier` that'll notify my app about the change occurred in theme preference.
```
class ThemesNotifier with ChangeNotifier {}
```

Next comes defining `ThemeData` for `light` and `dark` themes:
```
static final List<ThemeData> themeData = [
  ThemeData(
      brightness: Brightness.light,
      primaryColor: Colors.blue,
      accentColor: Colors.lightBlueAccent),
  ThemeData(
      brightness: Brightness.dark,
      primaryColor: Colors.orange,
      accentColor: Colors.yellowAccent)
];
```

Let's initialize default `MyThemes` and `ThemeData`:
```
MyThemes _currentTheme = MyThemes.light;
ThemeData _currentThemeData = themeData[0];
```

Lastly, setters and getters to update and access `MyThemes` and `ThemeData`:
```
void switchTheme() => currentTheme == MyThemes.light
    ? currentTheme = MyThemes.dark
    : currentTheme = MyThemes.light;

set currentTheme(MyThemes theme) {
  if (theme != null) {
    _currentTheme = theme;
    _currentThemeData =
        currentTheme == MyThemes.light ? themeData[0] : themeData[1];

    //Notifies the theme change to app    
    notifyListeners();
  }
}

get currentTheme => _currentTheme;
get currentThemeData => _currentThemeData;
```

### Step #3. Notifying theme change to App ###

Sample App 'Themes Demo''s `build(...)` method uses `theme` attribute to assign `ThemeData` to app like below. `Provider.of<ThemesNotifier>(context).currentThemeData` is notified about a theme change happened in `ThemesNotifier`'s `switchTheme()` method.
```
@override
Widget build(BuildContext context) {
  return MaterialApp(
      theme: Provider.of<ThemesNotifier>(context).currentThemeData,
      home: Scaffold(
        appBar: AppBar(
          title: Text("Themes Demo"),
        ),
        body: body(),
      ));
}
```
Theme change is requested from `Switch Theme` button :
```
RaisedButton(
  child: Text("Switch Theme"),
  onPressed: () {
    Provider.of<ThemesNotifier>(context).switchTheme();
  },
),
```

That's all !

### Running on Flutter Web ###

**Note: Flutter Web project setup has been changed since Flutter 1.9 release.**

Please follow the direction on setting up Flutter Web project [here](https://flutter.dev/docs/get-started/web).
![Flutter-Web-Project]({attach}../../images/flutter/flutter_web.jpg)

**Source code repo:**
Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets-web/flutter_widgets/lib/themes)


### References: ###
1. [Provider Package](https://pub.dev/packages/provider#-readme-tab-)
2. [Flutter web](https://flutter.dev/docs/get-started/web)
3. [Open Issue about Flutter-Web merging Flutter](https://github.com/flutter/flutter/issues/34082)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
