class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Intuition: we hv to try to avoid adding -ve numbers to our net sum (res). Whenever we see the cur_sum is -ve we replace it with 0 in order to find max sum.

        # Initializing with [0] to handle the edge case where nums = [single -ve no]
        res = nums[0]
        cur_sum = 0

        for n in nums:                  # O(n)
            cur_sum = max(cur_sum, 0) 

            cur_sum += n
            
            res = max(res, cur_sum)
        
        return res


# O(n)
# O(n)
