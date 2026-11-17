# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #start from the head , put the next pointer to a variable
        #set the next pointer of the current one to be prev
        #set head to be the one stored in the variable

        prev, curr = None, head
        
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev