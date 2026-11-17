# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque 
        if not root: 
            return []
        nodes = deque([root])
        levels = []

        while nodes:
            temp = []
            tempv = []
            length = len(nodes)
            for i in range(length):
                node = nodes.popleft()
                if node: 
                    temp.append(node.left)
                    temp.append(node.right)
                    tempv.append(node.val)
            
            if temp:
                levels.append(tempv)
                nodes.extend(temp)
                temp = []
                tempv = []

        return levels 
