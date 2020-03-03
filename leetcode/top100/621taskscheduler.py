class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        从最多的任务开始，每一轮最多挑N+1种任务，不够算N+1。知道最后一轮里面没有任务了。
        :param tasks:
        :param n:
        :return:
        """
        hashMap = dict()
        for task in tasks:
            if task not in hashMap:
                hashMap[task] = 0
            hashMap[task] += 1
        queue = list(hashMap.keys())
        queue.sort(key=lambda x: hashMap[x], reverse=True)
        count = 0
        rest_item = len(queue)
        while rest_item > 0:
            k = 0
            for item in queue:
                if hashMap[item] == 0:
                    continue
                hashMap[item] -= 1
                if hashMap[item] == 0:
                    rest_item -= 1
                k += 1
                if k == n + 1:
                    break
            if rest_item > 0:
                count += (n + 1)
                queue.sort(key=lambda x: hashMap[x], reverse=True)
            else:
                count += k
        return count


class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        想不懂为啥保证数量最多的那个任务的待命时间填满了结果就是任务长度
        :param tasks:
        :param n:
        :return:
        """
        nums = [0 for _ in range(26)]
        for task in tasks:
            nums[ord(task) - ord('A')] += 1
        nums.sort()
        rounds = nums[25] - 1
        idles = rounds * n
        for i in range(24, -1, -1):
            if nums[i] == 0:
                break
            idles -= min(rounds, nums[i])
        return len(tasks) if idles <= 0 else idles + len(tasks)
