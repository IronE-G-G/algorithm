"""
75 颜色分类

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        排序计数

        """
        num0, num1, num2 = 0, 0, 0
        for num in nums:
            if num == 0:
                num0 += 1
            elif num == 1:
                num1 += 1
            else:
                num2 += 1
        for i in range(len(nums)):
            if i < num0:
                nums[i] = 0
            elif i < num0 + num1:
                nums[i] = 1
            else:
                nums[i] = 2


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        前后指针
        """
        p0, cur, p2 = 0, 0, len(nums) - 1
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1

            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1
        return nums


