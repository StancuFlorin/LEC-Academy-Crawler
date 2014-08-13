#!/bin/bash

i=0
while read link; do

	i=$(( $i + 1 ))

	python GetLesson.py $link > temp
	vimeo="$(cat temp | sed -n 1p)"
	title="$(cat temp | sed -n 2p)"
	chapper="$(cat temp | sed -n 3p)"

	title="$i - $title"

	echo $vimeo
	echo $title
	echo $chapper

	mkdir -p "$chapper"
	cd "$chapper"

	./../DownloadVimeo.sh $vimeo "$title"

	cd ..

	echo "DONE" $i

done < $1
