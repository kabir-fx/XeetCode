class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition - we will hv to divide the problem into smaller parts, instead of creating all the permutations of [1,2,3] we divide it into:
            [1,2,3] -> [2,3] -> [3]

        We then find all the permutations of [3] i.e [3]. We then go to the previous lvl [2,3] and add 2 to all possible indexes (len([2,3])) i.e 0 and 1 here.

        The permuation becomes -> [[2,3], [3,2]]

        We do the same for 1 and add it to all 3 indexes for both of these solutions
        """

        # Base case
        if len(nums) == 0:
            return [[]]
        
        # Keep breaking the list into smaller sub-problems by keep removing the 1 element. Since we get multiple permutations after breaking down - [[2,3], [3,2]], we store them all in the list
        new_perm = self.permute(nums[1:])
        res = []

        # Get the current iteration of permutation
        for p in new_perm:
            # Iterate thru all the possible indexes where we can place the element, +1 coz we can also place at the end of the list
            for i in range(len(p) +1):
                p_copy = p.copy()
                # Insert the prev element
                p_copy.insert(i, nums[0])

                # Append all the possible permutations in res and then forward it to the previous element. So the res which we will get for the final iteration will be 1 element short of being == len(nums)
                res.append(p_copy)

        return res


# O(n! * n^2)
# O(n! * n)
