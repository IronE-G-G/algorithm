"""
翻转单词的顺序列
思路1：利用python的内置语言，split-翻转-join，空间和时间复杂度都是O（n）
思路2：先翻转整个句子，再逐个翻转单词
"""


# -*- coding:utf-8 -*-
class Solution1:
    def ReverseSentence(self, s):
        # write code here
        w = s.split(' ')
        w.reverse()
        return ' '.join(w)


# -*- coding:utf-8 -*-
class Solution2:

    def reverse(self, string, begin, end):
        while begin < end:
            string[begin], string[end] = string[end], string[begin]
            begin += 1
            end -= 1

    def ReverseSentence(self, s):
        # write code here
        if len(s) <= 1:
            return s
        begin = 0
        end = 0
        s = list(s)
        self.reverse(s, begin, len(s) - 1)
        s.append('\0')
        while end < len(s):
            if s[end] == ' ' or s[end] == '\0':
                self.reverse(s, begin, end - 1)
                end += 1
                begin = end
            else:
                end += 1
        return ''.join(s[:-1])


if __name__ == '__main__':
    string = 'i am a student.'
    s = Solution2()
    print(s.ReverseSentence(string))
