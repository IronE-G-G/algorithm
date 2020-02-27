"""
Z字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
"""


class Solution:
    """
    使用numRows个列表存储字符
    """

    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        flag = 1
        rowi = 0
        for char in s:
            res[rowi].append(char)
            rowi += flag
            if rowi == numRows - 1 or rowi == 0:
                flag = -flag
        res = ''.join([''.join(row) for row in res])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convert('leetcode', 4))
