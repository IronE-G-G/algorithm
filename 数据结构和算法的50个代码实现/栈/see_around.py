def search(array):
    """
    向左看和向右看都维护一个站内单调递减的栈
    """
    stack = []
    left_count = []
    for i in range(len(array)):
        left_count.append(len(stack))
        while stack and stack[-1] <= array[i]:
            stack.pop()
        stack.append(array[i])
    print(left_count)
    stack = []
    right_count = [0 for _ in range(len(array))]

    for i in range(len(array) - 1, -1, -1):
        right_count[i] = len(stack)
        while stack and stack[-1] <= array[i]:
            stack.pop()
        stack.append(array[i])
    print([left_count[i] + right_count[i]+1 for i in range(len(left_count))])


if __name__ == '__main__':
    n = int(input())
    string = list(map(int, input().split()))
    print(string)
    search(string)
    # 3 3 5 4 4 4