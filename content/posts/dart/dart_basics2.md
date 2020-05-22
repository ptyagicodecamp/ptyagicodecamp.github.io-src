Title: Streams: Asynchronous Programming with Dart
Date: 05/20/2020
Authors: ptyagi
Category: Dart
Tags: Dart, Flutter
Summary: This article is the second part of introduction to asynchronous programming with Dart, and covers Streams in Dart.

![streams]({attach}../../images/dart/streams.jpg)

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

---

# Creating Stream

In this section, we'll learn to generate a stream of events consists of numbers using two different ways.

## Using Generator Function

One way to create stream by using [generator function](https://dart.dev/guides/language/language-tour#generators). It helps to produce lazily a sequence of values. In this example, we'll create stream using [`for`](https://dart.dev/guides/language/language-tour#for-loops) loop and `yield` keyword. The `yield` keywords is helpful in delivering values. The `async*` is an asynchronous [generator](https://dart.dev/guides/language/language-tour#generators) that returns a Stream object.

**Example#1:**
```
//Example#1. Creating Stream (of numbers) using asynchronous Generators
//Using yield, async*

//This will return a reference to the stream
Stream<int> createNumberStream(int last) async* {
  for (int i = 1; i <= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

//Printing numbers/events of Stream (Listening to Stream)
printStream(Stream stream) {
  stream.listen((s) => print(s));
}

void createStreamUsingGenerators() async {
  //Using `yield`, async* keywords
  var stream = createNumberStream(5);
  printStream(stream);
}
//----END----//

//Entry point function
void main() {
  //Run Example#1.
  createStreamUsingGenerators();
}
```

**Output:**

```
1
2
3
4
5
```

**Source Code** is available [here- Example#1](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).

---

2. Using `Stream.fromIterable()`

In this approach, [`Stream.fromIterable()`](https://api.flutter.dev/flutter/dart-async/Stream/Stream.fromIterable.html) takes an array of numbers as argument, and create a `Stream` of numbers delivering one event/number at a time.

**Example#2:**
```
//Example#2. Creating Stream of numbers using  `Stream.fromIterable()` method

void createStreamFromIterable() {
  var numbers = [1, 2, 3, 4, 5];
  Stream stream = Stream.fromIterable(numbers);
  printStream(stream);
}

//Printing numbers/events of Stream (Listening to Stream)
printStream(Stream stream) {
  stream.listen((s) => print(s));
}
//----END----//

//Entry point function
void main() {
  //Run Example#2.
  createStreamFromIterable();
}
```

**Output:**

```
1
2
3
4
5
```

**Source Code** is available [here- Example#2](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).

---

# Retrieving Events From Stream

We'll see two ways to print the events/numbers for the stream(s) created above.

## Using `listen`

In the above two examples, we printed events of a `Stream` using [`listen`](https://api.dart.dev/stable/1.24.3/dart-async/Stream/listen.html) by adding subscription to the given stream. Let's print messages before starting and after stream is finshed.

**Example#3.**

```
//Example#3. Accessing Stream using `listen`

void printStreamEventsUsingListen() {
  Stream stream = Stream.fromIterable([1, 2, 3, 4, 5]);
  print("Stream Starting");
  stream.listen(
    (s) => print(s),
  );
  print("Stream Finished");
}
//----END----//

//Entry point function
void main() {
  //Run Example#3.
  printStreamEventsUsingListen();
}
```

**Output:**

```
Stream Starting
Stream Finished
1
2
3
4
5
```

**Source Code** is available [here- Example#3](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).


## Using `await for`

Streams are iterated in a `await for` asynchronous for-loop. Streams are notified when there's last event arrives and `await for-loop` stops.
Let's see an example that takes the events from the stream generated above and print those numbers in events.

**Example#4.**

```
//Example#4. Accessing Stream using `await for`

void printStreamEventsUsingAwaitFor() async {
  Stream stream = Stream.fromIterable([1, 2, 3, 4, 5]);

  print("Stream Starting");
  await for (var num in stream) {
    print(num);
  }
  print("Stream Finished");
}
//----END----//

//Entry point function
void main() {
  //Run Example#4.
  printStreamEventsUsingAwaitFor();
}
```

**Output:**

```
Stream Starting
1
2
3
4
5
Stream Finished
```

**Source Code** is available [here- Example#4](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).

The difference between `listen` and `await for` is that in `listen` approach, code related with setting up stream executed first, and then events are printed. In the `await for` approach, events are printed as they come. This approach is works better when there are finite number of events in a stream, and stream does finish.

---

# Processing Stream Events

In this example, let add the numbers delivered by stream and return the total. Let's call this new function `addEvents(...)`. Events from Stream is accessed using `await for`, and added one by one. The `addEvents(...)` function needs to be marked with `async` because it uses `await` inside the function. This method returns `Future<int>`. This future is accessed from `addNumbersInStream()` function using `await` and prints the total on console.

**Example#5.**

```
//Example#5. Processing (Adding) Stream using `await for`

void addNumbersInStream() async {
  //Create a Stream consists of numbers
  Stream stream = Stream<int>.fromIterable([1, 2, 3, 4, 5]);

  var total = await addEvents(stream);
  print(total);
}

//Receiving events from Stream, adding and returning total
Future<int> addEvents(Stream<int> stream) async {
  var total = 0;
  await for (var num in stream) {
    total += num;
  }

  return total;
}
//----END----//

//Entry point function
void main() {
  //Run Example#5.
  addNumbersInStream();
}
```

**Output:**

```
15
```

**Source Code** is available [here- Example#5](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).

---

# Handling Errors in Streams

When error(s) occurred, a Stream can notify it as error event just like data event. Stream can notify error in one of these three ways:

* Stream notifies first error event and stops. We'll see few examples of this case in this article.
* Stream notifies multiple errors events.
* Stream notifies error event(s) and continue delivering events.

## Error Handling in `await for` block

An error event can be responded in `try/catch` block. Let's see one of the above case to handle one error event by putting `await for` loop in previous example inside `try/catch` block. To be able to see `catch` block respond to error event, we need to tweak `createStream` to throw `Exception` at some point. Assume error event occurs when accessing 5th number.

**Example#6.**

```
///Handling Exceptions (Code shared for listen and await for implementations)

//Generated Stream with numbers. Added exception on purpose for demonstration
Stream<int> createNumberStreamWithException(int last) async* {
  for (int i = 1; i <= last; i++) {
    if (i == 5) {
      throw new Exception("Demo exception when accessing 5th number");
    }
    yield i; //to be able to send spaced out events
  }
}

//Example #6. Handle Error in Stream using `await for`
void handlingExceptionUsingAwaitFor() async {
  var stream = createNumberStreamWithException(5);
  try {
    await for (var num in stream) {
      print(num);
    }
  } catch (e) {
    print(e);
  }
  print("Finished");
}
//----END----//

//Entry point function
void main() {
  //Run Example#6.
  handlingExceptionUsingAwaitFor();
}
```

**Output:**

```
1
2
3
4
Exception: Demo exception when accessing 5th number
Finished
```

**Source Code** is available [here- Example#6](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).

---

# Handling Errors using `listen()` method

This is the better way to handle errors when you want to handle multiple errors without exiting code at the encounter of first error.

**Example#7.**

```
///Handling Exceptions (Code shared for listen and await for implementations)

//Generated Stream with numbers. Added exception on purpose for demonstration
Stream<int> createNumberStreamWithException(int last) async* {
  for (int i = 1; i <= last; i++) {
    if (i == 5) {
      throw new Exception("Demo exception when accessing 5th number");
    }
    yield i; //to be able to send spaced out events
  }
}

//Example #7. Handle Error in Stream using `listen`
void handlingExceptionUsingListen() async {
  var stream = createNumberStreamWithException(5);
  stream.listen(
    (num) => print(num),
    onError: (e) => print(e),
    onDone: () => print("Finished"),
  );
}
//----END----//

//Entry point function
void main() {
  //Run Example#7.
  handlingExceptionUsingListen();
}
```

**Output:**

```
1
2
3
4
Exception: Demo exception when accessing 5th number
Finished
```

**Source Code** is available [here- Example#7](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams.dart).

---

#Summary

In this article, we learned about the Dart Streams. Streams are useful when we want to process events as they become available rather waiting for everything to return in one batch like Futures. In next article, we'll learn about the type of streams available in Dart.

---

# References

1. [Dart Futures](https://dart.dev/tutorials/language/futures)
2. [Dart Streams](https://dart.dev/tutorials/language/streams)
3. [Official Flutter Channel](https://www.youtube.com/watch?v=vl_AaCgudcY&list=PLjxrf2q8roU2HdJQDjJzOeO6J3FoFLWr2&index=14)


Happy cooking with Dart and Flutter :)


_Liked the article?
Couldn't find a topic of your interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
