class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        numTrees4i = [1]
        for lens in range(1, n+1):
            res = 0
            for root in range(1, lens+1):
                numLeft = numTrees4i[root-1]
                numRight = numTrees4i[lens-root]
                res+=numLeft*numRight
            numTrees4i.append(res)
        return numTrees4i[n]