class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right = len(height) -1
        leftheight,rightheight= height[left],height[right]
        result = 0
        while left < right:
            if leftheight<rightheight:
                left +=1
                leftheight = max(leftheight, height[left])
                result += leftheight - height[left]

            else:
                right -=1
                rightheight = max(rightheight, height[right])
                result +=rightheight- height[right]
        return result