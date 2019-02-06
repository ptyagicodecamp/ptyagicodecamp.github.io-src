Title: Flutter code recipe for AnimatedOpacity widget
Date: 2019-1-30 11:33PM
Authors: ptyagi
Category: Development, Flutter, Cross-platform
Tags: AnimatedOpacity, flutter, code-recipes, android, android Studio, iOS
Summary: AnimatedOpacity widget is used to achieve a smooth transition from one UI element to another.

## AnimatedOpacity

AnimatedOpacity widget is used to achieve a smooth transition from one UI element to another.

***Target Audience:*** Beginner
***Recipe:*** Achieve a smooth animation when transitioning from one UI element to another.

***Focus Widget:*** AnimatedOpacity

***Goal:*** Fade in and out a blue rectangle on a click of button. 
Interface is super simple and will look like this:

Blue Rectangle animates when button is pressed:
![Alt Blue Rectangle animates when button is pressed]({attach}../../media/flutter/animatedOpacity/animated_opacity.png)

Checkout AnimatedOpacity animation: 
<iframe width="560" height="315" src="https://www.youtube.com/embed/lKO8YTq_QcU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Lets's go! ###

We need three things to accomplish our goal of animating a blue rectangle.
1. Widget to animate: A blue rectangle
```
    Container(
        width: 100,
        height: 150,
        color: Colors.blue,
    );
```
    
2. StatefulWidget: A way to hold visibility state of rectangle.
`StatefulWidget` has `State` object that can hold and update some data for app. 
`State` object's [`setState`](https://docs.flutter.io/flutter/widgets/State/setState.html) method helps to rebuild widget reflecting the updated state of the app data.

```
class AnimatedOpacityRecipe extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _AnimatedOpacityRecipeState();
}
```

The State object will have the flag about the rectangle widget's visibility state say `_visible`.
`_visible` to `true` means that rectangle is visible or vice versa.
```
class _AnimatedOpacityRecipeState extends State<AnimatedOpacityRecipe> {
  bool _visible = true;
  
} 
```
    
Method `animatedOpacityWidget` returns the AnimatedOpacity widget.
`duration` property is to control the speed of animation. 
In this example, it takes 900 milliseconds to fade out the rectangle.
This is important to show a smooth transition. 
```
Widget animatedOpacityWidget() {
    return AnimatedOpacity(
      duration: Duration(milliseconds: 900),
      opacity: _visible ? 1 : 0,
      child: _blueRectangle(),
    );
  }
```    
3. OutlineButton widget: A button to toggle fade in/out rectangle
Button labeled 'Animate' to fade in/out rectangle.
`setState()` method toggles the visibility flag for the rectangle widget.
It forces Flutter to rebuilt `AnimatedOpacity` widget in accordance with new value of `_visible` flag.
```
...
OutlineButton(
  shape: new RoundedRectangleBorder(
    borderRadius: new BorderRadius.circular(8.0),
  ),
  child: Text("Press to Animate"),
  onPressed: () {
    setState(() => _visible = !_visible);
  },
)
...
```

####Complete example code ####
```
import 'package:flutter/material.dart';

//starting the app
void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Cookbook',
      theme: ThemeData(
        // This is the theme of your application.
        primarySwatch: Colors.green,
      ),
      home: AnimatedOpacityRecipe(title: 'AnimatedOpacity Demo'),
    );
  }
}

class AnimatedOpacityRecipe extends StatefulWidget {
  final String title;

  AnimatedOpacityRecipe({Key key, this.title}) : super(key: key);
  @override
  State<StatefulWidget> createState() => _AnimatedOpacityRecipeState();
}

class _AnimatedOpacityRecipeState extends State<AnimatedOpacityRecipe> {
  bool _visible = true;

  Widget _blueRectangle() {
    return Container(
      width: 100,
      height: 150,
      color: Colors.blue,
    );
  }

  Widget animatedOpacityWidget() {
    return AnimatedOpacity(
      duration: Duration(milliseconds: 900),
      opacity: _visible ? 1 : 0,
      child: _blueRectangle(),
    );
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:Text(widget.title),
      ),
      body: buildDemoComponent(context),
    );
  }

  Widget buildDemoComponent(BuildContext context) {
    return Material(
      child: Padding(
        padding: EdgeInsets.all(8.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              child: Text(
                  'Press button to see blue rectangle fade out and in'
              ),
              padding: EdgeInsets.all(20.0),
            ),
            animatedOpacityWidget(),
            OutlineButton(
              shape: new RoundedRectangleBorder(
                borderRadius: new BorderRadius.circular(8.0),
              ),
              child: Text("Press to Animate"),
              onPressed: () {
                //Toggles visibility of the rectangle
                setState(() => _visible = !_visible);
              },
            )
          ],
        ),
      ),
    );
  }
}
```
***Source code repo:*** 
Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/master/flutter_animated_opacity)


### References: ###
1. https://flutter.io/docs/cookbook/animation/opacity-animation.html
2. https://docs.flutter.io/flutter/widgets/Opacity-class.html


__Liked the article ?
Couldn't find a topic of your interest ? Please leave comments below about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)