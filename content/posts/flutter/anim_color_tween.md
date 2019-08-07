Title: Using ColorTween in Flutter app
Date: 08/07/2019
Authors: ptyagi
Category: Flutter
Tags: ColorTween, Animations, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development, Hummingbird
Summary: This recipe demonstrates using [ColorTween](https://api.flutter.dev/flutter/animation/ColorTween-class.html) animation class to achieve transition from one color to another.

**Target Audience:** Beginner

**Recipe:** Implement animation using ColorTween for Android, iOS and WebApp.

**Focus Widget:** [ColorTween](https://api.flutter.dev/flutter/animation/ColorTween-class.html)

**Goal:** Animating from one color to another for a quiz card's background based on the correct answer. We'll implement a card with picture of an animal in it, along with two choices to select from: 'Carnivorous' or 'Herbivorous'. When correct option is picked, background color of card will transition from grey to blue color in order to indicate correct selection otherwise background stays grey or turns grey from blue.

<div style="width:100%;height:100%;padding-bottom:50%;position:relative;"><iframe src="https://giphy.com/embed/MCitgRspdAVS9l7geK" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>



### ColorTween for Native platforms (Android & iOS) ###

**Step #1. Data (`items.dart`)**
I'll be creating a little data structure `CardItem` to keep track of model for UI card.
It has four parts to represent a Quiz card: `title`, `description`, `image` and `animalType`.
`title` and `description` are not used to render on Card UI. `image` has path to image in `assets` directory in Android Studio.
```
class CardItem {
  final String title;
  final String description;
  final String image;
  final String animalType;

  CardItem(this.title, this.description, this.image, this.animalType);

  CardItem.fromMap(Map<String, dynamic> data)
      : title = data["title"],
        description = data["description"],
        image = data["image"],
        animalType = data['animalType'];

  static List<CardItem> fromData(List<dynamic> data) {
    return data.map((item) => CardItem.fromMap(item)).toList();
  }
}
```
In the class above, you might have noticed `fromMap(...)` and `fromData(...)` methods, which are used to parse `json` data (intended to be fetched over network). In this recipe, I've hard-wired the sample `json` data as below:
```
[  
   {  
      "title":"cat",
      "description":"Cat is carnivorous animal.",
      "image":"assets/images/carnivorous_cat.jpg",
      "animalType":"carnivorous"
   },
   {
     ...
   },
   ...
]
```

Parsing json string above is done as below:
```
final List<CardItem> cardItems =
    CardItem.fromData(json.decode(Samples.jsonData()));
```

Now, importing `items.dart` in any class/file, will give access to `cardItems`. An item in list can be accessed as `cardItems[0], cardItems[1]` and so on.

**Step #2. User Interface (`color_tween.dart`)**
We'll be implementing following quiz like card to demonstrate transitioning from grey color to blue and vice versa.

UI's body has main three parts:

* [`Positioned Widget`](https://api.flutter.dev/flutter/widgets/Positioned-class.html): To display card.
* Image: image of the animal to quiz on.
* Row of [FlatButton](https://api.flutter.dev/flutter/material/FlatButton-class.html) widgets: Two FlatButton to present choice of `Carnivorous` in red and `Herbivorous` in green color.

![Color Tween]({attach}../../images/flutter/color_tween1.jpg)

**Step #2-a. Quiz Card UI anatomy:**
```
@override
Widget build(BuildContext context) {
  //we need screenSize to render card relative to the given device's screen size
  Size screenSize = MediaQuery.of(context).size;

  //Fetching image from `assets` folder
  DecorationImage decorationImage = DecorationImage(
      image: AssetImage(cardItems[0].image), fit: BoxFit.fitWidth);

  return Scaffold(
    appBar: AppBar(...),
    body: Container(
      ...

      Positioned(
        child: Card(
          ...
          //parent container to host the quiz card
          child: Container(
            alignment: Alignment.center,
            width: screenSize.width / 1.2,
            height: screenSize.height / 1.7,
            ...,

            //Contents of card: Image and FlatButtons for quiz options
            child: Column(
              children: <Widget>[

                //Image of quiz animal
                Container(
                  //Note: width of image is same as parent
                  width: screenSize.width / 1.2,

                  //Note: Image's height is smaller than parent, so that parent can contain image inside it.
                  height: screenSize.height / 2.2,

                  //Rendering image
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.only(
                        topLeft: Radius.circular(8.0),
                        topRight: Radius.circular(8.0),
                      ),
                      image: decorationImage),
                ),
                //Widget to contain FlatButtons for quiz options
                Container(
                  //Width remains same as of parent, however height needs to be calculated to position in under image.
                  width: screenSize.width / 1.2,
                  height:
                      screenSize.height / 1.7 - screenSize.height / 2.2,

                  child: Row(
                    ...
                    children: <Widget>[
                      FlatButton(
                        ..
                        //Animation trigger: This is where animation will be triggered
                        onPressed: () => {},
                        child: Container(
                          ..
                          child: Text("Carnivorous"),
                        ),
                      ),
                      FlatButton(
                        ..
                        //Animation trigger: This is where animation will be triggered
                        onPressed: () => {},
                        child: Container(
                          ..
                          child: Text("Herbivorous"),
                        ),
                      ),
                    ],
                  ),
                )
              ],
            ),
          ),
        ),

      ),
    ),
  );
}
```
**Step #3: Implementing ColorTween Animation**

Finally, time to implement transition animation from grey to blue color using ColorTween class. There are couple of steps that we would need to achieve that.

* Using [`SingleTickerProviderStateMixin`](https://api.flutter.dev/flutter/widgets/SingleTickerProviderStateMixin-mixin.html) with `Stateful` parent's `State`:
```
class ColorTweenAnimationDemo extends StatefulWidget {
  @override
  _ColorTweenAnimationDemoState createState() =>
      new _ColorTweenAnimationDemoState();
}

class _ColorTweenAnimationDemoState extends State<ColorTweenAnimationDemo>
    with SingleTickerProviderStateMixin {
      ...
}

```

* Initializing [`AnimationController`](https://api.flutter.dev/flutter/animation/AnimationController-class.html) and [`Animation`](https://api.flutter.dev/flutter/animation/Animation-class.html) inside `initState()`. AnimationController is intended to control the state of the animation like starting using `forward()`, revering using `reverse()` and stopping. `Animation<Color>` will be used to define value change between one color to another, which is from grey to blue in our case. `ColorTween` class is exactly what it says `between colors`. It begins with beginning color 'grey' and ends with `blue`. This transition behavior is attached with AnimationController `_controller` to manage the animation. A listener can be added to listen to state changes from where it starts until it stops.
```
...

AnimationController _controller;
Animation<Color> animation;

@override
void initState() {
  super.initState();

  _controller = AnimationController(
    duration: const Duration(milliseconds: 2000),
    vsync: this,
  );

  animation = ColorTween(
    begin: Colors.grey,
    end: Colors.blue,
  ).animate(_controller)
    ..addListener(() {
      setState(() {});
    });
}
```

* **Animating Card's background:** [Add `animation.value` as `color` attribute for `BoxDecoration(...)` in parent's card widget like below:](https://github.com/ptyagicodecamp/flutter_cookbook/blob/animations-native/flutter_widgets/lib/anims/color_tween.dart#L62:L65)
```
...
//parent container to host the quiz card
child: Container(
                  ...
                  width: screenSize.width / 1.2,
                  height: screenSize.height / 1.7,
                  decoration: BoxDecoration(
                    color: animation.value,
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                  ...
                )
...

```

* **Triggering animation:** We want our color change animation starts when we click the right answer which is `Carnivorous` in out case. When we press `FlatButton` at left, background color changes from grey to blue. When `FlatButton` at right, `Herbivorous` is clicked, `reverse()` animation is called, which changes color from blue to back to grey. Let's see how animation is started from FlatButton's `onPressed()` methods:
```
children: <Widget>[
  FlatButton(
    ..
    //Animation trigger: This is where animation will be triggered, responsible to change color from grey to blue.
    onPressed: () => {_controller.forward()},
    child: Container(
      ..
      child: Text("Carnivorous"),
    ),
  ),
  FlatButton(
    ..
    //Animation trigger: This is where the reverse animation will be triggered, responsible to change color back to grey.
    onPressed: () => {_controller.reverse()},
    child: Container(
      ..
      child: Text("Herbivorous"),
    ),
  ),
],
```

* **Disposing AnimationController:** Don't forget to dispose AnimationController.
```
@override
dispose() {
  _controller?.dispose();
  super.dispose();
}
```

### What about Flutter Web ? ###

**Note:** As of today Aug 7th, 2019- There's [an issue](https://github.com/flutter/flutter/issues/37761) in running Flutter Web App after upgrading to the latest version of Flutter SDK.

Let's achieve the same animations on Web platform. Please refer to my [this article](https://ptyagicodecamp.github.io/designing-cross-platform-flutter-prototype-for-landing-page-web-hummingbird-android-ios.html), if you're new to Flutter-Web / Hummingbird and need help with setting up web project.
In short, we would need to create an another branch say `animations-web` to host all web related code since web libraries are not pushed to same repository as of native platform. You'll need to fetch libraries directly from their Github repo.

* It means imports in native vs web platform are different. Make sure that all files have correct web intended imports.
```
Native:
import 'package:flutter/material.dart';

Web:
import 'package:flutter_web/material.dart';
```

* `pubspec.yaml`: I keep a backup for native and web `pubspec.yaml` config as `pubspec.yaml.web` and `pubspec.yaml.native` in both branches. Copy correct file's content into current `pubspec.yaml`.

* Building project in web branch `animations-web`:
```
flutter clean

flutter pub get

flutter packages pub global run webdev serve

```

**Source code repo:**

* Native (Android / iOS) recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/animations-native/flutter_widgets)

* Web (Hummingbird) recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/animations-web/flutter_widgets)


### References: ###
1. [ColorTween](https://api.flutter.dev/flutter/animation/ColorTween-class.html)
2. [AnimationController](https://api.flutter.dev/flutter/animation/AnimationController-class.html)
3. [Animation](https://api.flutter.dev/flutter/animation/Animation-class.html)
4. [SingleTickerProviderStateMixin](https://api.flutter.dev/flutter/widgets/SingleTickerProviderStateMixin-mixin.html)
5. [Positioned Widget](https://api.flutter.dev/flutter/widgets/Positioned-class.html)
6. [FlatButton](https://api.flutter.dev/flutter/material/FlatButton-class.html)


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
