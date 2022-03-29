#!/bin/bash

page_dir="pages"

echo "What would you like to name your page?"
read nice_name

echo "What type of page is this?"
IFS=$'\n'; select doc_type in $(ls -d $page_dir/* | sed 's/pages\///g')
do
    if [[ ! $doc_type ]]; then
        echo "Please select a valid type!"
    else
        echo "$doc_type selected"
        break
    fi
done

echo "Creating new doc "$nice_name" in $doc_type"

file_name=$(echo $nice_name | awk '{print tolower($0)}' | sed 's/ /_/'g)

echo "# $nice_name" > $page_dir/$doc_type/$file_name.md
echo >> $page_dir/$doc_type/$file_name.md

if [[ -f $page_dir/$doc_type/.template ]]; then
    echo "Template located in $doc_type, importing.."
    cat $page_dir/$doc_type/.template >> $page_dir/$doc_type/$file_name.md
    echo "Done!"
fi