"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #one pass to create all the nodes
        #one pass to construct the sequence

        #hashmap to contain all the created nodes
        nodes = {None : None}

        start = head
        while start:
            #create the new nodes
            newNode = Node(start.val)
            nodes[start] = newNode
            start = start.next
        
        start = head
        while start:
            node = nodes[start]
            nextt = nodes[start.next]
            random = nodes[start.random]
            node.next = nextt
            node.random = random
            start = start.next
        
        return nodes[head]


