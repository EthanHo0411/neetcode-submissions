# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use the tortoise and hare algorithm where the hare is one step ahead
        #if there is a cycle, the hare will eventually catch up to the tortoise 
        tortoise = head 
        hare = head

        while hare and hare.next:

            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True

        return False