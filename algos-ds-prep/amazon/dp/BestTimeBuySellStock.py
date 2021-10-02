class Solution:
    # Function to find the days of buying and selling stock for max profit.
    # tc = o(n) , sc = o(1)
    # This spproach is peaks and valleys approach
    def maxProfit(self, prices: List[int]) -> int:

        min_value = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > max_profit:
                max_profit = price - min_value
        return max_profit
