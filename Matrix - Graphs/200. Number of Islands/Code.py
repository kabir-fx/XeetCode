class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Intuition is to run a bfs at a point and mark all the corresponding nodes as visited. When the bfs ends it results in complete trvaersal of an island i.e increment res. Similarly run the bfs for all the rest of the elements in the grid.

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    self.bfs(row, col, grid)
                    res += 1  # Increment island count after BFS
        
        return res

    def bfs(self, r, c, grid):
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(r, c)])  # Initialize the deque with the starting point
        grid[r][c] = "0"  # Mark the starting cell as visited

        while q:
            row, col = q.popleft()
            # Explore neighbors: up, down, left, right
            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]
            for nr, nc in neighbors:
                # Check if the neighbor is within bounds and is land
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    q.append((nr, nc))
                    grid[nr][nc] = "0"  # Mark as visited




# O(r.c)   ------> Outer loop and BFS ensure that each element is only visited once
# O(min(r.c))   -> In the worst case, the BFS queue will hold the maximum number of cells along one dimension of the grid at any given time.
