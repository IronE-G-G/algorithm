"""
44 通配符匹配（困难）
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。


这道题不比正则化匹配的那道，单纯的*号匹配会比（字母+*）有更多种可能，
递归写容易超出时间限制。

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        状态：dpij：s前i个元素跟p前j个元素的匹配
        转移：
        dp00 = True，
        dp0i 判断p为连续*的情况
        for i in 。。
            for j in 。。
                if pj=si or pj='?'
                    dp[i+1][j+1] = dp[i][j]
                elif pj = '*'
                    dp[i+1][j+1] = (匹配) dp[i][j+1] or dp[i+1][j] (匹配空串)

        """
        if not p and not s:
            return True
        if not p and s:
            return False
        pLen = len(p)
        sLen = len(s)
        dp = [[False for _ in range(pLen + 1)] for _ in range(sLen + 1)]
        dp[0][0] = True

        for j in range(pLen):
            if p[j] == '*':
                dp[0][j + 1] = dp[0][j]
            else:
                break

        for i in range(sLen):
            for j in range(pLen):
                if p[j] == '?' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]
        return dp[-1][-1]







