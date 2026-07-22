class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #key= value(index)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[nums[i]] = i