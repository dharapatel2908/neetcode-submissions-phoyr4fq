class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        left =0 
        right = rows*cols -1
        while left <= right:
            middle = (right - left)//2 + left
            current_element = matrix[middle//cols][middle%cols]
            if current_element ==target:
                return True
            elif current_element> target:
                right = middle -1
            else:
                left = middle +1
        return False

