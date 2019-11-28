class Solution:
    def firstMissingPositive(self, nums) -> int:
        lens = len(nums)
        for index in range(lens):
            while 0 < nums[index] <= lens and nums[index] != index + 1:
                item = nums[index]
                if nums[index] == nums[item - 1]:
                    nums[index] = -1
                nums[index], nums[item - 1] = nums[item - 1], nums[index]
        for index in range(lens):
            if index + 1 != nums[index]:
                return index + 1
        return lens + 1


if __name__ == '__main__':
    # a = Solution()
    # arr = [1, 1]
    # print(a.firstMissingPositive(arr))
    ss = 'abc'
    print(ss[:1]+ss[2:])
