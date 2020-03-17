class Solution:
    """
    有序数组合并
    """
    def merge(self, arr1, arr2):
        if not arr1:
            return arr2
        if not arr2:
            return arr1
        sorted_arr = []
        len1, len2 = len(arr1), len(arr2)
        cur1, cur2 = 0, 0
        while cur1 < len1 and cur2 < len2:
            if arr1[cur1] < arr2[cur2]:
                sorted_arr.append(arr1[cur1])
                cur1 += 1
            else:
                sorted_arr.append(arr2[cur2])
                cur2 += 1
        return sorted_arr + arr1[cur1:] + arr2[cur2:]


if __name__ == '__main__':
    arrA = [1, 2, 3, 6, 7]
    arrB = [4, 7, 8, 9]
    s = Solution()
    print(s.merge(arrA, arrB))
