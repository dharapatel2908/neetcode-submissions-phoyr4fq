class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1:
            return 0
        jumps = 0
        end = 0
        far =0 
        for i in range(n):
            far = max(far,nums[i]+i)
            if i == end:
                jumps +=1
                end = far
                if end>= n-1:
                    break
        return jumps