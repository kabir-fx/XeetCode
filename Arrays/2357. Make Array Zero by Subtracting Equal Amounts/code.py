class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Intuition - This is a question to understand the problem. In our case the number of operations required will always be:
            no. of operations = unique elements in nums (excluding 0s)
        """

        nums = list(set(nums))
        res = [num for num in nums if num > 0]

        return len(res)
        

# O(n)
# O(n)
