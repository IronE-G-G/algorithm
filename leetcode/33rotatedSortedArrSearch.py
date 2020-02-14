"""
33 搜索旋转排序数组（中等）
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

思路：二分法，
mid == target：
    return
mid != target:
    mid>=left (左边部分有序):
         根据target 是否落在左边，即有序的部分进行判断
    else(mid<left,=> mid<=right):
        右边有序
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        lens = len(nums)
        left = 0
        right = lens - 1
        while left <= right:
            mid = (left + right) // 2
            midValue = nums[mid]
            if midValue == target:
                return mid
            else:
                # 数组只有两个的时候midValue=坐标left的元素
                if midValue >= nums[left]:
                    if nums[left] <= target < midValue:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if midValue < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
