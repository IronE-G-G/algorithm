# -*- coding:utf-8 -*-
"""
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
思路：第n块有放竖直方向（2*1）和放水平方向（1*2）两种。如果放竖直则有f(n-1)种；
放水平则需要搭上另一块水平放置的，则有f(n-2)种。
所以是斐波那契数列。
"""
class Solution:
    def rectCover(self, number):
        # write code here
        if number<=2:
            return number
        pre = 1
        cur = 2
        for i in range(3, number+1):
            next = pre+cur
            pre = cur
            cur = next
        return cur