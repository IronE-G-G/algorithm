"""
149 直线上的最多点数
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        以每个点为基准，算过这个点的线里面过点最多的线，以斜率的分子分母的最大公约数连成子串为key，（0，-inf，普通）
        """
        if len(points) < 3:
            return len(points)
        res = 0
        N = len(points)

        for i in range(N):
            hashMap = dict()
            duplicates = 0
            maxsize = 0
            for j in range(i + 1, N):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                if x == 0 and y == 0:
                    duplicates += 1
                    continue
                if x == 0:
                    key = '-inf'
                elif y == 0:
                    key = '0'
                else:
                    c = self.gcd(x, y)
                    x = x // c
                    y = y // c
                    key = '%d@%d' % (x, y)
                if key not in hashMap:
                    hashMap[key] = 1
                else:
                    hashMap[key] += 1
                maxsize = max(maxsize, hashMap[key])
            res = max(res, maxsize + duplicates + 1)
        return res

    def gcd(self, a, b):
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
