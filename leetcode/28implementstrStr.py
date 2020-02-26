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


class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        KMP 算法
        用next_i记录以i结尾的子串的前缀后缀匹配情况，
        比如说a a b a a,对于最后一个a，最长的可匹配前缀是a a，
        我们想记录的是这个可匹配前缀的下一个位置即b所在的位置
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        M, N = len(needle), len(haystack)
        if M > N:
            return -1
        if M == N:
            return 0 if haystack == needle else -1

        # 构建next数组
        next_dp = [0 for _ in range(M)]
        j = 0
        for i in range(1, M):
            if needle[i] == needle[j]:
                next_dp[i] = j + 1
                j += 1
            else:
                while j > 0:
                    # 在j的位置不匹配，但j-1位置之前一部分是匹配的，回退到可匹配前缀的下一个位置
                    j = next_dp[j - 1]
                    if needle[j] == needle[i]:
                        next_dp[i] = j + 1
                        j += 1
                        break
        # matching
        j = 0
        for i in range(N):
            if haystack[i] == needle[j]:
                j += 1
                if j == M:
                    return i + 1 - j
                    break
            else:
                while j > 0:
                    j = next_dp[j - 1]
                    if haystack[i] == needle[j]:
                        j += 1
                        break
        return -1