class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Follow up after 2873. Maximum Value of an Ordered Triplet I. Intuition is now to remove the outer loop (3). Create a new array which holds the max value for each value after mid, eliminating the need to loop rest of the elements.

        N = len(nums)
        res = 0
    
        left = nums[0]
        # Not using copy results in modifying the actual nums array.
        dum = nums.copy()

        for i in reversed(range(N-1)):
            if dum[i] < dum[i+1]:
                dum[i] = dum[i+1]
            
        for mid in range(1, N-1):
            if nums[mid] >= left:
                left = nums[mid]
                continue
            
            res = max(res, (left - nums[mid]) * dum[mid+1])
    
        return res


# O(n)
# O(n)
