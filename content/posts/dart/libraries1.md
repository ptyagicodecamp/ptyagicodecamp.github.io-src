Title: Dart Libraries (Part1)
Date: 05/08/2020
Authors: ptyagi
Category: Dart
Tags: export, import, part, libraries, dart, cross-platform, flutter, code-recipes, development
Summary: This article is the Part-1 of introduction to using libraries in Dart/Flutter.

![Libraries-part1]({attach}../../images/dart/libraries.png)

# Introduction

This article is an introduction to using libraries in Dart/Flutter. A library is a reusable module for frequently used programs/code. It helps to write modular code base. In Dart, each app is a library. This article is divided into two parts.

**Part-1:** This part covers how to use Dart libraries including following:

* Using Prefix for library
* Importing specific APIs
* Defer/delay loading library

**Part-2:** The second part covers understanding following directives:

* The `part` directive
* The `library` directive
* The `export` directive

---

# Setup

Let's create two libraries `lib1` and `lib2` for demonstration.

# `lib1`

This library has APIs to calculate sum and difference of two integers.

* Addition API: The `int addition(int a, int b)` calculates sum of two given integers and returns an integer.

* Subtraction API: The `int subtraction(int a, int b)` calculates difference of two given integers and returns an integer.

* `int _add(int a, int b)`: It is an internal function/method that does perform the real addition. This method is used by addition api. Identifiers with underscore (\_) prefix are only available inside library.

**SourceCode:** Please refer to [`lib1.dart`](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries/lib1.dart)

```
  int addition(int a, int b) => _add(a, b);

  int subtraction(int a, int b) => a - b;

  int _add(int a, int b) => a + b;

```

# `lib2`

This library has APIs to check if the given number is even or odd.

* Even number API (`bool isNumberOdd(int num)`): This api take a number and returns true if its even or vice versa.
* Odd number API (`bool isNumberOdd(int num)`): This api take a number and returns true if its odd or vice versa.

**SourceCode:** Please refer to [`lib2.dart`](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries/lib2.dart)

```
  bool isNumberOdd(int num) => num.isOdd;

  bool isNumberEven(int num) => num.isEven;

```

---

# Using Prefix for library

Let's use `lib1.dart` to calculate addition of two numbers 5 and 2, and use `lib2.dart` to check if number 5 is even or odd. For `lib2.dart`, a prefix `check` is used. This is used to access `lib2`'s APIs thereafter. All `lib2`'s API's can be accessed using `check` alias.

The `lib_prefix.dart`:

**SourceCode:** Please refer to [`lib_prefix.dart`](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries/lib_prefix.dart)

```
import 'lib1.dart';
import 'lib2.dart' as check; //Using prefix for lib2

void main() {
  int num1 = 5;
  int num2 = 2;

  int sum = addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");

  //Using check to access the API
  print("is number even? ${check.isNumberEven(num2)}");
}
```

**Output:**

```
Sum of 5 and 2 is 7
is number even? true
```

---

# Importing specific APIs

Dart libraries allow to import only specific apis using `show` and `hide` keywords.

**`show`:**

The `show` is used when a specific API needs to be made visible/accessible. For example, in `lib1.dart`, I want to access only `subtraction(...)` API.

The `lib_show.dart`:

**SourceCode:** Please refer to [`lib_show.dart`](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries/lib_show.dart)

```
import 'lib1.dart' show subtraction;

void main() {
  int num1 = 5;
  int num2 = 2;

  //Compile-time error because addition is no longer visible
  //int sum = addition(num1, num2);

  int difference = subtraction(num1, num2);
  print("Difference of $num1 and $num2 is $difference");
}

```

**Output:**

```
Difference of 5 and 2 is 3
```

**`hide`:**

The `hide` is used when everything but a specific API is made accessible/visible.

The `lib_hide.dart`:
**SourceCode:** Please refer to [`lib_hide.dart`](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries/lib_hide.dart)

```
import 'lib1.dart' hide subtraction;

void main() {
  int num1 = 5;
  int num2 = 2;

  int sum = addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");

  //Compile-time error because subtraction() API is hidden
  //int difference = subtraction(num1, num2);
  //print("Difference of $num1 and $num2 is $difference");
}
```

**Output:**

```
Sum of 5 and 2 is 7
```

---

# Defer/delay loading library

A deferred library is loaded when it's actually used/needed. It's declared using `deferred as <name>` in import statement. The library uses `loadLibrary()` method to invoke itself. The `loadLibrary()` method returns a `Future`. That's why library invocation needs to be done in a `async` block.

The `lib_deferred.dart`:
**SourceCode:** Please refer to [`lib_deferred.dart`](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries/lib_deferred.dart)

```
import 'lib1.dart' deferred as lib1;

void main() {
  int num1 = 5;
  int num2 = 2;

  delayedInvocation(num1, num2);
}

Future delayedInvocation(int num1, int num2) async {
  //Loads lib1 here
  int sum = await lib1.addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");
}
```

**Output:**

```
Sum of 5 and 2 is 7
```

---

# Summary

In this article, we saw few ways to use Dart libraries. We learned how to use prefix to refer to libraries in import statements, importing only specific libraries, and delaying loading libraries until they are needed.

That's it for this article. Check out the [Dart Vocabulary Series](https://ptyagicodecamp.github.io/a-dartflutter-vocabulary-series.html) for other Dart stuff.

---


# Check out YouTube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries)

---

# References

* [Official Dart Language Tour](https://dart.dev/guides/language/language-tour)


Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
