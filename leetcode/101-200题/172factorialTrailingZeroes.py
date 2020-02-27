"""
172 阶乘后的0
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        0的出现是5*2，而5的个数比2的多，所以要算5的因子个数
        :param n:
        :return:
        """
        count = 0
        while n >= 5:
            count += n // 5
            n = n // 5
        return count
