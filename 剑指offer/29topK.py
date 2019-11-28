# -*- coding:utf-8 -*-
"""
最小的k个数：输入n个整数，找出其中最小的K个数。
思路：使用堆排序，维护一个大顶堆。
堆性质：完全二叉树，父结点i，左子节点 （2*i+1），右子节点 （2*i+2）
"""


class Solution:
    res = []

    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k or k == 0:
            return []
        # 建堆
        self.res = tinput[:k]
        for i in range((k - 1) // 2, -1, -1):
            self.adjustHeap(k, i)

        # 数组中剩余的数跟大顶堆的根节点进行比较，堆调整
        for item in tinput[k:]:
            if item < self.res[0]:
                self.res[0] = item
                self.adjustHeap(k, 0)
        arrLen = k
        for i in range(k - 1, 0, -1):
            self.res[i], self.res[0] = self.res[0], self.res[i]
            arrLen -= 1
            self.adjustHeap(arrLen, 0)
        return self.res

    def adjustHeap(self, k, i):
        left = 2 * i + 1
        right = left + 1
        target = i
        if left < k and self.res[i] < self.res[left]:
            target = left
        if right < k and self.res[right] > self.res[i] and self.res[right] > self.res[left]:
            target = right
        if target != i:
            self.res[i], self.res[target] = self.res[target], self.res[i]
            self.adjustHeap(k, target)
