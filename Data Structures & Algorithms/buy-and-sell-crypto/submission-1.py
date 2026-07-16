class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy,sell = 0,1
        profit = 0

        while buy <= len(prices)-2:
            if sell == len(prices):
                buy += 1
                sell = buy + 1
                continue
            current_profit = prices[sell] - prices[buy]
            if current_profit > profit:
                profit = current_profit
            sell += 1
        return profit