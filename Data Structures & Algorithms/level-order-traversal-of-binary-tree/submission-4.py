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
        temp = []
        val = []
        res = [[root.val]]

        while nodes:
            node = nodes.popleft()

            if node.left:
                temp.append(node.left)
                val.append(node.left.val)

            if node.right:
                temp.append(node.right)
                val.append(node.right.val)
            
            if not nodes:
                if temp:
                    nodes.extend(temp)
                    res.append(val)
                    val = []
                    temp = []
        return res