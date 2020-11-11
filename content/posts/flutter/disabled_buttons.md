Title: Disabling Flutter Buttons
Date: 11/11/2020
Authors: ptyagi
Category: Widgets
Tags: Widgets, cross-platform, Flutter, code-recipes, Android, Android Studio, iOS, development, responsive
Summary: This micro article gives pointers to disable buttons in Flutter applications.

![DisabledButtons]({attach}../../images/flutter/disabled_buttons.jpg)


This micro article shows how to disable the RaisedButton and FlatButton widgets in Flutter applications.

The `RaisedButton` and/or `FlatButton` widget(s) can be disabled by assigning `onPressed` property to `null`. They can be disabled when `onPressed` property is not used at all. In order to make these widgets clickable, a function needs to be assigned to the `onPressed` property.

**Checkout the companion video tutorial:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Disabling `RaisedButton` Widget


```Dart

RaisedButton(
  child: Text("Disabled Button"),
  onPressed: null,
  disabledColor: Colors.black12,
  disabledElevation: 1,
  disabledTextColor: Colors.blueGrey,
),
```

---

# Disabling `FlatButton` Widget

```Dart
FlatButton(
  child: Text("Disabled Button"),
  onPressed: null,
  disabledColor: Colors.black12,
  disabledTextColor: Colors.blueGrey,
),
```

---

# Source Code Repo

* Please checkout the full source code for this example [here](https://github.com/ptyagicodecamp/flutter_cookbook2/blob/master/lib/buttons/disabled_buttons.dart)

* Flutter Cookbook2 project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook2)


# References
1. [RaisedButton](https://api.flutter.dev/flutter/material/RaisedButton-class.html)
2. [FlatButton](https://api.flutter.dev/flutter/material/FlatButton-class.html)
3. [TextButton](https://api.flutter.dev/flutter/material/TextButton-class.html)

Happy cooking with Flutter :)

_Liked the article? Let me know with 👏👏👏

Couldn't find a topic of interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
Follow me at [twitter](https://twitter.com/ptyagi13)
