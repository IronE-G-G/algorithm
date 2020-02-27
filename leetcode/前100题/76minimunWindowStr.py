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
        双指针滑动窗口

        """
        needed = Counter(t)
        needed_N = len(needed)
        windows = Counter()
        satisfy = 0
        left, right = 0, 0
        min_str = ''
        min_len = len(s) + 1
        while right < len(s):
            if s[right] in needed:
                windows[s[right]] += 1
                # 不需要特地记录满足条件的字母是谁，因为取了等号
                if windows[s[right]] == needed[s[right]]:
                    satisfy += 1
            right += 1
            while satisfy == needed_N:
                if right - left < min_len:
                    min_len = right - left
                    min_str = s[left:right]
                if s[left] in windows:
                    windows[s[left]] -= 1
                    if windows[s[left]] < needed[s[left]]:
                        satisfy -= 1
                left += 1

        return min_str


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", 'ABC'))
