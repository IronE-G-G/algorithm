"""
扔n个骰子，求所有点数之和出现的概率
思路1：递归思想，扔一颗骰子，然后跟n-1个骰子的结果做计算
思路2：动态规划思想，递推，用一个数组保存n-1个骰子的概率结果。
"""


class Solution1:

    def getDicePointProbRecursively(self, n):
        if n == 0:
            return
        if n == 1:
            return [1 / 6] * 6
        res = [0] * (6 * n - n + 1)
        for prevPoint, prob in enumerate(self.getDicePointProbRecursively(n - 1)):
            for singlePoint in range(6):
                res[prevPoint + singlePoint] += prob * 1 / 6
        return res

    def printDicePointProb(self, n):
        arr = self.getDicePointProbRecursively(n)
        print(sum(arr))
        return [(index + n, prob) for index, prob in enumerate(arr)]


class Solution2:
    def getDicePointProb(self, n):
        preSum = [1 / 6] * 6
        if n == 1:
            return preSum
        cnt = 2
        prevNTypes = 6
        while cnt <= n:
            # 计算n个骰子有多少种点数
            nTypes = 6 * cnt - cnt + 1
            curSum = [0] * nTypes
            for tsum in range(nTypes):
                for point in range(6):
                    restPoint = tsum - point
                    # 判断剩余的点数是否能由n-1个骰子掷出来
                    if restPoint >= 0 and restPoint < prevNTypes:
                        curSum[tsum] += preSum[restPoint] * 1 / 6
            prevNTypes = nTypes
            preSum = curSum
            cnt += 1
        return [(index + n, prob) for index, prob in enumerate(curSum)]


if __name__ == '__main__':
    s = Solution1()
    print(s.printDicePointProb(7))
