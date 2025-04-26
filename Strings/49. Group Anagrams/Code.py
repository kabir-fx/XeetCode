class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Intuition: use a list of size 26 to store the occurence of each character in a word. After creating list of occurences of each characters, use this list as key and keep appending the words as values.

        Since, lists are mutable they cannot be used as keys in a hash map, hence we typecaste them to a tuple. So in hashmap:

        key -> value
        tuple(list containing all the occurences of each character) -> all the words matching the frequencies of characters in this list.          
        """
        
        # Ensures we can append elements even to a an uninitialized key
        hm = defaultdict(list)

        for s in strs:
            dum = [0]*26
            for c in s:
                dum[ord(c) - ord('a')] += 1
            
            hm[tuple(dum)].append(s)
        
        # Typecasting to list due to question's requirement
        return list(hm.values())

"""
Time Compl -> O(n*m)        where, n = number of words in strs; m = length of longest word     
Space Compl -> O(n): Extra Space
               O(n*m): Space for output list
"""
