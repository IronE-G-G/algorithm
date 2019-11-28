class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j]+arr[i][j-1]
        return arr[n-1][m-1]


if __name__ == '__main__':
    m, n = 7, 3
    print(Solution().uniquePaths(m,n))