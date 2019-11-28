# -*- coding:utf-8 -*-
"""
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
思路：
f(n)=f(n-1)+...+f(0)
f(n-1)=f(n-2)+...+f(0)
所以f(n) = f(n-1)+f(n-1) = 2*f(n-1) = (2^2)*f(n-2) = (2^n)*f(0) = 2^n
"""
class Solution:
    def jumpFloorII(self, number):
        """
        每个台阶都可能被踩也可能不被踩,最后一块是青蛙落脚点一定被踩， 2^(n-1)
        """
        # write code here
        if number < 2:
            return number
        return self.jumpFloorII(number-1)*2
