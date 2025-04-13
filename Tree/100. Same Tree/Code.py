# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Intuition: filter out all the cases where we dont have both the nodes with same val.
        if (not p and not q): return True

        # Only continue the iteration when we have both non-null nodes with same values
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Return False for anything else
        return False
    

# O(n)
# O(n)      | The total space used is the number of stack frames times the space per frame -> O(1) * O(n)
