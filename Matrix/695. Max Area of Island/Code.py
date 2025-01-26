class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Same as 200, just we use a variable to store the max area.

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0

            cnt = 0

            while q:
                r,c = q.popleft()
                cnt += 1

                nb = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

                for nr,nc in nb:
                    if nr == ROWS or nr < 0 or nc < 0 or nc == COLS or grid[nr][nc] == 0:
                        continue
                    else:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            
            return cnt
        
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res = max(res, bfs(r, c))

        
        return res





# O(r.c)
# O(min(r.c))
