class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        parent = list(range(n))
        rank = [0] *n
        def find(x):
            if parent[x] !=x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            nonlocal components
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            if rank[rootA]< rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA]> rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] +=1
            components-=1
            
        
        for u,v in edges:
           union(u,v)
        return components