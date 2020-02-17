# coding=utf-8

import unittest
from ddt import ddt, data, unpack
import zh2digit

cases = [
    {'zh': "有十五个月，七天，十周", 'result': ['有', 15, '个月，', 7, '天，', 10, '周']},
    {'zh': "有一千零十五个月", 'result': ['有', 1015, '个月']},
    {'zh': '二十三个', 'result': [23, '个']},
    {'zh': '十三四天', 'result': [14, '天']},
]

@ddt
class TestZh2Digit(unittest.TestCase):

    @data(*cases)
    @unpack
    def test(self, zh, result):
        res = zh2digit.to_digit(zh)
        self.assertEqual(res, result)


if __name__ == '__main__':
    unittest.main()
