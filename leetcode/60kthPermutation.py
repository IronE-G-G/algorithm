"""
60 第k个排列（中等）

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。


思路：递归求每个数字
"""
from math import factorial


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        找规律：
        每个数在第一个位置的次数都是相等的，即(n-1)!次，因此可以通过 ceil(k/(n-1)!)确定第一个数是什么，
        同理，求n个数组合的第二个数即是求n-1个数的第一个数
        """
        res = []
        candidates = [i for i in range(1, n + 1)]

        def helper(candidates, k, n):
            if n == 1:
                res.append(str(candidates[0]))
                return
            index = k // factorial(n - 1)
            rest = k % factorial(n - 1)
            if rest != 0:
                index += 1
            res.append(str(candidates.pop(index - 1)))
            helper(candidates, rest, n - 1)

        helper(candidates, k, n)

        return ''.join(res)




