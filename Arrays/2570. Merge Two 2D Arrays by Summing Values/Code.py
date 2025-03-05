class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []

        # Instead of popping out the elements uitilize 2 pointers for the 2 given arrays and increment the pointers to traverse both arrays(both are sorted) and compare their first element.

        l,r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] == nums2[r][0]:
                res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])

                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                res.append(nums1[l])

                l += 1
            else:
                res.append(nums2[r])

                r += 1
        
        if l < len(nums1): 
            while l < len(nums1):
                res.append(nums1[l])
                l += 1

        if r < len(nums2): 
            while r < len(nums2):
                res.append(nums2[r])
                r += 1

        return res



# O(n + m)
# O(1)
