Title: Animating using AnimatedPositioned Flutter widget
Date: 2019-11-14 1:33PM
Authors: ptyagi
Category: Flutter
Tags: AnimatedPositioned, cross-platform, flutter, code-recipes, android, android Studio, iOS, development
Summary: Code recipe for implementing AnimatedPositioned Flutter widget.  


## Introduction

`AnimatedPositioned` widget is the animated version of the `Positioned` widget.

In this article, we'll see how `AnimatedPositioned` widget is used to animate an image in it. We'll observe animation behavior for various types of [curves](https://api.flutter.dev/flutter/animation/Curves-class.html).

**Target Audience:** Beginner

**Recipe:** Animating an image in `AnimatedPositioned` widget.

**Focus Widget:** `AnimatedPositioned`

**Goal:** Animate an image inside `AnimatedPositioned` using various types given [AnimationCurves](https://gist.github.com/ptyagicodecamp/92f7ab72466b65a82da2c44f1c2fc262)


![code recipe demo]({attach}../../images/flutter/anim_positioned_1.jpg)


**AnimationCurves:**

![animation curves]({attach}../../images/flutter/anim_curves.jpg)

---

**Checkout YouTube video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/NRxaBMecN9E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Structure of `AnimatedPositioned` widget

`AnimatedPositioned` uses `duration` and `curve` properties to animate from previous position to a new position. The `duration` value controls how long animation would take whereas `curve` property's value provides the type of animation [Curve](https://api.flutter.dev/flutter/animation/Curves-class.html)

```
AnimatedPositioned(
      width: selected ? 400.0 : 200.0,
      height: selected ? 200.0 : 400.0,
      duration: Duration(seconds: 2),
      curve: dropDownValue != null ? dropDownValue.curveCubic : Curves.linear,
      child: Image.asset('assets/images/sea.jpg'),
    ),
```

### Recipe's Code Structure ###

I'm using a drop down to choose the different type of `curve`. Animation curves used in this code recipe are available in the source code as well as [here](https://gist.github.com/ptyagicodecamp/92f7ab72466b65a82da2c44f1c2fc262).

`AnimatedPositioned` needs to be implemented inside a `StatefulWidget` since it can only animate when position is changed.

`AnimationCurve dropDownValue` holds the current selection from the [AnimationCurves](https://gist.github.com/ptyagicodecamp/92f7ab72466b65a82da2c44f1c2fc262) drop down widget.

```
class AnimatedPositionedDemo extends StatefulWidget {
  @override
  _AnimatedPositionedDemoState createState() => _AnimatedPositionedDemoState();
}

class _AnimatedPositionedDemoState extends State<AnimatedPositionedDemo> {
  AnimationCurve dropDownValue;
  bool selected = false;

  ...
}  
```

Boolean `selected` keeps track of when 'Animate' button is pressed or image is touched.

'Animate' button next to dropDown widget. It updates the value of `selected` as below:

```
Widget playAnimation(BuildContext context) {
  return RaisedButton(
    color: Colors.blueAccent,
    child: Text("Animate"),
    onPressed: () => setState(() {
      selected = !selected;
    }),
  );
}
```

### Implementing `AnimatedPositioned` widget ###

`AnimatedPositioned` widget's default `position` or `width` / `height` are  200.0 and 400.0 respectively. When user presses 'Animate' button for a selected Curve type in dropDown widget, position or `width` and `height` are updated to 400.0 and 200.0 respectively. `AnimatedPositioned` updates its position to a new value with in `2` seconds as provided in `duration` attribute using current selection for `curve` property.

```
Widget animatedPositionedWidget(BuildContext context) {
  return AnimatedPositioned(
    width: selected ? 400.0 : 200.0,
    height: selected ? 200.0 : 400.0,
    duration: Duration(seconds: 2),
    curve: dropDownValue != null ? dropDownValue.curveCubic : Curves.linear,
    child: Image.asset('assets/images/sea.jpg'),
  );
}
```

I encourage you to Checkout the code below, and play around with different types of Curve animations to pick an animation that would work best for you.

### Source code repo ###

1. `AnimatedPositioned` code recipe is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/blob/animations/flutter_animations/flutter_animations/lib/animations/anim_positioned.dart)
2. Source code for all other animation code recipes is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/animations/flutter_animations/flutter_animations)


### References: ###

1. [AnimatedPositioned](https://api.flutter.dev/flutter/widgets/AnimatedPositioned-class.html)
2. [Animation Curves](https://api.flutter.dev/flutter/animation/Curves-class.html)


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
