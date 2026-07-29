class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if abs(s2-s1)>=0:
                s3 = abs(s2-s1)
                heapq.heappush(stones,-s3)
        return -stones[0]
        