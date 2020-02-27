"""
166 分数到小数
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 不能除
        if denominator == 0:
            return
        # 越界
        if numerator == -2 ** 32 and denominator == -1:
            return

            # 符号处理，sign = 1:negative
        sign = (denominator > 0) ^ (numerator > 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer = str(numerator // denominator)

        # 符号要先转成字符串再加，因为 -0 = 0
        if sign == 1:
            integer = '-' + integer

        numerator = numerator % denominator
        # 整数返回
        if numerator == 0:
            return integer

        visited = dict()
        count = 0
        res = []
        while numerator != 0:
            if numerator in visited:
                cycle_len = count - visited[numerator]
                cycle = res[count - cycle_len:count]
                return str(integer) + '.' + ''.join(res[:count - cycle_len]) + '(' + ''.join(cycle) + ')'
            visited[numerator] = count
            count += 1
            numerator *= 10
            res.append(str(numerator // denominator))
            numerator %= denominator
        return str(integer) + '.' + ''.join(res)





