class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        dp 保存每一层经过第i个元素的最小路径和
        """
        if not triangle:
            return 0
        N = len(triangle)
        sumPath = triangle[0]
        for i in range(1, N):
            newSumPath = [sumPath[0] + triangle[i][0]]
            for j in range(1, i):
                newSumPath.append(min(sumPath[j - 1], sumPath[j]) + triangle[i][j])
            newSumPath.append(sumPath[-1] + triangle[i][-1])
            sumPath = newSumPath
        return min(sumPath)
