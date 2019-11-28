class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle)
        if N == 1:
            return triangle[0][0]
        base = triangle[N - 1]
        for row in range(N - 2, -1, -1):
            newBase = []
            for ind, item in enumerate(triangle[row]):
                minBase = min(base[ind:(ind + 2)])
                newBase.append(minBase + item)
            base = newBase
        return base[0]


if __name__ == '__main__':
    triangle = [[1], [2, 3]]
    print(Solution().minimumTotal(triangle))
