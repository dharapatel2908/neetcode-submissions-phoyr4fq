class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combo = []
        result =[]
        total = 0
        def bt(start,combo, total):
            if total == target:
                result.append(combo.copy())
                return
            if total> target:
                return
            for i in range(start,len(candidates)):
                if i> start and candidates[i] == candidates[i-1]:
                    continue
                combo.append(candidates[i])
                bt(i+1,combo,total+candidates[i])
                combo.pop()
        bt(0,combo,total)
        return result
