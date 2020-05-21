Title: Futures: Asynchronous Programming with Dart
Date: 05/20/2020
Authors: ptyagi
Category: Dart
Tags: Dart, Flutter
Summary: This article is the first part of introduction to asynchronous programming with Dart, and covers Futures in Dart.

***Target Audience:*** Beginner

#Introduction

This article is a part of three part series focused on asynchronous Programming with Dart. This article covers Futures in Dart to execute program asynchronously.

* **Part-1 (Current)** Futures: Asynchronous Programming with Dart
* [Part-2](https://ptyagicodecamp.github.io/streams-asynchronous-programming-with-dart.html) Streams: Asynchronous Programming with Dart
* [Part-3](https://ptyagicodecamp.github.io/types-of-streams-asynchronous-programming-with-dart.html) Types of Streams: Asynchronous Programming with Dart

---

#Futures

"Futures" are Future objects that represent the results of asynchronous operations. Asynchronous operations don't block the thread and their processing finishes at a later time. Asynchronous operations results are returned as [`Futures`](https://api.dart.dev/stable/2.8.2/dart-async/Future-class.html). Functions that do expensive work should use asynchronous model for executing their work. Future object is represented as `Future<T>`, where T is the type of results returned from the expensive operation.

Asynchronous operations in Dart can be achieved in two ways:

1. Using `await` and `async`
2. Using `Future` API.

# `await` and `async`

The `await` and `async` keywords are used together. The function that supposed to be doing the expensive work is marked with keyword `async`. Inside the function, the expensive call is prefixed by keyword `await`. Program suspends when `await` is called or function return or reaches at the end of the function.

Let's see in following code snippet how `async` and `await` keywords are used. `await` can only be called in function which is marked/declared as `async`. `Future` keyword before the function `makeDataCall()` means that this function will be executing  asynchronously and will be suspended when come across `await`.

```
// Expensive function could be a function that takes
// long time to process data and return results.
// Assume this function takes long time to return in real-world
String getExpansiveData() {
  return "I'm expansive data";
}

// This is the asynchronous function that makes the expensive
// data call and prints the results.
Future<void> makeDataCall() async {
  var data = await getExpansiveData();
  print(data);
}
//----END----//

//Entry point function
void main() {
  //Run Example#1.
  makeDataCall();
}

```

The `makeDataCall()` returns a `Future` of type `void` because there's nothing returned by this function. It simply prints the results using `print()` function.

**Output:**

```
I'm expansive data
```

***Note:*** You can run this code in [DartPad](https://dartpad.dev/) by copy and pasting above code as is.

**Source Code** is available [here- Example#1](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).

---

## Error Handling (Try/Catch Block)

In this section, we'll see how to handle exceptions thrown in the long running asynchronous operations. When `await` keyword is used, asynchronous call behaves like a synchronous one. In such cases, error handling for asynchronous and synchronous code is handled similar way.

The asynchronous call prefixed with `await` keyword is wrapped in a `try`/`catch` block. When an exception is thrown in the `try` block, the `catch` block executes its code.

Let's add the try/catch block in previous code, and see how it'll look like now. Let's name this function as `makeDataCallWithException()`. This function throws an `Exception` at purpose in `try` block to demonstrate the point here.

```
//Example#2. Demonstrating handling exception thrown in asynchronous operations

//Expansive operations ended up throwing exception
String getExpansiveDataWithException() {
  throw Exception("Error occurred in fetching data");
}

//Asynchronous function that makes the expensive data call
Future<void> makeDataCallWithException() async {
  try {
    await getExpansiveDataWithException();
  } catch (e) {
    print(e.toString());
  }
}
//----END----//

//Entry point function
void main() {
  //Run Example#2.
  makeDataCallWithException();
}
```

**Output:**

```
Exception: Error occurred in fetching data
```

**Source Code** is available [here- Example#2](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).

---

## Sequencing Function Calls

It's possible to control the order of execution of asynchronous functions using sequencing with help of `await` and `async`. Let's see how this is done in example below. In this example, there are three functions `getDataA()`, `getDataB()`, and `getDataC()`. We want them to execute one after another. The `await` keyword does exactly that. It executes the function synchronously until it comes across `await`, and wait there for it to finish before execute next line, in this case another `await` call.

```
//Example#3. Sequencing order of asynchronous calls

void getDataA() {
  print("dataA");
}

void getDataB() {
  print("dataB");
}

String getDataC() {
  return "dataC";
}

//Entry point function
Future<void> sequencingOperations() async {
  //Order matters.
  //Functions will execute in the order they were called.
  await getDataA();
  await getDataB();

  //getDataC() will execute first and will
  //pass its data into print() function
  print(await getDataC());
}
//----END----//

//Entry point function
void main() {
  //Run Example#3.
  sequencingOperations();
}
```

**Output:**

Each of the above methods will execute one by one starting from `getDataA()` and finishing executing `getDataC()`.

```
dataA
dataB
dataC
```

**Source Code** is available [here- Example#3](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).


---

# `Future` API

Another way to execute asynchronous operations is to use `Future` API. In the `Future` API, the [`then()`](https://api.dart.dev/stable/2.8.2/dart-async/Future/then.html) method is used to register a callback, which fires up on the completion of `Future`.

Let's see two variant of using Future API.

* `Future<String>`: Future returning `String` data type .
* `Future<void>`: Future returning `void`.

## `Future<String>`

Example below transforms our earlier example code of `await` and `async` into a `Future` API implementation. Lookout for the use of `then()` in `mainWithFutureAPI()` function. In this example, `Future` is returning `String`.

```
Using Future API (Future is returning String type)

//Future with String data is being returned.
//This function returns the instance of
//Future and not the actual data.
Future<String> makeDataCallFutureString() async {
  return await getExpansiveData();
}

// Assume this function takes long time to return in real-world.
String getExpansiveData() {
  return "I'm expansive data";
}


void mainWithFutureAPI() {
  var theFuture = makeDataCallFutureString();

  //then() is called at the instance of Future
  theFuture.then((value) {
    print(value);
  });
}
//----END----//


//Entry point function
void main() {
  //Run Example#4.
  mainWithFutureAPI();
}
```

**Output:**

```
I'm expansive data
```

**Source Code** is available [here- Example#4](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).

---

## `Future<void>`

Let's look at another example of `Future` API. In this example, `Future` doesn't return anything and looks like `Future<void>`. In such case, `then()` callback will use an `unused argument`, represented as `_` by convention. Checkout the code snippet below to see it in action.

```
//Example#5. Using Future API (Future is returning void type)

//Future doesn't return anything
Future<void> makeDataCallFutureVoid() async {
  await getExpansiveData();
}

// Assume this function takes long time to return in real-world.
String getExpansiveData() {
  return "I'm expansive data";
}

void mainWithFutureAPIVoid() {
  var theFuture = makeDataCallFutureVoid();
  //then() uses underscore as unused argument.
  theFuture.then((_) {
    //_ is not used
    print("There's nothing to be printed here. Work is already done.");
  });
}
//----END----//

//Entry point function
void main() {
  //Run Example#5.
  mainWithFutureAPIVoid();
}
```

**Output:**

```
There's nothing to be printed here. Work is already done.
```

**Source Code** is available [here- Example#5](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).

---

# Error Handling - `Future` API

`Future` API uses chaining to handle exceptions. Error is caught and handled in `catchError()` block. The `catchError()` is chained with `then()` method.

```
// Example#6. Future API - Error Handling

// Future with String data is being returned.
// This function returns the instance of
// Future and not the actual data.
Future<String> makeDataCallFutureAPIError() async {
  var data = await getExpansiveData();
  throw Exception("Error occurred in making data call: $data");
}

// Assume this function takes long time to return in real-world.
String getExpansiveData() {
  return "I'm expansive data";
}

void mainWithFutureAPIError() {
  var theFuture = makeDataCallFutureAPIError();

  //Error is caught and handled in catchError block
  theFuture.then((value) {
    print(value);
  }).catchError((error) {
    print(error);
  });
}
//----END----//

// Entry point function
void main() {
  //Run Example#6.
  mainWithFutureAPIError();
}
```

**Output:**

```
Exception: Error occurred in making data call: I'm expansive data
```

**Source Code** is available [here- Example#6](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).

---

# Usage of `Future.wait()`

The [`Future.wait()`](https://api.dart.dev/stable/2.8.2/dart-async/Future/wait.html) is used when multiple asynchronous functions needs to be executed before calling another function. This could be useful when data from multiple sources/functions is needed to be able to take next step.
In another version, we're using Future API to accomplish what we did using `async` & `await` in ['Example#3'](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart) above.

```
//Example#7. Using `Future.wait()`

Future<String> getData(data) {
  return data;
}

Future<String> getDataAFuture() async {
  return await getData("dataA");
}

Future<String> getDataBFuture() async {
  return await getData("dataB");
}

Future<String> getDataCFuture() async {
  return await getData("dataC");
}

mainWithFutureAPIWait() async {
  //Chaining Futures in order
  await Future.wait([
    getDataAFuture(),
    getDataBFuture(),
    getDataCFuture(),
  ])
      .then(
        (List responses) => print(responses),
      )
      .catchError((error) => print(error));
}
//----END----//

//Entry point function
void main() {
  //Run Example#7.
  mainWithFutureAPIWait();
}

```

**Output:**

```
[dataA, dataB, dataC]
```

**Source Code** is available [here- Example#7](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/futures/futures_await.dart).

---

#Summary

In this article, we saw how to use Futures to perform asynchronous operations in Dart. We explored `await`/`async` and Future API approaches to do so. Futures are like promises, which return results whenever they are complete. However, there's another approach to access asynchronous events using Streams. Streams provide results as they come until processing is finished. We'll explore Streams in next article.

# References

1. [Dart Futures Code Lab](https://dart.dev/tutorials/language/futures)
2. [Dart Future](https://dart.dev/guides/libraries/library-tour#future)
3. [Dart Streams](https://dart.dev/tutorials/language/streams)

Happy cooking with Dart and Flutter :)

_Liked the article?
Couldn't find a topic of your interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_
