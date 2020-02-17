# 中文数字转换器

将中文大写数字书写的数转换成阿拉伯数

## 使用说明

输入的字符应该在[零一二两三四五六七八九十百千万]的范围之内
支持的最大数为九万九千九百九十九

```python
import zh2digit

zh = '二十三'
res = zh2digit.to_digit(zh) # res = 23

zh = '十二三'
res = zh2digit.to_digit(zh) # res = 13, 只保留最大的时间
```
