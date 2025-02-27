class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Intuition is to run a brute force approach where we pair all the values in the arr. 
        # We can slightly optimize it by storing all the values in the hashset/map to quickly iterate/identify the values in the arr which may imitate Fib. like behaviour.
        
        # Set to store all the val in arr 
        hs = set(arr)
        res = 0

        for i in range(len(arr) -1):
            for j in range(i+1, len(arr)):         # j will always be +1 than i
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                
                # Identifying whether the fib no corresponding to i and j is present in arr.
                while nxt in hs:
                    length += 1
                    prev,cur = cur,nxt
                    nxt = prev + cur

                    # Can also add after the while loop has ended but A/Q in the case where the while condition evaluates to false it will still append the res to 2 which is not as per expected behaviour.
                    res = max(res, length) 

        return res



# O(n^2.logn)
# O(n)
