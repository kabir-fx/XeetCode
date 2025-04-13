# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Intuition: At every node inside the iteration for dfs we have to calculate the diameter [By adding the max heights of left and right] and then compare with res to determine the maximum.
        res = 0

        def dfs(root):
            nonlocal res
            if not root: return 0
            
            # Extract both the left and right max values            
            left = dfs(root.left)
            right = dfs(root.right)

            # Cal diam. at each node
            res = max(res, left + right)

            # Return the hieght to maintain dfs
            return 1 + max(left, right)          
        
        dfs(root)
        return res


# O(n)     | n is the number of nodes
# O(h)     | h is the height of the tree
