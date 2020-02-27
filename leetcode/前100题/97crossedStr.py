"""
97 交错匹配
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        dp状态：dpij为s1前i个和s2前j个是不是为交错字符串
        转移
        dp[i][j] = (dp[i-1][j] and s1[i-1] == s2[i+j-1]) or (dp[i][j-1] and s2[j-1] == s2[i+j-1])

        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]
