class Solution:
    def pacificAtlantic(self, ht: List[List[int]]) -> List[List[int]]:
        # Intuition - we have to only focus on starting from borders. We keep a set for both the oceans and then start the bfs from all the nodes present at the edge of the matrix. The indexes that have intersection in both the sets are the results.

        # From the edge we will only propogate for the pairs that hv value >= current pair [Reverse Thinking].
        pas_hs, atl_hs = set(), set()
        res = []
        ROWS, COLS = len(ht), len(ht[0])

        def bfs(r,c,visit):             
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r,c = q.popleft()

                nb = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),     
                    (r, c - 1)
                ]

                for nr,nc in nb:        
                    if 0 <= nr < ROWS and 0 <= nc < COLS and ht[r][c] <= ht[nr][nc] and (nr,nc) not in visit:
                        q.append((nr,nc))
                        # Appending the pairs here itself otherwise we will hv to wait for this loop to be over in order append to set. Making numerous repeated calls to the common eligible neighbours
                        visit.add((nr,nc))


        for r in range(ROWS):           # O(r.c)
            # Pacific Border [Left col]
            bfs(r, 0, pas_hs)
            # Atl Border [Right Col]
            bfs(r, COLS-1, atl_hs)
        

        for c in range(COLS):           # O(r.c)
            # Pacific Border [Top Row]
            bfs(0, c, pas_hs)
            # ATL Border [Bottom Row]
            bfs(ROWS - 1, c, atl_hs)
                 
        for r in range(ROWS):           # O(r.c)
            for c in range(COLS):
                # Append the pairs that are present in both the sets
                if (r,c) in pas_hs and (r,c) in atl_hs:
                    res.append([r,c])
        
        return res



# O(r.c)
# O(r.c)
