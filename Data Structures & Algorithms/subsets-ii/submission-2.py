class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        combo = []
        def bt(initial):
            result.append(combo.copy())
            visited = set()
            for i in range(initial,len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                combo.append(nums[i])
                bt(i+1)
                combo.pop()
        bt(0)
        return result