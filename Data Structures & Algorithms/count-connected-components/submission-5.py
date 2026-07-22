class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        rank = [0]*n
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            nonlocal components
            rootx,rooty = find(x), find(y)
            if rootx== rooty:
                return 
            elif rank[rootx] >rank[rooty]:
                parent[rooty] = rootx
            elif rank[rootx] <rank[rooty]:
                parent[rootx] = rooty

            else:
                parent[rooty] = rootx
                rank[rootx] +=1
            components-=1

        for u,v in edges:
            union(u,v)
        return components