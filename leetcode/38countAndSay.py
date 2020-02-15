"""
38 外观数列（简单）
外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221


"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return None
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        pre = '11'
        count = 2
        while count < n:
            res = ''
            preChar = pre[0]
            nChar = 1
            for char in pre[1:]:
                if char == preChar:
                    nChar += 1
                else:
                    res = res + str(nChar) + preChar
                    nChar = 1
                    preChar = char
            # 走到最后
            res = res + str(nChar) + preChar
            count += 1
            pre = res
        return res
