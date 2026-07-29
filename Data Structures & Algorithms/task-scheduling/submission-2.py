class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxtask = 0
        count = Counter(tasks)
        highest_freq = max(count.values())
        for freq in count.values():
            if freq == highest_freq:
                maxtask +=1
        answer =(highest_freq-1)*(n+1)+maxtask
        return max(answer,len(tasks))