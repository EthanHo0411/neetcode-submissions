# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        from collections import deque

        #handle empty root
        if not root:
            return "None"
        #idea is to create a level order traversal string of the root
        nodes = deque([root])
        res = []
        while nodes:
            node = nodes.popleft()
            if not node:
                res.append("None")
            else:
                res.append(str(node.val))
                nodes.append(node.left)
                nodes.append(node.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #convert the string back to a value list 
        if data == "None":
            return None
        data = data.split(",")
        data = [int(x) if x != "None" else None for x in data]

        #perform level order traversal to restore the tree
        data = deque(data)
        root = TreeNode(data.popleft())
        nodes = deque([root])

        while nodes:
            node = nodes.popleft()
            if not node:
                continue
            #link left node and right node
            left = data.popleft()
            right = data.popleft()
            node.left = TreeNode(left) if left is not None else None
            node.right = TreeNode(right) if right is not None else None

            nodes.append(node.left)
            nodes.append(node.right)
        return root 

