def bubbleSort(arr):
    if len(arr) <= 1:
        return arr
    arrLen = len(arr)
    while arrLen > 1:
        for j in range(1, arrLen):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        arrLen -= 1

    return arr


if __name__ == '__main__':
    arr = [1, -1]
    print(bubbleSort(arr))
