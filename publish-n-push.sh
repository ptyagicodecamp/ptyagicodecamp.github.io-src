#!/bin/bash

echo "generating contents and publishing..."
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
git add .
git commit -m "$1"
git push origin master
