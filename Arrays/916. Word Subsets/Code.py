class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Intuition is to create a unified Hash Map for the 2 list which includes the max of the count of characters. 
        # On comparison with list 1, if the count is greater than unified list then append in the res list.

        # Hash Map to store the count of the entire 2 list
        count_2 = defaultdict(int)
        for w in words2:
            # Hash Map for the count of each word
            count_w = Counter(w)
            
            for c, cnt in count_w.items():
                # Comparison b/w values in unified dict and values of the current word
                count_2[c] = max(count_2[c], cnt)

        res = []
        # 2 list iteration
        for w in words1:
            count_1 = Counter(w)
            flag = True
            for c, cnt in count_2.items():
                if count_1[c] < cnt:
                    flag = False
                    break
            
            res.append(w) if flag else None
                
        return res
