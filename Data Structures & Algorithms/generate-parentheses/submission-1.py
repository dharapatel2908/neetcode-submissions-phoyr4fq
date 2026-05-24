class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def bt(s,i,c):
            if len(s) == 2*n:
                result.append(s)
                return
            
            if i< n:
                bt(s+'(',i +1,c)
            if i>c:
                bt(s+')',i,c+1)
        
        bt('',0,0)
        return result