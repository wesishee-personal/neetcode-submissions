func maxProfit(prices []int) int {
	maxProfit := 0
	if len(prices) < 2 {
		return 0
	}
	if len(prices) == 2 {
		maxProfit = prices[1] - prices[0]
		return max(maxProfit, 0)
	}
	left, right := 0,1
	for left < right {
		currentProfit := prices[right] - prices[left]
		if currentProfit > maxProfit {
			maxProfit = currentProfit
		}
		if currentProfit < 0 {
			left++
			right++
		} else {
			right++
		}
		if right >= len(prices) {
			right--
			left++
		}
	}
	return maxProfit
}
