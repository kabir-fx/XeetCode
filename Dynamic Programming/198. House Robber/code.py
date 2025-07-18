class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP

        Intuition - The max at any given posititon can be found with this recurrence relationship:
                nums = [1,2,3,1]
                rob = max(
                    nums[i] + rob[2:], 
                    rob[i+1]
                    )
        
        Using this exp we hv tp caculate the max profit we can accumalate from all the houses.

        We use 2 variables to store the values (maximums) id [i-1] and [i-2] indexes. So for i = 3:
            rob1 = 1, rob2 = 2
        
        Then using the. expression we calculate the maximum of current index using the expression above.

        i = 0: r1 = 0, r2 = 0
            cur_max = 1
            r1 = 0, r2 = 1
        
        i = 1: r1 = 0, r2 = 1
            cur_max = 2
            r1 = 1, r2 = 2
        
        i = 2: r1 = 1, r2 = 2
            cur_max = 4
            r1 = 2, r2 = 4
        
        i = 3: r1 = 2, r2 = 4
            cur_max = 4
            r1 = 4, r2 = 4

        res = 4
        """
        
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            cur_max = max(
                        nums[i] + rob1,
                        rob2
                        )
            # Update the position of both the robs
            rob1 = rob2
            rob2 = cur_max
        
        # At the end rob2 will be at last element and will hold the maximum of the entire array
        return rob2



# O(n)
# O(1)
