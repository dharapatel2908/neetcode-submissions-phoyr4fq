class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        area_max = 0
        def dfs(r,c):
            if r<0 or c<0 or c>= cols or r>= rows:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            area = dfs(r+1,c) +dfs(r-1,c) +dfs(r,c+1)+dfs(r,c-1)
            return area +1
        
        for r in range(rows):
            for c in range(cols):
                area_max = max(area_max,dfs(r,c))
        return area_max
