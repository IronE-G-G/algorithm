class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        分层单调栈
        """

        if not matrix:
            return 0
        res = 0
        preHeight = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            newHeight = [0 for j in range(len(matrix[0]))]
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    newHeight[j] = preHeight[j] + 1
            tmp = self.computeRectInHist(newHeight)
            res = max(tmp, res)
            preHeight = newHeight
        return res

    def computeRectInHist(self, heights):

        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = heights[stack.pop()] * (i - stack[-1] - 1)
                res = max(res, tmp)
            stack.append(i)
        return res


if __name__ == '__main__':
    rect = [['1', '0'], ['0', '1']]
    s = Solution()
    print(s.maximalRectangle(rect))
