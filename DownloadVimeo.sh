#!/bin/sh

url="$(curl --referer http://www.lec-academy.ro $1 | grep -o -P '(?<=\"url":").*(?=\","height":)')"
wget -O "$2.mp4" $url