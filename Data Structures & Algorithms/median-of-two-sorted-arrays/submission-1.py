class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2):
            nums1, nums2 = nums2,nums1
        
        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m
        
        while left<= right:
            i = (left + right) //2
            j = (m+n+1)//2 - i

            maxLeftX = float("-inf") if i == 0 else nums1[i-1]
            minRightX = float("inf") if i == m else nums1[i]

            
            maxLeftY = float("-inf") if j == 0 else nums2[j-1]
            minRightY = float("inf") if j == n else nums2[j]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m+n) %2==0:
                    return (max(maxLeftX,maxLeftY)+ min(minRightX,minRightY))/2
                else:
                    return max(maxLeftX,maxLeftY)

            elif maxLeftX > minRightY:
        
                right =i-1
            else:
                left = i +1
        raise ValueError("Input arrays are not sorted properly")