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
        dp
        状态：dpij为s1的前i个和s2的前j个跟s3的前i+j个是否匹配
        """
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False
        dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        dp[0][0] = True
        for j in range(len2):
            if dp[0][j] and s2[j] == s3[j]:
                dp[0][j + 1] = True
            else:
                break
        for i in range(len1):
            if dp[i][0] and s1[i] == s3[i]:
                dp[i + 1][0] = True
            else:
                break

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]
