"""
从1到n整数中1出现的次数
思路：
拿2120举例：
固定个位（0）为1，则其他三位的取法有0-211一共212种
固定十位（2）为1，则其他三位的取法有左边（0-21）22种*右边（0-9）10种。
固定百位（1）为1，则其他三位的取法有左边（0-1）2种*右边（00-99）100种+21种（2100-2120）
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        base = 1
        res = 0
        while n >= base:
            low_part = n % base
            high_part = n // base
            if high_part % 10 == 0:
                res += high_part // 10 * base
            elif high_part % 10 == 1:
                res += high_part // 10 * base + low_part + 1
            else:
                res += (high_part // 10 + 1) * base
            base = base * 10
        return res
        # write code here
