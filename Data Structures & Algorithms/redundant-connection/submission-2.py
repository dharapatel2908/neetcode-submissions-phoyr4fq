class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)+1
        rank = [1]*length 
        parent = [i for i in range(length)]
        def find(x):
            if x!= parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootx, rooty = find(x),find(y)
            if rootx == rooty:
                return False
            elif rank[rooty]>rank[rootx]:
                parent[rootx]= rooty
            elif rank[rooty]<rank[rootx]:
                parent[rooty]= rootx    
            else:
                parent[rootx] = rooty
                rank[rooty]+=1
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]