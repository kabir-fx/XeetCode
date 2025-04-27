class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition: First get all the frequencies of all the elements in nums. [Similar to Counter]. So the format in heashmap is: 

        key -> value
        n -> freq 

        Then we will utilize a min-heap. First for each n,f pair in hashmap we will heappush the pairs in the form of tuples -> (f, n). This ensures that f is used for calculations and appending in this min-heap.

        Now whenever the len(heap) > k, we heappop the smallest pair form this min-heap ensuring that only the 2 largest pairs are kept in the min-heap.

        Heap after 1 push: [(3,1)]
        Heap after 2 push: [(2,2), (3,1)]
        Heap after 3 push: [(1,3), (3,1), (2,2)] → now size > k ➔ pop (1,3)
        
        Then at the end we append the k in a list k times
        """
        hm = {}
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        # O(n)

        heap = []
        for n,f in hm.items():
            heapq.heappush(heap, (f,n))

            # Remove the smallest amongst all the pairs 
            if len(heap) > k:
                heapq.heappop(heap)
        # O(n.logkt)   -> Each heap operation takes logk time as size of heap only frows upto k.

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        # O(k.logkt)

        return res


# O(n.logkt)          | n is the no of elements in nums; k is the number of top frequent elements
# O(n+k)
