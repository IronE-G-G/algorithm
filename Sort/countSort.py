def countSort(arr):
    min_value = min(arr)
    max_value = max(arr)
    count_table = [0 for _ in range(max_value - min_value + 1)]
    for i in range(len(arr)):
        count_table[arr[i] - min_value] += 1
    res = []
    for i in range(max_value - min_value + 1):
        res += [i] * count_table[i]

    return res


if __name__ == '__main__':
    print(countSort([1, 2, 3, 4, 3, 2, 1]))
