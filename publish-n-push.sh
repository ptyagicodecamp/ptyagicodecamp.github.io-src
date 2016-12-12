#!/bin/bash

make publish
git add .
git commit -m "$1"
git push origin master
cd output
git add .
git commit -m "$1"
git push origin master
