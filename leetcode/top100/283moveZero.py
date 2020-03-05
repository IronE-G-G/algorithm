"""
283 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 冒泡 On2
        2 双指针，left指向第一个0，right指向left右边的第一个非0
        3 滚雪球
        """
        if len(nums) <= 1:
            return
        left, right = 0, 1
        N = len(nums)
        while left < N - 1:
            if nums[left] == 0:
                right = left + 1
                while right < N and nums[right] == 0:
                    right += 1
                if right == N:
                    break
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        return


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        3 滚雪球
        """
        ballsize = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ballsize += 1
            else:
                if ballsize == 0:
                    continue
                nums[i - ballsize] = nums[i]
                nums[i] = 0
