class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Intuition: Apply 2x Binary search for both rows and then thier columns in inner loop.
        bottom, top = 0, len(matrix) -1

        while bottom <= top:
            mid = (bottom + top) // 2

            if target < matrix[mid][0]:
                top = mid -1
            elif matrix[mid][-1] < target:
                bottom = mid +1
            else:
                l,r = 0, len(matrix[mid])

                while l <= r:
                    m = (l+r) // 2

                    if target < matrix[mid][m]:
                        r = m-1
                    elif target > matrix[mid][m]:
                        l = m+1
                    else:
                        return True

                return False

        return False


# O(logm + logn) = O(log(m.n))
# O(1)
