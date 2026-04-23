class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        minheap = []
        for x,y in points:
            dist = (x**2) +(y**2)
            minheap.append([dist,x,y])
        print(minheap)

        heapq.heapify(minheap)
        while k>0:
            val,x1,y1= heapq.heappop(minheap)
            result.append([x1,y1])
            k-=1
        return result
