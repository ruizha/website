#!/bin/bash

scss_dir="./static/scss"
css_dir="./static/css"
ext=".css"
for file in $scss_dir/*
do
    fname="${file%.*}"
    echo "scss $file $css_dir/$(basename $fname)$ext"
    scss $file $css_dir/$(basename $fname)$ext
done
