Title: Saving Image in Finger Painting App in Flutter
Date: 08/16/2020
Authors: ptyagi
Category: Flutter
Tags: Canvas, Painting, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: This code recipe focuses on saving your finger painted image in device's image gallery.

![Canvas-Painting]({attach}../../images/flutter/canvas_header.jpg)

**Target Audience:** Beginner

**Recipe:** This code recipe covers saving canvas painting created in previous article [Building Cross-Platform Finger Painting App in Flutter](https://ptyagicodecamp.github.io/building-cross-platform-finger-painting-app-in-flutter.html), to device's image gallery.

**Focus Plug-in:** [image_gallery_saver](https://pub.dev/packages/image_gallery_saver)

---

**Checkout the companion video tutorial:**
<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# `pubspec.yaml` dependencies

Add `image_gallery_saver` plugin in the `pubspec.yaml`:
```
dependencies:
  image_gallery_saver: ^1.5.0
```
Add following dependencies in `pubspec.yaml` to handle permissions on Android platform:

```
dependencies:
  permission_handler: ^5.0.1+1
```

---

# iOS Info.plist

You need to add following entry in the `Info.plist`:

```
<key>NSPhotoLibraryAddUsageDescription</key>
<string>Need to access photo library to save your creation</string>
```

# GlobalKey & RepaintBoundary Widget

We'll use global key to keep track of the widget to be saved. The `Stack` widget is wrapped in [`RepaintBoundary`](https://api.flutter.dev/flutter/widgets/RepaintBoundary-class.html) widget to create separate display list of its child.

```
class _CanvasPaintingState extends State<CanvasPainting> {
  GlobalKey globalKey = GlobalKey();

  @override
Widget build(BuildContext context) {
  return MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Scaffold(
      body: GestureDetector(
        ...
        child: RepaintBoundary(
          key: globalKey,
          child: Stack(
            children: <Widget>[
              Center(
                child: Image.asset("assets/images/hut.png"),
              ),
              CustomPaint(
                size: Size.infinite,
                painter: MyPainter(
                  pointsList: points,
                ),
              ),
            ],
          ),
        ),
      ),
      ...
    ),
  );
}

}  
```
# Adding Save FAB

```
FloatingActionButton(
  heroTag: "paint_save",
  child: Icon(Icons.save),
  tooltip: 'Save',
  onPressed: () {
    //min: 0, max: 50
    setState(() {
      _save();
    });
  },
)
```

# Saving Image to Gallery

The FAB's `onPressed()` method calls the asynchronous `_save()` method to save the current state of canvas as image to gallery.

```
Future<void> _save() async {
  RenderRepaintBoundary boundary =
      globalKey.currentContext.findRenderObject();
  ui.Image image = await boundary.toImage();
  ByteData byteData = await image.toByteData(format: ui.ImageByteFormat.png);
  Uint8List pngBytes = byteData.buffer.asUint8List();

  //Request permissions if not already granted
  if (!(await Permission.storage.status.isGranted))
    await Permission.storage.request();

  final result = await ImageGallerySaver.saveImage(
      Uint8List.fromList(pngBytes),
      quality: 60,
      name: "canvas_image");
  print(result);
}
```

# Source code repo

* Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/canvas/painting.dart)

* Code recipe project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)

### References: ###

1. Building Cross-Platform Finger Painting App in Flutter](https://ptyagicodecamp.github.io/building-cross-platform-finger-painting-app-in-flutter.html)
2. [The image_gallery_saver Plugin](https://pub.dev/packages/image_gallery_saver)


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
