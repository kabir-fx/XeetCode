class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Intuition - we will use BFS approach, for each iteration after going thru all the neighbours we increment the count of minutes.

        q = deque()
        res = 0
        # We keep a count of current fresh oranges to indentify how many oranges are left after we are done iterating over all the possible neighbours
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        # Only increment the count of minutes if there are any fresh oranges present in the grid
        while q and fresh > 0:
            res += 1

            # Iterate thru all the neighbours in the current iteration
            for _ in range(len(q)):
                r,c = q.popleft()
                nb = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]

                for nr,nc in nb:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            
        return res if fresh == 0 else -1



# O(r*c)
# O(r*c)
