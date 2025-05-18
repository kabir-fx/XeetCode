class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Intuition: use a hashmap to store the freq of both the strings and then return their comparison
        h1, h2 = {}, {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            h1[s[i]] = 1 + h1.get(s[i], 0) 
            h2[t[i]] = 1 + h2.get(t[i], 0)

        return h1 == h2 


# O(n)
# O(n)
