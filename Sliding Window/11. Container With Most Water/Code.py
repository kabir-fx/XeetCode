class Solution:
    def maxArea(self, ht: List[int]) -> int:
        # Intuition: use a 2 pointer approach with pointers intialized at 2 extreme ends. Now from whichever end we face a smaller value we move the pointer from it towards middle coz our goal is to reach the next maximum to store maximum water as that is only possible if the wall is bigger from smaller end.
        # For equal we move from left as we already start from extreme right end covering maximum area. Also if there is a right maximum value it will we be covered anyways when we compare rigth value with left maximum.
        l,r = 0, len(ht) -1
        res = 0

        while l < r:
            area = (r -l) * min(ht[l], ht[r])
            res = max(res, area)

            if ht[l] <= ht[r]:
                l += 1
            else:
                r -= 1

        return res


# O(n)
# O(1)
