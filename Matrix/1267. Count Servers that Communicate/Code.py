class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Intuition is to in first iteration find the row_sum and col_sum for each row and col. Then in the next iteration if the element has either (row_sum or col_sum) > 1 whilst also being a server we increment the res.

        ROWS, COLS = len(grid), len(grid[0])

        row_cnt, col_cnt = [0] * ROWS, [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    # Incrementing the values corresponding to their respective row and col
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    if row_cnt[r] > 1 or col_cnt[c] > 1:
                        res += 1

        return res







# O(r.c)
# O(r.c)
