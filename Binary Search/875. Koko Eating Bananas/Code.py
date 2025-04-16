class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Intuition: The range of solution will always be between [1, max(piles)], so we need to run Binary search in order to determine the smallest value.
        l, r = 1, max(piles)
        
        # Maximum will always be highest value in the pile, our goal is to minimize this value.
        res = r
        while l <= r:
            mid = (l+r) // 2
            
            # Dummy var. to hold the sum of all the dividends
            dum = 0

            for n in piles:
                dum += ceil(n / mid)
            
            if dum <= h:
                res = min(mid, res)

                r = mid -1
            else:
                l = mid +1
        
        return res


# O(logn.m)
# O(1)
