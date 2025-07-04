# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Intuition: Linked list fundamentals - run the loop while any of the 3 is non null. If any/both of lists are null keep iterating with their net contribution is 0 until all 3 values are collapsed to None.
        res = ListNode()
        head = res
        carry = 0

        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            cur_sum = l1Val + l2Val + carry

            carry = cur_sum // 10

            res.next = ListNode(cur_sum%10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next
        
        return head.next
        


# O(MAX(n, m))
# O(MAX(n, m))
