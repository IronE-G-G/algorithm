def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
    splitPoint = len(arr) // 2
    left = mergeSort(arr[:splitPoint])
    right = mergeSort(arr[splitPoint:])
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + left + right


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 9]
    print(mergeSort(arr))
