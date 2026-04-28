class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bt(initial):
            if initial == len(nums):
                result.append(nums.copy())
                return 
            for i in range(initial, len(nums)):
                nums[initial],nums[i] =nums[i],nums[initial]
                bt(initial+1)
                nums[initial],nums[i] =nums[i],nums[initial]
        
        bt(0)
        return result