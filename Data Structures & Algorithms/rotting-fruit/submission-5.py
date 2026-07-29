class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid),len(grid[0])
        fresh_fruit = 0
        time = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    fresh_fruit +=1
                if grid[r][c] ==2:
                    queue.append((r,c))
       
        while queue and fresh_fruit>0:
            for _ in range(len(queue)):
                r,c  = queue.popleft()

                for dr,dc in directions:
                    nr = r +dr
                    nc = c+dc
                    if 0<= nr< rows and 0 <= nc < cols and grid[nr][nc] ==1:
                        grid[nr][nc]=2
                        queue.append((nr,nc))
                        fresh_fruit -=1
            time +=1
        return time if fresh_fruit ==0 else -1