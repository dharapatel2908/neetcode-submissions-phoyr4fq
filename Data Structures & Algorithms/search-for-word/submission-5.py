class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])

        def bt(i,r,c):
            if i ==len(word):
                return True
            if r<0 or r>= rows or c<0 or c>= cols:
                return False
            
            if word[i] != board[r][c] or board[r][c] =="#":
                return False
            temp = board[r][c]
            board[r][c] ="#"
            found = (bt(i+1,r+1,c) or bt(i+1,r-1,c) or bt(i+1,r,c+1) or bt(i+1,r,c-1))
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if bt(0,r,c):
                    return True
        return False