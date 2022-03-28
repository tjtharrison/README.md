#!/bin/bash

article_dir="articles"

echo "What would you like to name your article?"
read nice_name

echo "Creating new doc "$nice_name""

file_name=$(echo $nice_name | awk '{print tolower($0)}' | sed 's/ /_/'g)

echo "# $nice_name" > $article_dir/$file_name.md