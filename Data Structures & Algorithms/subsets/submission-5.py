class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def df(i):
            if i>= len(nums):
                result.append(path.copy())
                return
            path.append(nums[i])
            df(i+1)
            path.pop()
            df(i+1)
        df(0)
        return result