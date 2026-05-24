class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col = len(matrix), len(matrix[0])
        rows, cols = [False]* row , [False]*col

        for r in range(row):
            for c in range(col):
                if matrix[r][c] ==0:
                    rows[r] = True
                    cols[c] = True
        for i in range(row):
            for j in range(col):
                if rows[i] or cols[j]:
                    matrix[i][j] =0
        
                