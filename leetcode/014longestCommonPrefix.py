"""
最长公共前缀（简单）
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        common = strs[0]
        for candidate in strs[1:]:
            if not common:
                return ''
            common = self.findCommonStr(common, candidate)
        return common

    def findCommonStr(self, str1, str2):
        flag = -1
        minLen = min(len(str1), len(str2))
        for ind in range(minLen):
            if str1[ind] == str2[ind]:
                flag = ind
            else:
                break
        return str1[:(flag + 1)] if flag != -1 else ''
