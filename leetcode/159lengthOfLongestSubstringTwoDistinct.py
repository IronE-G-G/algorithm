"""
159 至多包含两个不同字符的最长子串
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

类似的双指针滑动窗口题目：
3 无重复字符的最长子串
76 最小覆盖子串
340 至多包含k个不同字符的最长子串

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        dpi：以i结尾的最长子串（长度，另外的那个字符最晚出现的坐标，没有用-1）
        """
        N = len(s)
        if N < 3:
            return N
        dp = [[1, -1] for _ in range(N)]
        res = 2
        for i in range(1, N):
            if s[i] == s[i - 1]:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]
            else:
                if dp[i - 1][1] == -1 or s[i] == s[dp[i - 1][1]]:
                    dp[i][0] = dp[i - 1][0] + 1
                    dp[i][1] = i - 1
                else:
                    dp[i][0] = i - dp[i - 1][1]
                    dp[i][1] = i - 1
            res = max(res, dp[i][0])
        return res

class Solution1:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        双指针，左开右闭
        :param s:
        :return:
        """
        lookup = dict()
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if s[end] not in lookup:
                counter+=1
                lookup[s[end]]=0
            lookup[s[end]]+=1
            end+=1
            while counter>2:
                if lookup[s[start]]==1:
                    counter-=1
                    lookup.pop(s[start])
                else:
                    lookup[s[start]]-=1
                start+=1
            max_len = max(max_len, end-start)
        return max_len

