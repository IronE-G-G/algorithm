"""
寻找两个有序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。


/*
思路来自 leetcode官方题解下面 @负债养猫人 的评论

    * 1.首先，让我们在任一位置 i 将 A(长度为m) 划分成两个部分：
    *            leftA            |                rightA
    *   A[0],A[1],...      A[i-1] |  A[i],A[i+1],...A[m - 1]
    *
    * 由于A有m个元素，所以有m + 1中划分方式(i = 0 ~ m)
    *
    * 我们知道len(leftA) = i, len(rightA) = m - i;
    * 注意：当i = 0时，leftA是空集，而当i = m时，rightA为空集。
    *
    * 2.采用同样的方式，将B也划分为两部分：
    *            leftB            |                rightB
    *   B[0],B[1],...      B[j-1] |   B[j],B[j+1],...B[n - 1]
    *  我们知道len(leftA) = j, len(rightA) = n - j;
    *
    *  将leftA和leftB放入一个集合，将rightA和rightB放入一个集合。再把这两个集合分别命名为leftPart和rightPart。
    *
    *            leftPart         |                rightPart
    *   A[0],A[1],...      A[i-1] |  A[i],A[i+1],...A[m - 1]
    *   B[0],B[1],...      B[j-1] |  B[j],B[j+1],...B[n - 1]
    *
    *   如果我们可以确认：
    *   1.len(leftPart) = len(rightPart); =====> 该条件在m+n为奇数时，该推理不成立
    *   2.max(leftPart) <= min(rightPart);
    *
    *   median = (max(leftPart) + min(rightPart)) / 2;  目标结果
    *
    *   要确保这两个条件满足：
    *   1.i + j = m - i + n - j(或m - i + n - j + 1)  如果n >= m。只需要使i = 0 ~ m，j = (m+n+1)/2-i =====> 该条件在m+n为奇数/偶数时，该推理都成立
    *   2.B[j] >= A[i-1] 并且 A[i] >= B[j-1]
    *
    *   注意:
    *   1.临界条件：i=0,j=0,i=m,j=n。需要考虑
    *   2.为什么n >= m ? 由于0 <= i <= m且j = (m+n+1)/2-i,必须确保j不能为负数。
    *
    *   按照以下步骤进行二叉树搜索
    *   1.设imin = 0,imax = m，然后开始在[imin,imax]中进行搜索
    *   2.令i = (imin+imax) / 2, j = (m+n+1)/2-i
    *   3.现在我们有len(leftPart) = len(rightPart)。而我们只会遇到三种情况：
    *
    *      ①.B[j] >= A[i-1] 并且 A[i] >= B[j-1]  满足条件
    *      ②.B[j-1] > A[i]。此时应该把i增大。 即imin = i + 1;
    *      ③.A[i-1] > B[j]。此时应该把i减小。 即imax = i - 1;
    *
    * */
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        # make sure m<=n
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        iMin, iMax = 0, m
        halfLen = (m + n + 1) // 2
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = halfLen - i
            if i > iMin and nums1[i - 1] > nums2[j]:
                iMax = i - 1
            elif i < iMax and nums2[j - 1] > nums1[i]:
                iMin = i + 1
            else:
                if i == 0:
                    median = nums2[j - 1]
                elif j == 0:
                    median = nums1[i - 1]
                else:
                    median = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return median
                else:
                    if i == m:
                        median1 = nums2[j]
                    elif j == n:
                        median1 = nums1[i]
                    else:
                        median1 = min(nums1[i], nums2[j])
                    return (median + median1) / 2
        return 0.0


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
