class Solution:
    def maxDepth(self, s: str) -> int:
        # Intuition: Like what are we doing here

        res = 0
        cur = 0

        for c in s:                     # O(n)
            if c == '(':
                cur += 1
            elif c == ')':
                cur -= 1
            
            res = max(res, cur)
        
        return res


# O(n)
# O(1)
