class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        f1 = True if (nums[0]%2 == 0) else False
        f2 = not f1
        
        for i in range(1, len(nums)):
            if nums[i]%2 == nums[i-1] & 1:
                return False

        return True
