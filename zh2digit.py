# coding=utf-8

_zh2digit_base = dict(zip('零一二两三四五六七八九十百千万',
    [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]))
_carry = set('十百千万')

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
    digit = 0
    digit_sub = 0
    i = 0
    while i < len(zh):
        ch = zh[i]
        if ch in _zh2digit_base:
            if ch not in _carry:
                # 是一个数字，不是'万千百十'
                if ch != '零':
                    if i-1 >= 0 and zh[i-1] not in _carry:
                        # 解决'十三四'的问题, 保留最长的时间
                        digit_sub -= _zh2digit_base[zh[i-1]]
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
        else:
            # 其它字符
            raise ValueError("input should be in [零一二两三四五六七八九十百千万]")
        i += 1
    digit += digit_sub
    return digit