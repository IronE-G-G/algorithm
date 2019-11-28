# -*- coding:utf-8 -*-
"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路：动态规划思想，第k个数是前面的k-1个数分别乘上2/3/5的最小值。
为了减少空间复杂度，仅维护三个指针给因子2，3，5。
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        arr = [1]
        t2, t3, t5 = 0, 0, 0
        for cnt in range(1, index):
            target = min(arr[t2] * 2, arr[t3] * 3, arr[t5] * 5)
            if arr[t2] * 2 == target:
                t2 += 1
            if arr[t3] * 3 == target:
                t3 += 1
            if arr[t5] * 5 == target:
                t5 += 1
            arr.append(target)
        return arr[index - 1]


if __name__ == '__main__':
    n = 1000
    s = Solution()
    print(s.GetUglyNumber_Solution(n))
