#!/bin/sh

. ./site.conf

search=$(
	find $POSTS -name draft |
	grep -E '[0-9]{14}'     |
	xargs grep "."          |
	sed \
		-e 's/\/draft:/:/' \
		-e 's/<[^>]*>//g' \
		-e '/.*:.*:/d' -e '/.*: *$/d')

echo "$search" | cut -d ':' -f 1 > cache/search.postname
echo "$search" | cut -d ':' -f 2- > cache/search.sentence
