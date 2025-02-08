"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_cp = {None: None}

        cur = head
        h2 = ListNode()

        while cur:
            node = ListNode(cur.val)
            node_cp[cur] = node

            cur = cur.next

        cur = head
        while cur:
            h2 = node_cp[cur]

            h2.next = node_cp[cur.next]
            h2.random = node_cp[cur.random]

            cur = cur.next
        
        return node_cp[head]
