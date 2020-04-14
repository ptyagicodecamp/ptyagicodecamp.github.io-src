Title: Dart Enums
Date: 04/14/2020
Authors: ptyagi
Category: Dart
Tags: enum, dart, cross-platform, flutter, code-recipes, development
Summary: This article explains Dart Enums and when and how to use them.


![enums]({attach}../../images/dart/enums.png)

# Introduction

Enums (a.k.a Enumerated Types) were added as an experimental feature in [Dart 1.8 release](https://news.dartlang.org/2014/11/dart-18-library-improvements-and.html). Enums are like a class that represent a fixed number of constant values.

Imagine that you're working on a weather application, and you need a way to represent different states for weather. For example, weather can be sunny, cloudy or rainy. Now, you have two ways to represent these states in your code.

## Using Constants

You can represent each state using a `const` [keyword](https://dart.dev/guides/language/language-tour#keywords).

```
const SUNNY = 'Sunny';
const CLOUDY = 'Cloudy';
const RAINY = 'Rainy';
```

## Using Enumerated Types

Another way to represent the same information is to use enumerated types using the `enum` keyword.

```
enum Weather {
  SUNNY,
  CLOUDY,
  RAINY,
}
```


In the following section, let's explore the cases where using Enums make more sense.

---

# Switch

When using `switch` block, constants behave differently than enums.

### Using Constants

When different type of weather state is represented using `const`, it's okay with
`switch` block to declare `case` block for one constant. `default` block is optional as well.
There's no compilation error when only one case block for `SUNNY` is declared, without `default` block.

```
//Using constants to display weather information
void mainSwitchConstants() {
  const SUNNY = 'Sunny';
  const CLOUDY = 'Cloudy';
  const RAINY = 'Rainy';

  //#1. Switch doesn't complain for const, but raise error for enums
  var choice = SUNNY;
  switch (choice) {
    case SUNNY:
      print("Sunny weather today");
      break;
  }
}

```

**Output:**

```
Sunny weather today
```


### Using Enums

The `switch` block for enums requires case blocks for all of the enum class `Weather` members. The `default` block is required when case blocks for all enumerated type members are not available. Otherwise, you would see the compilation error like below:

![enums]({attach}../../images/dart/enums_switch.jpg)


Here's `switch` block with case blocks for all enum members:

```
//Using Enums to display weather information
void mainSwitchEnums() {
  var weather = Weather.SUNNY;

  //Following code will complain about
  // not including other types of weather
  //OR use default
  switch (weather) {
    case Weather.SUNNY:
      print("Sunny weather today!");
      break;
    case Weather.CLOUDY:
      print("Cloudy today!");
      break;
    case Weather.RAINY:
      print("Rainy and gloomy weather.");
      break;
  }
}
```

**Output:**

```
Sunny weather today!
```

Check out the `switch` block when there's only `default` block is available. It prints the value of the current enum passed.

```
//Only default case. No compilation issue
void mainSwitchEnumsDefault() {
  var weather = Weather.SUNNY;

  switch (weather) {
    default:
      print("Current weather:${weather}");
  }
}
```

**Output:**

```
Current weather:Weather.SUNNY
```

---


# Iterating

The another reason to use enums over constants could be to iterate over all the different types of weather. For constants, you would need a list to store all values, and then iterate over that list.
However, for enums, all the members of enums can be listed using `Weather.values`. Let's print all the members of `Weather` enumerated type.

```
void mainIterating() {
  //#2. enums can iterate on all types at once.
  //No need to create a list of const
  Weather.values.forEach((w) => print(w));
}
```

**Output:**

```
Weather.SUNNY
Weather.CLOUDY
Weather.RAINY
```

---


# Enums extension

Enumerated types are supported by extensions. Check out my previous article on Dart Extensions [here](https://ptyagicodecamp.github.io/dart-extensions.html#dart-extensions). Let's add an extension method `console()` to print index of enum and a custom message `about` along with it.

```
extension WeatherExt on Weather {
  //custom message for each weather type
  static const weatherMap = {
    Weather.SUNNY: "What a lovely weather",
    Weather.CLOUDY: "Scattered showers predicted",
    Weather.RAINY: "Will be raining today",
  };

  //prints enum index and custom message
  void console() {
    print("${this.index} ${this.about}");
  }

  //about property returns the custom message
  String get about => weatherMap[this];
}
```

Next, iterate over all the members, and use extension method `console()` to print the custom message for each weather type.

```
void mainExtension() {
  //#3. Enum extensions. Using extension method console
  Weather.values.forEach((w) => w.console());
}
```

**Output:**

```
0 What a lovely weather
1 Scattered showers predicted
2 Will be raining today
```

---

# Companion Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/enums.dart)

---

# References

1. [Enumerated Types](https://dart.dev/guides/language/language-tour#enumerated-types)
2. [Dart Extensions](https://ptyagicodecamp.github.io/dart-extensions.html#dart-extensions)


Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
