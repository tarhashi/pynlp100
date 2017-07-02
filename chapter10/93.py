# -*- coding:utf-8 -*-
with open('family_result.txt') as f:
    total_lines = 0
    rights = 0
    for line in f:
        total_lines = total_lines + 1
        xs = line.strip().split()
        if xs[3] == xs[4]:
            rights = rights + 1
    print('{} ({}/{})'.format(rights / total_lines, rights, total_lines))