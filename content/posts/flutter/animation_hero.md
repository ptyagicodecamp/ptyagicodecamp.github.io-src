Title: Flutter code recipe for Hero animation
Date: 2019-1-30 11:33PM
Authors: ptyagi
Category: Flutter
Tags: hero-animation, cross-platform, flutter, code-recipes, android, android Studio, iOS, development
Summary: Navigating from one page to another using Hero animation.

## Animation Hero

Hero animation is a useful transition when items are listed with small icons. Tapping on
icons can open in another page with enlarged icon widget.

**Target Audience:** Beginner
**Recipe:** Hero animation to transition a list icon into an enlarged view on another detail page.

**Focus Widget:** Hero Widget
```
Hero(
    tag: 'hero-rectangle',
    child: _blueDetailRectangle(),
),
```

**Goal:** Animate and enlarge list item icon using `Hero` widget.
Tapping on a list item icon, opens up the item in another page with enlarged icon.

![List item icon]({attach}../../media/flutter/animationHero/1.png)
![Detail page icon]({attach}../../media/flutter/animationHero/2.png)


Checkout Hero animation:
<iframe width="560" height="315" src="https://www.youtube.com/embed/InhIo7HNU-I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Lets's go! ###

We need these things to accomplish our goal.
1. List item along with Icon: I'll be using a rectangle widget for icon.

Icon widget in list item at first page:

```
    Widget _blueIconRectangle() {
        return Container(
          width: 50,
          height: 50,
          color: Colors.blue,
    );
  }
```  
`Hero` widget in list:
```
Widget buildWidget(BuildContext context) {
    return Center(
        ...
              child: Hero(
                tag: 'hero-rectangle',
                child: _blueIconRectangle(),
              ),
              onTap: () => _gotoDetailsPage(context),

        ...
  }
```
2. Enlarged icon to display on the second page.

```
  Widget _blueDetailRectangle() {
    return Container(
      width: 200,
      height: 200,
      color: Colors.blue,
    );
  }
```
Using enlarged icon in second page:

```
void _gotoDetailsPage(BuildContext context) {
    Navigator.of(context).push(MaterialPageRoute(
      builder: (ctx) => Scaffold(
            body: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Hero(
                    tag: 'hero-rectangle',
                    child: _blueDetailRectangle(),
                  ),
                  Text(
                      'This is where you can see details about the list item tapped at previous page.'),
                ],
              ),
            ),
          ),
    ));
  }
```
Notice that `Navigator.of(context).push()` is needed to navigate to second page from first page
using the same tag.

3. Making sure both widgets in step #1 and step #2 ***have same tag***.
Hero transitions use the same tag to identify the start and destination widgets.


####Complete example code ####
```
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: HeroAnimationRecipe(title: 'Hero Animation'),
    );
  }
}

class HeroAnimationRecipe extends StatefulWidget {
  HeroAnimationRecipe({Key key, this.title}) : super(key: key);
  final String title;

  @override
  _HeroAnimationRecipeState createState() => _HeroAnimationRecipeState();
}

class _HeroAnimationRecipeState extends State<HeroAnimationRecipe> {

  Widget _blueIconRectangle() {
    return Container(
      width: 50,
      height: 50,
      color: Colors.blue,
    );
  }

  Widget _blueDetailRectangle() {
    return Container(
      width: 200,
      height: 200,
      color: Colors.blue,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: buildDemoWidget(context),
    );
  }

  Widget buildDemoWidget(BuildContext context) {
    return Center(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          SizedBox(
            height: 20.0,
          ),
          ListTile(
            leading: GestureDetector(
              child: Hero(
                tag: 'hero-rectangle',
                child: _blueIconRectangle(),
              ),
              onTap: () => _gotoDetailsPage(context),
            ),
            title: Text('Tap on the icon to view hero animation transition.'),
          ),
        ],
      ),
    );
  }

  void _gotoDetailsPage(BuildContext context) {
    Navigator.of(context).push(MaterialPageRoute(
      builder: (ctx) => Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Hero(
                tag: 'hero-rectangle',
                child: _blueDetailRectangle(),
              ),
              Text(
                  'This is where you can see details about the list item tapped at previous page.'),
            ],
          ),
        ),
      ),
    ));
  }
}

```
**Source code repo:**
Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/master/flutter_hero_animation)


### References: ###
1. [Cookbook](https://flutter.io/docs/development/ui/animations/hero-animations)
2. [Reference](https://flutterbyexample.com/hero-transition)
3. [Youtube video](https://www.youtube.com/watch?v=Be9UH1kXFDw)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
