class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []
        total = 0
        def bt(i,combo,total):
            if total == target:
                result.append(combo.copy())
                return
            if i>= len(nums) or total > target:
                return
            combo.append(nums[i])
            bt(i,combo,total+nums[i])
            combo.pop()
            bt(i+1,combo,total)
        bt(0,combo,total)
        return result