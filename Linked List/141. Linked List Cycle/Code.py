# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # When there is no cycle in the list, the l faster and continuously loops through the cycle. With each step, it reduces the gap between itself and the slow pointer by one node. 
        # This process continues until the fast pointer catches up to the slow pointer, confirming a cycle.oop ends when the fast pointer becomes null. If a cycle exists, the fast pointer moves

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False







# O(n)
# O(n)
