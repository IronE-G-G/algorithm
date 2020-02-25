"""
153 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMin(self, nums) -> int:
        """
        binary search
        """
        if not nums:
            return
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                # 不越过去是为了保留逆序的部分
                left = mid
            elif nums[mid] == nums[left]:
                return min(nums[left], nums[right])
            else:
                right = mid
        return nums[left]


class Solution1:
    def findMin(self, nums) -> int:
        """
        binary search
        跟右边比比较简单
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]