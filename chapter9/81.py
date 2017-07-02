# -*- coding:utf-8 -*-
# 国名はここから取得
# http://www.benricho.org/translate/countrycode.html

countries = []
with open('countries.txt', 'r') as f:
    for line in f.readlines():
        c = line.strip()
        if len(c.split()) > 1:
            countries.append(c)
countries.sort(key=lambda x: len(x.split()), reverse=True)

with open('tokens2.txt', 'w') as w:
    with open('tokens.txt', 'r') as f:
        for line in f.readlines():
            for c in countries:
                line = line.replace(c, c.replace(' ', '_'))
            w.write(line)