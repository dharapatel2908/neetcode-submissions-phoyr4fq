class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0
        while left< right:
            width= right -left
            height = min(heights[right], heights[left])
            area= max(area,width*height)
            if heights[left]<heights[right]:
                left+=1
            else:
                right -=1
        return area