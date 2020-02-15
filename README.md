# 中文数字转换器

将中文大写数字书写的数转换成阿拉伯数。

## 使用说明

```python
import zh2digit

zh = '有二十三个月，十周，四天'

res = zh2digit.to_digit(zh)

# res = ['有', 23, '个月，', 10, '周，', 4, '天']
```
