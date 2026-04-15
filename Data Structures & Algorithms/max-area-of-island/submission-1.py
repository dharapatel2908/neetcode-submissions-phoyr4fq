class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        max_val = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>= col:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1 +dfs(r,c+1)+dfs(r,c-1)+dfs(r+1,c)+dfs(r-1,c)
        
        for r in range(row):
            for c in range(col):
                max_val = max(dfs(r,c),max_val)
        return max_val
