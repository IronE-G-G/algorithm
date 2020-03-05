"""
416 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    res = False

    def canPartition(self, nums: List[int]) -> bool:
        """
        转化成求数组中的某些元素的和为特定值
        背包问题 dfs+剪枝不能过 换动态规划, 感觉更像BFS
        存储[0,i-1]区间选择一些元素和的结果
        """
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        nums.sort(reverse=True)
        pre_lookup = set([0])
        for i in range(len(nums)):
            if nums[i] == target:
                return True
            if nums[i] > target:
                continue
            now_lookup = set()
            now_lookup.update(pre_lookup)
            for item in pre_lookup:
                if item + nums[i] == target:
                    return True
                if item + nums[i] < target:
                    now_lookup.add(item + nums[i])
            pre_lookup = now_lookup
        return False
