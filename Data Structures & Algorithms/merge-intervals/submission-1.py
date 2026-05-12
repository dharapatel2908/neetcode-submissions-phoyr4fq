class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        intervals.sort(key = lambda x:x[0])
        merge = [intervals[0]]
        for i in intervals[1:]:
            last = merge[-1]
            if i[0] <=last[1]:
                last[1] =max(last[1],i[1])
            else:
                merge.append(i)
        return merge