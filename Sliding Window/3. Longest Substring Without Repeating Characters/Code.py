class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Intuition: use a sliding window approach to determine the length of the maximum window

        If we find a duplicate we need to remove the element at l pointer until that duplicate has not been removed from the set.

        Update the res at every step to determine maximum.
        """
        res,l = 0, 0

        hs = set()

        for r in range(len(s)):
            while hs and s[r] in hs:
                hs.remove(s[l])
                l += 1
            
            hs.add(s[r])
            res = max(res, r-l+1)
        
        return res


# O(n)           n -> number of elements in list; The time complexity is O(n) because each character in the string is processed at most twice: once when added to the set (hs.add(s[r])) and once when removed from the set (hs.remove(s[l])) if a duplicate is found.
# O{m}           m -> number of unique elements
