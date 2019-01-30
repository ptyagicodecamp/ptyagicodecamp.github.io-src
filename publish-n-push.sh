#!/bin/bash

source ~/virtualenvs/pelican/bin/activate
echo "generating contents and publishing..."
make html && make publish
echo "pushing code to source repo..."
git add .
git commit -m "publishing new content"
git push origin master
echo "pushing generated website to github"
cd output
git add .
git commit -m "publishing output html"
git push origin master
cd ..
echo "updating submodule"
git add .
git commit -m "updating submodule info"
git push origin master
