class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        island = 0
        visited = [[False for _ in range(col)]for _ in range(row)]

        def dfs(r,c,grid,visited):
            if r< 0 or c<0 or r>= row or c>= col:
                return
            if grid[r][c] =="0":
                return
            if visited[r][c] == True:
                return

            visited[r][c] = True
            dfs(r,c+1,grid,visited)
            dfs(r,c-1,grid,visited)
            dfs(r-1,c,grid,visited)
            dfs(r+1,c,grid,visited)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] =="1" and visited[r][c] == False:
                    island+=1
                    dfs(r,c,grid,visited)
        return island