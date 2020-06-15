Title: Dart's Callable Classes
Date: 06/14/2020
Authors: ptyagi
Category: Dart
Tags: callable-classes, dart, cross-platform, flutter, code-recipes, development
Summary: This article introduce the Callable Class feature of Dart language.

![enums]({attach}../../images/dart/callable.jpg)

# Introduction

In Dart, functions are objects too. It's an object of type [`Function`](https://api.dart.dev/stable/2.8.4/dart-core/Function-class.html). Similar to other objects, functions can be passed as arguments to other functions, and can be assigned to variables as well.

A Callable class allows its instance to be called as function. This feature of Dart language is useful in making named-functions.

---

# Check out YouTube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/Xx3AySX1R0U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Implementing Callable Class

All Dart functions have `call` method. In order to make a class ***Callable***, the `call()` method needs to be implemented. Let's declare a callable class below:

```
class Addition {
  int call(int a, int b) => a + b;
}
```

The above class' `call` method takes two arguments and returns their sum.

---

# Using Callable Class

Let's check out using the `Addition` callable class in code below. The `addition` object is of `Addition` type. Now, `addition(1, 2)` can be called to calculate the sum of given numbers.

```
void main() {
  Addition addition = Addition();
  var result = addition(1, 2);
  print(result);
}
```

**Output:**

```
3
```
---


# Summary

In this article, we learned that Dart is a true object-oriented language. Dart's functions are also objects. We learned to implement a callable class.

That's it for this article. Check out the [Dart Vocabulary Series](https://ptyagicodecamp.github.io/a-dartflutter-vocabulary-series.html) for other Dart stuff.

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/callable_class.dart)

---

# References

1. [Function type](https://api.dart.dev/stable/2.8.4/dart-core/Function-class.html)
2. [Language Tour](https://dart.dev/guides/language/language-tour#callable-classes)


Happy Darting :)

_Liked the article?
Couldn't find a topic of interest? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share!

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
