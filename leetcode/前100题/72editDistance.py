"""
72 编辑距离（困难）

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        dp
        状态：dp[i][j]代表word1前i个元素匹配word2前j个元素所需要的最小步数
        dp[0][0] = 0
        dp[0][j] = dp[0][j-1]+1：插入操作 j>0
        dp[i][0] = dp[i-1][0]+1: 删除操作 i>0

        word1[i-1] != word2[j-1]
        dp[i][j] = min(dp[i-1][j-1]（替换）, dp[i-1][j]（删除）,  dp[i][j-1]（插入）)
        """
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for j in range(1, len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            dp[i][0] = i
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]

