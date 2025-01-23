class Solution:
    def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
        # Intuition is to use Multi-Source BFS [BFS with multiple starting points]

        # For all the water in matrix, we start a bfs i.e inserting into queue. For all their neighbours which are not visited we increase their value by 1.

        ROWS, COLS = len(mat), len(mat[0])

        # Can also do without a Hashset by marking the rest of the points as -1 and then identifying and incrementing only those neighbours who are -1.
        q,s = deque(), set()

        # Intializing the queue and Hashset with elements containing the water.
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    q.append((r,c))
                    
                    # Marking as visited 
                    s.add((r,c))

                # Reintializing all the values in the matrix, basically like creating a new matrix.
                mat[r][c] = 0

        while q:
            r,c = q.popleft()

            # Finding all the possible neighbours
            nb = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]

            for n1,n2 in nb:
                # Removing the visited as well as invalid neigbours
                if ((n1, n2) in s) or n1 < 0 or n1 == ROWS or n2 < 0 or n2 == COLS:
                    continue
                else:
                    # Incrementing the ht
                    mat[n1][n2] = mat[r][c] + 1

                    q.append((n1, n2))
                    
                    # Mark as visited
                    s.add((n1, n2))
            
        
        return mat






# O(r.c)     -> r=row, c=col
# O(r.c)
