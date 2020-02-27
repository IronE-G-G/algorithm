"""
135 分发糖果
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        满足两个条件然后取最大值
        """
        N = len(ratings)
        left_neighbors = [1 for _ in range(N)]
        right_neighbors = [1 for _ in range(N)]

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left_neighbors[i] = left_neighbors[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_neighbors[i] = right_neighbors[i + 1] + 1

        return sum([max(left_neighbors[i], right_neighbors[i]) for i in range(N)])


class Solution1(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        扫描的时候要注意方向，从左到右扫描的时候是能跟之前的比，如果跟之后的比的话前面的值也需要修改
        """
        N = len(ratings)
        candies = [1 for _ in range(N)]

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)
