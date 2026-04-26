class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        current = 0
        for num in nums:
            if current<0:
                current= 0
            current+=num
            maxsub = max(maxsub,current)
        return maxsub