class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp ={}
        def stairs(i):
            if i>=len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i]+ min(stairs(i+1), stairs(i+2))
            return dp[i]

        return min(stairs(0),stairs(1))