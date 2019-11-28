"""
表示数值的字符串
"""
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        pattern = re.compile('[+-]?[0-9]*(.[0-9]+)?([eE][-]?[0-9]+)?')
        return True if re.fullmatch(pattern, s) else False


if __name__ == '__main__':
    s = Solution()
    print(s.isNumeric('12e'))
