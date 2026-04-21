class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Method 1:
        # If we directly go to the last element of the each row and compare it if the target is smaller then only search that row or else skip it.
        rows, cols = len(matrix), len(matrix[0])
        r,c = 0,cols-1

        while r< rows and c>= 0:
            if matrix[r][c]> target:
                c-=1
            elif matrix[r][c]< target:
                r+=1
            else:
                return True
        return False


        #Method 2:
        # If we just consider the 2D matrix as big 1D sorted array and then search the element
