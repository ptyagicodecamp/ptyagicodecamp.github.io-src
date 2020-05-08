Title: Dart Libraries
Date: 05/07/2020
Authors: ptyagi
Category: Dart
Tags: export, libraries, dart, cross-platform, flutter, code-recipes, development
Summary: This article is a quick introduction for using libraries in Dart/Flutter.


![enums]({attach}../../images/dart/libraries.png)

# Introduction

A library is a reusable module of frequently used programs/code. It helps to write modular code base. In Dart, each app is a library.  

Purpose of a library is twofold:

1. Providing APIs
2. Restricting variable's visibility. Identifiers with underscore (\_) prefix are only available inside library.

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

# Privacy

Let's import `lib1.dart` to use `addition(..)` method. Please note trying to `_add(...)` method will show a compile time error since it's private and available for use inside `lib1.dart` only

```
import 'lib1.dart';

void main() {
  int num1 = 5;
  int num2 = 2;

  int sum = addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");
}
```

**Output:**

```
Sum of 5 and 2 is 7
```

However, calling an api form `lib2.dart` will give compile-time error.

```
import 'lib1.dart';

void main() {
  int num1 = 5;
  int num2 = 2;

  //Compile-time error because api is not available
  print("is number even? ${isNumberEven(num2)}");
}

```

# Using `part` directive

The use of `part` directive is most common in auto-generated code. Traditionally, `part` directive is a glue between two tightly coupled libraries.

**Note:** Related code is available in its own folder `libraries/maths_part`.

For example, assume `lib1.dart` and `lib2.dart` are two huge libraries that were spilt into two. In normal circumstances, I would add both libraries in `import` statements at the top of `maths_part/part_main.dart` in order to access APIs from both libraries. In such scenarios, `part` directive could come handy.

The `lib1.dart` file:

```
//importing lib1 brings-in all apis from lib2 as well
part 'lib2.dart';

int addition(int a, int b) => _add(a, b);

int subtraction(int a, int b) => a - b;

int _add(int a, int b) => a + b;

```

The `lib2.dart` file:

```
part of 'lib1.dart';

bool isNumberOdd(int num) => num.isOdd;

bool isNumberEven(int num) => num.isEven;

```

The `part_main.dart` file:

```
import 'lib1.dart';

void main() {
  int num1 = 5;
  int num2 = 2;

  int sum = addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");

  print("is number even? ${isNumberEven(num2)}");
}
```

**Output:**

```
Sum of 5 and 2 is 7
is number even? true
```

# `library` directive

The `library` directive is used to [auto-generate documentation(https://dart.dev/guides/libraries/create-library-packages#documenting-a-library) for library using [`dartdoc`](https://github.com/dart-lang/dartdoc#dartdoc) tool.

# Generating documentation

1. Add `library` directive at the top of `lib1.dart`:

```
library math_lib1;
```

2. Create a directory `math_lib1`, and move `lib1.dart` under it.  

3. Add `pubspec.yaml` under `math_lib1` directory:

```
name: math_lib1
description: Math operations library
version: 0.0.1
```

4. Use `dartdoc` tool to create documentation:

```
  $ cd math_lib1

  # Generates documentation
  $ dartdoc

  # Documentation available at `http://localhost:8080/`
  $ dhttpd --path doc/api
```



# Using `export` directive

This directive is used to export only public apis.

**Note:** Related code is available in its own folder `libraries/maths_export`.

The `lib1.dart` and `lib2.dart` files are available under `lib/src/` folder. The files under `lib/src/` directory are hidden. The `lib/maths_export.dart` file use `export` directive to make `lib1.dart` public.

The `lib/maths_export.dart`:

```
export 'src/lib1.dart';
```

An external file `lib_export.dart` imports `maths_export.dart` like below:

```
import 'math_export/lib/maths_export.dart';

void main() {
  int num1 = 5;
  int num2 = 2;

  int sum = addition(num1, num2);
  print("Sum of $num1 and $num2 is $sum");

  //Compile-time error because lib2.dart is not exported
  //print("is number even? ${isNumberEven(num2)}");
}

```

**Output:**

```
Sum of 5 and 2 is 7
```

---

# Summary

In this article, we saw how

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
