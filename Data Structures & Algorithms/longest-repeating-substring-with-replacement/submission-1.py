class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        max_freq=0
        char_set = {}

        for right in range(len(s)):
            char_set[s[right]]= char_set.get(s[right],0)+1
            max_freq =max(max_freq, char_set[s[right]])

            while (right-left +1)-max_freq >k:
                char_set[s[left]]-=1
                left+=1

            result = max(result,right-left+1)

        return result