# -*- coding:utf-8 -*-
# stop words from
# http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/English.txt
from stop_words import is_stopword
import unittest


class StopwordTest(unittest.TestCase):
    def test_is_stopword(self):
        self.assertTrue(is_stopword('a', ['a', 'the']))
        self.assertFalse(is_stopword('radio', ['a', 'the']))

if __name__ == '__main__':
    unittest.main()