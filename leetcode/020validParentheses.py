"""
有效的括号（简单）

"""


class Solution:
    def isValid(self, s: str) -> bool:
        dd = {'}': '{', ')': '(', ']': '['}
        queue = []
        for char in s:
            if queue and char in dd and dd[char] == queue[-1]:
                queue.pop()
            else:
                queue.append(char)
        return not queue
