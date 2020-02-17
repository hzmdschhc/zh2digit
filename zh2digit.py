# coding=utf-8

_base = dict(zip('一二两三四五六七八九', [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]))
_carry = dict(zip('十百千万', [10, 100, 1000, 10000]))

def _transform_base(zh):
    """
    标准中文大写数转换成阿拉伯数
    标准:
        1. '十百千万'前有基本数字
        2. 没有'零'
        3. 没有两个基本数字连续出现的情况
        4. 基本数字在[一二两三四五六七八九]范围内
    """
    def transform_in_10k(text):
        """转换一万以内的标准中文大写数"""
        digit = 0
        digit_sub = 0
        for ch in text:
            if ch in _base:
                digit_sub += _base[ch]
            elif ch in _carry:
                digit_sub *= _carry[ch]
                digit += digit_sub
                digit_sub = 0
            else:
                raise ValueError(F"'{ch}' not in [一二两三四五六七八九十百千万]")
        digit += digit_sub
        return digit

    subs = zh.split('万')
    digit = 0
    for index, sub in enumerate(subs):
        digit_sub = transform_in_10k(sub)
        digit += digit_sub * (10000 ** (len(subs) - index - 1))
    return digit


def transform(zh):
    """
    将用中文大写的数转换成阿拉伯数, 支持最多到99999

    Args:
        zh: string, 包含的字符应在[零一二两三四五六七八九十百千万]范围内

    Returns:
        int, 转换之后的阿拉伯数
        e.g.

        zh = "十五", 则返回15
    """
    # standard
    if len(zh) > 0 and zh[0] in _carry:
        # 十 -> 一十, 百 -> 一百
        zh = '一' + zh
    zh = zh.replace('零', '')

    bag = []
    previous_is_base = False
    for ch in zh:
        if ch in _base:
            if previous_is_base:
                # 前一个字符也是基本数字, 则丢弃掉上一个数字
                bag.pop()
            bag.append(ch)
            previous_is_base = True
        elif ch in _carry:
            bag.append(ch)
            previous_is_base = False
        else:
            # 其它字符，直接忽略
            pass
    zh = ''.join(bag)
    digit = _transform_base(zh)
    return digit