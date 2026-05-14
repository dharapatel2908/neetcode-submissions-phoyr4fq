class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currentmin, currentmax = 1,1
        for num in nums:
            temp = num *currentmax
            currentmax = max(temp,num,num * currentmin)
            currentmin = min(temp,num,num * currentmin)
            result = max(result, currentmax)
        return result