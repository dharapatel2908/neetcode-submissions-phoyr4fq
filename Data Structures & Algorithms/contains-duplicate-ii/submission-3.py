class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,min(len(nums),i+k+1)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False

        ## we will use set to check whether it contains duplicate
        window = set()
        left = 0
        for right in range(len(nums)):
            if abs(left- right) > k: ## to maintain window size
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
        