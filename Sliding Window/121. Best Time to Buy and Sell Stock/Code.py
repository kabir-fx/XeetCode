class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Intuition: use a 2 pointer approach intialized at 0 and 1, increment l only when a value lower than l is found at r.
        res = 0

        l,r = 0, 1

        while r < len(prices):
            res = max(res, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1

        return res


# O(n)
# O(1)
