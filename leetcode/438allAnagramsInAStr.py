"""
438 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

思路：暴力，双指针滑动窗口

"""

from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        双指针滑动
        """
        lens, lenp = len(s), len(p)
        if lens < lenp:
            return []
        left, right = 0, 0
        needs = Counter(p)
        windows = Counter()

        res = []
        count = 0

        while right < lens:
            if s[right] in needs:
                windows.update(s[right])
            count += 1
            right += 1
            if count == lenp + 1:
                if s[left] in needs:
                    windows.subtract(s[left])
                left += 1
                count -= 1
            if windows == needs:
                res.append(left)
        return res





