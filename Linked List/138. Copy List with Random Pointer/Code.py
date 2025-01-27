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
        # Intuition is to use a Hashmap which will store all the orignal node along with their copies so that in the 2 iteration we can just look up the node being pointed to head.random and assign it our copy.random linked list.
        orig_copy = {}

        cur = head
        copy = Node(-1)
        cure = copy

        while cur:
            copy.next = Node(cur.val)
            copy = copy.next

            orig_copy[cur] = copy

            cur = cur.next

        copy = cure.next
        cur = head

        while cur:
            if cur.random:
                copy.random = orig_copy[cur.random]
            else:
                copy.random = None

            copy = copy.next
            cur = cur.next

        return cure.next






# O(n)
# O(n)
