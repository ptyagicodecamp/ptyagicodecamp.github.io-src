Title: Futures: Asynchronous Programming with Dart
Date: 2018-03-17 03:55PM
Authors: ptyagi
Category: Development
Tags: dart2, asynchronous, dev
Summary: "Futures" are Future objects that represent the results of asynchronous operations. Asynchronous operations don't block the thread and their processing finishes at a later time. Asynchronous operations results are returned as `Futures`.

"Futures" are Future objects that represent the results of asynchronous operations. Asynchronous operations don't block the thread and their processing finishes at a later time. Asynchronous operations results are returned as `Futures`. Functions that do expensive work should use asynchronous model for executing their work. Future object is represented as `Future<T>`, where T is the type of results returned from the expensive operation.

Asynchronous operations in Dart can be achieved in two ways:
1. Using `await` and `async`
2. Using `Future` API.

This article is covering following topics:
* await and async
* Error Handling (try/catch block)
* Sequencing function calls
* Future API
* Error Handling - Future API
* Usage of Future.wait()

### await and async ###
await and async keywords are used together. The function that supposed to be doing the expensive work will be marked with keyword async. Inside function, the expensive call is prefixed by keyword await. Program suspends when await is called or function return or reaches at the end of the function.

Let’s see in following code snippet how async and await keywords are used. await can only be called in function which is marked/declared as async. Future keyword before the function makeDataCall() means that this function will be executing asynchronously and will be suspended when come across await.

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

### Error Handling (try/catch block) ###
When an exception is thrown in try block, catch block executes it’s code. Error handling for asynchronous and synchronous code is handled similar way. Let’s add the try/catch block in previous code, and see how it’ll look like now. I’m throwing an Exception on purpose in try block to demonstrate the point here.

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

### Sequencing function calls ###
It’s possible to control the order of execution of asynchronous functions using sequencing with help of await and async. Let’s see how this is done in example below.

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

### Future API ###
In Future API, then() method is used to register a callback, which fires up on completion of Future. Example below transforms our earlier example code of await and async into Future API. Lookout for the use of then() in main() function.

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

Let’s look at another example of Future API. In this example, Future doesn’t return anything and looks like this Future<void>. In such case, then() callback will use an unused argument, represented as _ by convention. Checkout the code snippet below to see it in action.

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

### Error Handling - Future API ###
Future API uses chaining to handle exceptions. Error is caught and handled in catchError() block. catchError() is chained with then() method.
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

### Usage of Future.wait() ###
Future.wait() is used when multiple asynchronous functions needs to be executed before calling another function. This could be useful when data from multiple sources/functions is needed to be able to take next step.

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

***References:***
[DartLang](https://www.dartlang.org/tutorials/language/futures)
