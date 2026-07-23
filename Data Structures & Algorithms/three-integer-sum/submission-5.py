class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]# storing the output
        nums.sort() # sorting them which will help me with the third pointer

        for i in range(len(nums)):
            if nums[i]> 0:
                break
            if i>0 and nums[i] == nums[i-1]: # this part is helping with the third pointer
                continue
            #Now I will starting with the two pointer
            left = i+1
            right = len(nums)-1

            while left < right:
                totalsum = nums[i] +nums[left] +nums[right]
                if totalsum>0:
                    right-=1
                elif totalsum<0:
                    left +=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left -1] and left< right:
                        left+=1
        return result

