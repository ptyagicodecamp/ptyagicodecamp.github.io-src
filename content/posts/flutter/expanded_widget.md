Title: Responsive Flutter layout with Expanded widget
Date: 10/15/2020
Authors: ptyagi
Category: FlutterLayouts
Tags: FlutterLayouts, cross-platform, Flutter, code-recipes, Android, Android Studio, iOS, development, responsive
Summary: This article shows how to use Expanded widget to create responsive layout.

![Expanded]({attach}../../images/flutter/expanded.jpg)

**Target Audience:** Beginner

**Recipe:** Learn to use Expanded layout widget to create responsive layouts for Flutter applications.

**Focus Widget:** [Expanded](https://api.flutter.dev/flutter/widgets/Expanded-class.html)

---

The `Expanded` widget is a single child layout widget which means it can have only one child assigned to it. In this example, the `Row` widget has three children built using `childWidget()`. Each of the child is wrapped in the `Expanded` widget. All children expands themselves in the direction of main-axis, which is horizontal in this case. However, when a value for `flex` property can be provided to resolve any competition for the space. In the second example below, each `Expanded` widget is provided the `flex` value.


**Checkout the companion video tutorial:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/_iaFCRLBhzc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Using `Expanded` Widget

```dart
Row(
   children: [
     Expanded(
       child: childWidget(""),
     ),
     Expanded(
       child: childWidget(""),
     ),
     Expanded(
       child: childWidget(""),
     ),
   ],
 )
```

---

# Using ExpanDed widget (flex Property)

```Dart
Row(
   children: [
     Expanded(
       flex: 4,
       child: childWidget("4/8"),
     ),
     Expanded(
       flex: 3,
       child: childWidget("3/8"),
     ),
     Expanded(
       flex: 1,
       child: childWidget("1/8"),
     ),
   ],
 )
```

# Source Code Repo

* Please checkout the full source code for this example [here](https://github.com/ptyagicodecamp/flutter_cookbook2/blob/master/lib/responsive_widgets/expanded.dart)

* Flutter Cookbook2 project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook2)


# References
1.[Expanded](https://api.flutter.dev/flutter/widgets/Expanded-class.html)

Happy cooking with Flutter :)

_Liked the article? Let me know with 👏👏👏

Couldn't find a topic of interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
Follow me at [twitter](https://twitter.com/ptyagi13)
