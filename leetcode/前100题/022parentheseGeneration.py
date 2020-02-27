"""
22 括号生成（中等）
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。


"""

class Solution:
    def generateParenthesis(self, n: int):
        nParenthese = [set(), set(['()'])]
        if n == 1:
            return ['()']
        for i in range(2, n + 1):
            newSet = set()
            # 有外扩号
            for outer in range(1, i):
                inner = i - outer
                for item in nParenthese[inner]:
                    if item not in newSet:
                        newSet.add("(" * outer + item + ")" * outer)
            # 没有外扩号,分成两部分
            for j in range(1, i):
                rest = i - j
                for item1 in nParenthese[j]:
                    for item2 in nParenthese[rest]:
                        newSet.add(item1 + item2)
                        newSet.add(item2 + item1)
            nParenthese.append(newSet)
        return sorted(nParenthese[-1])


if __name__ == '__main__':
    n = 5
    s = Solution()
    pred = set(s.generateParenthesis(n))
    res = ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))",
           "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()",
           "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()",
           "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()",
           "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()",
           "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"]
    res = set(res)
    print(pred == res)
