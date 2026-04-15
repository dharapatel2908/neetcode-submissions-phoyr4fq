class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         row = len(grid)
#         col = len(grid[0])
#         INF = 2147483647
#         direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
    
#         def bfs(r,c):
#             steps =0
#             q = deque()
#             q.append([r,c])
#             visited = set()
#             visited.add((r,c))
#             while q:
#                 for _ in range(len(q)):
#                     ro, co = q.popleft()
#                     if grid[ro][co] ==0:
#                         return steps
#                     for dr,dc in direction:
#                         nr, nc = ro+dr, co+dc
#                         if (0<=nr<row and 0<=nc<col and (nr,nc) not in visited and grid[nr][nc]!= -1):
#                             visited.add((nr,nc))
#                             q.append((nr,nc)) 
#                 steps+=1
#             return INF
#         for r in range(row):
#             for c in range(col):
#                 if grid[r][c] == INF:
#                     grid[r][c] =bfs(r,c)

# DFS
        row = len(grid)
        col = len(grid[0])
        INF = 2147483647
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(r,c,dis):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]== -1 or grid[r][c]<dis:
                return
            grid[r][c]=dis
            for dr, dc in direction:
                dfs(r+dr,c+ dc, dis +1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==0:
                    dfs(r,c,0)




