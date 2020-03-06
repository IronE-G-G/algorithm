"""
581 最短无序连续子数组
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        排序后比较
        """
        left, right = len(nums), 0
        sorted_num = sorted(nums)
        for i in range(len(nums)):
            if nums[i]!=sorted_num[i]:
                left=min(left, i)
                right = max(right, i)
        return right-left+1 if right-left>0 else 0


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        栈方法找最左边界和最右边界
        """
        if len(nums) == 1:
            return 0
        stack = []
        left = len(nums)
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                left = min(left, stack[-1])
                stack.pop()
            stack.append(i)

        stack = []
        right = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack[-1])
                stack.pop()
            stack.append(i)
        return 0 if right - left < 0 else right - left + 1



