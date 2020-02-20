"""
89 格雷编码
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        n位的格雷二进制表示位
        ‘0’拼接n-1位的结果
        ‘1’拼接n-1位的结果的逆
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        pre = ['0', '1']
        for i in range(2, n + 1):
            now0 = ['0' + item for item in pre]
            now1 = ['1' + item for item in pre[::-1]]
            pre = now0 + now1
        return [int(x, 2) for x in pre]
