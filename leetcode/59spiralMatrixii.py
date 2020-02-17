"""
59 螺旋矩阵ii（中等）
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, top, right, down = 0, 0, n - 1, n - 1
        num = 1
        while num <= n ** 2:
            if top <= down:
                for j in range(left, right + 1):
                    res[top][j] = num
                    num += 1
                top += 1
            if right >= left:
                for i in range(top, down + 1):
                    res[i][right] = num
                    num += 1
                right -= 1
            if down >= top:
                for j in range(right, left - 1, -1):
                    res[down][j] = num
                    num += 1
                down -= 1
            if left <= right:
                for i in range(down, top - 1, -1):
                    res[i][left] = num
                    num += 1
                left += 1
        return res
