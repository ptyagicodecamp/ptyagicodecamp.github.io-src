Title: The `runes` Property
Date: 04/05/2020
Authors: ptyagi
Category: Dart
Tags: runes, Runes, dart, cross-platform, flutter, code-recipes, development
Summary: This article describes what `runes` property means in Dart's language.

![runtimeType]({attach}../../images/dart/runes.png)

# Background

In the digital world, all characters, numbers or symbols are represented using a unique numeric value, known as Unicode. The Unicode standard provides three distinct encoding forms for Unicode characters: UTF-8 (using 8-bit), UTF-16 (16-bit), and UTF-32 (32-bit units). Data is converted in one of these encoding during data transfer.
In this article, we'll explore Dart language's one of the String class property known as `runes` to retrieve this encoded data.

# What is `runes` Property?

In Dart, a string is represented using sequence of UTF-16 known as code units. A code unit is the number of bits used by the given encoding.

**Code Point:** A character in a string is represented by one or more code point(s). One code point is represented by one or more code units.


**Code Unit:** A code unit is the number of bits used by an encoding. For UTF-16 encoding, it uses two bytes.

The `runes` property returns an iterable of Unicode code-points of this string of `Runes` type. The [`Runes`](https://api.dart.dev/stable/2.7.2/dart-core/Runes-class.html) is the integer representation for unicode code points of a String.

---

# Usage

The [String Class](https://api.dart.dev/stable/2.7.2/dart-core/String-class.html) has following methods to access runes for a String.

## The [`codeUnitAt`](https://api.dart.dev/stable/2.7.2/dart-core/String/codeUnitAt.html) Method

This method returns the UTF-16 (16-bit) _code unit_ at the given index for the String.

```
  String myStr = "Mask";

  ///Code unit at 0th position is M.
  ///UTF-16 decimal representation for ASCII character 'M' is 77
  ///Reference: https://www.fileformat.info/info/unicode/char/004d/index.htm
  print("Code Unit for Letter M: ${myStr.codeUnitAt(0)}");

```

**Output:**
```
Code Unit for Letter R: 77
```

---

## The [`codeUnits`](https://api.dart.dev/stable/2.7.2/dart-core/String/codeUnits.html) Property

This property provides an unmodifiable list of the UTF-16 _code unit(s)_ of this string.

```
  String myStr = "Mask";
  print("Code Units for word Mask: ${myStr.codeUnits}");

```

**Output:**
```
Code Units for word Mask: [77, 97, 115, 107]
```

---

## The [`runes`](https://api.dart.dev/stable/2.7.2/dart-core/String/runes.html) Property

This property returns the list of Unicode UTF-16 _code point(s)_ for the given string. In this case, code points are same as of code units. The `myStr.runes` returns the `Iterable<int>`.

```
  String myStr = "Mask";
  print("Runes for word Mask: ${myStr.runes}");
```

**Output:**

```
Runes for word Mask: (77, 97, 115, 107)
```

---

## Example

Let's use hex representation for word "Mask". Hex for "M" is "004D", "A" is "0061", "S" is "0073", and "K" is "006B".

```
//Representing Mask in hex
String hexStr = "\u004D\u0061\u0073\u006B";
print("From hex to String - maskStr: ${hexStr}");

Runes codeUnits = Runes(hexStr);
print("Code Units: ${codeUnits}");
print("Code Units To String: ${String.fromCharCodes(codeUnits)}");
```

**Output:**

```
From hex to String - maskStr: Mask
Code Units: (77, 97, 115, 107)
Code Units To String: Mask
```

---

## Example

Let's try another example to get `runes` for a symbol represented using 32-bit, using unicode character for [mask emoji](https://www.compart.com/en/unicode/U+1F637).

```
//Unicode character encoding : https://www.compart.com/en/unicode/U+1F637
//Decimal representation : 128567
String smileyMask = "\u{1F637}"; //needs 32 bit
print("Smiley with mask: ${smileyMask}");

// Prints Code Points for smiley with mask
print("Code Points in smily with mask: ${smileyMask.runes}");

//Printing String for code points
print(String.fromCharCodes(Runes(smileyMask)));
```

**Output:**

```
Smiley with mask: 😷
Code Points in smily with mask: (128567)
😷
```

---
# Companion Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/TODO" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
# Source Code

Please checkout the source code at Github [here](https://github.com/ptyagicodecamp/dart_vocab/blob/master/src/runes.dart)


---
# References

1. [Runes Class](https://api.dart.dev/stable/2.7.2/dart-core/Runes-class.html)
2. [String Class](https://api.dart.dev/stable/2.7.2/dart-core/String-class.html)
3. [String Class `runes` property](https://api.dart.dev/stable/2.7.2/dart-core/String/runes.html)
4. [Mask Face UTF-16](https://www.fileformat.info/info/unicode/char/1f637/index.htm)
5. [Character List for UTF-16](http://www.fileformat.info/info/charset/UTF-16/list.htm)
6. [Decimal to Hexadecimal converter](https://www.rapidtables.com/convert/number/decimal-to-hex.html)

Happy Darting :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave a comment or reach out at [twitter](https://twitter.com/ptyagi13) about the topics you would like me to share !

[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
