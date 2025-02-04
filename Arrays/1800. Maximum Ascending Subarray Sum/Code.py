class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                res = max(res, s)
                s = nums[i]
            else:
                s += nums[i]
        
        return max(res, s)
