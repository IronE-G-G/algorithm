class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        push x+当前最小值
        """
        self.stack = [float('inf')]

    def push(self, x: int) -> None:
        minimun = min(self.stack[-1], x)
        self.stack.append(x)
        self.stack.append(minimun)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-2]

    def getMin(self) -> int:
        return self.stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
