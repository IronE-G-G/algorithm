"""
76 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

类似：3 无重复字符的最长子串，438 找到字符串中所有字母异位词
"""

from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        双指针滑动窗口+哈希表
        从左到右增加right
        while 符合条件：
            开始移动left（优化窗口）

        """
        if not t or not s:
            return ''
        needs = Counter(t)
        windows = Counter()
        left, right = 0, 0
        lens = len(s)
        res = ''
        minLen = lens + 1
        # 记录窗口所匹配上的字符种类
        match = 0
        while right < lens:

            if s[right] in needs:
                windows.update(s[right])
                if windows[s[right]] == needs[s[right]]:
                    match += 1
                while match == len(needs):

                    if right - left + 1 < minLen:
                        res = s[left:(right + 1)]
                        minLen = right - left + 1
                    if s[left] in windows:
                        windows.subtract(s[left])
                        if windows[s[left]] < needs[s[left]]:
                            match -= 1
                    left += 1
            right += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", 'ABC'))
