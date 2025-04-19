class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Intuition: Leyman approach is to use a Hashmap which will yield a O(n) comlpexity with a single pass solution. But can we make O(1) space solution by utilizing the sorted nature of the array.

        # Approach is to use a Binary Search esque solution except we calculate cur_sum instead of target and yield a O(n) solution.
        l,r = 0, len(nums) -1

        while l < r:
            cur_sum = nums[l] + nums[r]

            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        
        return -1


# O(n)
# O(1)
