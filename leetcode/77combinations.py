"""
77 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        回溯
        """
        nums = [i for i in range(1, n + 1)]
        res = []

        def backtrack(k, candidates, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(len(candidates)):
                backtrack(k, candidates[(i + 1):], path + [candidates[i]])

        backtrack(k, nums, [])

        return res
