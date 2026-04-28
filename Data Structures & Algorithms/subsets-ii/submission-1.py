class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        subsets = []
        def bt(i):
            result.append(subsets.copy())
            used = set()
            for i in range(i,len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                subsets.append(nums[i])
                bt(i+1)
                subsets.pop()
        bt(0)
        return result