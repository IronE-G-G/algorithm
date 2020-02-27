"""
128 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        对当前数字-1不在哈希表中的数字进行寻找，如果当前数字-1在哈希表中，那么当前数字所在的最长序列肯定不是以当前数字开头的
        """
        if len(nums) <= 1:
            return len(nums)
        numset = set(nums)
        maximun = 1
        for num in nums:
            if num - 1 not in numset:
                current_num = num
                total = 1
                while current_num + 1 in numset:
                    current_num += 1
                    total += 1
                maximun = max(maximun, total)
        return maximun


class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序
        """
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        maxinum = 1
        pre = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                maxinum = max(pre + 1, maxinum)
                pre += 1
            else:
                pre = 1
        return maxinum
