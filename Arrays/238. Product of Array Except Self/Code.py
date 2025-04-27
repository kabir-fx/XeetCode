class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Intuition: We maintain a prefix and a suffix array to store the product upto that element. We then multiply these arrays to yield result.

        To optimize memory we utitilize a single list where we perform all operation
        
        For nums = [1,2,3,4]

        1 Pass:
        [1,1,2,6]

        2 Pass:
        [24,12,4,1]

        When we multiply these 2
        """
        res = [1] * len(nums)
        prefix = 1
        for i,n in enumerate(nums):
            res[i] = prefix
            prefix *= n

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# O(n)
# O(1)      | Output array not considered as extra space
