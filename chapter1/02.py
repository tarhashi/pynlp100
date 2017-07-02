# -*- coding: utf-8 -*-
import functools
from operator import add

str1 = 'パトカー'
str2 = 'タクシー'

print(functools.reduce(add, functools.reduce(add, zip(str1, str2))))