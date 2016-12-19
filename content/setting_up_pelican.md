Title: My take on Pelican and Github pages from a beginner's perspective
Date: 2016-12-08 10:20
Authors: ptyagi
Category: Python
Tags: pelican 
Summary: This post is about my experience setting up githup pages using Pelican from scratch assuming no prior experience in Python webframeworks.


### Setting up environment:

1. First we need a pacakge manager to install necessery tools and packages. I chose Homebrew. Install Homebrew package manager and other needed tools for Mac by pasting this command in terminal:
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install wget`

2. Now, use Homebrew to install python, pip and other related tools. As time of this writing, it will install Python 2.7.12. 
`brew install python`

3. Setup  [vitutalenv tool](https://virtualenv.pypa.io/en/stable/) to keep python installations separate in their own sandbox: `pip install virtualenv`
  1. Creating virtualenv for pelican
    ```
    mkdir -p ~/virtualenvs
    cd ~/virtualenvs
    virtualenv pelican
    cd pelican
    source bin/activate
    ```

4. Install pelican: `pip install pelican`
5. Install markdown package: `pip install pelican markdown`


### Setting up github repos:

1. One repo for source code for blog generator: ptyagicodecamp.github.io-src
2. One repo for generated html blog contents: ptyagicodecamp.github.io


### Setting up Blog with Pelican:

1. Clone github source repo into your local working directory:
```
git clone https://github.com/ptyagicodecamp/ptyagicodecamp.github.io-src.git githubpages
cd githubpages
```

2. Create output directory inside `githubpages` directory to hold generated html pages to add it as a git submodule: `git submodule add https://github.com/ptyagicodecamp/ptyagicodecamp.github.io.git output`

3. Setup pelican : 
```
pelican-quickstart
> Where do you want to create your new web site? [.]
> What will be the title of this web site? **Title of your blog**   
> Who will be the author of this web site? **your name**
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
> What is your URL prefix? (see above example; no trailing slash) http://username.github.io
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] 	America/Mazatlan
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
Error: [Errno 17] File exists: '~/githubpages/content'
Error: [Errno 17] File exists: '~/githubpages/output'
Done. Your new project is available at ~/githubpages
```

Note: Make DELETE_OUTPUT_DIRECTORY = False in publishconf.py to NOT delete output dir, since its a submodule.


### Writing your first blog post:

Don't forget to install Markdown package: `pip install Markdown`. Also, don’t overlook that “.md” files needs meta-data at the beginning of file. Failing to do so, would give error that “NameTile” is failing. Meta data looks like this:
```
Title: My first title
Date: 2016-12-08 10:20
Modified: 2016-12-08 19:30
Category: Python
Tags: pelican, publishing
```
Now, write your first blog post by typing in terminal(or your faviorite editor) : `vi content/<post-name>.md`

Note: you're not required to use '.md' formatting, you can also use `.rst` formats too.


### Build, Commit and Push posts :

Note: if you run into issue that pelicanconf.py doesn't exist, its because you may not have python environment loaded. You would need to execute this on terminal re-activate environment: source ~/virtualenvs/pelican/bin/activate

1. To generate HTML contents and start local webserver, type this on terminal: 'make html && make serve`

2. Generate website using: `make publish`

3. Committing to Github:
At this point you can add all contents to github. 
To add submodule in output directory:
```
cd  output
git add .
git commit -m “Adding my contents”
git push -u origin master
cd ..
echo “*.pyc” >> .gitignore #you can also add this by manually editing .gitignore file
git add .
git commit -m “first commit”
git push -u origin master
```

### Visting your Brand new Blog

You can visit your blog at https://username.github.io


### Script to publish and push to github repo automatically:
I created `publish-n-push.sh` script to automate generating html contents and pushing everything to github:
```
echo "publising changes..."
make html && make publish
echo "pushing code to source repo..."
git add .
git commit -m "$1"
git push origin master
echo "pushing generated website to github"
cd output
git add .
git commit -m "$1"
git push origin master
cd ..
```

Using this script: 
```
cd githubpages
./publish-n-push.sh "commit-message"
```

### References
* Here's wonderful tutorial about [Markdown syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/) 
* I refered [this](https://fedoramagazine.org/make-github-pages-blog-with-pelican/) tutorial as a reference.













