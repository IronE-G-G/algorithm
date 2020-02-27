class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        暴力 On2
        """
        N = len(gas)
        for i in range(N):
            count = 0
            total = 0
            while count<N:
                now = (i+count)%N
                total+=(gas[now]-cost[now])
                count+=1
                if total<0:
                    break
            if count == N and total>=0:
                return i
        return -1


class Solution1(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        如果在开往i+1汽油站时curr_gas为负数，那么从出发汽油站到这个汽油站之前的汽油站都到不了这个汽油站
        所以从i+1开始

        """
        N = len(gas)
        total_gas = 0
        curr_gas = 0
        start_station = 0
        for i in range(N):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                curr_gas = 0
                start_station = i + 1

        return start_station if start_station < N and total_gas >= 0 else -1
