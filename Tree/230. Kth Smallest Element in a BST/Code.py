# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Intuition: either use in-order traversal as it would directly yield a sorted array. II) After reaching the root from the left portion we keep decrementing k until it reaches 0 and yields the solution.
        cnt, res = k, root.val

        def dfs(root):
            nonlocal res, cnt

            if not root: return

            dfs(root.left)
            
            cnt -= 1

            if cnt == 0:
                res = root.val
                return

            dfs(root.right)
        
        dfs(root)
        return res


# O(n)
# O(n)
