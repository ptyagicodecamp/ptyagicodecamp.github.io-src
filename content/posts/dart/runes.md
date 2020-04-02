Title: The `runes` Property
Date: 04/01/2020
Authors: ptyagi
Category: Dart
Tags: Runes, dart, cross-platform, flutter, code-recipes, development
Summary: TODO

# What is `Runes` ?
A code unit is the number of bits an encoding uses. ... A code point is a character and this is represented by one or more code units depending on the encoding

In Dart, a String is sequence of UTF-16 code units. The `runes` is the integer representation for unicode code points of a String.

**Code Point:** A code point is a character in a string. One code point can be represented by one or more code units.

**Code Unit:** A code unit is the number of bits used by an encoding. For UTF-16 encoding, it uses two bytes.


The [String Class](https://api.dart.dev/stable/2.7.2/dart-core/String-class.html) has following methods to access runes for a String.

## The [`codeUnitAt`](https://api.dart.dev/stable/2.7.2/dart-core/String/codeUnitAt.html) Method

This method returns the 16-bit UTF-16 code unit at the given index for the String.

## The [`codeUnits`](https://api.dart.dev/stable/2.7.2/dart-core/String/codeUnits.html) Property

Returns an unmodifiable list of the UTF-16 code units of this string.

## The [`runes`](https://api.dart.dev/stable/2.7.2/dart-core/String/runes.html) Property

This property returns the list of Unicode UTF-16 code points for the given string.
---

# Usage

---
# Companion Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
# Source Code

Please checkout the source code at Github [here]()


---
# References: ###

1. [Runes](https://api.dart.dev/stable/2.7.2/dart-core/Runes-class.html)
2. [Smiling Face UTF-16](https://www.fileformat.info/info/unicode/char/263a/index.htm)
3. [Character List for UTF-16](http://www.fileformat.info/info/charset/UTF-16/list.htm)

Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
