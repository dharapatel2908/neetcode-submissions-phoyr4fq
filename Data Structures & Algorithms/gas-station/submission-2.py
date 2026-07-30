class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        current = 0
        start  = 0
        n = len(gas)
        for i in range(n):
            diff = gas[i]- cost[i]
            total += diff
            current += diff

            if current<0:
                start =i+1
                current = 0
        if total >=0:
            return start
        else:
            return -1