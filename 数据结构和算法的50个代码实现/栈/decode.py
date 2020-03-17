def decode(s):
    num_stack = []
    # 记录左括号
    stack = []
    i = 0
    while True:
        if i == len(s):
            break
        if s[i] == '[':
            stack.append(i)
        elif s[i] == '|':
            num_stack.append(i)
        elif s[i] == ']':
            left = stack.pop()
            split_i = num_stack.pop()
            num = int(s[(left + 1):split_i])
            right = s[(i + 1):]
            s = s[:left] + s[(split_i + 1):i] * num
            i = len(s)-1
            s =s+right
        i += 1
    return s


if __name__ == '__main__':
    print(decode(input()))
