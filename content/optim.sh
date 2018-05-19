#!/bin/sh
find . -name "*-s.jpg" | xargs rm -v
find . -name "*.jpg" |
xargs -I{} sh -c '
  orig="{}";
  echo "{}";
  convert "$orig" -strip -resize 800x pnm:- |
  mozcjpeg -outfile "${orig%.jpg}-s.jpg"'
find . -name "*.png" |
xargs -I{} sh -c '
  orig="{}";
  echo "{}";
  convert "$orig" -strip -resize 800x pnm:- |
  mozcjpeg -outfile "${orig%.png}-s.jpg"'
