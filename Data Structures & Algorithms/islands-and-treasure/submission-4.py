class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF =2147483647
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,dis):
            if r<0 or c<0 or r>= rows or c>= cols:
                return
            if grid[r][c] == -1 or grid[r][c]< dis:
                return 
            grid[r][c] = dis
            for dr,dc in direction:
                dfs(r+dr,c+dc,dis+1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 0:
                    dfs(r,c,0)