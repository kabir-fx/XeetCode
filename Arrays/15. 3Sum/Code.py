class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Intuition: Iteratively go over each element and then use the 2 pointer approach on the rest [Right Side] of the array. Sorting the array is crucial as it allows to keep track of unique elements and makes 2 pointer approach viable.
        
        # Goal is to reduce time complexity by making optimizations in the loop
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Break the loop since the array is sorted for all the elements > 0 its not possible to then result 0
            if nums[i] > 0: break

            # Make optimization by skipping all the duplicates
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            # Initialze the pointers
            l,r = i+1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Increment any pointer as the other pointer will be updated automatically
                    l += 1
                    # Optimize the code by skipping duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                elif s > 0:
                    r -= 1
                else:
                    l += 1
        
        return res


# O(n^2)
# O(m)
