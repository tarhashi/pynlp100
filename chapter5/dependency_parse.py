# -*- coding:utf-8 -*-

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f'surface:{self.surface}, base:{self.base}, pos:{self.pos}, pos1:{self.pos1}'

class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def __str__(self):
        return f'dst:{self.dst}, srcs:{self.srcs}'

    def surface(self):
        return ''.join([morph.surface for morph in self.morphs if morph.pos != '記号'])

    def is_include_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def find_pos(self, pos):
        return [morph for morph in self.morphs if morph.pos == pos]

    def is_include(self, pos=None, pos1=None, base=None):
        for morph in self.morphs:
            matched = True
            if pos is not None and morph.pos != pos:
                matched = False
            if pos1 is not None and morph.pos1 != pos1:
                matched = False
            if base is not None and morph.base != base:
                matched = False
            if matched:
                return True
        return False

    def find(self, pos=None, pos1=None, base=None):
        return [morph for morph in self.morphs if morph.pos == pos and morph.pos1 == pos1]

class DependencyParser:
    @classmethod
    def parse(cls, filepath):
        with open(filepath, 'r') as f:
            sentences = []
            chunks = []
            chunk = None
            for line in f.readlines():
                if line.strip() == 'EOS':
                    cls._set_srcs(chunks)
                    sentences.append(chunks)
                    chunks = []
                elif line[0] == '*':
                    chunk = cls._parse_chunk_header(line)
                    chunks.append(chunk)
                else:
                    chunk.morphs.append(cls._parse_morph(line))
        return sentences

    @staticmethod
    def _parse_morph(line):
        surface, x = line.split('\t', 1)
        data = x.split(',')
        return Morph(surface, data[6], data[0], data[1])

    @staticmethod
    def _parse_chunk_header(line):
        xs = line.split()
        dst = int(xs[2][:-1])
        return Chunk(dst=dst)

    @staticmethod
    def _set_srcs(chunks):
        for i in range(len(chunks)):
            chunk = chunks[i]
            if chunk.dst != -1:
                chunks[chunk.dst].srcs.append(i)