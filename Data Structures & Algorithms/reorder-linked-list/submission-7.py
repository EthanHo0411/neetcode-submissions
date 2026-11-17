# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #search for the middle pointer using the hare and tortoise approach
        start = head

        hare = head.next
        tortoise = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        
        #tortoise here is the last element of the first half 
        #now tortoise.next is the head of the second half of the linked list
        #reverse this half of the linkedlist

        curr = tortoise.next
        #set tortoise.next to None to disconnect the first list from the second
        prev = tortoise.next = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        #now combine the list
        #use prev because curr is None
        first, second = head, prev
        while second:
            #store the next node of list1 head
            nextt1 = first.next

            #store the next node of list2 head
            nextt2 = second.next 

            #point the current list1 head to the list2 head
            first.next = second

            #set the next node of this list2 head to be the stored next node of list1 head
            second.next = nextt1

            #set the list1 head to be nextt1 and list2 head to be nextt2
            first = nextt1
            second = nextt2
        

