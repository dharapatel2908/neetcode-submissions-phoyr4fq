class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def count_sort():
            count = defaultdict(int)
            minval,maxval = min(nums),max(nums)
            for val in nums:
                count[val] +=1
            
            index = 0
            for val in range(minval, maxval+1):
                while count[val]>0:
                    nums[index] = val
                    index +=1
                    count[val] -=1
        count_sort()
        return nums
            