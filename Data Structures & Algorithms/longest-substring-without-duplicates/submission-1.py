class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result =0
        window_sum = set()
        for right in range(len(s)):
            while s[right] in window_sum:
                window_sum.remove(s[left])
                left+=1
            window_sum.add(s[right])
            result = max(result,right-left+1)
        return result
