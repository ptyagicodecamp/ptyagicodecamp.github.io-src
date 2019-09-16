Title: Dart cheat-sheet for Kotlin (Android) developers
Date: 07/13/2019
Authors: ptyagi
Category: Flutter
Tags: Kotlin, Dart, Cross-platform, Flutter, Code-recipes, Android, Android Studio, iOS, development
Summary: Dart reference guide for Kotlin (Android) developers

This post is my effort to provide my fellow Kotlin developers a hand to pick up on Dart. Idea is to provide equivalent solution in both languages. The demonstrated code is not the only solution for a particular problem, but just one way of doing things. Style of article is to perform a task in both languages. For example, print "Hello World!" in Kotlin and Dart.

I've used [Kotlin Playground](https://play.kotlinlang.org) and [DartPad](https://dartpad.dartlang.org/) to run and play around with languages.

### Task: Print "Hello World" ###

**Kotlin:**
```
fun main() {
  println("Hello World")
}
```
_Output:_
```
Hello World
```

**Dart:**
```
void main() {
  print("Hello World");
}

```
_Output:_
```
Hello World
```
---

### Task: How to delete duplicates in a List ###

**Kotlin:**
```
fun main() {
  var myList = listOf('A', 'A', 'B', 'C', 'A', 'D', 'B', 'C')
  myList = myList.distinct()
  print(myList)
}
```
_Output:_
```
[A, B, C, D]
```

Another way in Kotlin. Note usage of `arrayOf()` instead `listOf`.
```
fun main() {
  val myList = arrayOf('A', 'A', 'B', 'C', 'A', 'D', 'B', 'C')
  val noDupsList = myList.distinct()
  print(noDupsList)
}
```
_Output:_
```
[A, B, C, D]
```

**Dart:**
```
//Delete duplicates from myList
void main() {
  var myList = ['A', 'A', 'B', 'C', 'A', 'D', 'B', 'C'];
  myList = Set.of(myList).toList();
  print(myList);
}
```
_Output:_
```
[A, B, C, D]
```

---

### Task:  ###

**Kotlin:**
```
```
_Output:_



**Dart:**
```
```

_Output:_

---

### Task:  ###

**Kotlin:**
```
```
_Output:_



**Dart:**
```
```

_Output:_

---
Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_

Follow me at [twitter](https://twitter.com/ptyagi13)
