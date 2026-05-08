class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def stairs(i):
            if i<=2:
                return i
            if i in dp:
                return dp[i]
            dp[i] = stairs(i-1)+stairs(i-2)
            return dp[i]
        return stairs(n)
