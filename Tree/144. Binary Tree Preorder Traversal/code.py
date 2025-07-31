# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Intuition - Since we have to focus on appending left side values of tree first thus we will call the recursive function on left first, for the cases where no left child is present or for the cases where only the root is present or if there is only right node we call dfs on right node as well.
        """

        res = []

        def dfs(root):                      # O(n)
            if not root: return None

            res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res


# O(n) | we visit each node once
# O(n) | equal to the size of tree
