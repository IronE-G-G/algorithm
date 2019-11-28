import math


def heapAdjust(arr, i, arrLen):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < arrLen and arr[left] > arr[i]:
        largest = left
    if right < arrLen and arr[right] > arr[i] and arr[right] > arr[left]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapAdjust(arr, largest, arrLen)


def buildMaxHeap(arr):
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapAdjust(arr, i, len(arr))


def heapSort(arr):
    buildMaxHeap(arr)
    arrLen = len(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arrLen -= 1
        heapAdjust(arr, 0, arrLen)


if __name__ == '__main__':
    array = [9, 2, 6, 4, 5, 10, 50, 2, 100]
    heapSort(array)
    print(array)