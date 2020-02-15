# coding=utf-8


_zh2digit_base = dict(zip('零一二两三四五六七八九万千百十',
    [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10000, 1000, 100, 10]))
_carry = set('万千百十')

def to_digit(zh):
    """
    将用中文大写的数转换成阿拉伯数

    Args:
        zh: string

    Returns:
        A list, 包含zh中所有中文大写数转换后的数和其它部分
        e.g.

        zh = "有十五个月", 则返回['有', 15, '个月']
    """
    res = []
    i = 0
    while i < len(zh):
        if zh[i] in _zh2digit_base:
            # 提取中文大写数字
            digit = 0
            digit_sub = 0
            while i < len(zh) and zh[i] in _zh2digit_base:
                ch = zh[i]
                if ch not in _carry:
                    # 是一个数字，不是'万千百十'
                    if ch != '零':
                        digit_sub += _zh2digit_base[ch]
                elif digit_sub == 0:
                    # '万千百十'开头
                    digit_sub = _zh2digit_base[ch]
                    if ch != '十':
                        # '万千百'开头
                        digit += digit_sub
                        digit_sub = 0
                else:
                    # 一个数字后接'万千百十'
                    digit_sub *= _zh2digit_base[ch]
                    digit += digit_sub
                    digit_sub = 0
                i += 1
            digit += digit_sub
            res.append(digit)
        else:
            # 其它字符
            start = i
            while i < len(zh) and zh[i] not in _zh2digit_base:
                i += 1
            res.append(zh[start: i])
    return res
