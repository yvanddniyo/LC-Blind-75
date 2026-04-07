from typing import List

# Two Pointer


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # left -> r -> sell
        maxP = 0

        while r < len(prices):  # We move r forward through the array
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


prices = [7, 1, 5, 3, 6, 4]

s = Solution()
result = s.maxProfit(prices)
print("->", result)
