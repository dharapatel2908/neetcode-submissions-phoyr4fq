class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        parent = list(range(n))
        rank = [0]*n
        components =n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(A,B):
            nonlocal components
            rootA = find(A)
            rootB = find(B)
            if rootA == rootB:
                return False
            if rank[rootA]< rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootB]< rank[rootA]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] +=1
            components -=1
            return True

        for u,v in edges:
            if not union(u,v):
                return False
        return components ==1