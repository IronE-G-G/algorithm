import re


def computeSum(num1, num2):
    pattern = re.compile('^-?\d+$')
    if not (re.match(pattern, num1) and re.match(pattern, num2)):
        return "input format is incorrect."
    if len(num1) == 1 and num1[0] == '0':
        return num2
    if len(num1) == 1 and num2[0] == '0':
        return num1
    flag1, flag2 = 0, 0
    if num1[0] == '-':
        flag1 = 1
        num1 = num1[1:]
    if num2[0] == '-':
        flag2 = 1
        num2 = num2[1:]
    flag = 0
    sign = 0
    if flag1 and flag2:
        sign = 1
    elif flag1 and not flag2:
        flag = 1
        if num1 > num2:
            sign = 1
        else:
            num1, num2 = num2, num1
    elif not flag1 and flag2:
        flag =1
        if num1 < num2:
            sign = 1
            num1, num2 = num2, num1
    result = []
    carry = 0
    len1 = len(num1)
    len2 = len(num2)

    for index in range(len1 - 1, -1, -1):
        if index >= len2:
            num2Digit = 0
        else:
            num2Digit = int(num2[index])
        num1Digit = int(num1[index]) + carry
        carry = 0
        if flag == 1:
            res = num1Digit - num2Digit
            if res < 0:
                carry = -1
                res = res + 10
        else:
            res = num1Digit + num2Digit
            if res > 10:
                carry = 1
                res = res - 10
        result.insert(0, str(res))
    if sign == 1:
        result.insert(0, '-')

    return int(''.join(result))


if __name__ == '__main__':
    num1 = '126'
    num2 = '395'
    print(computeSum(num1, num2))
    num1 = '-126'
    num2 = '395'
    print(computeSum(num1, num2))
    num1 = '126'
    num2 = '-395'
    print(computeSum(num1, num2))
    num1 = '-126'
    num2 = '126'
    print(computeSum(num1, num2))

