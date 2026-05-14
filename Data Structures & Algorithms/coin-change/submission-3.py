class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recurse(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            result = float('inf')
            for i in coins:
                if amount - i>=0:
                    result = min(result,1+ recurse(amount - i))
            memo[amount] = result
            return result
        coin =recurse(amount)
        return -1 if  coin >= float('inf') else coin