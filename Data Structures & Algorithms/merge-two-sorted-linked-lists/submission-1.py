# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create two node for the original node list
        head1 = list1
        head2 = list2
        #create dummy node used to indicate the start 
        start = ListNode(0,None) 
        #start constructing the list from the dummy node
        result = start
        while head1 and head2:
            nextt = None
            if head1.val <= head2.val:
                #store the next poitner of the list
                #remove the next pointer from the current head of the list
                #set the current head to be the next item of the current dummy 
                #restore the head of the list for next iteration
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
        #add the rest of the list directly to the end
        if not head1:
            result.next = head2
        else:
            result.next = head1
        return start.next
