class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Intuition is to use 2 pointer approach on both lists but we need to return queries in orignal order in which they are given.
        
        items.sort()

        q_i = sorted((q, i) for i,q in enumerate(queries))

        res = [0] * len(queries)
        mx = 0
        i = 0
        for q, idx in q_i:
            while i < len(items) and items[i][0] <= q:
                mx = max(mx, items[i][1])
                i += 1
            
            res[idx] = mx

        return res

