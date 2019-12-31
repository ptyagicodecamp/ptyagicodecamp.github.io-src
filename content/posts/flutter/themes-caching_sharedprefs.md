Title: Persisting theme using SharedPreferences (Android, iOS, and Web)
Date: 12/30/2019
Authors: ptyagi
Category: Flutter
Tags: Caching, SharedPreferences, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Persisting theme setting using [SharedPreferences plugin](https://pub.dev/packages/shared_preferences)

![x-platform-themes]({attach}../../images/flutter/themes_sharedprefs.png)

### Background ###

In [this previous article](https://ptyagicodecamp.github.io/implement-flutter-themes-using-provider.html), we saw how to implement theme switching using Provider. In this article, we'll see how to persist the selected theme using SharedPreferences Flutter plugin. iOS platform uses `NSUserDefaults` and Android platform uses `SharedPreferences` implementations to store simple data to disk asynchronously.

The difference between persisting data using SharedPreferences plugin vs [local database](https://ptyagicodecamp.github.io/persist-theme-setting-in-localdatabase-moor-plugin.html) is that SharedPreferences plugin can not guarantee that writes will be persisted to disk after app restarts. However, saving data to local database is more reliable.

**Target Audience:** Beginner

**Recipe:** Persisting selected theme using [SharedPreferences plugin](https://pub.dev/packages/shared_preferences).

**Focus Widget:** [SharedPreferences plugin](https://pub.dev/packages/shared_preferences)

**Goal:** Persisting chosen theme in disk. Implement a simple UI with an image, text and a button to switch themes. Page's default theme is light. Clicking on "Switch Theme" button will apply dark theme to page, and vice versa. Switching theme will save selected theme using SharedPreferences plugin for Android, iOS and FlutterWeb. Flutter Web is supported since [version: 0.5.6](https://pub.dev/packages/shared_preferences#056).

**Light Theme:**

![light-theme]({attach}../../images/flutter/ios_themes2.jpg)


**Dark Theme:**

![dark-theme]({attach}../../images/flutter/ios_themes3.jpg)

---

**Checkout the companion video tutorial:**
<iframe width="560" height="315" src="https://www.youtube.com/embed/" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

**Note:** In this article, I'll only focus on persisting data using SharedPreferences plugin. Please refer to [previous article](https://ptyagicodecamp.github.io/implement-flutter-themes-using-provider.html) for app architecture and other details.

### Step #1. `pubspec.yaml` ###
Add package dependencies in `pubspec.yaml`:
```
dependencies:
  flutter:
    sdk: flutter

  #SharedPreferences plugin for Android, iOS and Web
  shared_preferences: ^0.5.6
```

### Step #2. App's entry point ###

This code recipe is a part of the [code recipes](https://ptyagicodecamp.github.io/flutter-live-booklet-flutter-component-recipes.html#flutter-live-booklet-flutter-component-recipes) app as shown below:

![x-cookbook-flutter]({attach}../../images/flutter/cookbook_menu.jpg)

---

There are two ways to run this code recipe:

1. StandAlone: Use following code snippet at the top of the [themes_db.dart](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/themes/sharedPrefs/themes_sharedPrefs.dart) to run it independently.
```
void main() => runApp(ChangeNotifierProvider<ThemesNotifierSharedPrefs>(
    child: ThemesSharedPrefsCaching(),
    builder: (BuildContext context) {
      return ThemesNotifierSharedPrefs();
    }));
```

2. Code Recipe App: Use following code in [`router.dart`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/router.dart) to run this code recipe as part of the code recipe app.

```
case THEMES_DEMO_SHAREDPREFS:
  return MaterialPageRoute(builder: (context) {
    return ChangeNotifierProvider<ThemesNotifierSharedPrefs>(
      child: ThemesSharedPrefsCaching(),
      builder: (BuildContext context) {
        return ThemesNotifierSharedPrefs();
      },
    );
  });
  break;
```

### Step #3. Loading theme from SharedPreferences ###

Stateful widget `ThemesSharedPrefsCaching` loads active theme using `Provider.of<ThemesNotifierSharedPrefs>(context)
        .loadActiveThemeData(context);`

**themes_sharedPrefs.dart:**

```
class _ThemesSharedPrefsCachingState extends State<ThemesSharedPrefsCaching> {
  @override
  Widget build(BuildContext context) {
    Provider.of<ThemesNotifierSharedPrefs>(context)
        .loadActiveThemeData(context);
    return MaterialApp(
        theme: Provider.of<ThemesNotifierSharedPrefs>(context).currentThemeData,
        home: Scaffold(
          appBar: AppBar(
            title: Text("Theme Caching (SharedPreference)"),
          ),
          body: body(),
        ));
  }
  ...
}  
```

**themes_notifier_sp.dart:**

Fetching `theme_id` from database, loading and notifying currentTheme:

```
class ThemesNotifierSharedPrefs with ChangeNotifier {

  ...

  Future<void> activateTheme(MyThemes theme) async {
    var sharedPrefs = await SharedPreferences.getInstance();
    await sharedPrefs.setInt('theme_id', theme.index);
  }

  void loadActiveThemeData(BuildContext context) async {
    var sharedPrefs = await SharedPreferences.getInstance();
    int themeId = sharedPrefs.getInt('theme_id') ?? MyThemes.light.index;
    currentTheme = MyThemes.values[themeId];
  }

  set currentTheme(MyThemes theme) {
    if (theme != null) {
      _currentTheme = theme;
      _currentThemeData = themeData[_currentTheme.index];
      notifyListeners();
    }
  }

}
```


### Step #4. Switching and Saving theme to database ###

Switching theme toggles previously selected theme. We don't need to explicitly remove old theme since sharedPrefs key `theme_id` is updated to new value. Newly updated `currentTheme` overwrites the `theme_id` using api `activateTheme(...)`.

```
class ThemesNotifierSharedPrefs with ChangeNotifier {

  ...

  void switchTheme(BuildContext context) async {
    currentTheme == MyThemes.light
        ? currentTheme = MyThemes.dark
        : currentTheme = MyThemes.light;

    activateTheme(currentTheme);
  }

  ...
}
```

All Done !

### Source Code ###
1. Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/themes/db)

2. Code recipe project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)


### References: ###
1. [SharedPreferences plugin](https://pub.dev/packages/shared_preferences)
2. [Cross-platform ToDo App template](https://github.com/appleeducate/moor_shared)
3. [Previous article: Implement Flutter themes using Provider](https://ptyagicodecamp.github.io/implement-flutter-themes-using-provider.html)
4. [Related article: Persisting theme in LocalDatabase (Moor plugin)](https://ptyagicodecamp.github.io/persist-theme-setting-in-localdatabase-moor-plugin.html)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
