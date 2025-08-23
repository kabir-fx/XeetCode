# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Intuition: we will run a bfs search and then at each lvl we will determine whether we have to append the lvl as it is or first reverse the lvl and then append it.

        The time complexity for the overall algorithm will remain O(n) since we are reversing only half a times, so time required to run these extra operations sums upto to O(n), thus ensuring the overall time complexity remains at O(n)

        Instead of using a flag we could also ensure that we only reverse when the length of the res is odd - to be fancy.
        """
    
        if not root: return []
        q = deque([root])
        flag = True
        res = []

        while q:
            store = []
            for i in range(len(q)):
                cur = q.popleft()

                q.append(cur.left) if cur.left else None
                q.append(cur.right) if cur.right else None

                store.append(cur.val)
            
            if flag:
                res.append(store)
            else:
                new_cur = [n for n in reversed(store)]
                res.append(new_cur)
            flag = not flag
            
            # store = [n for n in reversed(store)] if len(res) % 2 else store
            # res.append(store)       
        
        return res
            
            
# O(n)
# O(n)

