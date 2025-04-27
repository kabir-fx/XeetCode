class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Intution: we will use 3 separate hashmap to store the hashsets of all correspondings rows, cols and sq. This hashmap can also be interchanged for a list in list.

        We will use index of each corresponding rows or cols to identify in their correspondings hashmaps.

        rows[2] ---> will be used to identify the the elements of the 2 row in the matrix. All the elements of this 2 row will be stored at this index. Here, row is a hashmap and 2 is the index of the hashset. In hashmap:

        key -> val
        index -> hashset

        For 3x3 sq in the matrix, we divide the corresponding r,c each by 3 [lower] to yield in which sq will the element lie. For ex:
        
        for matrix[2][3] it will lie in [2//3, 3//3] -> [0,1] quadrant of the matrix. Hence, using this anotation the entire matrix can be divided into 9 quadrants. For sq matrix instead of a single index it will hold index in this form:
        
        key -> val
        (r // 3, c // 3) -> hashset

        For each element in the matrix first we will check whther its already present in any of the quadrants [return False if yes] else we then append this element in all of 3 hashmaps
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sq = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sq[(r//3,c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sq[(r//3, c//3)].add(board[r][c])
        
        return True


# O(n^2)
# O(n^2)
