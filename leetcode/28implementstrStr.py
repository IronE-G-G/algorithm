"""
28 实现strStr（）
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        N = len(haystack)
        matchN = len(needle)
        for ind in range(N - matchN + 1):
            if haystack[ind:ind + matchN] == needle:
                return ind
        return -1

        # 直接调用python的str类里面的函数
        # return haystack.find(needle)
