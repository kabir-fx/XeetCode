class Solution:
    def climbStairs(self, n: int) -> int:
        """
        DP - Bottom-Up

        Intuition - This problem can be solved with recursion but it wont be optimal as we would hv to do repeated work for a lot of cases:

            dfs(0)
            ├─ dfs(1)
            │  ├─ dfs(2)
            │  │  ├─ dfs(3) → i == n → return 1
            │  │  └─ dfs(4) → i > n → return 0
            │  │  return 1 + 0 = 1
            │  └─ dfs(3) → i == n → return 1
            │  return 1 + 1 = 2
            └─ dfs(2)
               ├─ dfs(3) → i == n → return 1
               └─ dfs(4) → i > n → return 0
               return 1 + 0 = 1
            return 2 + 1 = 3
        
        Here we are doing repeated work for dfs(2), dfs(3) and dfs(4)

        The optimal approach will be to cache the result of for the n which we have already caculated. Thus we use DP. We can use both Top-Down/Bottom-Up appraoch but since we hv to find all possible ways to climb the stairs - Bottom-Up approach is more intuitive.

        We will maintain a cache of size n+1 and then start from -1 and -2 indexes. cache[-1] = 1 (default value) and cache[-2] = 1 since there is only one way of going from n-1 to n that is by adding 1. Then for each of the rest indexes (reversed order) the value of the current idex wil the sum of its i+1 and i+2 indexes.
        """

        cache = [0] * (n+1)

        for i in reversed(range(n+1)):
            if i >= n-1:
                cache[i] = 1
            else:
                cache[i] = cache[i+2] + cache[i+1]
        
        return cache[i]


# O(n)
# O(n)
