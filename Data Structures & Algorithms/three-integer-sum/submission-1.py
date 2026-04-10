class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        count = Counter(nums)
        # print(count)
        for i in range(len(nums)):
            count[nums[i]] -=1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                count[nums[j]]-= 1
                if j-1> i and nums[j] == nums[j-1]:
                    continue
                target = -(nums[j]+ nums[i])
                if count[target]>0:
                    result.append([nums[i],nums[j],target])
            for j in range(i+1, len(nums)):
                count[nums[j]]+=1
        return result

    