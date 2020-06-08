Title: Dart Generators
Date: 06/07/2020
Authors: ptyagi
Category: Dart
Tags: generators, dart, cross-platform, flutter, code-recipes, development
Summary: This article explains Dart Generator functions.


![enums]({attach}../../images/dart/todo.png)

# Introduction

Dart generator functions are used to generate sequence of values on-demand and lazily. Such value sequence can be generated either synchronously or asynchronously.

There are two types of generator functions to support both ways:

* Synchronous Generator: Synchronous generator function returns an [Iterable]() object. That means first the values are generated and then returned lazily on-demand by the function.
* Asynchronous Generator: Asynchronous generator function returns a [Stream]() object. The sequence values are generated on demand as they become available.


Let's use an example to generate numbers starting from a given number say 5, until 0. We'll observe both ways (asynchronous and synchronous generators) to create this number sequence.

# Using `sync*` - Synchronous Generator

The synchronous generator function is marked with `sync*`. The values are returned using `yield` keyword.

```
void main1() {
  print("Getting CountDown Iterable [sync* + yield]");
  Iterable<int> sequence = countDownFromSync(5);

  print("Starting...");

  for (int value in sequence) {
    print(value);
  }
  print("DONE");
}

//sync*
Iterable<int> countDownFromSync(int num) sync* {
  while (num > 0) {
    yield num--;
  }
}
```

**Output:**

```
Getting CountDown Iterable [sync* + yield]
Starting...
5
4
3
2
1
DONE
```

# Using `async*` - Asynchronous Generator

The asynchronous generator function is marked with `async*`. The values are returned using `yield` keyword.

```
void main2() {
  print("Getting CountDown Stream [async* + yield]");
  Stream<int> sequence = countDownFromAsync(5);

  print("Starting...");

  sequence.listen((int value) {
    print(value);
  });
  print("DONE");
}

//async*
Stream<int> countDownFromAsync(int num) async* {
  while (num > 0) {
    yield num--;
  }
}
```

**Output:**

```
Getting CountDown Stream [async* + yield]
Starting...
DONE
5
4
3
2
1
```

# Using `sync* + yield*` - Recursive Synchronous Generator

When generator functions are used recursively, `yield*` is used to mark such recursive function calls.

```
void main3() {
  print("Getting CountDown Iterable [sync* + yield*]");
  Iterable<int> sequence = countDownFromSyncRecursive(5);

  print("Starting...");

  for (int value in sequence) {
    print(value);
  }
  print("DONE");
}

//sync* + yield* for recursive functions
Iterable<int> countDownFromSyncRecursive(int num) sync* {
  if (num > 0) {
    yield num;

    yield* countDownFromSyncRecursive(num - 1);
  }
}
```

**Output:**

```
Getting CountDown Iterable [sync* + yield*]
Starting...
5
4
3
2
1
DONE
```

# Using `async* + yield*` - Recursive Asynchronous Generator


```
void main4() {
  print("Getting CountDown Stream [async* + yield*]");
  Stream<int> sequence = countDownFromAsyncRecursive(5);

  print("Starting...");

  sequence.listen((int value) {
    print(value);
  });
  print("DONE");
}

//async* + yield* for recursive functions
Stream<int> countDownFromAsyncRecursive(int num) async* {
  if (num > 0) {
    yield num;

    yield* countDownFromAsyncRecursive(num - 1);
  }
}
```
**Output:**

```
Getting CountDown Stream [async* + yield*]
Starting...
DONE
5
4
3
2
1
```

---

# Summary

In this article, we saw how to use Dart's generator function to produce a on-demand sequence of values synchronously and asynchronously in iterative and recursive manner.

That's it for this article. Check out the [Dart Vocabulary Series](https://ptyagicodecamp.github.io/a-dartflutter-vocabulary-series.html) for other Dart stuff.

---


# Check out YouTube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/generators.dart)

---

# References

1. [Dart language tour](https://dart.dev/guides/language/language-tour#generators)
2. [Beyond Async](http://dartdoc.takyam.com/articles/beyond-async/)


Happy Darting :)

_Liked the article?
Couldn't find a topic of interest? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share!

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
