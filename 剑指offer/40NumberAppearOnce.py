"""
20191120
面试题40：数组中只出现一次的数字
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
思路1：使用一个集合判断元素是否在集合中。
思路2：通过异或操作，相同的两个数字异或结果为0，最终会得到那两个不同的数字的异或结果（非0）。
通过这个结果的第一个非0位将数组分成两组，分别再次计算两组的异或。
"""


class Solution1:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        uniqueNumber = set()
        for item in array:
            if item in uniqueNumber:
                uniqueNumber.remove(item)
            else:
                uniqueNumber.add(item)
        return list(uniqueNumber)


class Solution2:
    def getTotalXor(self, array):
        xor = array[0]
        for item in array[1:]:
            xor = xor ^ item
        return xor

    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor = self.getTotalXor(array)
        digitN = 0
        while xor != 0:
            if xor & 1 == 0:
                xor = xor >> 1
                digitN += 1
            else:
                break
        subArr0 = []
        subArr1 = []
        for item in array:
            if item >> digitN & 1 == 1:
                subArr1.append(item)
            else:
                subArr0.append(item)
        res0 = self.getTotalXor(subArr0)
        res1 = self.getTotalXor(subArr1)
        if res0 > res1:
            res0, res1 = res1, res0
        return [res0, res1]
