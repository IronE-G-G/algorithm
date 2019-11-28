def fastSort(arr):
    if len(arr) <= 1:
        return arr
    med = arr[len(arr) // 2]
    left = []
    right = []
    center = []
    for item in arr:
        if item < med:
            left.append(item)
        elif item == med:
            center.append(item)
        else:
            right.append(item)
    left = fastSort(left)
    right = fastSort(right)
    return left + center + right


if __name__ == '__main__':
    arr = [1, 5, 2, 3, 2]
    print(fastSort(arr))
