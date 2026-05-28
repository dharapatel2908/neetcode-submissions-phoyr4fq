class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i,val in counter.items():
            if val> len(nums)//2:
                return i