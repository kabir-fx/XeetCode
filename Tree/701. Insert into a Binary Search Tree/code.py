# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Intuition: our aim is to reach the left node while traversing the tree using BST's properties. 
        
        We then attach the newly created node to the older None position
        """
        new_node = TreeNode(val)
        if not root:
            return new_node

        cur = root
        
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = new_node
                    return root
                cur = cur.right
            
            else:
                if not cur.left:
                    cur.left = new_node
                    return root
                cur = cur.left


# O(h)      | Since we are following BST's principles and not bfs/dfs
# O(1)
