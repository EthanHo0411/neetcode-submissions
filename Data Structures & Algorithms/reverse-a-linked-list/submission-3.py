# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #start from the head , put the next pointer to a variable
        #set the next pointer of the current one to be prev
        #set prev to the current head
        #set head to be the one stored in the variable
        #continue until the curr node is none
        #return prev as the curr at the end is the next of prev

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev