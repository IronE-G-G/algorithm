"""
整数转罗马数字
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

贪心算法，数字，字符串
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romance = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        for ind, item in enumerate(integer):
            while num >= item:
                res = res + romance[ind]
                num -= item
        return res
