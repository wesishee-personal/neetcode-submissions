class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right = left + 1
                continue
            if prices[right] - prices[left] <= max_profit:
                if right == len(prices) - 1 and left < right:
                    left += 1
                else: right += 1
            else:
                max_profit = prices[right] - prices[left]
                right += 1
        return max_profit

        # while buy <= len(prices)-2:
        #     if sell == len(prices):
        #         buy += 1
        #         sell = buy + 1
        #         continue
        #     current_profit = prices[sell] - prices[buy]
        #     if current_profit > profit:
        #         profit = current_profit
        #     sell += 1
        # return profit