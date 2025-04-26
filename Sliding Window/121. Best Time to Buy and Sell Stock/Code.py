class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Intuition: use a 2 pointer approach intialized at 0 and 1, increment l only when a value lower than l is found at r.
        l = 0
        res = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            
            res = max(res, profit)

            if prices[l] > prices[r]: l = r
        
        return res


# O(n)
# O(1)
