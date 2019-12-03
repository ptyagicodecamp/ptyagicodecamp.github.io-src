Title: Text-to-Speech Flutter Plugin (Android & iOS)
Date: 12/02/2019
Authors: ptyagi
Category: Flutter
Tags: Text-to-Speech, TTS, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Code recipe to demonstrate Text-To-Speech Flutter plugin in action.

**Target Audience:** Beginner

**Recipe:** Using text-to-speech Flutter plugin to read aloud text.

**Focus Plugin:** Text-To-Speech Flutter plugin: [flutter_tts](https://pub.dev/packages/flutter_tts)

**Goal:** We've a card with an image and its description. Clicking on play button will start reading aloud card's description, and stops when done.

***Note:*** This recipe has been added to Flutter cookbook code recipe app as shows below.

![Flutter-Cookbook-Widgets]({attach}../../images/flutter/tts_menu.jpg)

---
**Android:**

![Flutter-TTS-Android]({attach}../../images/flutter/tts_android.png)

![Flutter-TTS-Android2]({attach}../../images/flutter/tts_android2.png)

---
**iOS:**

![Flutter-TTS-iOS]({attach}../../images/flutter/tts_ios.jpg)


![Flutter-TTS-iOS2]({attach}../../images/flutter/tts_ios2.jpg)

---
**Checkout the Youtube video:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/ktsIgzhko6c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
### Lets's go! ###

This code recipe demonstrate implementation for [Text-to-speech Flutter plugin](https://pub.dev/packages/flutter_tts)

###`pubspec.yaml` dependencies ###

Add dependency for flutter_tts plugin:

```
dependencies:
  flutter_tts: ^0.7.0
```

---

### StatefulWidget ###

We need `StatefulWidget` as parent widget since we'll be triggering speaking on the touch of the play button.

* ``description`` is the text to be read on the click on play button.
* `isPlaying` is the flag to keep track whether text is being read or not. We need this flag to show appropriate `Icon` (play or stop) in the card.
* `FlutterTts _flutterTts` is the instance of `flutter_tts` plugin. It's a wrapper around the native implementation for Android and iOS to interact with native functionality. Under the hood, it uses `TextToSpeech` for Android, and `AVSpeechSynthesizer` for iOS platform.

```
class TTSPluginRecipe extends StatefulWidget {
  @override
  _TTSPluginRecipeState createState() => _TTSPluginRecipeState();
}

class _TTSPluginRecipeState extends State<TTSPluginRecipe> {
  String description =
      "The Griffith Observatory is the most iconic building in Los Angeles, perched high in the Hollywood Hills, 1,134 feet above sea level.";

  bool isPlaying = false;
  FlutterTts _flutterTts;    
}      
```

### Plugin management: Initializing & Disposing ###

Initializing plugin for Android is slightly different than for iOS. We need to detect the platform to run the specific code. Please checkout [`PlatformUtil`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/plugins/platform/platform.dart) to understand how I'm detecting platforms.

```
@override
void initState() {
  super.initState();
  initializeTts();
}

initializeTts() {
  _flutterTts = FlutterTts();

  if (PlatformUtil.myPlatform() == MyPlatform.ANDROID) {
    _flutterTts.ttsInitHandler(() {
      setTtsLanguage();
    });
  } else if (PlatformUtil.myPlatform() == MyPlatform.IOS) {
    setTtsLanguage();
  } else if (PlatformUtil.myPlatform() == MyPlatform.WEB) {
    //not-supported by plugin
  }

  _flutterTts.setStartHandler(() {
    setState(() {
      isPlaying = true;
    });
  });

  _flutterTts.setCompletionHandler(() {
    setState(() {
      isPlaying = false;
    });
  });

  _flutterTts.setErrorHandler((err) {
    setState(() {
      print("error occurred: " + err);
      isPlaying = false;
    });
  });
}


@override
void dispose() {
  super.dispose();
  _flutterTts.stop();
}

```

Don't forget to stop flutter_tts plugin instance in `dispose()` method.

### Speaking & Stopping ###

Speaking and Stop speaking is pretty straight forward. All you need to call plugin's `speak(String text)` and `stop()` methods / apis.

```
Future _speak(String text) async {
  if (text != null && text.isNotEmpty) {
    var result = await _flutterTts.speak(text);
    if (result == 1)
      setState(() {
        isPlaying = true;
      });
  }
}

Future _stop() async {
  var result = await _flutterTts.stop();
  if (result == 1)
    setState(() {
      isPlaying = false;
    });
}
```

### Exploring plugin's features ###

**Setting Language:**

```
void setTtsLanguage() async {
  await _flutterTts.setLanguage("en-US");
}
```

**Getting list of supported languages:**
```
  await flutterTts.getLanguages`
```

**Setting Voice:**
```
_flutterTts.setVoice("en-us-x-sfg#male_1-local")
```

**Getting list of supported voices:**
```
  await flutterTts.getVoices
```

---

### Source code repo ###

* Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/lib/tts)

* Code recipe project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)

---

### References: ###

1. [Plugin flutter_tts](https://pub.dev/packages/flutter_tts)
2. [`PlatformUtil`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets/flutter_widgets/lib/plugins/platform/platform.dart)


Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
