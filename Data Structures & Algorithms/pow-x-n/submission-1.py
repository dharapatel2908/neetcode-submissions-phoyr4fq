class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        
        result =1
        abs_n =abs(n)

        for _ in range(abs_n):
            result*=x
        
        if n< 0:
            result = 1/result
        
        return result