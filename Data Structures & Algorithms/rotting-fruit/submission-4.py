class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        queue = deque()
        visited = set()
        fresh_fruit = 0
        time = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh_fruit +=1
        if fresh_fruit == 0:
            return 0
        while queue and fresh_fruit> 0:
            length = len(queue)
            for i in range(length):
                r,c = queue.popleft()
                for nr, nc in directions:
                    dr,dc = r+nr, c+nc
                    if dr<rows and dr>=0 and dc >=0 and dc<cols and grid[dr][dc] == 1:
                        grid[dr][dc] =2
                        queue.append((dr,dc))
                        fresh_fruit -=1
            time+=1

        return time if fresh_fruit== 0 else -1

        


        