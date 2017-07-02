# -*- coding:utf-8 -*-
import re

class NLP:
    @staticmethod
    def get_lines(filepath):
        lines = []
        with open(filepath, 'r') as f:
            split_pattern = re.compile(r'[?.;:!]\s+?(?=[A-Z])')
            end_pattern = re.compile(r'[?.;:!]?\s+?$')
            for line in f.readlines():
                if line == '\n':
                    continue
                lines = lines + [re.sub(end_pattern, '', line) for line in split_pattern.split(line)]
        return lines

    @staticmethod
    def get_words(line):
        return [re.sub('[,]+$', '', word) for word in re.split(r'\s+', line)]