# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Intuition: 1) use dfs | 2) Take the max no. upto that point down with us.

        # Create a separate function to help take max val down. Return the net res indicating total good nodes
        def dfs(root, mx):
            if not root:
                return 0

            # If current node is good, increment the count and undate the max val. with itself 
            if root.val >= mx:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, mx) + dfs(root.right, mx)

        # Intialize the recursion as root is considered good 
        return dfs(root, root.val)


# O(n)
# O(h)
