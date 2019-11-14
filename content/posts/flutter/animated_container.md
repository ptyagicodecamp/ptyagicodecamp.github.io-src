Title: Animating using AnimatedContainer Flutter widget
Date: 2019-11-13 11:33PM
Authors: ptyagi
Category: Flutter
Tags: AnimatedContainer, cross-platform, flutter, code-recipes, android, android Studio, iOS, development
Summary: Code recipe for implementing AnimatedContainer Flutter widget.  


## Introduction

`AnimatedContainer` widget is the animated version of the `Container` widget.

In this article, we'll see how `AnimatedContainer` widget is used to animate an image in it. We'll observe animation behavior for various types of [curves](https://api.flutter.dev/flutter/animation/Curves-class.html).

**Target Audience:** Beginner

**Recipe:** Animating a container widget using `AnimatedContainer` widget.

**Focus Widget:** `AnimatedContainer`

**Goal:** Animate an image inside `AnimatedContainer` using various types given [AnimationCurves](https://gist.github.com/ptyagicodecamp/92f7ab72466b65a82da2c44f1c2fc262)


![code recipe demo]({attach}../../images/flutter/anim_container_1.jpg)


**AnimationCurves:**

![animation curves]({attach}../../images/flutter/anim_curves.jpg)

---

**Checkout YouTube video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/0NVLyjtWJqc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Structure of `AnimatedContainer` widget

`AnimatedContainer` uses `duration` and `curve` properties to animate from previous values to new values of `width`, `height`, `color`, and `alignment`. `duration` value controls how long animation would take whereas `curve` property's value provides the type of animation [Curve](https://api.flutter.dev/flutter/animation/Curves-class.html)

```
AnimatedContainer(
        width: 100.0, //width of the container
        height: 100.0,
        color: Colors.blue,
        alignment: Alignment.center,
        duration: Duration(seconds: 2),
        curve: Curves.fastOutSlowIn,
        child: FlutterLogo(size: 75),
      ),
```

---

### Recipe's Code Structure ###

I'm using a drop down to choose the different type of `curve`. Animation curves used in this code recipe are available in the source code as well as [here](https://gist.github.com/ptyagicodecamp/92f7ab72466b65a82da2c44f1c2fc262).

`AnimatedContainer` needs to be implemented inside a `StatefulWidget` since its values are changed, and it provides animation while switching from old values to newer values.

`AnimationCurve dropDownValue` holds the current selection from the [AnimationCurves](https://gist.github.com/ptyagicodecamp/92f7ab72466b65a82da2c44f1c2fc262) drop down widget.

```
class AnimatedContainerDemo extends StatefulWidget {
  @override
  _AnimatedContainerDemoState createState() => _AnimatedContainerDemoState();
}

class _AnimatedContainerDemoState extends State<AnimatedContainerDemo> {
  AnimationCurve dropDownValue;
  bool selected = false;
  ...
}  
```

Boolean `selected` keeps track of when `Animate` button is pressed or image is touched.

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

---

### Implementing `AnimatedContainer` widget ###

`AnimatedContainer` is wrapped around `GestureDetector` to let user start animation by touch in addition to pressing 'Animate' button exclusively. User can choose one over another to start animation.

`AnimatedContainer` widget's default `width` is  200 and default `height` is 400, and its alignment is `topCenter`. When user presses 'Animate' button for a selected Curve type in dropDown widget, `width` updates to 400, `height` updated to 200, and its alignment changes to `center`. `AnimatedContainer` updates to new values with in `2` seconds as provided in `duration` attribute using current selection for `curve` property.

```
Widget animatedContainer(BuildContext context) {
  return GestureDetector(
    onTap: () {
      setState(() {
        selected = !selected;
      });
    },
    child: AnimatedContainer(
      width: selected ? 400.0 : 200.0,
      height: selected ? 200.0 : 400.0,
      alignment: selected ? Alignment.center : AlignmentDirectional.topCenter,
      duration: Duration(seconds: 2),
      curve: dropDownValue != null ? dropDownValue.curveCubic : Curves.linear,
      child: Image.asset('assets/images/sea.jpg'),
    ),
  );
}
```

I encourage you to Checkout the code below, and play around with different types of Curve animations to pick an animation that would work best for you.

---

### Source code repo ###

1. `AnimatedContainer` code recipe is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/blob/animations/flutter_animations/flutter_animations/lib/animations/anim_container.dart)
2. Source code for all other animation code recipes is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/animations/flutter_animations/flutter_animations)

---

### References: ###

1. [AnimatedContainer](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)
2. [Animation Curves](https://api.flutter.dev/flutter/animation/Curves-class.html)


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
