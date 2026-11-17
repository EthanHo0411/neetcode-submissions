# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first figure out the middle of the list
        slow, fast = head , head.next 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        middle = slow.next
        #disconnect the partitions
        prev = slow.next = None

        #reverse the right partition
        while middle: 
            temp = middle.next 
            middle.next = prev 
            prev = middle 
            middle = temp

        middle = prev    
        #then create the new list in place
        #insert until the end of middle is met
        left = head 
        while middle: 
            #save the next node for both partition
            futurel = left.next 
            futurer = middle.next
            #insert the right nodes into the left partition
            left.next = middle 
            middle.next = futurel
            #restore the lists  
            middle = futurer
            left = futurel 
        


