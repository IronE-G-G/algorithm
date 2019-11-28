"""
1、将原有序数组（升序）s转化成局部有序数组a, 判断指定数字是否在数组a中，如果有返回相应index，反之返回-1，要求时间复杂度不高于O(n)。
示例1，input：a = {18，21，22，50，3，8，10，11} , target = 8  output : 5

2、给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
"""


def maxSubStr(s):
    maxlen = 1
    i = 0
    while i < len(s):
        uniqueChar = dict()
        j = i
        while j < len(s):
            # print(i, j, maxlen)
            if s[j] not in uniqueChar:

                uniqueChar[s[j]] = j
                j += 1
            else:
                maxlen = max(maxlen, j - i)
                i = uniqueChar[s[j]] + 1
                break
        if j == len(s):
            maxlen = max(maxlen, j - i)
            break
    return maxlen


def search(arr, target):
    start, end = 0, len(arr) - 1
    while start < end:
        center = (start + end) // 2
        if arr[center] == target:
            return center
        if arr[center] > arr[start]:
            if arr[start] < target < arr[center]:
                end = center - 1
            else:
                start = center + 1
        else:
            if arr[center] < target < arr[end]:
                start = center + 1
            else:
                end = center - 1
    return -1


if __name__ == '__main__':
    print(search([18, 21, 22, 50, 3, 8, 10, 11], 8))
