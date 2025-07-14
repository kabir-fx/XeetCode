class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Intuition - We will start our bfs search from the edge of the matrix. For all the pair of indexes that are eligible we will replace them with "A".

        After all the elgible pairs hv been marked we will run the loop to replace:
                A -> O
                O -> X
        """
        ROWS, COLS = len(board), len(board[0])

        def bfs(r,c):
            q = deque([(r,c)])
            board[r][c] = "A"

            while q:
                r,c = q.popleft()

                nb = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]

                for nr,nc in nb:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                        q.append((nr,nc))
                        # Mark the current pair as soon as found to eliminate the repeated traversal among the neighbours
                        board[nr][nc] = "A"

        
        for r in range(ROWS):                   # O(r.c)
            if board[r][0] == "O":  bfs(r,0)
            if board[r][COLS - 1] == "O":  bfs(r,COLS - 1)

        for c in range(COLS):                   # O(r.c)
            if board[0][c] == "O":  bfs(0,c)
            if board[ROWS - 1][c] == "O":  bfs(ROWS - 1,c)

        for r in range(ROWS):                   # O(r.c)
            for c in range(COLS):
                if board[r][c] == "A":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"



# O(r.c)
# O(r.c)
