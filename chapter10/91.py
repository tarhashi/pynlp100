# -*- coding:utf-8 -*-

with open('family.txt', 'w') as w:
    with open('questions-words.txt', 'r') as f:
        section = ''
        for line in f:
            if line[0] == ':':
                section = line.strip().split(' ', 1)[1]
            else:
                if section == 'family':
                    w.write(line)