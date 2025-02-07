class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if k >= len(nums): return nums

        cnt_mp = Counter(nums)

        mx_heap = [[-v, k] for k,v in cnt_mp.items()]

        heapq.heapify(mx_heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(mx_heap)[1])
        
        return res
