class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Intuition: Similar to top frequent elements. Our goal is to append the top frequent characters in res.

        We accompolish this by first creating a frequency counter and then utilizaing max-heap to pop the most frequent characters into res.
        """

        store = {}

        for c in s:                             # O(n)
            store[c] = 1 + store.get(c, 0)

        heap = []
        for k,v in store.items():               # O(m.logm)
            heapq.heappush(heap, (-v, k))
        
        res = ""

        for _ in range(len(heap)):              # O(m.logm)
            v,k = heapq.heappop(heap)
            cur = k * (-v)

            res += cur
        
        return res



# O(m.logm)             | m = no of uniques elements in the array
# O(n)                  | n = total no of elements in the array
