"""
162 寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        大于左边也大于右边
        """
        if not nums:
            return
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i + 1]:
                return 0
            if i == len(nums) - 1 and nums[i] > nums[i - 1]:
                return i
            if 0 < i < len(nums) - 1 and nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
