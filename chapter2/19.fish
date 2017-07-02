#!/usr/bin/env fish
cut -f 1 hightemp.txt | sort | uniq -c | sort -r -k 1