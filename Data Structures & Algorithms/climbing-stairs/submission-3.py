class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0:0,1:1,2:2}
        def stairs(i):
            if i in dp:
                return dp[i]
            dp[i] = stairs(i-1)+stairs(i-2)
            return dp[i]
        return stairs(n)
