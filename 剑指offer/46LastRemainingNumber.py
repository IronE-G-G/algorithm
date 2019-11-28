# -*- coding:utf-8 -*-
"""
面试题46 圆圈中剩下的最后一个数
假设n个数，从0开始，每次删除第m步的数字，求最后剩下的那个数
原始序列：0，1，2，..., n-1
第一个被删除的数是(m-1)%n，假设等于k
那么原始序列变为：0,1,2,3,...,k-1,k+1,...,n-1
因为下一次从k+1开始，整理一下序列变为: k+1,...n-1,0,1,...,k-1
原始序列最后剩下的数跟这个序列的结果是一样的。
将该序列映射到：0,1,2,...,n-2，映射函数为p(x) = (x-k-1)%n, 逆映射为p-1(y) = (y+k+1)%n
用f(n,m)来表示n个数走m步最后生下来的那个数，通过递推
f(n,m) = p-1(f(n-1,m)) = (f(n-1,m)+k+1)%n = (f(n-1,m)+m)%n
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 1:
            return 0
        if m <= 0:
            return -1
        last = 0
        for num in range(2, n + 1):
            last = (last + m) % num
        return last
