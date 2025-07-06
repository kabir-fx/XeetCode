class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Intuition: sort the products as required. Then we will start building the entire searchWord char by char. We will then match this building searchWord with the starting indexes of all the products present in the sorted products.
        products.sort()
        res = []

        cur_w = ""
        for i,c in enumerate(searchWord):       # O(n)
            cur = []
            cur_w += c

            for p in products:      # O(k)
                if i < len(p) and cur_w == p[:i+1] and len(cur) < 3:
                    cur.append(p)
            
            res.append(cur)
        
        return res


# O(n.k)
# O(n)
