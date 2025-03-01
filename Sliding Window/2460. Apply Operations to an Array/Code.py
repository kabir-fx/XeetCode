class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # For the I half the problem used the linear approach
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2

                nums[i+1] = 0
        
        # II half can be solved by allocating extra memory for a new array
        # res = [0] * len(nums)
        # ant = 0

        # # for n in nums:
        # #     if n == 0:
        # #         continue

        # #     res[ant] = n
        # #     ant += 1

        # # return res    


        # This is approach changes the array in place using Quick sort principles.
        # Here, l tracks the non - zero no and keeps shifting with the i pointer whenever a new NZ element is found but stays there if i is zero. Whenever i again becomes NZ is exhanges its values and increments by 1.
        # This ensures if there is ever a NZ element present after the exhange it will be exchanged again with i.
        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        
        return nums




# O(n)
# O(n)
