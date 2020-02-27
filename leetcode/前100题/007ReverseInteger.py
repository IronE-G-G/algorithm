"""
整数反转
难度：简单
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

思路：分正负处理，
对于负数，要考虑末位整数是0的情况。
-10//10=1 -11//10=2 -11%10=9 -10%10=0
"""

class Solution:
    def reverse(self, x: int) -> int:
        MAX_VALUE = 2 ** 31 // 10
        flag = x > 0
        rev = 0
        if flag:
            while x:
                pop = x % 10
                x = x // 10
                # 2 4 8 6 2 4 8 6...第31个是8
                if rev > MAX_VALUE or (rev == MAX_VALUE and pop > 7):
                    return 0
                rev = rev * 10 + pop
        else:
            # x is negative
            while x:
                pop = x % 10
                x = x // 10
                if pop != 0:
                    pop -= 10
                    x += 1
                if rev < -MAX_VALUE or (rev == MAX_VALUE and pop < -8):
                    return 0
                rev = rev * 10 + pop
        return rev
