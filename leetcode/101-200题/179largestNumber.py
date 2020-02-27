"""
179 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        1.转成字符排序
        """

        def gt(str1, str2):
            return str1 + str2 > str2 + str1

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            split_i = len(nums) // 2
            left_arr = mergeSort(nums[:split_i])
            right_arr = mergeSort(nums[split_i:])
            res = []
            left, right = 0, 0
            while left < len(left_arr) and right < len(right_arr):
                greater_than = gt(left_arr[left], right_arr[right])
                if greater_than:
                    res.append(left_arr[left])
                    left += 1
                else:
                    res.append(right_arr[right])
                    right += 1
            res = res + left_arr[left:] + right_arr[right:]
            return res

        nums = [str(num) for num in nums]
        sorted_nums = mergeSort(nums)

        # 以0开头证明这个数组都是0
        if sorted_nums[0] == '0':
            return '0'

        return ''.join(sorted_nums)


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution2:
    """
    利用sort的key属性
    """
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
