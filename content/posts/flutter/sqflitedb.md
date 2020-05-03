Title: Persisting Data in Local DB for Flutter (Android & iOS)
Date: 05/02/2020
Authors: ptyagi
Category: Flutter
Tags: sqflite, cross-platform, flutter, code-recipes, android, android Studio, iOS, development
Summary: This article demonstrates persisting data in local database in Flutter App.


**Target Audience:** Beginner

**Recipe:** Persisting products data in local database using `sqflite` Flutter plugin.

**Focus Widget:** Flutter plugin [sqflite](https://pub.dev/packages/sqflite).

**Goal:** In this recipe, we'll create, save, and retrieve two objects of custom data type, `Product` in the local sqlite database. We'll create two files for this recipe:

* **User Interface** -[`ecom.dart`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets-code/flutter_widgets/lib/persistence/ecom.dart) : User interface to load data from local database.

* **Database** -[`ecom_db.dart`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets-code/flutter_widgets/lib/persistence/ecom_db.dart): This file contains all code related to sqlite database.

The user interface will load two demo products in a `ListView` as shown in this screenshot:

![products_db]({attach}../../images/flutter/localdb_products.jpg)


---

# Flutter Cookbook

This code recipe is added in the [Flutter Cookbook](https://ptyagicodecamp.github.io/flutter-live-booklet-flutter-component-recipes.html) app as well. Source code link is available at the end of this article.

![localdb_cookbook]({attach}../../images/flutter/localdb_cookbook.jpg)

---

---

# `pubspec.yaml` dependency

Add `sqflite` plugin dependency as below:

```
dependencies:
  flutter:
    sdk: flutter

  #Local database
  sqflite: ^1.3.0
```

**Note:** The `sqflite` plugin has dependency on [`path`](https://pub.dev/packages/path) plugin. Please add this dependency it's not already present in your configuration file.

---

# User Interface

In this code recipe, there're only two product items used for demonstration purposes. Each item has an image, title, description, and price.

The UI is composed of widgets as shown below:

![localdb_interface]({attach}../../images/flutter/localdb_products_lined.jpg)

**Note:** This article is not intended for learning to build user interface. Hence, I'll quickly review the UI structure. Please refer to source code to see full code.

Main interface is rendered using `ListView` widget. The `ListView` widget has a `Column` widget as its child. The custom widget `positionedBlock()` is added as `Column` widget's child.

**positionedBlock():** This method returns interface for each item in the list. It's is aligned in `topCenter` using `Align` widget. A `Stack` widgets contains two `Positioned` widgets for product description and image.
The first `Positioned` widget is added in the background to display product information (in a `Column` widget). The another `Positioned` widget contains the product's image.

The main screen is a `StatefulWidget` since we want to update data retrieved from local database. Sample data in database is added as soon as the app starts. We'll go over database details in next section. The `initDB()` method is called rom `initState()` method. The `initState()` method executes once during screen startup-time. We want to keep data ready in database for querying by `build()` method.

```
class ProductListing extends StatefulWidget {
  @override
  _ProductListingState createState() => _ProductListingState();
}

class _ProductListingState extends State<ProductListing> {
  @override
    void initState() {
      super.initState();
      //insert demo data
      initDB();
  }
}
```

## Rendering Data from Database

The `_ProductListingState` widget's `build()` method is responsible for updating data at the interface. It uses `FutureBuilder` widget to render data returned from asynchronous methods like `Future`. Usually data is returned asynchronously from database or remote network operations. `FutureBuilder` widget helps render data asynchronously at user interface side.

```
body: FutureBuilder(
    //fetching products from db
    future: allProducts(),
    builder: (context, AsyncSnapshot snapshot) {
      if (!snapshot.hasData) {
        //loading circular progress bar
        return Center(child: CircularProgressIndicator());
      } else {
        return Container(
          child: ListView.builder(
            itemCount: snapshot.data.length,
            scrollDirection: Axis.vertical,
            itemBuilder: (BuildContext context, int index) {
              return Column(
                children: [
                  //custom widget
                  positionedBlock(context, snapshot.data[index]),
                  Divider(
                    thickness: 2,
                  ),
                ],
              );
            },
          ),
        );
      }
    }),
```


The `allProducts()` method returns a list of `Product` of `Future` type. Each product entry uses `positionedBlock(...)` method to display product details. Checkout the source code for this [here](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets-code/flutter_widgets/lib/persistence/ecom.dart).

Let's explore the database side of things next.

---

# Local Database

The `sqflite` plugin access to sqlite database on Android and iOS devices for Flutter. Let's check out the database operations next.

**Note:** Refer [`ecom_db.dart`](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets-code/flutter_widgets/lib/persistence/ecom_db.dart).

## Creating Database

The `openDatabase()` method takes database path, version of the database to support db upgrades & downgrades, and a way to create table using `onCreate:` attribute.

The `getDatabasesPath()` provides the physical location of database on device. The `join()` methods is a utility method to join the given paths into single path as per the current platform's file separator. You need `path` plugin to access `join()` method.

```
Future<Database> db() async {
  return openDatabase(
    join(await getDatabasesPath(), 'products_database.db'),
    onCreate: (db, version) {
      return db.execute(
        'CREATE TABLE IF NOT EXISTS $tableProducts(id INTEGER PRIMARY KEY, title TEXT, description TEXT, image TEXT, price REAL)',
      );
    },
    // Version provides path to perform database upgrades and downgrades.
    version: 1,
  );
}

```

The `db()` will return `Database` as `Future`. Initializing database is an asynchronous operation. The database reference is being held in `database` variable, and product table name is `products` and stored in `tableProducts` constant. A table `products` is created if doesn't exist already.

## Product class

The Product is represented with class `Product`. A product object has `id`, `title`, `description`, `image`, and `price`.

```
class Product {
  final int id;
  final String title;
  final String description;
  final String image;
  final double price;

  Product({this.id, this.title, this.description, this.image, this.price});

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'image': image,
      'price': price,
    };
  }

  @override
  String toString() {
    return 'Product("id": ${this.id}, "title": ${this.title}, "description": ${this.description}, '
        '"image": ${this.image}, "price":${this.price});';
  }
}

```

## Inserting Product

Inserting data into a table is an asynchronous operation as well. First get a reference to database and then pick a conflictAlgorithm. It is a rule to resolve conflicts. In our case, we want to replace old content with new content if record is already present. Hence, it makes sense to pick `ConflictAlgorithm.replace` conflictAlgorithm.

```
Future<void> insertProduct(Product product) async {
  // Get a reference to the database.
  final Database db = await database;

  // Insert the Product into the correct table.
  // Specify `conflictAlgorithm`.
  // In this case, if the same product is inserted
  // multiple times, it replaces the previous data.
  await db.insert(
    tableProducts,
    product.toMap(),
    conflictAlgorithm: ConflictAlgorithm.replace,
  );
}
```

## Querying All Products

We want to render all products from the table into interface. In our case, there are only two products.

```
Future<List<Product>> allProducts() async {
  // Get a reference to the database.
  final Database db = await database;

  // Query the table for all The Products.
  final List<Map<String, dynamic>> maps = await db.query(tableProducts);

  // Convert the List<Map<String, dynamic> into a List<Product>.
  return List.generate(
    maps.length,
    (i) {
      return Product(
          id: maps[i]['id'],
          title: maps[i]['title'],
          description: maps[i]['description'],
          image: maps[i]['image'],
          price: maps[i]['price']);
    },
  );
}
```

## Updating Product

In this code recipe, we're not editing an existing item. However, `db.update(...)` method is useful to update the items. Remember to make use of `whereArgs` to avoid SQL injections.

```
Future<void> updateProduct(Product product) async {
  // Get a reference to the database.
  final db = await database;

  // Update the given Product.
  await db.update(
    tableProducts,
    product.toMap(),
    // Ensure that the Product has a matching id.
    where: "id = ?",
    // Pass the Products's id as a whereArg to prevent SQL injection.
    whereArgs: [product.id],
  );
}
```

## Deleting Product

We're not deleting any item either in this sample. Similar to `update`, remember to use `whereArgs` to keep SQL injections on the bay.

```
Future<void> deleteProduct(int id) async {
  // Get a reference to the database.
  final db = await database;

  // Remove the Product from the database.
  await db.delete(
    tableProducts,
    // Use a `where` clause to delete a specific product.
    where: "id = ?",
    // Pass the Products's id as a whereArg to prevent SQL injection.
    whereArgs: [id],
  );
}
```


## Inserting Sample Data into Table

In our sample, we're creating following two products, and inserting into database using `await` keyword to keep it asynchronous. The product images are loaded from local assets folder.

```
void initDB() async {
  var prod1 = Product(
    id: 1,
    title: 'Shoes',
    description: 'Rainbow Shoes',
    image: 'shoes.jpeg',
    price: 65.0,
  );

  var prod2 = Product(
    id: 2,
    title: 'Dress',
    description: 'Summer Dress',
    image: 'dress.png',
    price: 50.0,
  );

  // Insert a product into the database.
  await insertProduct(prod1);

  await insertProduct(prod2);
}
```

That's all ! In this code recipe, we added two products in local database, and displayed both product entries in Flutter App.

---

# Source Code Repo

* Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/blob/widgets-code/flutter_widgets/lib/persistence)

* Flutter Cookbook project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)

---

# References

1. The [`path`](https://pub.dev/packages/path) Plugin
2. The [`sqflite`](https://pub.dev/packages/sqflite) Plugin

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
