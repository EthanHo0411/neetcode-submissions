# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        start = ListNode(0,None) 
        result = start
        while head1 and head2:
            nextt = None
            if head1.val <= head2.val:
                nextt = head1.next
                head1.next = None
                result.next = head1
                head1 = nextt
            else:
                nextt = head2.next
                head2.next = None
                result.next = head2
                head2 = nextt
            result = result.next
        if not head1:
            result.next = head2
        else:
            result.next = head1
        return start.next
