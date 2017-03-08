#!/bin/bash
#find command to find files f is variable here which is holding all file names
#while loop is used here with condition read upto size of f as array
find . -name "*.png" | while read f
do
#variable is newname is assign value of f here f/old_extension/new_extension
    newname=${f/.png/.png}
#$f is to access data of f, similarly $newname for access data of newname
    convert "$f" -resize 50% "../resized1/$newname"
done
