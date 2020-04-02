Title: The `runtimeType` Property
Date: 04/02/2020
Authors: ptyagi
Category: Dart
Tags: runtimeType, dart, cross-platform, flutter, code-recipes, development
Summary: This article describes what `runtimeType` property means in Dart's world.

# What is `runtimeType` Property ?

The `runtimeType` property is used to find out the runtime type of the object. The keyword `var` in Dart language lets a variable store any type of data. The `runtimeType` property helps to find what kind of data is stored in the variable using `var` keyword. In the next section, we'll explore usage of this property in for different type of data.


# Usage

Let's see a few examples of using `runtimeType` property below. You can execute code samples in [DartPad](https://dartpad.dev/) online.

  * **`int`:** Find the type of the variable storing an integer value. An integer in dart is represented using [`int`](https://api.flutter.dev/flutter/dart-core/int-class.html) class.

In this examples, variable `myNumber` is storing an integer. The keyword `var` in Dart lets a variable store any type of data. Calling `runtimeType` on the variable will return the data type of the variable.

```
//Variable myNumber is storing an integer value
var myNumber = 1;

//myNumber.runtimeType will print the data type for the variable
print("Type of myNumber: ${myNumber.runtimeType}");
```

**Output:**
```
Type of myNumber: int
```

---

 * **`String`:** Find the type of the variable storing a string value.

In this examples, variable `myString` is storing a string. The keyword `var` in Dart lets a variable store any type of data. Calling `runtimeType` on the variable will return the data type of the variable.

```
//Variable myString is storing an string value
var myString = "This is String";

//myString.runtimeType will print the data type for the variable
print("Type of myString: ${myString.runtimeType}");
```

**Output:**
```
Type of myString: String
```

---

  * **`double`:** Find the type of the variable storing a double value.

In this examples, variable `myDouble` is storing a double. The keyword `var` in Dart lets a variable store any type of data. Calling `runtimeType` on the variable will return the data type of the variable.

```
//Variable myDouble is storing an string value
var myDouble = 1.0;

//myDouble.runtimeType will print the data type for the variable
print("Type of myDouble: ${myDouble.runtimeType}");
```

**Output:**
```
Type of myDouble: double
```

  * **`List<int>`:** Find the type of the variable storing a list of integers.

In this examples, variable `myList` is storing a list of integers. The keyword `var` in Dart lets a variable store any type of data. Calling `runtimeType` on the variable will return the data type of the variable.

```
//Variable myList is storing an string value
var myList = [1, 2, 3];

//myList.runtimeType will print the data type for the variable
print("Type of myList: ${myList.runtimeType}");
```

**Output:**
```
Type of myList: List<int>
```

---

# Companion Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here]()

---

# References: ###
1. [runtimeType](https://api.dart.dev/stable/2.7.2/dart-core/Object/runtimeType.html)


Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)