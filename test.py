# coding=utf-8

import unittest
from ddt import ddt, data, unpack
import zh2digit

cases = [
    {'zh': "二十三", 'result': 23},
    {'zh': "十五", 'result': 15},
    {'zh': "百五", 'result': 105},
    {'zh': "一千零五十", 'result': 1050},
    {'zh': "十二三", 'result': 13},
    {'zh': "九万九千九百九十九", 'result': 99999},
]

@ddt
class TestZh2Digit(unittest.TestCase):

    @data(*cases)
    @unpack
    def test(self, zh, result):
        res = zh2digit.transform(zh)
        self.assertEqual(res, result)


if __name__ == '__main__':
    unittest.main()
