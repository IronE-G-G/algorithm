"""
340 至多包含k个不同字符的最长子串

给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        max_len = 0
        counter = 0
        lookup = dict()
        left, right = 0, 0
        while right < N:
            if s[right] not in lookup:
                lookup[s[right]] = 0
                counter += 1
            lookup[s[right]] += 1
            right += 1
            while counter > k:
                if lookup[s[left]] == 1:
                    counter -= 1
                    lookup.pop(s[left])
                else:
                    lookup[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
