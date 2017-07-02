#!/usr/bin/env fish
set line_count (cat hightemp.txt|wc -l|tr -d ' ')
set elm_count (expr $line_count / $argv[1])
split -l $elm_count hightemp.txt