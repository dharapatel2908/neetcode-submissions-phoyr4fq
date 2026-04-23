class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        result = []
        for x,y in points:
            dis = (x**2) +(y**2)
            minheap.append([dis,x,y])
        heapq.heapify(minheap)
        while k>0:
            dist, x,y = heapq.heappop(minheap)
            result.append([x,y])
            k-=1
        return result