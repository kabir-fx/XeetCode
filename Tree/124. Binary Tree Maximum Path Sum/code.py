# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Intuition - to find the maximum path we need to compute 2 caculations:

        1) Path sum with split i.e if we just focus on the root, what would be the sum of the path with = root + max(root.left) + max(root.right)
        2) Path sum without split i.e we bring the parent root in the picture, in doing so we cant select both the child of the current root we have to pick the max so = parentRoot + root + max(root.left, root.right)

        We will perform DFS to start the caculation from the leafe of the tree and then work our way up. We will caculate and updates the res for both of the operations at each node to find the maximum Path sum.
        """
        res = float("-inf")

        def dfs(root):
            nonlocal res

            if not root: return 0

            # Find both childs; since our aim is to maximise the sum - for the scenario where both of my chilren are -ve I'll be better off not adding either of them to my current sum, thus we replace them with 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # Operation 1 - Sum with the split
            res = max(res, root.val + left + right, root.val)

            # Operation 2 - Sum without the split; returning this since it will be used by parent root as well for their Operation 2
            return root.val + max(left, right)
        
        dfs(root)
        return res


# O(n)          | n = no. of nodes in the tree
# O(h)          | h = ht of the tree
