"""
寻找两个有序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

思路：
1 先排好序 求第（m+n）/2那个数 考虑单数双数 O(m+n)
2 直接找，奇数的话我们要知道第len//2+1个数，偶数的话我们要知道len//2和len//2+1个数，所以用个pre记录前一个数。
3 寻找第k小数
4 利用中位数左右两边数目相等的性质
"""


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1 先排好序 求第（m+n）/2那个数 考虑单数双数 两次遍历
        """
        sorted_arr = []
        left1, left2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        while left1 < len1 and left2 < len2:
            if nums1[left1] < nums2[left2]:
                sorted_arr.append(nums1[left1])
                left1 += 1
            else:
                sorted_arr.append(nums2[left2])
                left2 += 1
        sorted_arr = sorted_arr + nums1[left1:] + nums2[left2:]
        total = len1 + len2
        if total % 2 == 1:
            return sorted_arr[total // 2]
        else:
            return (sorted_arr[total // 2] + sorted_arr[total // 2 - 1]) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        2 直接找，奇数的话我们要知道第len//2+1个数，偶数的话我们要知道len//2和len//2+1个数，所以用个pre记录前一个数。
        """
        m, n = len(nums1), len(nums2)
        pre, now = None, None
        lens = m + n
        cur1, cur2 = 0, 0
        for i in range(lens // 2 + 1):
            pre = now
            if cur1 == m:
                now = nums2[cur2]
                cur2 += 1
            elif cur2 == n:
                now = nums1[cur1]
                cur1 += 1
            else:
                if nums1[cur1] < nums2[cur2]:
                    now = nums1[cur1]
                    cur1 += 1
                else:
                    now = nums2[cur2]
                    cur2 += 1
        if lens % 2 == 1:
            return now
        return (pre + now) / 2


class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        3 寻找第k小数
        """

        def findKthElement(arr1, arr2, k):
            if len(arr1) > len(arr2):
                arr1, arr2 = arr2, arr1
            if not arr1:
                return arr2[k - 1]
            if k == 1:
                return min(arr1[0], arr2[0])
            cur1 = min(len(arr1), k // 2)
            if arr1[cur1 - 1] < arr2[k // 2 - 1]:
                return findKthElement(arr1[cur1:], arr2, k - cur1)
            return findKthElement(arr1, arr2[k // 2:], k - k // 2)

        lens = len(nums1) + len(nums2)
        median = findKthElement(nums1, nums2, lens // 2 + 1)
        if lens % 2 == 1:
            return median
        median1 = findKthElement(nums1, nums2, lens // 2)
        return (median + median1) / 2


class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        4 中位数两边的数量相等。
        总数为偶数：i+j=m-i+n-j
        总数为奇数：i+j=m-i+n-j+1
        ==> j=(m+n+1)//2-i
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        # 二分查找位置
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            if i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            else:
                # 边界判断
                if j == 0:
                    res1 = nums1[i - 1]
                elif i == 0:
                    res1 = nums2[j - 1]
                else:
                    res1 = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return res1
                if i == m:
                    res2 = nums2[j]
                elif j == n:
                    res2 = nums1[i]
                else:
                    res2 = min(nums1[i], nums2[j])

                return (res1 + res2) / 2











