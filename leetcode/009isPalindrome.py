"""
回文数：数字，越界处理，临界处理，字符串

思路1：转换成字符串来解决
思路2：数字处理，将反转后的数字算出来。注意判断是否越界
思路3：翻转一半数字
"""


class Solution1:
    """
    字符串处理
    """

    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        return x == x[::-1]


class Solution2:
    """
    数字处理
    """

    def isPalindrome(self, x: int) -> bool:
        INT_MAX = (2 ** 31) // 10
        if x < 0:
            return False
        reverse = 0
        origin = x
        while x != 0:
            pop = x % 10
            x = x // 10
            if reverse < INT_MAX or (reverse == INT_MAX and pop <= 7):
                reverse = reverse * 10 + pop
            else:
                return False
        return reverse == origin


class Solution3:
    """
    只翻转一半数字
    """

    def isPalindrome(self, x: int) -> bool:
        # 特殊情况处理，比如10
        if (x % 10 == 0 and x != 0) or x < 0:
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return x == reverse or x == reverse // 10
