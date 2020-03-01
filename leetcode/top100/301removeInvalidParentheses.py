"""
301 删除无效的括号
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def check(self, s):
        left_count = 0
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                left_count += 1
            elif char == ')':
                if left_count > 0:
                    left_count -= 1
                else:
                    return False

        return left_count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        BFS
        每一层减一个元素，检查是否出现有效的括号，如果有就终止并检查这个层的其他字符串
        """
        if not s:
            return [""]
        queue = {s}
        res = set()
        while queue:
            next_queue = set()
            for item in queue:
                if self.check(item):
                    for item in queue:
                        if self.check(item):
                            res.add(item)
                    return res

                for i in range(len(item)):
                    if item[i] == ')' or item[i] == '(':
                        next_queue.add(item[:i] + item[i + 1:])
            queue = next_queue


class Solution1:
    def check(self, s):
        left_count = 0
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                left_count += 1
            elif char == ')':
                if left_count > 0:
                    left_count -= 1
                else:
                    return False
        return left_count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        DFS，先确定需要弹出的左括号和右括号个数，再遍历选择弹出
        """
        if not s:
            return [""]
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        res = set()

        def dfs(s, start, rest_left, rest_right):
            if rest_left == 0 and rest_right == 0:
                if self.check(s):
                    res.add(s)
                return
            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if rest_right > 0 and s[i] == ')':
                    dfs(s[:i] + s[i + 1:], i, rest_left, rest_right - 1)
                # 剪枝，右括号没有减完的话左括号不能开始减
                if rest_right == 0 and rest_left > 0 and s[i] == '(':
                    dfs(s[:i] + s[i + 1:], i, rest_left - 1, rest_right)

        dfs(s, 0, left, right)
        return res





