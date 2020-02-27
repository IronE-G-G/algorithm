"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。


所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

思路：回溯算法，dps
类似题目：找零钱
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        n = len(candidates)

        def search(i, total, path):
            if total == target:
                res.append(path)
                return
            if i == n:
                return
            # 第i个再用一遍
            for ind in range(i, n):
                if total + candidates[ind] > target:
                    break
                search(ind, total + candidates[ind], path + [candidates[ind]])

        search(0, 0, [])
        return res
