class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left,right = 0, len(height)-1
        ht_left, ht_right = height[left],height[right]
        res = 0
        while left < right:
            if ht_left < ht_right:
                left+=1
                ht_left = max(ht_left, height[left])
                res += ht_left - height[left]
            else:
                right-=1
                ht_right = max(ht_right, height[right])
                res += ht_right - height[right]
        return res