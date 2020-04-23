Title: Dart Static keyword
Date: 04/22/2020
Authors: ptyagi
Category: Dart
Tags: static, class-variables, class-methods, dart, cross-platform, flutter, code-recipes, development
Summary: This article demonstrates using `static` keyword in Dart.


![enums]({attach}../../images/dart/static.png)

# Introduction

In Dart language, the `static` keyword is used to declare class level variables and methods. A class level variable is useful to declare constants and implement the class-wide state.

The class methods can be called from other classes using class name they are defined in.

Usually, utility classes use static variables and methods to provide easy and quick access to methods and constants.

---

# Using `static` keyword

Let's take an example of a string utility class, say `StringUtils`. This class contains a convenience method, say `reverse(String str)`, to reverse the given string . This utility class has a constant `dart` which is inferred to contain a String value of "oh dart".

```
class StringUtils {
  static const dart = "oh dart";

  static String reverse(String str) {
    return String.fromCharCodes(str.runes.toList().reversed);
  }
}
```

**Note:** In case you're interested in learning about `runes` used in code above to reverse the string, then check out [my article](https://ptyagicodecamp.github.io/the-runes-property.html) on Runes.


## Running Code

The class level variable can be accessed using class name. In code below, `StringUtils` is needed to access either constant `dart` or static method `reverse(...)`.

```
void main() {
  String reversedStatic = StringUtils.reverse(StringUtils.dart);
  print(reversedStatic);
}
```

**Output:**

```
trad ho
```
---

# Few Facts about Static Variables

* Static variables are not initialized until they're used.
* Useful for representing class state and constants.
* Constants names are declared using [lowerCamelCase](https://dart.dev/guides/language/effective-dart/style#identifiers) convention.

---

# Few Facts about Static Methods

* Static / Class methods don't have access to `this` keyword.
* Static methods can be used as compile-time constants, and can be passed as parameters to constant constructor. Let's create a class `SomeObj` with a `const` constructor:

```
class SomeObj {
  final String myStr;

  const SomeObj(this.myStr);
}
```

## Running Code

Now the static method `reverse(...)` is passed as parameter to `const SomeObj(...)` constructor.

```
void main() {
  SomeObj obj = SomeObj(StringUtils.reverse(StringUtils.dart));
  print(obj.myStr);
}
```

**Output:**

```
trad ho
```

---

# Tip

Dart supports top-level variables, constants, and methods.
Usually utility methods are put together in a class of static methods.

In Dart, if such utility methods are not logically related, then they shouldn't be put inside a class. Such Methods can be put at top-level in a dart file.

The above static utility variable / methods can be moved to top-level. You don't need a class for namespace purposes. It's recommended to create a library instead for grouping methods according to namespaces.

```
//Utility method at top-level
const dart = "oh dart";

String reverse(String str) {
  return String.fromCharCodes(str.runes.toList().reversed);
}
```

## Running Code

```
void main() {
  //Moving utility method/variable to top-level
  String reversedStr = reverse(dart);
  print(reversedStr);
}
```

**Output:**

```
trad ho
```

**Note:** Avoid classes with only static members in it as per [this lint rule](https://dart-lang.github.io/linter/lints/avoid_classes_with_only_static_members.html).

---

# Summary

In this article, you learned how to use `static` keyword in Dart language. You learned facts about class variables and methods, and alternate implementaion for utitility classes without using `static` keywords.

Check out the [Dart Vocabulary Series](https://ptyagicodecamp.github.io/a-dartflutter-vocabulary-series.html) for other Dart stuff.

---


# Check out YouTube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/static.dart)

---

# References

1. [DartPad: Online Dart Editor](https://dartpad.dev/)
2. [Language Tour](https://dart.dev/guides/language/language-tour#class-variables-and-methods)


Happy Darting :)

_Liked the article?
Couldn't find a topic of your interest? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share!

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
