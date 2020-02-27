"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

思路：递归
"""


class Solution:
    dd = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        return self.combine(digits, [''])

    def combine(self, digits, paths):
        if not digits:
            return paths
        newPaths = []
        for path in paths:
            for char in self.dd[digits[0]]:
                newPaths.append(path + char)
        return self.combine(digits[1:], newPaths)
