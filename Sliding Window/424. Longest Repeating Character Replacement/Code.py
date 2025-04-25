class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Intuition: use a hash map tp store the freq. of all the elements present in the sliding window. There we will track the variable with the highest freq and ensure that the difference b/w the this element of highest freq and the window size never differ more than k. 
        
        We update the window size whenever difference is more than k by decrementing the freq in hashmap and and incrementing the l of window.

        Also if it happens that the 1 element [l] has to be replaced with another element [since diff is greater than k], this approach ensures that we pick next immediate element after l [excluding duplicates].
        """
        hm = {}
        res = 0

        l = 0
        # Variable to point to the highest freq of an element in trhe hashmap 
        maxf = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1

            # Always compare after incrementing whether maxf has changed or not
            maxf = max(maxf, hm[s[r]])

            while (r-l +1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r-l +1)              
        
        
        return res


# O(n)
# O(m)
