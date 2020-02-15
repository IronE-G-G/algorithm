"""
40 组合总和 ii （中等）
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        n = len(candidates)

        def search(i, total, candidates, path):
            if total == target and path not in res:
                res.append(path)
                return
            if i == n:
                return
            for ind in range(i, n):
                if total + candidates[i] > target:
                    break
                # 剪枝
                if ind > i and candidates[ind] == candidates[ind - 1]:
                    continue
                search(ind + 1, total + candidates[ind], candidates, path + [candidates[ind]])

        search(0, 0, candidates, [])
        return res
