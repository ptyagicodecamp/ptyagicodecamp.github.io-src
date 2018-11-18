#!/bin/bash

source ~/virtualenvs/pelican/bin/activate
echo "generating contents and publishing..."
make html && make publish
echo "pushing code to source repo..."
git add .
git commit -m "$1"
git fetch origin master
git push origin master
echo "pushing generated website to github"
cd output
git add .
git commit -m "$1"
git push origin master
cd ..
echo "updating submodule"
git add .
git commit -m "updating submodule info"
git push origin master
