# -*- coding:utf-8 -*-
"""
用两个栈实现队列
思路：push操作放在s1中。当要pop的时候，判断s2中是否有元素，有就从s2走一个。
     没有就吧s1中的pop到s2中；再从s2中pop一个元素。

衍生：用两个队列实现栈：push到长度不为0的队列。
     pop的时候，长度不为0（假设为k）的队列把k-1个元素移动到另一个队列，最后一个输出。
"""
class Solution:
    """
    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
    """
    s1 = []
    s2 = []

    def push(self, node):
        self.s1.append(node)
        # write code here

    def pop(self):
        if self.s2:
            return self.s2.pop()
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()
        # return xx
