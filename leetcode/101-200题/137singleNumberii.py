"""
137 只出现一次的数字ii
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos, three = 0, 0, 0
        for num in nums:
            # 位数为两次
            twos |= ones & num
            # 位数为1次
            ones ^= num
            # 收集ones和twos中为1的位并清零
            three = ones & twos
            ones ^= three
            twos ^= three
        return ones
