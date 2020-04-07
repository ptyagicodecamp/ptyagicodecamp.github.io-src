Title: Dart Extensions
Date: 04/07/2020
Authors: ptyagi
Category: Dart
Tags: extension, dart, cross-platform, flutter, code-recipes, development
Summary: This article explains what extension methods, operators, and properties are, and how to use them.

# Introduction

Dart Extensions were first introduced in Dart 2.6 as preview. Later on, they have been released in Dart 2.7 officially. The extensions feature is the way to add functionality to existing libraries.

Sometimes you may want to add utility method(s) in a third-party library or in a core class like [String](https://api.dart.dev/stable/2.7.2/dart-core/String-class.html) for your convenience. However, it may not be possible to add your methods in those classes all the time. The closest possible solution is to write utility and/or wrapper classes with `static` methods and members. These extra classes can bloat your code base and increases the number of objects in general.

In such scenarios, extensions feature can come handy. It may look like wrapper classes, but they are different than wrapper classes. In wrapper classes, object is explicitly passed as arguments to the static methods. However, extensions implicitly extends the type.

There are three types of Dart extensions :

* Extension methods
* Extension operators
* Extension properties

# Defining Extensions

In Dart, all three types of extensions are defined inside one code block. The code block starts with `extension` followed by an optional name for the extension and `on` keyword, and then the type.

For example, if I want to add a custom functionality to `List` data type, then the extension code block would look like below:

```
extension<T> MyList on List<T> {
  //extension methods

  //extension operators

  //extension properties
}
```

The `MyList` is optional. It's only needed when extensions are written in a separate file, and are being imported into another dart file. However, if you have another similar local / private extension, you might see conflicts. To avoid such conflicts, you may want to hide external extension like below:

```
//extensions2.dart has MyList extension definition
import 'extensions2.dart' hide MyList;
```

In the following section, let's explore few examples to use it.

---

# Usage

Let's get started by defining a local `extension<T>` block `on` `List<T>` type. We'll be exploring different type of data types, so using generic type `T`.

```
extension<T> on List<T> {
  //extension methods

  //extension operators

  //extension properties
}
```

## Extension Methods

In this section, we'll add two extension methods. We've a list of prices.

**#1. Extension:**

First, let's add an extension method `priceList()` to return the prices listing. This method doesn't do anything important, but demonstrate how extensions implicitly extends the type using `this`.

```
extension<T> on List<T> {
  //Extension Method: demo
  List<T> priceList() => this.map((item) => item).toList();

}
```

**Using:**

```
void main() {
  //List of prices
  List prices = [1, 1.99, 4];

  print("Price listing:");

  //priceList() is being called on `prices`
  print(prices.priceList());
}
```

**Output:**

```
Price listing:
[1, 1.99, 4]
```

---

**#2. Extension:**

The `priceLabels(String symbol)` extension method iterates over the price listing, and append a `symbol` prefix for each price.

```
extension<T> on List<T> {

  //Extension Method: Adding $ prefix
  List<String> priceLabels(String symbol) =>
      this.map((item) => "$symbol ${item}").toList();

}
```

**Using:**

```
void main() {
  //List of prices
  List prices = [1, 1.99, 4];

  print("\nPrice listing with \$ prefix");

  //The $ symbol is passed
  print(prices.priceLabels("\$"));
}
```

**Output:**

```
Price listing with $ prefix
[$ 1, $ 1.99, $ 4]
```

---

## Extension Operators

In this section, we'll add two extension operators. We've a list of prices similar to last example.

**#3. Extension:**

Let's define an operator extension for `^` operator. I want to use this operator to increases the price by the `n` times, where `n` is the argument passed into it.

```
extension<T> on List<T> {
  //Extension Operator: Hike up the price by n
  List<num> operator ^(int n) =>
    this.map((item) => num.parse("${item}") * n).toList();

}
```

**Using:**

```
void main() {
  //List of prices
  List prices = [1, 1.99, 4];

  print("\nPrice listing after hiking up prices 3x of the original value");

  //argument is passed after the operator sign
  print(prices ^ 3);
}
```

**Output:**

```
Price listing after hiking up prices 3x of the original value
[3, 5.97, 12]

```

---

**#4. Extension:**

Next define another operator extension for `-` operator. I want to use this operator to reduce the items' price to half when this operator is used.

```
extension<T> on List<T> {
  //Extension Operator: Reduce all prices by half
   List<num> operator -() =>
       this.map((item) => num.parse("${item}") / 2).toList();
}
```

**Using:**

```
void main() {
  //List of prices
  List prices = [1, 1.99, 4];

  print(
      "\nSale Price listing: prices are reduced by half of the original value");

  //no-arg operator is put before the list variable
  print(-prices);
}
```

**Output:**

```
Sale Price listing: prices are reduced by half of the original value
[0.5, 0.995, 2.0]

```

---

## Extension Property

In this section, we'll add one extension property. We've a list of prices similar to last example.


**#5. Extension:**

In this extension, we'll add a property to return total number of printed price tags needed for price listing, where 3 tags are needed per item. We've a list of prices similar to last example.

```
extension<T> on List<T> {
  //Extension Property: 3 printed labels for each price.
  int get numPrintedPriceTags => length * 3;
}
```

**Using:**

```
void main() {
  //List of prices
  List prices = [1, 1.99, 4];

  print("\nNumber of total price tags");
  print(prices.numPrintedPriceTags);
}
```

**Output:**

```
Number of total price tags
9

```

---

# Companion Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/extensions.dart)

---

# References

1. [Extension methods](https://dart.dev/guides/language/extension-methods)

2. [Dart Extension Methods Fundamentals](https://medium.com/dartlang/extension-methods-2d466cd8b308)

Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
