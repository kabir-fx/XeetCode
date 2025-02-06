class Solution:
    def check(self, nums: List[int]) -> bool:
        # Intuition is to use a Sliding Window approach to identify if there is a window of len = nums which has all the elements sorted.

        # We can either concatenate 2 nums arrays and then identify the window or better loop thru 1 to 2*len(nums) and for every index % N to always keep inex inbound.
        N = len(nums)

        # Window intialized with 1 as len ois of 0 - indexed array.
        cnt = 1

        if N==1: return True

        for i in range(1, 2*N):
            # If the current elemtn is greater than the prev i.e is sorted:
            if nums[i%N -1] <= nums[i%N]:
                cnt += 1
                if cnt == N:
                    return True
            else:
                cnt = 1
        
        return False




# O(n)
# O(1)
