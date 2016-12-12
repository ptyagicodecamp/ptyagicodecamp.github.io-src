#!/bin/bash

echo "publising changes..."
make publish
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
