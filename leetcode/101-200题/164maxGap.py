"""
164 最大间距
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2 基数排序+遍历
        """
        if len(nums) <= 1:
            return 0
        max_value = max(nums)
        base = 1

        while max_value // base > 0:
            sort_arr = [[] for _ in range(10)]
            # 按基数分桶
            for i in range(len(nums)):
                to_i_arr = nums[i] // base % 10
                sort_arr[to_i_arr].append(nums[i])
            nums = []
            for i in range(len(sort_arr)):
                nums += sort_arr[i]
            base *= 10

        # find max gap
        max_gap = 0
        for i in range(len(nums) - 1):
            max_gap = max(max_gap, nums[i + 1] - nums[i])
        return max_gap


class Solution1(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        桶排序
        为什么是max-min？
        我觉得是因为桶的size是根据区间长度以及数组的长度去推算的，在假设数组的分布是最均匀的情况以及规定桶的size是左开右闭区间，所以在一开始算数组的区间长度的时候这个区间也是取左开右闭的，然后最后的一个数是单独给她分配一个桶。因为是左开右闭，所以才是用max-min
        从大家举例的 2 4 6 8 这个例子来看
        桶长度 6/3=2，(如果桶的长度不是整数的话可以向上取整，因为在取整数的情况下[0,1.5) 和[0,2)是一样的)
        桶数量 6/2+1（为8分配一个桶）
        """
        from math import ceil

        if len(nums) <= 1:
            return 0
        min_value = min(nums)
        max_value = max(nums)
        if max_value == min_value:
            return 0

        N = len(nums)
        bucket_size = ceil((max_value - min_value) / (N - 1))
        bucket_num = max(1, (max_value - min_value) // bucket_size) + 1
        # contained, min, max
        bucket_min_max = [[False, float('inf'), float('-inf')] for _ in range(bucket_num)]
        for i in range(len(nums)):
            bucker_i = (nums[i] - min_value) // bucket_size
            bucket_min_max[bucker_i][0] = True
            min_i, max_i = bucket_min_max[bucker_i][1:]
            bucket_min_max[bucker_i][1] = min(min_i, nums[i])
            bucket_min_max[bucker_i][2] = max(max_i, nums[i])

        res = 0
        # 第一个箱子有最小值
        prev_max = bucket_min_max[0][2]

        for i in range(1, bucket_num):
            if not bucket_min_max[i][0]:
                continue
            res = max(res, bucket_min_max[i][1] - prev_max)
            prev_max = bucket_min_max[i][2]

        return res
