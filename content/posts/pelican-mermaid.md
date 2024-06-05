How to embed Mermaid Diagrams in Pelican generated Blog Post

Recently, I've come across the need to embed Mermaid diagram in one of my blog post. In this blog post, I wanted to use [Mermaid diagram to show various Agile methodologies workflows](https://ptyagicodecamp.github.io/what-makes-scrumban-an-effective-agile-framework.html). 
I prefer writing my blog posts in Markdown. In case, you are intereseted in learning to setup your own Pelican generated blog that can be hosted using Github pages, checkout [my this blog post](https://ptyagicodecamp.github.io/my-take-on-pelican-and-github-pages-from-a-beginners-perspective.html).

I embeded HTML code in Markdown file as below. This is a two step process:

## Import `mermaid` library

In your markdown file, import `mermaid` library within `<script>` tags.

```<script type="module">import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';  </script>```

Initialize the library:

```
mermaid.initialize({ startOnLoad: true });
```

## Wrap `mermaid` code in `<pre>` tag

```
<pre class="mermaid">
graph TD;
    A[Product Backlog] --> B[Sprint Planning];
    B --> C[Sprint Backlog];
    C --> D[Development];
    D --> E[Daily Stand-up];
    D --> F[Sprint Review];
    F --> G[Product Increment];
    G --> H[Sprint Retrospective];
    H --> B;
</pre>
```

## Everything all together!

```
<script type="module"> import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs'; mermaid.initialize({ startOnLoad: true }); </script>
<pre class="mermaid">
graph TD;
    A[Product Backlog] --> B[Sprint Planning];
    B --> C[Sprint Backlog];
    C --> D[Development];
    D --> E[Daily Stand-up];
    D --> F[Sprint Review];
    F --> G[Product Increment];
    G --> H[Sprint Retrospective];
    H --> B;
</pre>
```
