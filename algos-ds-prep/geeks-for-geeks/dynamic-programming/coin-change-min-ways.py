import sys


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeImpl(coins, amount)

    def coinChangeImpl(self, coins, amount) -> int:

        dp = [sys.maxsize for i in range(amount + 1)]

        dp[0] = 0

        for i in range(1, len(dp)):

            for coin in coins:

                if coin <= i:
                    sub_result = dp[i - coin]
                    if sub_result != sys.maxsize and sub_result + 1 < dp[i]:
                        dp[i] = 1 + sub_result
        if dp[amount] == sys.maxsize:
            return -1

        return dp[amount]