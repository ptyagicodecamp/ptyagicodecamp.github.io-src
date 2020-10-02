Title: Responsive Flutter layout with FittedBox widget
Date: 10/01/2020
Authors: ptyagi
Category: FlutterLayouts
Tags: FlutterLayouts, cross-platform, Flutter, code-recipes, Android, Android Studio, iOS, development
Summary: This article shows how to use FittedBox widget to create responsive layout.

![FittedBox]({attach}../../images/flutter/fitted_box.jpg)

**Target Audience:** Beginner

**Recipe:** Learn to use FittedBox layout widget to create responsive layouts for Flutter applications.

**Focus Widget:** [FittedBox](https://api.flutter.dev/flutter/widgets/FittedBox-class.html)

---

The `FittedBox` widget is a single child layout widget which means it can have only one child assigned to it. In this example, the `Row` widget is added as child to `FittedBox` widget. The `Row` widget has two `Image` widgets as its children. Normally, the second child of `Row` widget will overflow to right when it renders its children on a screen size which is not sufficient to accommodate all of its children. However, with `FittedBox` this problem of widget overflowing is solved. It scales and position its child within the parent widget.


**Checkout the companion video tutorial:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/xU5ZGOoBI08" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Using `FittedBox` Widget

```Dart
FittedBox(
 child: Row(
   children: [
     Image.asset('assets/flutter_icon.png'),
     Image.asset('assets/flutter_icon.png'),
   ],
 ),
)
```

---

# Source Code Repo

* Source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook2/blob/master/lib/responsive_widgets/fitted_box.dart#L80:L84)

* Flutter Cookbook2 project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook2)


# References
1.[FittedBox](https://api.flutter.dev/flutter/widgets/FittedBox-class.html)

Happy cooking with Flutter :)

_Liked the article?Liked the article? Let me know with 👏👏👏

Couldn't find a topic of interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
Follow me at [twitter](https://twitter.com/ptyagi13)
