# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use the hare and tortoise algo: 
        #the hare would catch up the tortoise if the linked list has a cycle
        #the hare is twice as fast as tortoise, so eventually it will catach up
        hare = head
        tortoise = head

        #if the linked list has no cycle , the hare would be none and terminate the loop
        #if the linked list has cycle , the hare and tortoise would be the same node
        #check if the hare and hare.next is true so that we can do hare.next.next
        while hare and hare.next:
            tortoise = tortoise.next 
            hare = hare.next.next
            if hare == tortoise:
                return True
        return False