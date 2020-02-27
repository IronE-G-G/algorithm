"""
96 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        for k in range(2, n + 1):
            res = 0
            for iroot in range(1, k + 1):
                res += dp[iroot - 1] * dp[k - iroot]
            dp[k] = res
        return dp[-1]
