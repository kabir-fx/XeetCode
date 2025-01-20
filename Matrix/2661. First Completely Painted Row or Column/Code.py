class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Intuition is to solve 2 Gaps: 1 - Determine where are the elements in the array exactly positioned in the matrix as the order may vary. 2 - How to determine when a row or a col is completely filled.

        # For 1: we use a hashmap to store the r,c coordinates for each element in array. For 2: we keep track of 2 arrays for a row and a col. Whenever the count of the either row,col reaches the threshold after appending we return the index as res.
        
        ROWS, COLS = len(mat), len(mat[0])

        # n -> (r, c)
        map = {}

        # Appending all the elements in the HashMap
        for r in range(ROWS):
            for c in range(COLS):
                map[mat[r][c]] = (r, c)


        # Initializing both the arrays to store the count of the all the marked elements for each row and col as we traverse the array.
        row, col = [0] * ROWS, [0] * COLS

        for i,n in enumerate(arr):
            r,c = map[n]

            row[r] += 1
            col[c] += 1

            # Verifying whether we hv crossed the index
            # Logic for condition on RHS: eg - COLS tells us how many no. of columns are present in the matrix but not how many elements does each col. have beneath it; that is determined by the no of ROWS. Hence, we determine whther count is equal to no of rows or not signifing whther whole col is occupied
            if row[r] == COLS or col[c] == ROWS:
                return i





# O(n.m)      n -> ROWS, m -> COLS
# O(n.m)      For building the hashmap which stores all the m.n elements of the matrix
