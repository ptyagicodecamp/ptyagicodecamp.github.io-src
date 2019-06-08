Title: Dart Basics (Part-2: Streams)
Date: 06/08/2019
Authors: ptyagi
Category: Dart
Tags: Dart, Flutter
Summary: Learn basics of Dart programming language. Flutter uses Dart to build awesome cross-platform mobile and web applications.

***Target Audience:*** Beginner

### Introduction ###
Learn basics of Dart programming language. Flutter uses Dart to build awesome cross-platform mobile and web applications. In this tutorial, I'll be covering two of the Dart language features below:

* [Part-1](https://ptyagicodecamp.github.io/dart-basics-part-1-futures.html#dart-basics-part-1-futures) Futures: Asynchronous Programming with Dart
* [Part-2](https://ptyagicodecamp.github.io/dart-basics-part-1-futures.html#dart-basics-part-2-futures) Streams: Asynchronous Programming with Dart


### Streams: Asynchronous Programming with Dart ###
Why Streams ? A Stream is a sequence of asynchronous events. Streams are useful in providing an asynchronous sequence of data.

#### Key Terms ####

**Stream:** A Stream is a sequence of asynchronous events. It lets you know whenever next event is ready rather you asking for it.  

**Data Sequence:** A Data sequence is made up of either user-generated event or data read from files.

**async:** functions with `await` keyword needs to be marked as `async` keyword. Functions marked with `async` keywords doesn't suspend immediately, but execute synchronously until first `await` or `return` is called.

#### Creating a stream ####
Let's see how to generate a stream of events consists of numbers in code below:
* Using for-loop and `yield` keyword
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

#### Retrieving events from stream ####
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

#### Responding to errors using Streams ####
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

#### Handling errors using `listen()` method ####
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

#### Type of Streams ####
1. Single subscription
Single subscription streams are meant to deliver events in order. This type of stream is used when order of events received matters like reading a file. Such type of Streams can be listened only once. Attempting to listening them again will throw an exception.
2. Broadcast (Multiple subscribers)
Broadcast streams are intended to deliver events to it's subscribers. Any subscriber can start listening to events as soon as they subscribe to it. A Broadcast stream can be listened multiple times.

Note: A Single Subscription stream can be converted into broadcast streams by using `asBroadcastStream()` method.

#### Two ways to subscribe to streams ####

##### Using `listen()` #####
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

##### Using subscription's handler #####
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

  var subscription = stream.listen(null);
  subscription.onData((x) => print("number $x"));
  subscription.onError((err) => print("error: $err"));
  subscription.onDone(() => print("finished"));
}
```

### Single Subscription Stream Operations ###
In this section, I'll be discussing usage of Stream's methods with help of examples.

#### Using `where()` method ####
Let's see an example to find and print a number greater than 3 in number stream in example above. In this example `listen()` method subscribes to stream and acts like a callback. Every time, a number meeting the criteria is found, its sent over to callback to take further action on it.

```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

main() async {
  var stream = createNumberStream(5);
  stream
    .where((x) => x>3) //Filters numbers greater than 3
  .listen((x) => print(x)); //prints numbers filtered
}
```

#### Using Stream's properties ####
* `first`: Retrieves the first event of the stream.
* `last`: Retrieves the last event of the stream.
* `length`: Retrieves length of the stream.
* `isEmpty`: Checks if stream is empty of not.

Let's use the previous example to see usage of these properties in action. Notice the pair method `then()` rather `listen()` when using properties.

```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

main() async {
  var stream = createNumberStream(5);

  //print the first number/event
  stream.first
  .then((x) => print("First event: $x"));

  //A fresh stream is needed.
  //Single subscription stream can't be re-listened.
  stream = createNumberStream(5);
  //print the last number/event
  stream.last
  .then((x) => print("Last event: $x"));


  stream = createNumberStream(5);
  //print the length of the stream
  stream.length
  .then((x) => print("Length of Stream: $x"));

  stream = createNumberStream(5);
  //Check if stream is empty
  stream.isEmpty
  .then((x) => print("Is Empty : $x"));


  stream = createNumberStream(0);
  //Verify an empty stream
  stream.isEmpty
  .then((x) => print("Is Empty : $x"));
}
```

#### Broadcast Streams Operations ####
Let's convert single subscription stream in previous example to broadcast stream using `asBroadcastStream()` method and re-examine all properties again. This time we don't need to create a fresh stream for each operation. Broadcast streams can have multiple subscribers or can be listened multiple times.
```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

main() async {
  var stream = createNumberStream(5);
  var bStream = stream.asBroadcastStream();

  //check if stream is broadcast stream or single
  if (bStream.isBroadcast) {
    print("Broadcast Stream");
  } else {
    print("Single Stream");
  }
  //print the first number/event
  bStream.first
  .then((x) => print("First event: $x"));

  //print the last number/event
  bStream.last
  .then((x) => print("Last event: $x"));

  //print the length of the stream
  bStream.length
  .then((x) => print("Length of Stream: $x"));

  //Check if stream is empty
  bStream.isEmpty
  .then((x) => print("Is Empty : $x"));

  //empty stream on purpose
  stream = createNumberStream(0);
  bStream = stream.asBroadcastStream();
  bStream.isEmpty
  .then((x) => print("Is Empty : $x"));
}
```
Let's see few methods that extract part of the data stream and create sub-streams of data. Listeners listen to these output sub-streams.

#### Using `take()` method ####
Creates the sub-stream for 'given number' of first events of original stream. Listener listens to this sub-stream and print all elements.

#### Using `skip()` method ####
Creates sub-stream of original stream after skipping first 'given number' of events from original stream. Listener listens to this sub-stream and print all elements.

#### Using `takeWhile()` method ####
`takeWhile()` method does the same thing as `take()` when a condition is full-filled. Let's add condition that pick/take first elements when number is positive but less than 3. There are two such numbers in [1, 2, 3, 4, 5], which is 1 and 2. `takeWhile()` will check the condition and will print these 2 numbers on console.

#### Using `skipWhile()` method ####
`skipWhile()` method is similar to `skip()` in addition to honoring the condition.

```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

main() async {
  var stream = createNumberStream(5);
  var bStream = stream.asBroadcastStream();

  //Creates a sub stream of 2 elements and
  //listen on it
  bStream.take(2)
  .listen((x) => print("take() : $x"));

  //skips first two numbers from [1,2,3,4,5]
  bStream.skip(2)
  .listen((x) => print("skipe() : $x"));

  bStream.takeWhile((x) => x>0 && x<3)
  .listen((x) => print("takeWhile() : $x"));

  //skips elements which are positive and
  //less than 3, and prints rest.
  bStream.skipWhile((x) => x>0 && x<3)
  .listen((x) => print("skipWhile() : $x"));
}
```

### Modifying the Stream: `transform()` method ###
`transform()` method
```
import 'dart:async';

//this is the stream generated above
Stream<int> createNumberStream(int last) async* {
  for (int i=1; i<= last; i++) {
    yield i; //to be able to send spaced out events
  }
}

main() async {
  var stream = createNumberStream(5);

  var transformer = new StreamTransformer
  .fromHandlers(handleData: (value, sink) {
    sink.add("My number is $value");
  });

  stream.transform(transformer)
  .listen(
    (x) => print(x),
    onError: (err) => print("error: $err"),
    onDone: () => print("finished")
    );
}
```
### References: ###
1. [Dart Futures](https://dart.dev/tutorials/language/futures)
2. [Dart Streams](https://dart.dev/tutorials/language/streams)

Happy cooking with Dart and Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
