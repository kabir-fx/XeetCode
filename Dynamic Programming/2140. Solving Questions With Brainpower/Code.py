class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        # The question involves either skipping or accepting each of the k,v pair in the array to maximize our output, this gives the intuition to utilize recursive backtracking approach.
        
        # Use cache to optimize the code and avoid recalculation
        cache = [0] * len(q)
        
        def baxk(i):
            # Base case to break out of recursion
            if i >= len(q): return 0

            # If the value is already calculated prviosuly avoid recalculation
            if cache[i]: return cache[i]
            
            reward, cost = q[i]
            
            cache[i] = max(
                # Skip the current pair
                baxk(i + 1),

                # Choose the current pair
                reward + baxk(cost + 1 + i)
            )

            return cache[i]
        
        return baxk(0)


# O(n)  [with help of caching]
# O(n)
