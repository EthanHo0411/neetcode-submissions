# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        #first get the length of the linkedlist
        counter = 0
        start = head
        while start:
            counter+=1
            start = start.next
        
        #now minus n from the counter to know the index of the tail of the list
        index = counter - n
        start = head
        prev = None
        i = 0
        while i <index:
            prev = start
            start = start.next
            i+=1
        
        #for cases of the first elememt being removed
        if not prev:
            return start.next
        else:
            #now the start is the number we want to remove
            #simply set the prev pointer to the next node of start 
            #then set the next of start to None to disconnect it
            prev.next = start.next
            start.next = None 
            return head


        