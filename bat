#!/usr/bin/env zsh
# -*- coding:utf-8 -*-

function conv(){
    local md=$1
    local html=`basename $md`
    local html=${html/.md/.html}
    local prefix=""

    if [ "$2" != "" ]; then
	prefix="-T $2"
    fi
    echo "$md -> $html"
    ./filter.rb < $md \
	| pandoc -s -t html5 -c github.css -o $html \
		 $prefix \
		 -H template/header.html \
		 -B template/before_body.html \
		 -A template/after_body.html
}

conv markdown/index.md
conv markdown/widget.md "Widget全般"
conv markdown/place.md "配置"
conv markdown/event.md "イベント"
conv markdown/label.md "Label Widget"
conv markdown/message.md "Message Widget"
conv markdown/button.md "Button Widget"

\rm -f **/*~ *~

