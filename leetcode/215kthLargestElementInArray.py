"""
215 数组中的第k个最大的元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        partition应用
        """

        def partition(arr, k):
            left, mid, right = [], [], []
            for num in arr:
                if num == arr[0]:
                    mid.append(num)
                elif num < arr[0]:
                    left.append(num)
                else:
                    right.append(num)
            if len(left) >= k:
                return partition(left, k)
            elif len(left) + len(mid) >= k:
                return mid[0]
            else:
                return partition(right, k - len(left) - len(mid))

        return partition(nums, len(nums) - k + 1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        堆排序
        维护一个大小为k的最小堆
        建堆,满二叉树结构
        调整堆
        """

        def heap_sort(nums):
            # build tree
            tree = [nums[i] for i in range(k)]

            # 节点与左右子节点比较，取最小的交换，并调整该子姐节点
            def adj_heap(i, arr_len):
                left, right = 2 * i + 1, 2 * i + 2
                minist = i
                if left < arr_len and tree[left] < tree[i]:
                    minist = left
                if right < arr_len and tree[right] < tree[i] and tree[right] < tree[left]:
                    minist = right
                if minist != i:
                    tree[minist], tree[i] = tree[i], tree[minist]
                    adj_heap(minist, arr_len)

            # build min heap,
            # 从最后的一层完整层开始调整，当k-1为左节点，k为偶数，
            # 且最后一个节点对应的父节点为k-1=2i+1 ===》i=(k-2)/2
            # 当k-1为右节点时，k为奇数，
            # 对应的父节点为k-1=2i+2 ===》 i=(k-3)/2 ～ (k-2)/2
            # 所以i=floor(k/2)-1
            for i in range(k // 2 - 1, -1, -1):
                adj_heap(i, k)

            # adjust
            for num in nums[k:]:
                if num > tree[0]:
                    tree[0] = num
                    adj_heap(0, k)

            # pop heap 在此题中可以不用这一步
            last = k - 1
            while last > 0:
                tree[0], tree[last] = tree[last], tree[0]
                last -= 1
                adj_heap(0, last)
            return tree[-1]

        return heap_sort(nums)
