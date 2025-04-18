class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Intuition: First find the pivot where the array is being divided into 2 sorted arrays. After finding the pivot we will determine in which half does the target lie in order to only search in that particular sub-array.
        l, r = 0, len(nums) -1

        # Always the smallest element in the array will be the pivot
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l
        l,r = 0, len(nums) -1

        # Determining whether the target is in the 2 half of the array
        if target >= nums[pivot] and target <= nums[r]:
            # If yes bring the lower bound to pivot to only search in 2 half
            l = pivot
        else:
            # else reduce the upper bound to pivot - 1
            r = pivot - 1

        # Typical Binary Search 
        while l <= r:
            m = (l+r) // 2
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1


# O(logn)
# O(1)
