class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Intuition for each pair in [left, mid, right] is to [max, min, max].
        N = len(nums)
        res = 0

        # Start the first pointer at 0 index
        left = nums[0]

        # Inntialize 2 pointer [mid] from the next position 
        for mid in range(1, N):
            # If the mid val is greater than previos, we skip initializing 3 pointer to avoid redundant work.
            if nums[mid] >= left:

                # Bring the left pointer to current the value and then start the 2 pointer from next position in next iteration.
                left = nums[mid]
                continue
            
            # If the mid value is smaller than left value we then initialize right pointer to calculate res against all the remaining values.
            for right in range(mid +1, N):
                res = max(res, (left - nums[mid]) * nums[right])
        
        return res


# O(n^2)         [Will be optimized in 2874. Maximum Value of an Ordered Triplet II]
# O(n)
