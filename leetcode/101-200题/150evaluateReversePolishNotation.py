"""
150 逆波兰表达式求值
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) == 3:
            return int(eval(tokens[0] + tokens[2] + tokens[1]))
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                calcuation = self.evalRPN(tokens[(i - 2):(i + 1)])
                rest = tokens[:(i - 2)] + [str(calcuation)] + tokens[(i + 1):]
                return self.evalRPN(rest)


class Solution1:
    def evalRPN(self, tokens) -> int:
        """
        栈方法
        """
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for expr in tokens:
            if expr not in '+-*/':
                stack.append(expr)
            else:
                item2 = stack.pop()
                item1 = stack.pop()
                val = int(eval(item1 + expr + item2))
                stack.append(str(val))
        return int(stack[-1])
