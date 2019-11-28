def insertSort(arr):
    if len(arr) <= 1:
        return arr
    res = [arr[0]]
    arrLen = 1
    for item in arr[1:]:
        j = 0
        while j < arrLen and item > arr[j]:
            j = j + 1
        if j == arrLen:
            res.append(item)
        else:
            res.insert(j, item)
        arrLen += 1
    return res


if __name__ == '__main__':
    arr = [1, 4, 2, 5]
    print(insertSort(arr))
