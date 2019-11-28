# -*- coding:utf-8 -*-
"""
替换空格
用python写的，没啥好说。
"""
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        arr = s.split(' ')
        return '%20'.join(arr)