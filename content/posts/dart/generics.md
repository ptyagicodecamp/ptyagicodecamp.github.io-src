Title: Dart Generics
Date: 04/28/2020
Authors: ptyagi
Category: Dart
Tags: generics, dart, cross-platform, flutter, code-recipes, development
Summary: This article explains Dart Generics and how to use them.


![generics]({attach}../../images/dart/generics.png)

# Introduction

***In Progress article***

Dart's collection can hold different data types in one collection. It's optional in Dart to mention data type for a value. Usually, its data type is inferred automatically. For example, `var myVar = 5;` will infer `myVar`'s dataType as `int`.

Generics are used to enforce a collection to contain values of same type of data, and hence implement type-safety.

**Type Safety:** Programming concept that allows a memory block to contain only one type of data.


## Declaring Type-safe collections

The angular brackets (<data type>) with data type enclosed, is used to declare the collection of given data type to ensure type-safety.

**Syntax:**

```
CollectionType <dataType> identifier = CollectionType <dataType>();
```

**Example:**

```
List<Int> numbers = List<Int>();
```

Generics are parameterized and use type variables notations to restrict the type of data. These type variables are represented using single letter names. A few typically used single letter names are:

* **E:** The letter `E` is used to represent the element type in a collection like [List](https://api.dart.dev/stable/2.8.0/dart-core/List-class.html).
* **K:** The letter `K` is used to represent the key type in associative collections like [Map](https://api.dart.dev/stable/2.8.0/dart-core/Map-class.html).
* **V:** The letter `V` is used to represent the value type in associative collections like [Map](https://api.dart.dev/stable/2.8.0/dart-core/Map-class.html).
* **R:** The letter `R` is used to represent the return type of a method or function.

You can also use a single letter of your choice or a descriptive word for parameter names / generics. Let's explore these two options in the following example.


```
//Example #1: Demonstrating use of single letter and descriptive words for generics
class Product {
  final int id;
  final double price;
  final String title;

  Product(this.id, this.price, this.title);
}

class Inventory {
  final int amount;

  Inventory(this.amount);
}

//Custom type variables- Single letter
class Store<P, I> {
  final HashMap<P, I> catalog = HashMap<P, I>();

  List<P> get products => catalog.keys.toList();
  void addInventory(P product, I inventory) {
    catalog[product] = inventory;
  }
}

//Custom type variables- Descriptive
class MyStore<MyProduct, MyInventory> {
  final HashMap<MyProduct, MyInventory> catalog =
      HashMap<MyProduct, MyInventory>();

  List<MyProduct> get products => catalog.keys;

  void addInventory(MyProduct product, MyInventory inventory) {
    catalog[product] = inventory;
  }
}

void mainParams() {
  Product milk = Product(1, 5.99, "Milk");
  Product bread = Product(2, 4.50, "Bread");

  Store<Product, Inventory> store1 = Store<Product, Inventory>();
  store1.addInventory(milk, Inventory(20));
  store1.addInventory(bread, Inventory(15));

  Store<Product, Inventory> store2 = Store<Product, Inventory>();
  store2.addInventory(milk, Inventory(10));
  store2.addInventory(bread, Inventory(12));
}
```
---

In this section, let's checkout the type-safe implementations for some of the Dart's collection data structures:

* List
* Set
* Map
* Queue

# List

---

# Set

---

# Map

---

# Queue

---

Another reason for using Generics is for code reuse. Generics for classes and methods help to be able to reuse same code for different implementations of data types.

Let's explore the details below.


---

# Generics Methods / Functions

```
//Example #2: Generics methods

//Function's return type (T).
//Function's argument (List<T>).
//Function's local variable (T last).
T lastProduct<T>(List<T> products) {
  T last = products.last;
  print("Retrieving last product: ");
  return last;
}

mainGenericMethods() {
  Store<Product, Inventory> store = Store<Product, Inventory>();
  Product milk = Product(1, 5.99, "Milk", Inventory(20));
  Product bread = Product(2, 4.50, "Bread", Inventory(15));
  store.updateInventory(milk, Inventory(20));
  store.updateInventory(bread, Inventory(15));

  Product product = lastProduct(store.products);
  print(product.title);
}
```

---

# Generics Classes

Restricting the type of values that can be supplied to the class. These supplied values are known as generic arguments.

```
//Example #3: Using Generics for classes

//Restricting the type of values that can be supplied to the class
class FreshProduce<T extends Product> {
  FreshProduce(int i, double d, String s);

  String toString() {
    return "Instance of Type: ${T}";
  }
}

mainGenericClass() {
  FreshProduce<Product> spinach = FreshProduce<Product>(3, 3.99, "Spinach");
  print(spinach.toString());

  //This code will give compile time error complaining that String is not of type Product
//  FreshProduce<String> spinach2 = FreshProduce<String>(3, 3.99, "Spinach");
//  print(spinach.toString());
}
```

---

# Summary

In this article, we saw how

That's it for this article. Check out the [Dart Vocabulary Series](https://ptyagicodecamp.github.io/a-dartflutter-vocabulary-series.html) for other Dart stuff.

---


# Check out YouTube Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/generics.dart)

---

# References

1. [How do Generics SubTypes work](https://dzone.com/articles/how-do-generic-subtypes-work)


Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
