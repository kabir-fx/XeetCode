class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Intuition: we need to maintain a min-heap which will help maintain the dist of min. pairs in order.
        # We will then extract the top k elements from this min heap
        min_heap = []
        res = []

        for i,j in points:          # O(n.logn)
            cur_sum = math.sqrt((i) ** 2 + (j) ** 2)

            heapq.heappush(min_heap, [cur_sum, [i, j]])
        
        for _ in range(k):          #O(k)
            res.append(heapq.heappop(min_heap)[1])
        
        return res



# O(n.logn)          | n.logn can be converted to k.logn if we just insert the elements normally in min_heap (O(n)) and then heapify(O(logn)) instead of heappushing.
# O(n)
