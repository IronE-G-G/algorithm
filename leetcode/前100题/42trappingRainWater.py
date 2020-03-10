"""
42 接雨水（困难）

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1 暴力 如何确定坐标i的高度，找左右两边最高的位置, maxMin
        2 leftmax维护一个单调递增栈，rightmax也维护一个单调递增栈，逆序进
        """
        res = 0
        for i in range(1, len(height) - 1):
            left = i - 1
            right = i + 1
            max_left, max_right = 0, 0
            while left >= 0:
                max_left = max(max_left, height[left])
                left -= 1
            while right < len(height):
                max_right = max(max_right, height[right])
                right += 1
            res += max(min(max_left, max_right), height[i]) - height[i]

        return res


class Solution1:
    def trap(self, height: List[int]) -> int:
        """
        2 dp保存leftmax和rightmax
        """
        if not height:
            return 0
        leftmax = [-1]
        pre_leftmax = height[0]
        for i in range(1, len(height) - 1):
            leftmax.append(pre_leftmax)
            pre_leftmax = max(pre_leftmax, height[i])

        rightmax = [-1 for _ in range(len(height))]
        pre_rightmax = height[-1]
        for i in range(len(height) - 2, 0, -1):
            rightmax[i] = pre_rightmax
            pre_rightmax = max(pre_rightmax, height[i])
        res = 0
        for i in range(1, len(height) - 1):
            res = res + max(height[i], min(leftmax[i], rightmax[i])) - height[i]
        return res


