Title: Dart Basics
Date: 06/08/2019
Authors: ptyagi
Category: Dart
Tags: Dart, Flutter
Summary: Learn basics of Dart programming language. Flutter uses Dart to build awesome cross-platform mobile and web applications.

***Target Audience:*** Beginner

### Introduction ###
Learn basics of Dart programming language. Flutter uses Dart to build awesome cross-platform mobile and web applications. In this tutorial, I'll be covering two of the Dart language features below:
#1. Futures: Asynchronous Programming with Dart
#2. Streams: Asynchronous Programming with Dart

### Futures: Asynchronous Programming with Dart ###
"Futures" are Future objects that represent the results of asynchronous operations. Asynchronous operations don't block the thread and their processing finishes at a later time. Asynchronous operations results are returned as `Futures`. Functions that do expensive work should use asynchronous model for executing their work. Future object is represented as `Future<T>`, where T is the type of results returned from the expensive operation.

Asynchronous operations in Dart can be achieved in two ways:
1. Using `await` and `async`
2. Using `Future` API.

#### `await` and `async` ####
`await` and `async` keywords are used together. The function that supposed to be doing the expensive work will be marked with keyword `async`. Inside function, the expensive call is prefixed by keyword `await`. Program suspends when `await` is called or function return or reaches at the end of the function.

Let's see in following code snippet how `async` and `await` keywords are used. `await` can only be called in function which is marked/declared as `async`. `Future` keyword before the function `makeDataCall()` means that this function will be executing  asynchronously and will be suspended when come across `await`.
```
import 'dart:async';

const data = "I'm expansive data";

//Asynchronous function that makes the expensive
//data call
Future<void> makeDataCall() async {
  var data = await getData();
  print(data);
}

//Expensive function that could be long running
//in real world.
String getData() {
  return data;
}

//Entry point function
void main() {
   makeDataCall();
}
```

#### Error Handling (try/catch block) ####
When an exception is thrown in try block, catch block executes it's code. Error handling for asynchronous and synchronous code is handled similar way.
Let's add the try/catch block in previous code, and see how it'll look like now. I'm throwing an `Exception` on purpose in `try` block to demonstrate the point here.
```
import 'dart:async';

const data = "I'm expansive data";

//Asynchronous funtion that makes the expensive
//data call
Future<void> makeDataCall() async {
  try {
    var data = await getData();
    throw Exception(
      "Error occurred in fetching data");
  } catch(e) {
    print(e.toString());
  }
}

//Expensive function that could be long running
//in real world.
String getData() {
  return data;
}

//Entry point function
void main() {
   makeDataCall();
}
```

#### Sequencing function calls ####
It's possible to control the order of execution of asynchronous functions using sequencing with help of `await` and `async`. Let's see how this is done in example below.
```
import 'dart:async';

const data = "I'm expansive data";

void getDataA() {
  print("dataA");
}

void getDataB() {
  print("dataB");
}

String getDataC() {
  return "dataC";
}

void printMyData(String data) {
  print(data);
}

//Entry point function
main() async {
  //order matters.
  //Functions will execute in the order they are called.
  await getDataA();
  await getDataB();

  //getDataC() will execute first and will
  //pass its data into printMyData
  printMyData(await getDataC());
}
```

#### `Future` API ####

In `Future` API, `then()` method is used to register a callback, which fires up on completion of `Future`.
Example below transforms our earlier example code of `await` and `async` into `Future` API. Lookout for the use of `then()` in `main()` function.
```
import 'dart:async';

const data = "I'm expansive data";

//Future with String data is being returned.
//This function returns the instance of
//Future and not the actual data.
Future<String> makeDataCall() async {
  var data = await getData();
  return data;
}

String getData() {
  return data;
}

void main() {
   var theFuture = makeDataCall();
  //then() is called at the instance of Future
  theFuture.then((value) {
                 print(value);
                 });

}
```

Let's look at another example of `Future` API. In this example, `Future` doesn't return anything and looks like this `Future<void>`. In such case, `then()` callback will use an `unused argument`, represented as `_` by convention. Checkout the code snippet below to see it in action.

```
import 'dart:async';

const data = "I'm expansive data";

//Future doesn't return anything
Future<void> makeDataCall() async {
  var data = await getData();
  print(data);
}

String getData() {
  return data;
}

void main() {
   var theFuture = makeDataCall();
  //then() uses underscore as unused argument.
  theFuture.then((_) {
                 //_ is not used
                 print("There's nothing to be printed here. Work is already done.");
                 });

}
```

#### Error Handling - `Future` API ####
`Future` API uses chaining to handle exceptions. Error is caught and handled in `catchError()` block. `catchError()` is chained with `then()` method.
```
import 'dart:async';

const data = "I'm expansive data";

//Future with String data is being returned.
//This function returns the instance of
//Future and not the actual data.
Future<String> makeDataCall() async {
  var data = await getData();
  //return data;
  throw Exception("Error occurred in making data call");
}

String getData() {
  return data;
}

void main() {
   var theFuture = makeDataCall();
  //Error is caught and handled in catchError block
  theFuture.then((value) {
                 print(value);
                 }).catchError((error){
                               print(error);});

}
```

#### Usage of `Future.wait()` ####
`Future.wait()` is used when multiple asynchronous functions needs to be executed before calling another function. This could be useful when data from multiple sources/functions is needed to be able to take next step.
```
import 'dart:async';

String getData(data) {
  return data;
}

Future<String> getDataA() async {
  var data = await getData("dataA");
  return data;
}

Future<String> getDataB() async {
  var data = await getData("dataB");
  return data;
}

Future<String> getDataC() async {
  var data = await getData("dataC");
  return data;
}

void printMyData(List<String> data) {
  print(data);
}

//Entry point function
main() async {
  await Future.wait([getDataA(), getDataB(), getDataC()])
    .then((List responses) => printMyData(responses))
    .catchError((error){});
}
```


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


### References: ###
1. [Dart Futures](https://dart.dev/tutorials/language/futures)
2. [Dart Streams](https://dart.dev/tutorials/language/streams)

Happy cooking with Dart and Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
