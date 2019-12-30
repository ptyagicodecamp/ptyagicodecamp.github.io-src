Title: Persist theme setting in LocalDatabase (Moor plugin)
Date: 12/30/2019
Authors: ptyagi
Category: Flutter
Tags: Caching, LocalDatabase, Moor, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Persisting theme setting in LocalDatabase using [Moor plugin](https://pub.dev/packages/moor)

![x-platform-themes]({attach}../../images/flutter/x-provider-themes.jpg)

### Background ###

In [this previous article](https://ptyagicodecamp.github.io/implement-flutter-themes-using-provider.html), we saw how to implement theme switching using Provider. In this article, we'll see how to save the selected theme in app's local database to persist the last selected theme across app restarts.

**Target Audience:** Beginner

**Recipe:** Persist selected theme in FlutterApp's local database using [Moor plugin](https://pub.dev/packages/moor).

**Focus Widget:** [Moor plugin](https://pub.dev/packages/moor)

**Goal:** Persisting chosen theme in local database. Implement a simple UI with an image, text and a button to switch themes. Page's default theme is light. Clicking on "Switch Theme" button will apply dark theme to page, and vice versa. Switching theme will save selected theme in app's local database using [Moor plugin](https://pub.dev/packages/moor).

**Light Theme:**

![light-theme]({attach}../../images/flutter/ios_themes2.jpg)


**Dark Theme:**

![dark-theme]({attach}../../images/flutter/ios_themes3.jpg)

---

**Checkout the companion video tutorial:**
<iframe width="560" height="315" src="https://www.youtube.com/embed/" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

**Note:** In this article, I'll only focus on persisting data in database. Please refer to [previous article](https://ptyagicodecamp.github.io/implement-flutter-themes-using-provider.html) for app architecture and other details.

### Step #1. `pubspec.yaml` ###
Add package dependencies in `pubspec.yaml`:
```
dependencies:
  flutter:
    sdk: flutter

  moor: ^2.2.0

  # Dart bindings to sqlite
  moor_ffi: ^0.2.0

  # Helper to find the database path on mobile
  path_provider: ^1.5.1
  path: ^1.6.4

  dev_dependencies:
    flutter_test:
      sdk: flutter

    #This generator library turns Table classes from moor into database code.
    moor_generator: ^2.2.0

    #generates files using Dart code.  
    build_runner: ^1.4.0
```

* [`moor` plugin](https://pub.dev/packages/moor) : Persistence library built on top of sqlite for Dart and Flutter. It works on Android, iOS and Web platforms for persisting data in local databases.

* [`moor_ffi` plugin](https://pub.dev/packages/moor_ffi) : This Flutter plugin generates Dart bindings to sqlite by using [`dart:ffi`](https://api.dart.dev/stable/2.7.0/dart-ffi/dart-ffi-library.html). `ffi` stands for `Foreign Function Interface`. This plugin can be used with Flutter and/or Dart VM applications and supports all platforms where sqlite3 is installed: iOS, Android (Flutter), macOS, Linux and Windows.

* [`path_provider` plugin](https://pub.dev/packages/path_provider) : This Flutter plugin is used for accessing filesystem on Android and iOS platforms.

* [`path` plugin](https://pub.dev/packages/path) : A cross-platform filesystem path manipulation library for Dart.

* [`moor_generator` plugin](https://pub.dev/packages/moor_generator) : This library contains the generator that turns your Table classes from moor into database code.

* [`build_runner` plugin](https://pub.dev/packages/build_runner) : This package is used to generate files. We need this package to be able to run this command `flutter packages pub run build_runner build --delete-conflicting-outputs` to generate `*.g.dart` files.

### Step #2.  Using Moor to prepare Database ###

First, we'll use Moor to prepare Database to save `theme_id` and `theme_name`. Selected theme's id will be saved. This table will have only one entry at a given time. When theme switched from `light` to `dark`, the older entry will be deleted, and newly selected theme's id will be added to this table. I kept it simple on purpose to demonstrate how moor can be integrated in your app.

Let's take look at our database file : `themes_pref.dart` below.

```
import 'package:flutter_widgets/themes/db/themes_notifier_db.dart';
import 'package:moor/moor.dart';

part 'theme_prefs.g.dart';

// this will generate a table called "theme_prefs" for us. The rows of that table will
// be represented by a class called "ThemePref".
class ThemePrefs extends Table {
  // MyThemes id
  IntColumn get theme_id => integer()();
  TextColumn get theme_name => text()();
}

// Moor prepares database table
@UseMoor(tables: [ThemePrefs])
class MyDatabase extends _$MyDatabase {
  MyDatabase(QueryExecutor e) : super(e);

  // Bump schemaVersion whenever there's change.
  @override
  int get schemaVersion => 1;

  //Keeping it simple
  //reset the database whenever there's update.
  // Add light theme as default theme after first launch and upgrade
  @override
  MigrationStrategy get migration {
    return MigrationStrategy(onCreate: (Migrator m) {
      return m.createAllTables();
    }, onUpgrade: (Migrator m, int from, int to) async {
      m.deleteTable(themePrefs.actualTableName);
      m.createAllTables();
    }, beforeOpen: (details) async {
      if (details.wasCreated) {
        await into(themePrefs).insert(ThemePrefsCompanion(
          theme_id: const Value(0),
          theme_name: Value(MyThemes.light.toString()),
        ));
      }
    });
  }

  void activateTheme(MyThemes theme) {
    ThemePref pref =
        ThemePref(theme_id: theme.index, theme_name: theme.toString());
    into(themePrefs).insert(pref);
  }

  void deactivateTheme(int i) =>
      (delete(themePrefs)..where((t) => t.theme_id.equals(i))).go();

  //The stream will automatically emit new items whenever the underlying data changes.
  Stream<bool> themeIdExists(int id) {
    return select(themePrefs)
        .watch()
        .map((prefs) => prefs.any((pref) => pref.theme_id == id));
  }

  Future<ThemePref> getActiveTheme() {
    return select(themePrefs).getSingle();
  }
}

```

Please note that this line will show error in the beginning because this file doesn't exist yet: `part 'theme_prefs.g.dart';`. You'll need to execute following command to generate sqlite bindings:

```
  flutter packages pub run build_runner build --delete-conflicting-outputs
```

`ThemePrefs` table contains only two fields: `theme_id` to save id for the theme and another field for saving name.
```
class ThemePrefs extends Table {
  // MyThemes id
  IntColumn get theme_id => integer()();
  TextColumn get theme_name => text()();
}
```

Following part actually prepares database table. This is the class where migration strategy is described. I kept migration strategy simple in this recipe. It resets the tables, and make `light` theme default in case of first launch or upgrade.

```
@UseMoor(tables: [ThemePrefs])
class MyDatabase extends _$MyDatabase {

}
```
### Step #3: Sharing Database implementation across platforms ###

We'll be creating one file to write shared code, and two files for native and web implementation for accessing database on corresponding platforms.

**Shared:** `shared.dart`

```
export 'unsupported.dart'
    if (dart.library.html) 'web.dart'
    if (dart.library.io) 'mobile.dart';
```

**Native (Android / iOS):** `mobile.dart`

```
//Note: Implementation borrowed from this To Do App Template project
//https://github.com/appleeducate/moor_shared
MyDatabase constructDb({bool logStatements = false}) {
  if (Platform.isIOS || Platform.isAndroid) {
    final executor = LazyDatabase(() async {
      final dataDir = await paths.getApplicationDocumentsDirectory();
      final dbFile = File(p.join(dataDir.path, 'db.sqlite'));
      return VmDatabase(dbFile, logStatements: logStatements);
    });
    return MyDatabase(executor);
  }
  if (Platform.isMacOS || Platform.isLinux) {
    final file = File('db.sqlite');
    return MyDatabase(VmDatabase(file, logStatements: logStatements));
  }
  if (Platform.isWindows) {
    final file = File('db.sqlite');
    return MyDatabase(VmDatabase(file, logStatements: logStatements));
  }
  return MyDatabase(VmDatabase.memory(logStatements: logStatements));
}
```

**Web:** `web.dart`

```
MyDatabase constructDb({bool logStatements = false}) {
  return MyDatabase(WebDatabase('db', logStatements: logStatements));
}

```

**Unsupported platform:** `unsupported.dart`

```
MyDatabase constructDb({bool logStatements = false}) {
  throw 'Platform not supported';
}
```

Checkout db plugin [source code here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/plugins/db).


### Step #4: App's entry point ###

This code recipe is a part of the [code recipes](https://ptyagicodecamp.github.io/flutter-live-booklet-flutter-component-recipes.html#flutter-live-booklet-flutter-component-recipes) app as shown below:

![x-cookbook-flutter]({attach}../../images/flutter/cookbook_menu.jpg)

---

There are two ways to run this code recipe:

1. StandAlone: Use following code snippet at the top of the [themes_db.dart](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/themes/db/themes_db.dart) to run it independently.
```
void main() => runApp(MultiProvider(
      providers: [
        Provider<MyDatabase>(
          builder: (_) => constructDb(logStatements: true),
          dispose: (context, db) => db.close(),
        ),
        ChangeNotifierProvider<ThemesNotifierDB>(
          builder: (_) {
            return ThemesNotifierDB();
          },
        )
      ],
      child: ThemesDBCaching(),
    ));
```

2. Code Recipe App: Use following code in [`rounter.dart`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/router.dart) to run this code recipe as part of the code recipe app.

```
case THEMES_DEMO_DB:
  return MaterialPageRoute(builder: (context) {
    return MultiProvider(
      providers: [
        Provider<MyDatabase>(
          builder: (_) => constructDb(logStatements: true),
          dispose: (context, db) => db.close(),
        ),
        ChangeNotifierProvider<ThemesNotifierDB>(
          builder: (_) {
            return ThemesNotifierDB();
          },
        )
      ],
      child: ThemesDBCaching(),
    );
  });
  break;
```

### Step #5: Loading theme from database ###

Stateful widget `ThemesDBCaching` loads active theme using `Provider.of<ThemesNotifierDB>(context).loadActiveThemeData(context);`

Here's code snippet:

```
class _ThemesDBCachingState extends State<ThemesDBCaching> {
  @override
  Widget build(BuildContext context) {

    Provider.of<ThemesNotifierDB>(context).loadActiveThemeData(context);

    return MaterialApp(
        theme: Provider.of<ThemesNotifierDB>(context).currentThemeData,
        home: Scaffold(
          appBar: AppBar(
            title: Text("Theme DB Caching (Moor)"),
          ),
          body: body(),
        ));
  }
  ...
}  
```

Fetching `theme_id` from database, loading and notifying currentTheme:

```
//fetch theme_id from database
Future<int> getActiveThemeID(BuildContext context) {
  return Provider.of<MyDatabase>(context)
      .getActiveTheme()
      .then((themePref) => themePref.theme_id);
}

//Load active theme using theme_id
void loadActiveThemeData(BuildContext context) async {
  int themeId = await getActiveThemeID(context);
  currentTheme = MyThemes.values[themeId];
}

//notify to listeners about the updated theme
set currentTheme(MyThemes theme) {
  if (theme != null) {
    _currentTheme = theme;
    _currentThemeData = themeData[_currentTheme.index];
    notifyListeners();
  }
}
```


### Step #6: Switching and Saving them to database ###

Switching theme toggles previously selected theme. `oldTheme` is removed from the database using `deactivateTheme(...)`. Newly updated `currentTheme` is added to database using `activateTheme(...)`.

```
void switchTheme(BuildContext context) async {
  var oldTheme = currentTheme;

  currentTheme == MyThemes.light
      ? currentTheme = MyThemes.dark
      : currentTheme = MyThemes.light;

  var myDatabase = Provider.of<MyDatabase>(context);
  var isOldThemeActive = myDatabase.themeIdExists(oldTheme.index);

  if (isOldThemeActive != null) {
    myDatabase.deactivateTheme(oldTheme.index);
  }

  myDatabase.activateTheme(currentTheme);
}
```

All Done !

### Source Code ###
1. Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/themes/db)

2. Code recipe project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)


### References: ###
1. [`moor` plugin](https://pub.dev/packages/moor)
2. [`moor_ffi` plugin](https://pub.dev/packages/moor_ffi)
3. [`path_provider` plugin](https://pub.dev/packages/path_provider)
4. [`path` plugin](https://pub.dev/packages/path)
5. [`moor_generator` plugin](https://pub.dev/packages/moor_generator)
6. [`build_runner` plugin](https://pub.dev/packages/build_runner)
7. [Cross-platform ToDo App template](https://github.com/appleeducate/moor_shared)
8. [Previous article: Implement Flutter themes using Provider](https://ptyagicodecamp.github.io/implement-flutter-themes-using-provider.html)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
