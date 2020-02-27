"""
42 接雨水（困难）

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""


class Solution(object):
    """
    暴力法，对每个元素都求它左右两边的最大高度，O(n2)
    """

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        rainHeight = [height[0]]
        i = 1
        n = len(height)
        while i < n - 1:
            left = 0
            maxleft = 0
            right = n - 1
            maxright = n - 1
            target = height[i]
            while left < i:
                if height[left] >= height[maxleft]:
                    maxleft = left
                left += 1
            while right > i:
                if height[right] >= height[maxright]:
                    maxright = right
                right -= 1
            res = max(target, min(height[maxleft], height[maxright]))
            rainHeight.append(res)
            i += 1
        total = 0
        for i in range(n - 1):
            total += (rainHeight[i] - height[i])
        return total


class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        dp求元素左右两边的最大高度
        """

        n = len(height)
        if n <= 2:
            return 0
        maxleft = [-1, height[0]]
        for i in range(2, n - 1):
            left = max(maxleft[-1], height[i - 1])
            maxleft.append(left)
        maxleft.append(-1)
        maxright = [-1, height[-1]]
        for i in range(n - 3, 0, -1):
            right = max(maxright[-1], height[i + 1])
            maxright.append(right)
        maxright.append(-1)
        maxright.reverse()
        total = 0
        for i in range(n):
            rainHeight = max(height[i], min(maxleft[i], maxright[i]))
            total += (rainHeight - height[i])
        return total
