"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        dpi：前i个元素的解码方法总数
        初始化dp0=1，dp1=1

        """
        if not s:
            return 0
        if s[0] == '0':
            return 0

        dp = [1 for _ in range(len(s) + 1)]
        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                dp[i] = dp[i - 1]
                if s[i - 2] == '1' or (s[i - 2] == '2' and '0' < s[i - 1] < '7'):
                    dp[i] += dp[i - 2]
        return dp[-1]
