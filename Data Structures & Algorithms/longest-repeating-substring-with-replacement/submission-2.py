class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        result = 0
        maxfreq= 0
        for i in range(len(s)):
            counter[s[i]] +=1
            maxfreq = max(maxfreq,counter[s[i]])

            while (i -left+1) -maxfreq> k:
                counter[s[left]] -=1
                left +=1
            result = max(maxfreq,i-left +1)
        return  result    
