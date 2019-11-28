# -*- coding:utf-8 -*-
"""
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
思路：斐波那契数列
"""


class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        else:
            pre = 1
            cur = 2
            for i in range(number - 2):
                nexti = pre + cur
                pre = cur
                cur = nexti
            return cur
