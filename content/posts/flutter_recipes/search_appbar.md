Title: Implementing Search action in AppBar.
Date: 2019-02-06
Authors: ptyagi
Category: Development, Flutter, Cross-platform
Tags: SearchDelegate, SearchAppBar, flutter, code-recipes, android, android Studio, iOS
Summary: Implementing Search action in AppBar using Flutter for Android and iOS mobile apps.

## Search in AppBar
In today's recipe, I'll show you how search action can be
integrated at top of the page. I'll be using Flutter's [SearchDelegate](https://docs.flutter.io/flutter/material/SearchDelegate-class.html)
component to achieve this. It comes packed with support for populating suggestions in search bar,
adding actions items to the right side of the search bar. I'm using dart's library `english_words` to
populate the list of words.

***Target Audience:*** Beginner

***Recipe:*** Implementing Search action in AppBar using Flutter for Android and iOS mobile apps.

***Focus Widget:*** [SearchDelegate](https://docs.flutter.io/flutter/material/SearchDelegate-class.html)

***Goal:*** In this recipe, I'll show you :
1. How to populate sorted english word list in app and search for a given word using Search bar at the top of the application.
2. How to build suggestion list for search bar.
3. How to add actions like "clear" to reset search bar, and a dummy action "mic" for voice input.


![Sorted Wordlist]({attach}../../media/flutter/search_appbar/wordlist.png)
![Search in Wordlist]({attach}../../media/flutter/search_appbar/wordlist_search.png)

//TODO: Youtube video in action

### Lets's go! ###

Step #0: Create "Flutter Application" project in Android Studio.

Step #1. Get dependencies. First thing to add `english_words` dependency in
`pubspec.yaml` to be able to populate English words in our recipe app's word list.
```
dependencies:
  flutter:
    sdk: flutter
  # This is needed to populate English words in app's word list.
  english_words: ^3.1.3
```

Step #2. Display Word list 
To display English word list as list in app, first thing is to import the dependency in `main.dart` file:
```
import 'package:english_words/english_words.dart' as words;
```

Step #3. Initialize word list in `SearchAppBarRecipeState` class.
Now, in the `_SearchAppBarRecipeState` class, fetch the list of words like below. Make sure
that you've a list data structure to hold word list. I'm using `kWords` for this purpose.
```
class _SearchAppBarRecipeState extends State<SeachAppBarRecipe> {
  //Data structure to hold word list
  final List<String> kWords;
  
  ...

    //Initializing kWords list with data fetched from english_words library
  _SearchAppBarRecipeState()
      : kWords = List.from(Set.from(words.all)),
        super();
        
  ...
}
```

Step #4. Sorting word list.
You'll notice at this point that data is un-sorted at this point. 
Let's make it alphabetically sorted as below:
```
class _SearchAppBarRecipeState extends State<SeachAppBarRecipe> {
  final List<String> kWords;
  ...

  //Initializing with sorted list of english words
  _SearchAppBarRecipeState()
      : kWords = List.from(Set.from(words.all))
    ..sort(
          (w1, w2) => w1.toLowerCase().compareTo(w2.toLowerCase()),
    ),
        super();
   ...
}
```

Step #5. Setup `SearchDelegate` to implement Search AppBar.
Search delegate is where all the magic happens. It holds two list of words. One list is of
the general word list passed during initialization. Another list `_history` contains the list of history words.
You can pre-populate `_history` list to give a baseline for history search items. This list will be shown when
user clicks on the search bar.
```
class _SearchAppBarDelegate extends SearchDelegate<String> {
  //list holds the full word list
  final List<String> _words;
  
  //list holds history search words.
  final List<String> _history;

    //initialize delegate with full word list and history words
  _SearchAppBarDelegate(List<String> words)
      : _words = words,
  //pre-populated history of words
        _history = <String>['apple', 'orange', 'banana', 'watermelon'],
        super();
        
  ...
}
``` 

Step #6. After setting up words list options in delegate, now its time to pick up an icon that will be placed at the
left side of search bar. Mostly, this icon menu is meant for navigating back to previous screen.
```
class _SearchAppBarDelegate extends SearchDelegate<String> {
  ...
  
    // Setting leading icon for the search bar.
    //Clicking on back arrow will take control to main page
    @override
    Widget buildLeading(BuildContext context) {
      return IconButton(
        tooltip: 'Back',
        icon: AnimatedIcon(
          icon: AnimatedIcons.menu_arrow,
          progress: transitionAnimation,
        ),
        onPressed: () {
          //Take control back to previous page
          this.close(context, null);
        },
      );
    }
        
  ...
}
``` 

Alright we got the icon for search bar ! What next ? 

Step #7. Now it's time to implement `buildResults` method to show searched item. This is where search query `this.query` will
display searched item. For sake of simplicity, I'll be adding two widgets only.
First widget is `Text` and will display message '===Your Word Choice==='. Second widget is
`GestureDetector` which has it's another `Text` widget as its `child`. Tapping on the `Text` widget will
take control back to previous page along with `this.query` parameter to display the searched word in main page.
```
class _SearchAppBarDelegate extends SearchDelegate<String> {
  ...
  
  //Builds page to populate search results.
  @override
  Widget buildResults(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Text('===Your Word Choice==='),
            GestureDetector(
              onTap: () {
                //Define your action when clicking on result item.
                //In this example, it simply closes the page
                this.close(context, this.query);
              },
              child: Text(
                this.query,
                style: Theme.of(context)
                    .textTheme
                    .display2
                    .copyWith(fontWeight: FontWeight.normal),
              ),
            ),
          ],
        ),
      ),
    );
  }
        
  ...
}
```

Step #8. Next, it's time for implementing `buildSuggestions` method of SearchDelegate class. 
So, what does building suggestions mean ? This is the list of suggestions for words that you'll see
when typing your search query in search bar. There're two parts of this. 
First, we've to pass the list of words that could be displayed as suggestions. 
Second, we need to implement the UI widget to display this suggestion list.

For data part, we display pre-populated history words when query term is empty. When user
starts typing then we show all the words that starts with search terms entered in search bar. That's it !
```
class _SearchAppBarDelegate extends SearchDelegate<String> {
  ...
  
  // Suggestions list while typing search query - this.query.
  @override
  Widget buildSuggestions(BuildContext context) {
    final Iterable<String> suggestions = this.query.isEmpty
        ? _history
        : _words.where((word) => word.startsWith(query));
        
        ...
  }
        
  ...
}
```

It's UI widget's turn now. As you can see `buildSuggestions` method returns a `Widget`.
We'll make a separate class say `_WordSuggestionList` to populate suggestion list widget and will
return it from `buildSuggestions`.
`_WordSuggestionList` is going to be a `StatelessWidget`, and has three things: First, list of suggestions.
Second, search query and last a callback say `ValueChanged<String> onSelected`. It'll be `ListView`
of size of number of suggestions provided. Each suggestion is displayed in `ListTile` widget. This widget will show
`history` icon for items fetched from pre-populated history words only. Text for widget will be updated as user is typing the search query.
```
class _WordSuggestionList extends StatelessWidget {
  const _WordSuggestionList({this.suggestions, this.query, this.onSelected});

  final List<String> suggestions;
  final String query;
  final ValueChanged<String> onSelected;

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme.subhead;
    return ListView.builder(
      itemCount: suggestions.length,
      itemBuilder: (BuildContext context, int i) {
        final String suggestion = suggestions[i];
        return ListTile(
          leading: query.isEmpty ? Icon(Icons.history) : Icon(null),
          // Highlight the substring that matched the query.
          title: RichText(
            text: TextSpan(
              text: suggestion.substring(0, query.length),
              style: textTheme.copyWith(fontWeight: FontWeight.bold),
              children: <TextSpan>[
                TextSpan(
                  text: suggestion.substring(query.length),
                  style: textTheme,
                ),
              ],
            ),
          ),
          onTap: () {
            onSelected(suggestion);
          },
        );
      },
    );
  }
}

```

Let's plug-in `_WordSuggestionList` back into `buildSuggestions` method:
```
class _SearchAppBarDelegate extends SearchDelegate<String> {
  ...
  
  // Suggestions list while typing search query - this.query.
  @override
  Widget buildSuggestions(BuildContext context) {
    final Iterable<String> suggestions = this.query.isEmpty
        ? _history
        : _words.where((word) => word.startsWith(query));
        
    //calling wordsuggestion list    
    return _WordSuggestionList(
          query: this.query,
          suggestions: suggestions.toList(),
          onSelected: (String suggestion) {
            this.query = suggestion;
            this._history.insert(0, suggestion);
            showResults(context);
          },
  }
        
  ...
}
```

Step #9. Building actions in SearchBar.
Last step is to add action menus in SearchBar's right side. I'll be adding two menu actions.
One is "Clear" icon to clear search query from search bar. Another is a "mic" icon, that could be
improved to accept voice input, which is beyond the scope of this recipe. However, if you would like me 
to write about another recipe for accepting voice input, feel free to contact me as mentioned at the end of this post.
```
class _SearchAppBarDelegate extends SearchDelegate<String> {
  ...
  
// Action buttons at the right of search bar.
  @override
  List<Widget> buildActions(BuildContext context) {
    return <Widget>[
      query.isNotEmpty ?
      IconButton(
        tooltip: 'Clear',
        icon: const Icon(Icons.clear),
        onPressed: () {
          query = '';
          showSuggestions(context);
        },
      ) : IconButton(
        icon: const Icon(Icons.mic),
        tooltip: 'Voice input',
        onPressed: () {
          this.query = 'TBW: Get input from voice';
        },

      ),
    ];
  }
        
  ...
}
```

Step #10. Finally, call Search Delegate from `SearchAppBarRecipeState`.
After creating `SearchDelegate` class, call it from `_SearchAppBarRecipeState` class and initialize it in `initState`.
```
class _SearchAppBarRecipeState extends State<SeachAppBarRecipe> {
    final List<String> kWords;
    
    //Calling search delegate class
    _SearchAppBarDelegate _searchDelegate;
    ...
    
    @override
    void initState() {
       super.initState();
       //Initializing search delegate with sorted list of English words
       _searchDelegate = _SearchAppBarDelegate(kWords);
    }
    
    ...
}
```

That's it !

####Complete example code ####
```
import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart' as words;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SeachAppBarRecipe',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: SeachAppBarRecipe(title: 'SeachAppBarRecipe'),
    );
  }
}

class SeachAppBarRecipe extends StatefulWidget {
  SeachAppBarRecipe({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _SearchAppBarRecipeState createState() => _SearchAppBarRecipeState();
}

class _SearchAppBarRecipeState extends State<SeachAppBarRecipe> {
  final List<String> kWords;
  _SearchAppBarDelegate _searchDelegate;

  //Initializing with sorted list of english words
  _SearchAppBarRecipeState()
      : kWords = List.from(Set.from(words.all))
    ..sort(
          (w1, w2) => w1.toLowerCase().compareTo(w2.toLowerCase()),
    ),
        super();


  @override
  void initState() {
    super.initState();
    //Initializing search delegate with sorted list of English words
    _searchDelegate = _SearchAppBarDelegate(kWords);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Text('Word List'),
        actions: <Widget>[
          //Adding the search widget in AppBar
          IconButton(
            tooltip: 'Search',
            icon: const Icon(Icons.search),
            //Don't block the main thread
            onPressed: () {
              showSearchPage(context, _searchDelegate);
            },
          ),
        ],
      ),
      body: Scrollbar(
        //Displaying all English words in list in app's main page
        child: ListView.builder(
          itemCount: kWords.length,
          itemBuilder: (context, idx) =>
              ListTile(
                title: Text(kWords[idx]),
                onTap: () {
                  Scaffold.of(context).showSnackBar(
                      SnackBar(
                          content: Text("Click the Search action"),
                          action: SnackBarAction(
                            label: 'Search',
                            onPressed: (){
                              showSearchPage(context, _searchDelegate);
                            },
                          )
                      )
                  );
                },
              ),
        ),
      ),
    );
  }

  //Shows Search result
  void showSearchPage(BuildContext context,
      _SearchAppBarDelegate searchDelegate) async {
    final String selected = await showSearch<String>(
      context: context,
      delegate: searchDelegate,
    );

    if (selected != null) {
      Scaffold.of(context).showSnackBar(
        SnackBar(
          content: Text('Your Word Choice: $selected'),
        ),
      );
    }
  }
}

//Search delegate
class _SearchAppBarDelegate extends SearchDelegate<String> {
  final List<String> _words;
  final List<String> _history;

  _SearchAppBarDelegate(List<String> words)
      : _words = words,
  //pre-populated history of words
        _history = <String>['apple', 'orange', 'banana', 'watermelon'],
        super();

  // Setting leading icon for the search bar.
  //Clicking on back arrow will take control to main page
  @override
  Widget buildLeading(BuildContext context) {
    return IconButton(
      tooltip: 'Back',
      icon: AnimatedIcon(
        icon: AnimatedIcons.menu_arrow,
        progress: transitionAnimation,
      ),
      onPressed: () {
        //Take control back to previous page
        this.close(context, null);
      },
    );
  }

  // Builds page to populate search results.
  @override
  Widget buildResults(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Text('===Your Word Choice==='),
            GestureDetector(
              onTap: () {
                //Define your action when clicking on result item.
                //In this example, it simply closes the page
                this.close(context, this.query);
              },
              child: Text(
                this.query,
                style: Theme.of(context)
                    .textTheme
                    .display2
                    .copyWith(fontWeight: FontWeight.normal),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Suggestions list while typing search query - this.query.
  @override
  Widget buildSuggestions(BuildContext context) {
    final Iterable<String> suggestions = this.query.isEmpty
        ? _history
        : _words.where((word) => word.startsWith(query));

    return _WordSuggestionList(
      query: this.query,
      suggestions: suggestions.toList(),
      onSelected: (String suggestion) {
        this.query = suggestion;
        this._history.insert(0, suggestion);
        showResults(context);
      },
    );
  }

  // Action buttons at the right of search bar.
  @override
  List<Widget> buildActions(BuildContext context) {
    return <Widget>[
      query.isNotEmpty ?
      IconButton(
        tooltip: 'Clear',
        icon: const Icon(Icons.clear),
        onPressed: () {
          query = '';
          showSuggestions(context);
        },
      ) : IconButton(
        icon: const Icon(Icons.mic),
        tooltip: 'Voice input',
        onPressed: () {
          this.query = 'TBW: Get input from voice';
        },

      ),
    ];
  }
}

// Suggestions list widget displayed in the search page.
class _WordSuggestionList extends StatelessWidget {
  const _WordSuggestionList({this.suggestions, this.query, this.onSelected});

  final List<String> suggestions;
  final String query;
  final ValueChanged<String> onSelected;

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme.subhead;
    return ListView.builder(
      itemCount: suggestions.length,
      itemBuilder: (BuildContext context, int i) {
        final String suggestion = suggestions[i];
        return ListTile(
          leading: query.isEmpty ? Icon(Icons.history) : Icon(null),
          // Highlight the substring that matched the query.
          title: RichText(
            text: TextSpan(
              text: suggestion.substring(0, query.length),
              style: textTheme.copyWith(fontWeight: FontWeight.bold),
              children: <TextSpan>[
                TextSpan(
                  text: suggestion.substring(query.length),
                  style: textTheme,
                ),
              ],
            ),
          ),
          onTap: () {
            onSelected(suggestion);
          },
        );
      },
    );
  }
}
```


***Source code repo:***
Recipe source code is available [here](https://github.com/ptyagicodecamp/flutter_cookbook/tree/master/search_appbar)


### References: ###
1. [Search Delegate](https://docs.flutter.io/flutter/material/SearchDelegate-class.html)
2. [Flutter Gallery](https://github.com/flutter/flutter/blob/master/examples/flutter_gallery/lib/demo/material/search_demo.dart)
3. [BuildActions](https://docs.flutter.io/flutter/material/SearchDelegate/buildActions.html)
4. [BuildResults]('https://docs.flutter.io/flutter/material/SearchDelegate/buildResults.html)

Happy cooking with Flutter :)

_Liked the article ?
Couldn't find a topic of your interest ? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write !
[BTW I love cupcakes and coffee both :)](https://www.paypal.me/pritya)_