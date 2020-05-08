Title: Dart Libraries (Part2)
Date: 05/08/2020
Authors: ptyagi
Category: Dart
Tags: export, import, part, libraries, dart, cross-platform, flutter, code-recipes, development
Summary: This article is a quick introduction for using libraries in Dart/Flutter.


![enums]({attach}../../images/dart/libraries.png)

# Introduction

This article is a quick introduction for using libraries in Dart/Flutter. It covers how to use Dart libraries. Checkout the Part-1, to learn about `part`, `library`, and `export` directives.


# Using Prefix for library

Let's create two libraries `lib1` and `lib2` for demonstration.

# `lib1`

```
  int addition(int a, int b) => _add(a, b);

  int subtraction(int a, int b) => a - b;

  int _add(int a, int b) => a + b;

```

# `lib2`

```
  bool isNumberOdd(int num) => num.isOdd;

  bool isNumberEven(int num) => num.isEven;

```

Let's use `lib1.dart` to find addition of two numbers 5 and 2, and use `lib2.dart` to check if number 5 is even or odd. For `lib2.dart`, a prefix `check` is used. All `lib2`'s API's can be accessed using `check` alias.

The `lib_prefix.dart`:

```
iimport 'lib1.dart';
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


# Importing specific APIs

Dart libraries allow to import only specific apis using `show` and `hide` keywords.

The `show` is used when a specific API needs to be made visible/accessible.

For example, in `lib1.dart`, I want to access only `subtraction(...)` API.

The `lib_show.dart`:

```
import 'lib1.dart' show subtraction;

void main() {
  int num1 = 5;
  int num2 = 2;

  //Compile-time error because addition is no longer visible
  //int sum = addition(num1, num2);

  int differnce = subtraction(num1, num2);
  print("Differnce of $num1 and $num2 is $differnce");
}

```

The `hide` is used when everything but a specific API is made accessible.

The `lib_hide.dart`:

```
import 'lib1.dart' hide subtraction;

void main() {
  int num1 = 5;
  int num2 = 2;

  int sum = addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");

  //Compile-time error because subtraction() API is hidden
  //int differnce = subtraction(num1, num2);
  //print("Differnce of $num1 and $num2 is $differnce");
}
```

# Deferred-Loading

A deferred library is loaded when it's actually used/needed. It's declared deferred in import statement using `deferred as <name>`. The library use `loadLibrary()` method to invoke itself. The `loadLibrary()` method returns a `Future`. library invocation needs to be done in a `async` block.

The `lib_deferred.dart`:

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

In this article, we saw learned few ways to use Dart libraries.

That's it for this article. Check out the [Dart Vocabulary Series](https://ptyagicodecamp.github.io/a-dartflutter-vocabulary-series.html) for other Dart stuff.

---


# Check out YouTube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/libraries)

---

# References

1.


Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
