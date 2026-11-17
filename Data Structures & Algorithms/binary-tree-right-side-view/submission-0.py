# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque
        nodes = deque([root])

        res = [root.val]
        temp = []

        while nodes:
            node = nodes.popleft()

            if node.left:
                temp.append(node.left)

            if node.right:
                temp.append(node.right)
            
            if not nodes:
                if temp:
                    res.append(temp[-1].val)
                    nodes.extend(temp)
                    temp = []
        return res
