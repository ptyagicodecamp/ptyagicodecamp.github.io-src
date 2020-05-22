Title: Types of Streams: Asynchronous Programming with Dart
Date: 05/21/2020
Authors: ptyagi
Category: Dart
Tags: Dart, Flutter
Summary: This article is the third and last part of introduction to asynchronous programming with Dart, and covers types of Streams in Dart.

***Target Audience:*** Beginner

#Introduction

This article is a part of three part series focused on asynchronous Programming with Dart. This article covers types of Streams in Dart to execute program asynchronously.

* [Part-1](https://ptyagicodecamp.github.io/futures-asynchronous-programming-with-dart.html) Futures: Asynchronous Programming with Dart
* [Part-2](https://ptyagicodecamp.github.io/streams-asynchronous-programming-with-dart.html) Streams: Asynchronous Programming with Dart
* **Part-3 (Current)** Types of Streams: Asynchronous Programming with Dart

---

# Types of Streams

1. **Single subscription**

Single subscription streams are meant to deliver events in order. This type of stream is used when order of events received matters like reading a file. Such type of Streams can be listened only once. Attempting to listening them again will throw an exception.

2. **Broadcast (Multiple subscribers)**

Broadcast streams are intended to deliver events to their subscribers. Any subscriber can start listening to events as soon as they subscribe to it. A Broadcast stream can be listened multiple times.

**Note:** A Single Subscription stream can be converted into broadcast streams by using `asBroadcastStream()` method.

---

# Subscribing To Stream

In this section, we'll see two ways to subscribe to a stream:

1. Using `listen()` method

2. Using Subscription's Handler


## Using `listen()`

**Example#1.**

```
//This will generate a stream and return reference to it.
Stream<int> createNumberStreamWithException(int last) async* {
  for (int i = 1; i <= last; i++) {
    if (i == 5) {
      throw new Exception("Demo exception when accessing 5th number");
    }
    yield i; //to be able to send spaced out events
  }
}

//Example#1. Subscribing to Stream using `listen()` method
void subscribeUsingListen() {
  Stream stream = createNumberStreamWithException(5);

  stream.listen(
    (x) => print("number: $x"),
    onError: (err) => print("error: $err"),
    onDone: () => print("Done"),
  );
}
//----END----//

//Entry point function
void main() {
  //Run Example#1.
  subscribeUsingListen();
}

```

**Output:**

```
number: 1
number: 2
number: 3
number: 4
error: Exception: Demo exception when accessing 5th number
Done
```

**Source Code** is available [here- Example#1](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

## Using Subscription's Handler

A Stream subscription handler can be get using passing `null` in the `listen()` like this `stream.listen(null)`.

**Example#2.**

```
//This will generate a stream and return reference to it.
Stream<int> createNumberStreamWithException(int last) async* {
  for (int i = 1; i <= last; i++) {
    if (i == 5) {
      throw new Exception("Demo exception when accessing 5th number");
    }
    yield i; //to be able to send spaced out events
  }
}

//Example#2. Subscribing to Stream using subscription handler
void subscribeUsingSubscriptionHandler() {
  Stream stream = createNumberStreamWithException(5);

  var subscription = stream.listen(null);
  subscription.onData((x) => print("number $x"));
  subscription.onError((err) => print("error: $err"));
  subscription.onDone(() => print("Done"));
}
//----END----//

//Entry point function
void main() {
  //Run Example#2.
  subscribeUsingSubscriptionHandler();
}

```

**Output:**

```
number 1
number 2
number 3
number 4
error: Exception: Demo exception when accessing 5th number
Done
```

**Source Code** is available [here- Example#2](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---
# Sample Stream

I'll be using following stream to demonstrate upcoming examples of Stream operations. If you're running code snippets in [DartPad](https://dartpad.dev/), make sure to add following code for creating a stream first.

```
//This will generate a stream and return reference to it.
Stream<int> createNumberStream(int last) async* {
  for (int i = 1; i <= last; i++) {
    yield i; //to be able to send spaced out events
  }
}
```
---

# Single Subscription Stream Operations

In this section, I'll be discussing usage of Stream's methods with help of examples.

## Using `where()` Method

Let's see an example to find and print a number greater than 3 in number stream in example above. In this example `listen()` method subscribes to stream and acts like a callback. Every time, a number meeting the criteria is found, its sent over to callback to take further action on it.

**Example#3.**

```
//Example#3. Demonstrating usage of `where()`
void filterUsingWhere() {
  var stream = createNumberStream(5);
  stream
      .where((x) => x > 3) //Filters numbers greater than 3
      .listen((x) => print(x)); //prints numbers filtered
}
//----END----//

//Entry point function
void main() {
  //Run Example#3.
  filterUsingWhere();
}

```

**Output:**

```
4
5

```

**Source Code** is available [here- Example#3](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

## Using Stream's Properties

In this section, we'll learn about following properties of a `Stream` with help of examples. Let's use the previous example to understand the usage of these properties in action. Notice the pair method `then()` rather `listen()` when using properties.

### `first`

Retrieves the first event of the stream.

**Example#4.**

```
//Example#4. Demonstrating usage of `first`
void first() {
  var stream = createNumberStream(5);

  //print the first number/event
  stream.first.then(
    (x) => print("First event: $x"),
  );
}
//----END----//

//Entry point function
void main() {
  //Run Example#4.
  first();
}

```

**Output:**

```
First event: 1
```

**Source Code** is available [here- Example#4](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

### `last`

Retrieves the last event of the stream.

**Example#5.**

```
//Example#5. Demonstrating usage of `last`
void last() {
  //A fresh stream is needed.
  //Single subscription stream can't be re-listened.
  var stream = createNumberStream(5);
  //print the last number/event
  stream.last.then((x) => print("Last event: $x"));
}
//----END----//

//Entry point function
void main() {
  //Run Example#5.
  last();
}

```

**Output:**

```
Last event: 5
```

**Source Code** is available [here- Example#5](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

### `length`

Retrieves length of the stream.

**Example#6.**

```
//Example#6. Demonstrating usage of `length`
void length() {
  var stream = createNumberStream(5);
  //print the length of the stream
  stream.length.then((x) => print("Length of Stream: $x"));
}
//----END----//

//Entry point function
void main() {
  //Run Example#6.
  length();
}

```

**Output:**

```
Length of Stream: 5
```

**Source Code** is available [here- Example#6](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

### `isEmpty`

Checks if stream is empty of not.

**Example#7.**

```
//Example#7. Demonstrating usage of `isEmpty`
void isEmpty() {
  var stream = createNumberStream(5);
  //Check if stream is empty
  stream.isEmpty.then((x) => print("Is Empty : $x"));

  //Create an empty stream
  stream = createNumberStream(0);
  //Verify an empty stream
  stream.isEmpty.then((x) => print("Is Empty : $x"));
}
//----END----//

//Entry point function
void main() {
  //Run Example#7.
  isEmpty();
}

```

**Output:**

```
Is Empty : false
Is Empty : true
```

**Source Code** is available [here- Example#7](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

# Broadcast Streams Operations

Let's convert single subscription stream in previous example to broadcast stream using `asBroadcastStream()` method and re-examine all properties again. This time we don't need to create a fresh stream for each operation. Broadcast streams can have multiple subscribers or can be listened multiple times.

**Example#8.**

```
//Example#8. Demonstrating BroadcastStream basic operations
void broadcastStreamBasicOperations() {
  var stream = createNumberStream(5);

  //Converting to broadcastStream
  var bStream = stream.asBroadcastStream();

  //check if stream is broadcast stream or single
  if (bStream.isBroadcast) {
    print("Broadcast Stream");
  } else {
    print("Single Stream");
  }
  //print the first number/event
  bStream.first.then((x) => print("First event: $x"));

  //print the last number/event
  bStream.last.then((x) => print("Last event: $x"));

  //print the length of the stream
  bStream.length.then((x) => print("Length of Stream: $x"));

  //Check if stream is empty
  bStream.isEmpty.then((x) => print("Is Empty : $x"));

  //empty stream on purpose
  stream = createNumberStream(0);
  bStream = stream.asBroadcastStream();
  bStream.isEmpty.then((x) => print("Is Empty : $x"));
}
//----END----//

//Entry point function
void main() {
  //Run Example#8.
  broadcastStreamBasicOperations();
}

```

**Output:**

```
Broadcast Stream
First event: 1
Is Empty : false
Is Empty : true
Last event: 5
Length of Stream: 5
```

**Source Code** is available [here- Example#8](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

Let's see few methods that extract part of the data stream and create sub-streams of data. Listeners listen to these output sub-streams.

## Using `take()` Method

Creates the sub-stream for 'given number' of first events of original stream. Listener listens to this sub-stream and print all elements.

**Example#9.**

```
//Example#9. Demonstrating BroadcastStream `take()` method
void broadcastStreamTake() {
  var stream = createNumberStream(5);

  //Converting to broadcastStream
  var bStream = stream.asBroadcastStream();

  //Creates a sub stream of 2 elements and
  //listen on it
  bStream.take(2).listen(
        (x) => print("take() : $x"),
      );
}
//----END----//

//Entry point function
void main() {
  //Run Example#9.
  broadcastStreamTake();

}

```

**Output:**

```
take() : 1
take() : 2

```

**Source Code** is available [here- Example#9](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).


---

## Using `skip()` Method

Creates sub-stream of original stream after skipping first 'given number' of events from original stream. Listener listens to this sub-stream and print all elements.

**Example#10.**

```
//Example#10. Demonstrating BroadcastStream `skip()` method
void broadcastStreamSkip() {
  var stream = createNumberStream(5);

  //Converting to broadcastStream
  var bStream = stream.asBroadcastStream();

  //skips first two numbers from [1,2,3,4,5]
  bStream.skip(2).listen(
        (x) => print("skip() : $x"),
      );
}
//----END----//

//Entry point function
void main() {
  //Run Example#10.
  broadcastStreamSkip();
}

```

**Output:**

```
skip() : 3
skip() : 4
skip() : 5

```

**Source Code** is available [here- Example#10](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

## Using `takeWhile()` Method

The `takeWhile()` method does the same thing as `take()` when a condition is full-filled. Let's add condition that pick/take first elements when number is positive but less than 3. There are two such numbers in [1, 2, 3, 4, 5], which is 1 and 2. `takeWhile()` will check the condition and will print these 2 numbers on console.

**Example#11.**

```
//Example#11. Demonstrating BroadcastStream `takeWhile()` method
void broadcastStreamTakeWhile() {
  var stream = createNumberStream(5);

  //Converting to broadcastStream
  var bStream = stream.asBroadcastStream();

  //Creates a sub-stream of items less than 3, and prints the sub-stream of [1,2].
  bStream.takeWhile((x) => x > 0 && x < 3).listen(
        (x) => print("takeWhile() : $x"),
      );
}
//----END----//

//Entry point function
void main() {
  //Run Example#11.
  broadcastStreamTakeWhile();

}

```

**Output:**

```
takeWhile() : 1
takeWhile() : 2
```

**Source Code** is available [here- Example#11](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

## Using `skipWhile()` method

The `skipWhile()` method is similar to `skip()` in addition to honoring the condition.

**Example#12.**

```
//Example#12. Demonstrating BroadcastStream `skipWhile()` method
void broadcastStreamSkipWhile() {
  var stream = createNumberStream(5);

  //Converting to broadcastStream
  var bStream = stream.asBroadcastStream();

  //skips elements which are positive and
  //less than 3, and prints rest.
  bStream
      .skipWhile((x) => x > 0 && x < 3)
      .listen((x) => print("skipWhile() : $x"));
}
//----END----//

//Entry point function
void main() {
  //Run Example#12.
  broadcastStreamSkipWhile();

}

```

**Output:**

```
skipWhile() : 3
skipWhile() : 4
skipWhile() : 5
```

**Source Code** is available [here- Example#12](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

# Modifying Stream: `transform()` Method

Transform stream's events to another type. In this example, a String of integers is transformed to stream of strings.

**Example#13.**

```
//Example#13. Demonstrating modifying a stream using `transform()` method
void modifyStreamUsingTransform() {
  //Stream of integer events is created.
  var stream = createNumberStream(5);

  //StreamTransformer prints the transformed event
  var transformer =
      StreamTransformer<int, String>.fromHandlers(handleData: (value, sink) {
    sink.add("My number is $value");
  });

  stream.transform(transformer).listen(
        (x) => print(x),
        onError: (err) => print("error: $err"),
        onDone: () => print("Done"),
      );
}
//----END----//

//Entry point function
void main() {
  //Run Example#13
  modifyStreamUsingTransform();

}

```

**Output:**

```
My number is 1
My number is 2
My number is 3
My number is 4
My number is 5
Done
```

**Source Code** is available [here- Example#13](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/streams/streams_types.dart).

---

# References

1. [Dart Futures](https://dart.dev/tutorials/language/futures)
2. [Dart Streams](https://dart.dev/tutorials/language/streams)

Happy cooking with Dart and Flutter :)

_Liked the article?
Couldn't find a topic of your interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
