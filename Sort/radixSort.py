def radicSort(nums):
    if len(nums) <= 1:
        return 0
    max_value = max(nums)
    base = 1

    while max_value // base > 0:
        sort_arr = [[] for _ in range(10)]
        # 按基数分桶
        for i in range(len(nums)):
            to_i_arr = nums[i] // base % 10
            sort_arr[to_i_arr].append(nums[i])
        nums = []
        for i in range(len(sort_arr)):
            nums += sort_arr[i]
        base *= 10
    return nums