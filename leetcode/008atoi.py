"""
 8.String to Integer (atoi)
 难度：中等
 请你来实现一个 atoi 函数，使其能将字符串转换成整数。

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # 标记起始位置
        start_flag = 0
        sign = 1  # 1 for positive
        res = 0
        MAX_VALUE = 2 ** 31 // 10
        MAX = 2 ** 31 - 1
        MIN = -(MAX + 1)
        for char in s:
            if start_flag == 0:
                # 跳过开头的空格
                if char == ' ':
                    continue
                # 正负符号处理
                elif char == '+':
                    start_flag = 1
                elif char == '-':
                    start_flag = 1
                    sign = -1
                # 开头即为数字
                elif '0' <= char <= '9':
                    start_flag = 1
                    res = int(char)
                # 开头不是有效整字符
                else:
                    return 0
            # 已经找到起始位置
            else:

                if '0' <= char <= '9':
                    pop = int(char)
                    if res < MAX_VALUE:
                        res = res * 10 + pop
                    elif res == MAX_VALUE and ((sign == 1 and pop < 8) or (sign == -1 and pop < 9)):
                        res = res * 10 + pop
                    else:
                        # 越界
                        return MAX if sign == 1 else MIN
                else:
                    break
        return res * sign
