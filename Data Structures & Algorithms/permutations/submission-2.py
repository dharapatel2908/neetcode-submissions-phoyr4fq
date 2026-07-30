class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bt(start):
            if len(nums) == start:
                result.append(nums.copy())
                return 
            for i in range(start,len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                bt(start +1)
                nums[start], nums[i] = nums[i], nums[start]
        bt(0)
        return result