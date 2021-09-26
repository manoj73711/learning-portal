from typing import List


#No of ways to make an amount with given coin denominations provided infinite number of coins
#TC: SC:
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        return self.changeImpl(coins, amount, len(coins))

    def changeImpl(self, coins: List[int], amount: int, n: int) -> int:

        if amount == 0:
            return 1
        if n == 0 or amount < 0:
            return 0

        res = int(self.changeImpl(coins, amount, n - 1))

        if coins[n - 1] <= amount:
            res += int(self.changeImpl(coins, amount - coins[n - 1], n))

        return res
