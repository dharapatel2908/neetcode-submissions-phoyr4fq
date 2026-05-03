class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        lastindex = {}
        for i,c in enumerate(s):
            lastindex[c] =i

        size = 0
        last = 0
        for i in range(len(s)):
            size +=1
            last = max(last,lastindex[s[i]])
            if i == last:
                result.append(size)
                size = 0
        return result