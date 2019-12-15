"""
盛最多水的容器（中等）：给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

keyword：数组，左右指针

"""
class Solution:
    """

    """
    def maxArea(self, height) -> int:
        start, end = 0, len(height) - 1
        maxArea = 0
        while start < end:
            gap = end - start
            # 变动短的那条边
            if height[start] < height[end]:
                mins = height[start]
                start += 1
            else:
                mins = height[end]
                end -= 1
            area = gap * mins
            if area > maxArea:
                maxArea = area
        return maxArea



