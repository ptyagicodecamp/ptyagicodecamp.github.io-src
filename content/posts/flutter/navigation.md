Title: Navigation and Routing in Flutter App
Date: 06/12/2020
Authors: ptyagi
Category: Navigation
Tags: Navigation, Routing, cross-platform, Flutter, code-recipes, Android, Android Studio, iOS, development
Summary: In this article, we'll learn about navigation and routing in a Flutter app.

#IN PROGRESS: COMING SOON

![TODO]({attach}../../images/flutter/TODO.jpg)

**Target Audience:** Beginner

**Recipe:** Implementing Navigation from home page to another page.

**Focus Widget:** [Navigator](https://api.flutter.dev/flutter/widgets/Navigator-class.html) Widget

**Goals:** We'll implement navigation from homepage's list item to its detailed view. In this recipe, we'll do two things:

* **Interface:**: Create a listing consisting of three items. Another page to display details for each item. Clicking on each item will open the detailed view for that item.

* **Navigation:** Implement navigation from home page to detail page using three different ways:

  * Un-named Routing
  * Named routing using MaterialApp's `routes` property
  * Named routing using MaterialApp's `onGenerateRoute` property.

---

**Checkout the companion video tutorial:**
<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

# Building Interface

## `PageListing` Screen

A minimal home page `PageListing` consists of three list items. Each item has a picture and sample title.

## `Item`

A data model `Item` to represent each row in homepage's list.

## `PageDetails` Screen

A page to show list entry `Item`'s detailed view. It's a simple page displaying item's image, details and its name in appBar.

## FAB on `PageDetails` Screen

There's a `floatingActionButton` in `PageDetails` to demonstrate passing data from detailed page back to homepage.

# Navigation

## Un-Named Routing

In un-name routing, the `MaterialPageRoutes` is pushed directly to the navigator. This approach contributes to boilerplate code which multiplies with growing screens/pages. It is very hard to keep track of logic around these routes since its spread out in multiple classes.

## Named Routing Using `routes` Property

The MaterialApp and WidgetApp provides the `routes` property. This property allows to specify routes in `Map<String, WidgetBuilder>`.
This option is great when there is no logic around the routes. For example, authentication or verification before you show the page. Only the data available global to app can be passed on to the second page.

## Named Routing Using `onGenerateRoute` Property

The MaterialApp and WidgetApp provides the `onGenerateRoute` property. It lets you specify a function returning a route. It can let the data pass using `settings`. Any verification logic can be easily be applied before showing the target page. There's always an option to default "not found" page when route or match is not found.


---

# Source Code Repo

* Recipe source code for `TODO` class is available [here]()

* Flutter Cookbook project's source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/widgets/flutter_widgets/)


# References
1.

Happy cooking with Flutter :)

_Liked the article?
Couldn't find a topic of your interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
