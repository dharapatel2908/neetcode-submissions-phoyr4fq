class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i, val in count.items():
            if val > len(nums)/2:
                return i
            
