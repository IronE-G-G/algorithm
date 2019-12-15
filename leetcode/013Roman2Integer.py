"""
罗马数转整数（简单）
思路：贪心算法，哈希索引
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romance = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = 0
        for ind, item in enumerate(romance):
            length = len(item)
            while s and s[:length] == item:
                res += integer[ind]
                s = s[length:]
        return res
