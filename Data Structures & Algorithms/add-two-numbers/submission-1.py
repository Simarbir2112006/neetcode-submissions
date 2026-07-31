# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        prev_curr = None

        tail_l1 = l1
        tail_l2 = l2
        prev = 0

        while tail_l1 and tail_l2:
            total = str(tail_l1.val + tail_l2.val + prev)

            if len(total) != 1:
                prev = int(total[0])
                curr.val = int(total[1])
            else:
                prev = 0
                curr.val = int(total)

            curr.next = ListNode()
            prev_curr = curr
            curr = curr.next
            tail_l1 = tail_l1.next
            tail_l2 = tail_l2.next

        while tail_l1:
            total = str(tail_l1.val + prev)

            if len(total) != 1:
                prev = int(total[0])
                curr.val = int(total[1])
            else:
                prev = 0
                curr.val = int(total)

            curr.next = ListNode()
            prev_curr = curr
            curr = curr.next
            tail_l1 = tail_l1.next

        while tail_l2:
            total = str(tail_l2.val + prev)

            if len(total) != 1:
                prev = int(total[0])
                curr.val = int(total[1])
            else:
                prev = 0
                curr.val = int(total)

            curr.next = ListNode()
            prev_curr = curr
            curr = curr.next
            tail_l2 = tail_l2.next
        
        if prev != 0:
            curr.val = prev
        else:
            prev_curr.next = None

        return head

