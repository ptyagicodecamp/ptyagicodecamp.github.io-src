Title: WebViewHelper Utility library
Date: 2016-12-16 3:06PM
Authors: ptyagi
Category: Android, WebView, library
Tags: android, webview, library
Summary: This post is about Opensource WebViewHelper library at [Github]{https://github.com/ptyagicodecamp/webview-android} 


### A little about WebView widgets:
Webview widget is used to display HTML contents in an Android app. HTML contents can be rendered in a TextView widget using Html.fromHtml() method to parse very basic text. So why do we need WebView widget ? WebView widget is capable of handling more advanced HTML tags, Javascript and CSS, which gives a native feel to HTML contents right in your app. But this doesn't come for free. WebViews are more memory intensive when compared to TextView widget.

### Background:
Pre Android 4.4, WebView was powered by WebKit. Starting Android 4.4, it’s powered by Chromium. Starting Android 5.0, WebView is distributed through Google Play Store. Starting Android 7.0, WebView uses Chrome browser app or System WebView app when Chrome browser is disabled.

Downside of newer implementation starting Android 5.0: Since System WebView implementation is distributed through Play Store and no more bundled in Android OS, its challenging for OEMs to keep their implementation of WebView in sync with Play Store’s System WebView. The two can go out of sync very quickly.

### Behaviors:
1. Any links embedded in a WebView widget will open in a WebView in Android 5.0 and over. 
2. On Android 4.4 and below, links embedded in a WebView will open in a Web Browser rather than in a WebView widget
3. By default, javascript is disabled in WebView widget. It can be turned on by `getSettings().setJavaScriptEnabled(true)`. I’ve created convenience class `WebViewHelper` around `android.webkit.WebView` class features.

### Using from Android Studio:
Add following in your project's `build.gradle` under `dependencies` block.
```
compile 'org.ptyagicodecamp:webview-android:0.0.1'
```

### How to use `WebViewHelper` class ?
1. Initializing: You would need to pass reference to `WebView` widget into `WebViewHelper` like this:
```
WebViewHelper webViewApi;
....

@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView = (WebView) findViewById(R.id.webView);
        //initialize WebViewHelper
        webViewApi = new WebViewHelper(webView);
    }
```

2. Use it !
```
public void loadUrl(View view) {
        webView.loadUrl("https://ptyagicodecamp.github.io/");
    }

    public void loadData(View view) {
        webViewApi.loadData("<html><a href=\"https://ptyagicodecamp.github.io/\">Click Here to visit my Blog</html>");
    }

    public void toggleJavaScript(View view) {

        if (((ToggleButton)view).isChecked()) {
            webViewApi.enableJS();
            Toast.makeText(this, "Javascript is enabled", Toast.LENGTH_LONG).show();
        } else {
            webViewApi.disableJS();
            Toast.makeText(this, "Javascript is disabled", Toast.LENGTH_LONG).show();
        }
    }
```

Source code is available [here]{https://github.com/ptyagicodecamp/webview-android}



