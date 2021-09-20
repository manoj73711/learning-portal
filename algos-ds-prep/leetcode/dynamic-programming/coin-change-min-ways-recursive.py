import sys
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeImpl(coins, amount)

    def coinChangeImpl(self, coins, amount) -> int:

        if amount == 0:
            return 0

        res = sys.maxsize

        for coin in coins:

            if coin <= amount:
                sub_result = self.coinChangeImpl(coins, amount - coin)
                if sub_result != sys.maxsize and sub_result + 1 < res:
                    res = sub_result + 1

        return res


