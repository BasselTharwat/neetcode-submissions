# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = pointer = ListNode()
        carry = 0


        while l1 or l2:
            sumNodes = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sumNodes // 10
            sumNodes = sumNodes % 10
            pointer.next = ListNode(sumNodes)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            pointer = pointer.next

        if carry > 0:
            pointer.next = ListNode(carry)

        return result.next
        