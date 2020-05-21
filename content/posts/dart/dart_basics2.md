Title: Streams: Asynchronous Programming with Dart
Date: 05/20/2020
Authors: ptyagi
Category: Dart
Tags: Dart, Flutter
Summary: This article is the second part of introduction to asynchronous programming with Dart, and covers Streams in Dart.


***Target Audience:*** Beginner

# Introduction

This article is a part of three part series focused on asynchronous Programming with Dart. This article covers Streams in Dart to execute program asynchronously.

* [Part-1](https://ptyagicodecamp.github.io/futures-asynchronous-programming-with-dart.html) Futures: Asynchronous Programming with Dart
* **Part-2 (Current)** Streams: Asynchronous Programming with Dart
* [Part-3](https://ptyagicodecamp.github.io/types-of-streams-asynchronous-programming-with-dart.html) Types of Streams: Asynchronous Programming with Dart


---

# Streams

A Stream is a sequence of asynchronous events. Streams are useful in providing an asynchronous sequence of data.

# Key Terms

**Stream:** A Stream is a sequence of asynchronous events. It lets you know whenever next event is ready rather you asking for it.  

**Data Sequence:** A Data sequence is made up of either user-generated event or data read from files.

**async:** Functions with `await` keyword needs to be marked as `async` keyword. Functions marked with `async` keywords doesn't suspend immediately, but execute synchronously until first `await` or `return` is called.

# Creating Stream

Let's see how to generate a stream of events consists of numbers in code below:

* Using ***for-loop*** and `yield` keyword

* Using `fromIterable()` method

```
import 'dart:async';

//this will return a reference to the stream
Stream<int> createNumberStream(int last) async* {
  for (int i=0; i< last; i++) {
    yield i; //to be able to send spaced out events
  }
}

printStream(Stream stream) {
  stream.listen((s) => print(s));
}
main() async {
  //Using `yield` keyword
  var stream = createNumberStream(5);
  printStream(stream);

  //Using fromIterable method
  var numbers = [1,2,3,4,5];
  stream = new Stream.fromIterable(numbers);
  printStream(stream);
}
```

---

# Retrieving events from stream

Streams are iterated in a `await for` asynchronous for-loop. Streams are notified when there's last event arrives and `await for-loop` stops.
Let's see an example that takes the events from the stream generated above and print those numbers in events.
```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=0; i< last; i++) {
    yield i; //to be able to send spaced out events
  }
}

//Receiving events from Stream
Future<int> printStream(Stream<int> stream) async {
  await for (var num in stream) {
    print(num);
  }
}
main() async {
  var stream = createNumberStream(5);
  printStream(stream);
}
```

Now, lets modify `printStream(..)` from printing numbers to let it add numbers and return the sum of number in events. Let's call this new function `addEvents(...)`

```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

//Receiving events from Stream
Future<int> addEvents(Stream<int> stream) async {
  var total = 0;
  await for (var num in stream) {
    total += num;
  }

  return total;
}
main() async {
  var stream = createNumberStream(5);
  var total = await addEvents(stream);
  print(total);
}
```

---

# Responding to errors using Streams

When error(s) occurred, a Stream can notifies it as error event just like data event. Stream can notify error in one of these three ways:

* Stream notifies first error event and stops.
* Stream notifies multiple errors events.
* Stream notifies error event(s) and continue delivering events.

An error event can be responded in `try/catch` block.
Let's see one of the above case to handle one error event by putting `await for` loop in previous example inside `try/catch` block. To be able to see `catch` block respond to error event, we need to tweak `createStream` to throw `Exception` at some point. Assume error event occurs when accessing 5th number.

```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    if (i==5) {
      throw new Exception(
        "Demo exception when accessing 5th number");
    }
    yield i; //to be able to send spaced out events
  }
}

//Receiving events from Stream
Future<int> addEvents(Stream<int> stream) async {
  var total = 0;
  try {
    await for (var num in stream) {
      total += num;
    }
  } catch (e) {
    return -1;
  }

  return total;
}
main() async {
  var stream = createNumberStream(5);
  var total = await addEvents(stream);
  print(total);
}
```

---

# Handling errors using `listen()` method

This is the better way to handle errors when you want to handle multiple errors without exiting code at the encounter of first error.

```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    if (i==5) {
      throw new Exception(
        "Demo exception when accessing 5th number");
    }
    yield i; //to be able to send spaced out events
  }
}

//Receiving events from Stream
Future<int> addEvents(Stream<int> stream) async {
  var total = 0;
  try {
    await for (var num in stream) {
      total += num;
    }
  } catch (e) {
    return -1;
  }

  return total;
}
main() async {
  var stream = createNumberStream(5);

  stream.listen(
  (x) => print("number: $x"),
    onError : (err) => print("error: $err"),
    onDone: () => print("finished")
  );
}
```

---


# References

1. [Dart Futures](https://dart.dev/tutorials/language/futures)
2. [Dart Streams](https://dart.dev/tutorials/language/streams)

Happy cooking with Dart and Flutter :)


_Liked the article?
Couldn't find a topic of your interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
