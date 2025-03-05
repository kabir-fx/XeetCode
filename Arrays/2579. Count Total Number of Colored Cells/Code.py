class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1

        # The series follow a pattern where each next iteration is a multiple of 4. We exploit it.

        for i in range(n):
            res += (4 * i)

        return res


# O(n)
# O(1)
