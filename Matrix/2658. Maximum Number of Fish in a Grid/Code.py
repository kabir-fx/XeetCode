class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # SOLVED BY SELFFFFFFFFF!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Use DFS to find the total area of a pond and mark all the nb as 0 after visitng. Track the max and return the res.

        def dfs(r,c):
            res = 0
            res += grid[r][c]

            grid[r][c] = 0

            nb = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for nr, nc in nb:
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid[nr][nc] == 0:
                    continue
                else:
                    res += dfs(nr, nc)
        
            return res


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    res = max(res, dfs(r, c))

        return res





# O(r.c)  >>>>>>>>>>>>>>>>> Each cell is visited only once in worst case
# O(r.c)
