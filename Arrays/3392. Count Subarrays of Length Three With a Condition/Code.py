class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Intuition: simply use a 2 pointer appriach placed at 0 and 2 index, where they are both incremented after matching the condition.
        
        For condition we can simply (nums[l] + nums[r]) == (nums[l+1])/2 as well, it is also accepted.
        """
        l = 0
        res = 0
        for r in range(2, len(nums)):
            if (nums[l] + nums[r])*2 == nums[l+1]:
                res += 1
            l += 1
        
        return res


# O(n)
# O(1)
