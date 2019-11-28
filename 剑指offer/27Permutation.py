# -*- coding:utf-8 -*-
"""
字符串的排列
思路：取出不同的字符做第一个字符，对剩下的字符进行全排列，跟第一个字符拼接,。

"""


class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        res = []
        unique_char = set()
        for ind, char in enumerate(ss):
            if ss[ind] not in unique_char:
                for subRes in self.Permutation(ss[:ind] + ss[(ind + 1):]):
                    temp = char + subRes
                    res.append(temp)
                    unique_char.add(ss[ind])
        return sorted(list(res))


if __name__ == '__main__':
    ss = 'abbc'
    s = Solution()
    print(s.Permutation(ss))
