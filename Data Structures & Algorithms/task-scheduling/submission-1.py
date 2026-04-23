class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # making frequency table and then the highest frequency count * n = slots:
        # then we will fill the highest frequency character with leaving n space 
        #then 2nd highest freq will remaining space interval of n.
        max_freq_task =0
        count = Counter(tasks)
        highest_freq = max(count.values()) 
        for freq in count.values():
            if freq == highest_freq:
                max_freq_task += 1
        answer = (highest_freq -1)* (n+1) + max_freq_task
        return max(answer,len(tasks))    