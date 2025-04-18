class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Intuition: our aim is to strictly find the minimum element. Using binary seach we we have to only focus on the specific portion of sub-array that actually contains the minimal element. 
        # The goal is at the end of the iteration our l will actually point to the minimal element that we have been searching the entire time
        
        l,r = 0, len(nums) -1
        if nums[l] < nums[r]: return nums[0]

        # Can't use <= otherwise we would be stuck in infinite loop due to else condition
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # If we use the generic [mid -1] then there's a chance to miss the smallest element in this case: [3,1,2]
                r = mid
            
        return nums[l]


# O(logn)
# O(1)
