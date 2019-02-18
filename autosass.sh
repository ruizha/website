#!/bin/bash

scss_dir="./static/scss"
css_dir="./static/css"
ext=".css"
for file in $scss_dir/*
do
    fname="${file%.*}"
    echo "sass $file $css_dir/$(basename $fname)$ext"
    sass $file $css_dir/$(basename $fname)$ext --style compressed
done
