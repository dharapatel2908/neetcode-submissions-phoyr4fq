class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        # for i, n in enumerate(nums):
        #     mapping[n] =i
        for i,n in enumerate(nums):
            difference = target - n
            if difference in mapping:
                return [mapping[difference],i]
            mapping[n] = i
